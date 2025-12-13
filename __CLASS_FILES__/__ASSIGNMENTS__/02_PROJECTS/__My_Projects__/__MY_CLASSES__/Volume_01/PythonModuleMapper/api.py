"""
API Receiver Endpoint with Queue System
Uses Command pattern for request handling and Observer pattern for queue notifications.

Design Patterns:
- Command Pattern: APICommand encapsulates requests as objects
- Observer Pattern: QueueObserver notifies on queue events
- Strategy Pattern: QueueStrategy for different queue backends

All dependencies injected via constructors.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Any, Callable
import asyncio
import json
from pathlib import Path


# ============================================================================
# Command Pattern: API Request Commands
# ============================================================================

class APICommand(ABC):
    """Abstract command for API operations"""
    
    @abstractmethod
    def execute(self) -> Dict[str, Any]:
        """Execute the command and return result"""
        pass
    
    @abstractmethod
    def undo(self) -> bool:
        """Undo the command if possible"""
        pass
    
    @abstractmethod
    def can_undo(self) -> bool:
        """Check if command can be undone"""
        pass


@dataclass
class ModuleDiscoveryResult:
    """Data structure for module discovery results (from scanner.py)"""
    module_name: str
    filepath: str
    is_package: bool
    classes: List[Dict[str, Any]]
    functions: List[Dict[str, Any]]
    imports: List[str]
    checksum: str
    discovered_at: str
    scanner_version: str
    docstring: Optional[str] = None
    
    def to_json(self) -> str:
        """Serialize to JSON"""
        return json.dumps(asdict(self))
    
    @classmethod
    def from_json(cls, json_str: str) -> 'ModuleDiscoveryResult':
        """Deserialize from JSON"""
        data = json.loads(json_str)
        return cls(**data)


class SubmitModuleCommand(APICommand):
    """Command to submit a module discovery result to the queue"""
    
    def __init__(
        self,
        module_result: ModuleDiscoveryResult,
        queue_strategy: 'QueueStrategy',
        observers: Optional[List['QueueObserver']] = None
    ):
        self.module_result = module_result
        self.queue_strategy = queue_strategy
        self.observers = observers or []
        self.success = None
        self.queue_id = None
    
    def execute(self) -> Dict[str, Any]:
        """Submit module to queue and notify observers"""
        try:
            # Add to queue
            self.queue_id = self.queue_strategy.enqueue(
                self.module_result,
                priority=1
            )
            self.success = True
            
            # Notify observers
            for observer in self.observers:
                observer.on_enqueued(self.module_result, self.queue_id)
            
            return {
                'status': 'success',
                'queue_id': self.queue_id,
                'module': self.module_result.module_name,
                'timestamp': datetime.utcnow().isoformat()
            }
        except Exception as e:
            self.success = False
            
            # Notify observers of error
            for observer in self.observers:
                observer.on_error(self.module_result, str(e))
            
            return {
                'status': 'error',
                'error': str(e),
                'module': self.module_result.module_name,
                'timestamp': datetime.utcnow().isoformat()
            }
    
    def undo(self) -> bool:
        """Remove from queue if possible"""
        if not self.can_undo():
            return False
        
        try:
            self.queue_strategy.remove(self.queue_id)
            
            # Notify observers
            for observer in self.observers:
                observer.on_removed(self.module_result, self.queue_id)
            
            return True
        except Exception:
            return False
    
    def can_undo(self) -> bool:
        """Can undo if successfully enqueued and not yet processed"""
        return self.success and self.queue_id is not None


class HealthCheckCommand(APICommand):
    """Command to check system health"""
    
    def __init__(self, queue_strategy: 'QueueStrategy', db_factory: Any = None):
        self.queue_strategy = queue_strategy
        self.db_factory = db_factory
        self.success = None
    
    def execute(self) -> Dict[str, Any]:
        """Check queue and database health"""
        try:
            queue_stats = self.queue_strategy.get_stats()
            
            db_healthy = True
            if self.db_factory:
                try:
                    # Test database connection
                    session = self.db_factory.get_session()
                    session.close()
                except Exception:
                    db_healthy = False
            
            self.success = True
            
            return {
                'status': 'healthy',
                'timestamp': datetime.utcnow().isoformat(),
                'queue': queue_stats,
                'database': 'connected' if db_healthy else 'disconnected'
            }
        except Exception as e:
            self.success = False
            return {
                'status': 'unhealthy',
                'error': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    def undo(self) -> bool:
        """Health checks cannot be undone"""
        return False
    
    def can_undo(self) -> bool:
        return False


class GetMetricsCommand(APICommand):
    """Command to retrieve system metrics"""
    
    def __init__(self, queue_strategy: 'QueueStrategy', metrics_collector: Any = None):
        self.queue_strategy = queue_strategy
        self.metrics_collector = metrics_collector
        self.success = None
    
    def execute(self) -> Dict[str, Any]:
        """Get queue and processing metrics"""
        try:
            metrics = {
                'timestamp': datetime.utcnow().isoformat(),
                'queue': self.queue_strategy.get_stats()
            }
            
            if self.metrics_collector:
                metrics['processing'] = self.metrics_collector.get_metrics()
            
            self.success = True
            return metrics
        except Exception as e:
            self.success = False
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.utcnow().isoformat()
            }
    
    def undo(self) -> bool:
        """Metrics queries cannot be undone"""
        return False
    
    def can_undo(self) -> bool:
        return False


# ============================================================================
# Observer Pattern: Queue Event Notifications
# ============================================================================

class QueueObserver(ABC):
    """Abstract observer for queue events"""
    
    @abstractmethod
    def on_enqueued(self, module_result: ModuleDiscoveryResult, queue_id: str):
        """Called when module is enqueued"""
        pass
    
    @abstractmethod
    def on_dequeued(self, module_result: ModuleDiscoveryResult, queue_id: str):
        """Called when module is dequeued for processing"""
        pass
    
    @abstractmethod
    def on_processed(self, module_result: ModuleDiscoveryResult, queue_id: str):
        """Called when module processing completes"""
        pass
    
    @abstractmethod
    def on_error(self, module_result: ModuleDiscoveryResult, error: str):
        """Called when error occurs"""
        pass
    
    @abstractmethod
    def on_removed(self, module_result: ModuleDiscoveryResult, queue_id: str):
        """Called when module is removed from queue"""
        pass


class LoggingObserver(QueueObserver):
    """Observer that logs queue events"""
    
    def __init__(self, log_file: Optional[Path] = None):
        self.log_file = log_file
    
    def _log(self, event: str, details: Dict[str, Any]):
        """Write log entry"""
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event': event,
            'details': details
        }
        
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(entry) + '\n')
        else:
            print(f"[{event}] {details}")
    
    def on_enqueued(self, module_result: ModuleDiscoveryResult, queue_id: str):
        self._log('ENQUEUED', {
            'module': module_result.module_name,
            'queue_id': queue_id
        })
    
    def on_dequeued(self, module_result: ModuleDiscoveryResult, queue_id: str):
        self._log('DEQUEUED', {
            'module': module_result.module_name,
            'queue_id': queue_id
        })
    
    def on_processed(self, module_result: ModuleDiscoveryResult, queue_id: str):
        self._log('PROCESSED', {
            'module': module_result.module_name,
            'queue_id': queue_id
        })
    
    def on_error(self, module_result: ModuleDiscoveryResult, error: str):
        self._log('ERROR', {
            'module': module_result.module_name,
            'error': error
        })
    
    def on_removed(self, module_result: ModuleDiscoveryResult, queue_id: str):
        self._log('REMOVED', {
            'module': module_result.module_name,
            'queue_id': queue_id
        })


class MetricsObserver(QueueObserver):
    """Observer that collects processing metrics"""
    
    def __init__(self):
        self.metrics = {
            'total_enqueued': 0,
            'total_processed': 0,
            'total_errors': 0,
            'total_removed': 0,
            'modules_by_status': {}
        }
    
    def on_enqueued(self, module_result: ModuleDiscoveryResult, queue_id: str):
        self.metrics['total_enqueued'] += 1
        self.metrics['modules_by_status'][queue_id] = 'enqueued'
    
    def on_dequeued(self, module_result: ModuleDiscoveryResult, queue_id: str):
        self.metrics['modules_by_status'][queue_id] = 'processing'
    
    def on_processed(self, module_result: ModuleDiscoveryResult, queue_id: str):
        self.metrics['total_processed'] += 1
        self.metrics['modules_by_status'][queue_id] = 'processed'
    
    def on_error(self, module_result: ModuleDiscoveryResult, error: str):
        self.metrics['total_errors'] += 1
    
    def on_removed(self, module_result: ModuleDiscoveryResult, queue_id: str):
        self.metrics['total_removed'] += 1
        if queue_id in self.metrics['modules_by_status']:
            del self.metrics['modules_by_status'][queue_id]
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current metrics"""
        return self.metrics.copy()


# ============================================================================
# Strategy Pattern: Queue Backends
# ============================================================================

class QueueStrategy(ABC):
    """Abstract strategy for queue backend"""
    
    @abstractmethod
    def enqueue(self, item: ModuleDiscoveryResult, priority: int = 1) -> str:
        """Add item to queue, return queue ID"""
        pass
    
    @abstractmethod
    def dequeue(self) -> Optional[tuple[ModuleDiscoveryResult, str]]:
        """Remove and return next item with its queue ID"""
        pass
    
    @abstractmethod
    def remove(self, queue_id: str) -> bool:
        """Remove specific item from queue"""
        pass
    
    @abstractmethod
    def peek(self) -> Optional[ModuleDiscoveryResult]:
        """View next item without removing"""
        pass
    
    @abstractmethod
    def get_stats(self) -> Dict[str, Any]:
        """Get queue statistics"""
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Check if queue is empty"""
        pass


class InMemoryQueueStrategy(QueueStrategy):
    """In-memory queue using asyncio.Queue"""
    
    def __init__(self, maxsize: int = 0):
        self.queue = asyncio.Queue(maxsize=maxsize)
        self.items = {}  # queue_id -> ModuleDiscoveryResult
        self.counter = 0
        self.total_enqueued = 0
        self.total_dequeued = 0
    
    def enqueue(self, item: ModuleDiscoveryResult, priority: int = 1) -> str:
        """Add item to queue"""
        queue_id = f"queue_{self.counter}_{datetime.utcnow().timestamp()}"
        self.counter += 1
        
        # Store item
        self.items[queue_id] = item
        
        # Add to queue (non-blocking)
        try:
            self.queue.put_nowait((priority, queue_id, item))
            self.total_enqueued += 1
            return queue_id
        except asyncio.QueueFull:
            del self.items[queue_id]
            raise Exception("Queue is full")
    
    def dequeue(self) -> Optional[tuple[ModuleDiscoveryResult, str]]:
        """Remove and return next item"""
        try:
            priority, queue_id, item = self.queue.get_nowait()
            self.total_dequeued += 1
            return (item, queue_id)
        except asyncio.QueueEmpty:
            return None
    
    def remove(self, queue_id: str) -> bool:
        """Remove specific item (not efficient for asyncio.Queue)"""
        if queue_id in self.items:
            del self.items[queue_id]
            return True
        return False
    
    def peek(self) -> Optional[ModuleDiscoveryResult]:
        """View next item without removing"""
        # asyncio.Queue doesn't support peek, return None
        return None
    
    def get_stats(self) -> Dict[str, Any]:
        """Get queue statistics"""
        return {
            'size': self.queue.qsize(),
            'maxsize': self.queue.maxsize,
            'total_enqueued': self.total_enqueued,
            'total_dequeued': self.total_dequeued,
            'pending': len(self.items)
        }
    
    def is_empty(self) -> bool:
        return self.queue.empty()


# ============================================================================
# API Endpoint Handler
# ============================================================================

class APIEndpointHandler:
    """
    Main API endpoint handler using Command pattern.
    
    Dependency Injection:
    - queue_strategy: Queue backend strategy
    - observers: List of queue observers
    - db_factory: Optional database factory for health checks
    """
    
    def __init__(
        self,
        queue_strategy: QueueStrategy,
        observers: Optional[List[QueueObserver]] = None,
        db_factory: Any = None
    ):
        self.queue_strategy = queue_strategy
        self.observers = observers or []
        self.db_factory = db_factory
        self.command_history: List[APICommand] = []
    
    def submit_module(self, module_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Submit a module discovery result.
        
        Args:
            module_data: Dictionary containing ModuleDiscoveryResult fields
        
        Returns:
            Response dictionary with status and queue_id
        """
        # Create ModuleDiscoveryResult from dict
        module_result = ModuleDiscoveryResult(**module_data)
        
        # Create and execute command
        command = SubmitModuleCommand(
            module_result=module_result,
            queue_strategy=self.queue_strategy,
            observers=self.observers
        )
        
        result = command.execute()
        
        # Store in command history for potential undo
        if command.success:
            self.command_history.append(command)
        
        return result
    
    def health_check(self) -> Dict[str, Any]:
        """Check system health"""
        command = HealthCheckCommand(
            queue_strategy=self.queue_strategy,
            db_factory=self.db_factory
        )
        return command.execute()
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get system metrics"""
        # Find MetricsObserver
        metrics_collector = None
        for observer in self.observers:
            if isinstance(observer, MetricsObserver):
                metrics_collector = observer
                break
        
        command = GetMetricsCommand(
            queue_strategy=self.queue_strategy,
            metrics_collector=metrics_collector
        )
        return command.execute()
    
    def undo_last(self) -> Dict[str, Any]:
        """Undo last command if possible"""
        if not self.command_history:
            return {'status': 'error', 'error': 'No commands to undo'}
        
        last_command = self.command_history[-1]
        
        if not last_command.can_undo():
            return {'status': 'error', 'error': 'Command cannot be undone'}
        
        success = last_command.undo()
        
        if success:
            self.command_history.pop()
            return {'status': 'success', 'message': 'Command undone'}
        else:
            return {'status': 'error', 'error': 'Undo failed'}


# ============================================================================
# Example Usage (for testing)
# ============================================================================

if __name__ == '__main__':
    # Setup: Dependency Injection
    queue_strategy = InMemoryQueueStrategy(maxsize=100)
    
    observers = [
        LoggingObserver(),
        MetricsObserver()
    ]
    
    api_handler = APIEndpointHandler(
        queue_strategy=queue_strategy,
        observers=observers
    )
    
    # Example: Submit module
    module_data = {
        'module_name': 'collections',
        'filepath': '/usr/lib/python3.9/collections.py',
        'is_package': False,
        'classes': [{'name': 'OrderedDict', 'lineno': 100}],
        'functions': [{'name': '__init__', 'lineno': 50}],
        'imports': ['sys', 'os'],
        'checksum': 'abc123',
        'discovered_at': datetime.utcnow().isoformat(),
        'scanner_version': '1.0.0'
    }
    
    result = api_handler.submit_module(module_data)
    print("Submit result:", result)
    
    # Check health
    health = api_handler.health_check()
    print("Health:", health)
    
    # Get metrics
    metrics = api_handler.get_metrics()
    print("Metrics:", metrics)
