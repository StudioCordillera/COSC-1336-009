"""
Async Queue Workers for Module Processing

Uses Observer pattern for notifications and async/await for concurrency.
Workers dequeue modules from QueueStrategy and write to database via UnitOfWork.

Design Patterns:
- Observer Pattern: WorkerObserver notifies on processing events
- Strategy Pattern: ProcessingStrategy for different processing modes
- Unit of Work Pattern: Database transaction management

All dependencies injected via constructors.
"""

import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict, Any, Callable
from enum import Enum
import json

# Import existing components
from api import QueueStrategy, ModuleDiscoveryResult
from models import (
    DatabaseSessionFactory, UnitOfWork,
    Module, Class, Function, Relationship
)
from taxonomy import TaxonomyMapper, create_taxonomy_entity


# ============================================================================
# Observer Pattern: Worker Event Notifications
# ============================================================================

class WorkerObserver(ABC):
    """Abstract observer for worker events"""
    
    @abstractmethod
    def on_processing_start(self, module_name: str, worker_id: int):
        """Called when worker starts processing a module"""
        pass
    
    @abstractmethod
    def on_processing_complete(self, module_name: str, worker_id: int, duration: float):
        """Called when processing completes successfully"""
        pass
    
    @abstractmethod
    def on_processing_error(self, module_name: str, worker_id: int, error: str):
        """Called when processing encounters an error"""
        pass
    
    @abstractmethod
    def on_worker_started(self, worker_id: int):
        """Called when worker starts"""
        pass
    
    @abstractmethod
    def on_worker_stopped(self, worker_id: int):
        """Called when worker stops"""
        pass


class LoggingWorkerObserver(WorkerObserver):
    """Observer that logs worker events"""
    
    def on_processing_start(self, module_name: str, worker_id: int):
        print(f"[Worker-{worker_id}] 🔄 Processing: {module_name}")
    
    def on_processing_complete(self, module_name: str, worker_id: int, duration: float):
        print(f"[Worker-{worker_id}] ✅ Completed: {module_name} ({duration:.2f}s)")
    
    def on_processing_error(self, module_name: str, worker_id: int, error: str):
        print(f"[Worker-{worker_id}] ❌ Error: {module_name} - {error}")
    
    def on_worker_started(self, worker_id: int):
        print(f"[Worker-{worker_id}] 🚀 Started")
    
    def on_worker_stopped(self, worker_id: int):
        print(f"[Worker-{worker_id}] 🛑 Stopped")


class MetricsWorkerObserver(WorkerObserver):
    """Observer that collects processing metrics"""
    
    def __init__(self):
        self.metrics = {
            'total_processed': 0,
            'total_errors': 0,
            'total_duration': 0.0,
            'workers_active': 0,
            'modules_by_status': {}
        }
        self.lock = asyncio.Lock()
    
    async def on_processing_start(self, module_name: str, worker_id: int):
        async with self.lock:
            self.metrics['modules_by_status'][module_name] = 'processing'
    
    async def on_processing_complete(self, module_name: str, worker_id: int, duration: float):
        async with self.lock:
            self.metrics['total_processed'] += 1
            self.metrics['total_duration'] += duration
            self.metrics['modules_by_status'][module_name] = 'complete'
    
    async def on_processing_error(self, module_name: str, worker_id: int, error: str):
        async with self.lock:
            self.metrics['total_errors'] += 1
            self.metrics['modules_by_status'][module_name] = f'error: {error}'
    
    async def on_worker_started(self, worker_id: int):
        async with self.lock:
            self.metrics['workers_active'] += 1
    
    async def on_worker_stopped(self, worker_id: int):
        async with self.lock:
            self.metrics['workers_active'] -= 1
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current metrics (thread-safe)"""
        return {
            **self.metrics,
            'avg_duration': self.metrics['total_duration'] / self.metrics['total_processed']
                if self.metrics['total_processed'] > 0 else 0
        }
    
    # Sync versions for compatibility
    def on_processing_start(self, module_name: str, worker_id: int):
        asyncio.create_task(self.on_processing_start(module_name, worker_id))
    
    def on_processing_complete(self, module_name: str, worker_id: int, duration: float):
        asyncio.create_task(self.on_processing_complete(module_name, worker_id, duration))
    
    def on_processing_error(self, module_name: str, worker_id: int, error: str):
        asyncio.create_task(self.on_processing_error(module_name, worker_id, error))
    
    def on_worker_started(self, worker_id: int):
        asyncio.create_task(self.on_worker_started(worker_id))
    
    def on_worker_stopped(self, worker_id: int):
        asyncio.create_task(self.on_worker_stopped(worker_id))


# ============================================================================
# Queue Processor: Dequeue and Process Modules
# ============================================================================

class QueueProcessor:
    """
    Processes modules from queue and writes to database.
    
    Dependency Injection:
    - queue_strategy: Queue to dequeue from
    - db_factory: Database factory for creating sessions
    - observers: List of worker observers
    """
    
    def __init__(
        self,
        queue_strategy: QueueStrategy,
        db_factory: DatabaseSessionFactory,
        observers: Optional[List[WorkerObserver]] = None,
        taxonomy_mapper: Optional[TaxonomyMapper] = None
    ):
        self.queue_strategy = queue_strategy
        self.db_factory = db_factory
        self.observers = observers or []
        self.taxonomy_mapper = taxonomy_mapper or TaxonomyMapper()
    
    def notify_processing_start(self, module_name: str, worker_id: int):
        """Notify observers of processing start"""
        for observer in self.observers:
            observer.on_processing_start(module_name, worker_id)
    
    def notify_processing_complete(self, module_name: str, worker_id: int, duration: float):
        """Notify observers of completion"""
        for observer in self.observers:
            observer.on_processing_complete(module_name, worker_id, duration)
    
    def notify_processing_error(self, module_name: str, worker_id: int, error: str):
        """Notify observers of error"""
        for observer in self.observers:
            observer.on_processing_error(module_name, worker_id, error)
    
    async def process_one(self, worker_id: int) -> bool:
        """
        Process one module from queue.
        
        Args:
            worker_id: ID of the worker processing
            
        Returns:
            True if module was processed, False if queue was empty
        """
        # Dequeue module
        item = self.queue_strategy.dequeue()
        
        if item is None:
            return False
        
        module_result, queue_id = item
        module_name = module_result.module_name
        
        start_time = datetime.utcnow()
        self.notify_processing_start(module_name, worker_id)
        
        try:
            # Write to database using Unit of Work
            with UnitOfWork(self.db_factory) as uow:
                # Check if module already exists
                existing = uow.repositories['module'].get_by_name(module_name)
                
                if existing:
                    # Update existing module
                    module = existing
                    module.filepath = module_result.filepath
                    module.analyzed_at = datetime.utcnow()
                    module.checksum = module_result.checksum
                else:
                    # Create new module
                    module = Module(
                        name=module_result.module_name,
                        filepath=module_result.filepath,
                        is_package=module_result.is_package,
                        checksum=module_result.checksum,
                        analyzed_at=datetime.utcnow(),
                        docstring=module_result.docstring
                    )
                    uow.repositories['module'].add(module)
                
                # Commit module first to get ID
                uow.commit()
                
                # Add classes and build name-to-id mapping
                class_map = {}  # Maps class name to class entity
                for class_data in module_result.classes:
                    cls = Class(
                        module_id=module.id,
                        name=class_data['name'],
                        lineno=class_data.get('lineno', 0),
                        parent_class_id=None,  # TODO: Handle nested classes
                        docstring=class_data.get('docstring')
                    )
                    uow.repositories['class'].add(cls)
                    class_map[class_data['name']] = (cls, class_data)
                
                # Commit classes to get IDs for relationship tracking
                uow.commit()
                
                # Track inheritance relationships
                for class_name, (cls, class_data) in class_map.items():
                    bases = class_data.get('bases', [])
                    for base_name in bases:
                        # Check if base class exists in current module
                        if base_name in class_map:
                            base_cls = class_map[base_name][0]
                            relationship = Relationship(
                                from_type='class',
                                from_id=cls.id,
                                to_type='class',
                                to_id=base_cls.id,
                                relationship_type='inherits'
                            )
                            uow.repositories['relationship'].add(relationship)
                        else:
                            # Base class from another module - lookup by name
                            base_classes = uow.repositories['class'].get_by_name(base_name)
                            if base_classes:
                                # Use first match (TODO: improve resolution)
                                relationship = Relationship(
                                    from_type='class',
                                    from_id=cls.id,
                                    to_type='class',
                                    to_id=base_classes[0].id,
                                    relationship_type='inherits'
                                )
                                uow.repositories['relationship'].add(relationship)
                
                # Add functions and link methods to classes
                for func_data in module_result.functions:
                    parent_name = func_data.get('parent')
                    class_id = None
                    is_method = False
                    
                    # Link method to parent class
                    if parent_name and parent_name in class_map:
                        class_id = class_map[parent_name][0].id
                        is_method = True
                    
                    func = Function(
                        module_id=module.id,
                        class_id=class_id,
                        name=func_data['name'],
                        lineno=func_data.get('lineno', 0),
                        is_async=func_data.get('is_async', False),
                        is_method=is_method,
                        docstring=func_data.get('docstring'),
                        args=json.dumps(func_data.get('args', [])),
                        returns=func_data.get('returns'),
                        decorators=json.dumps(func_data.get('decorators', []))
                    )
                    uow.repositories['function'].add(func)
                
                # Commit functions to get IDs for taxonomy
                uow.commit()
                
                # Categorize functions with taxonomy mapper
                for func_data in module_result.functions:
                    parent_name = func_data.get('parent')
                    
                    # Get function from database by name
                    funcs = uow.repositories['function'].get_by_name(func_data['name'])
                    if not funcs:
                        continue
                    
                    # Find the function we just added (match by module_id)
                    func = None
                    for f in funcs:
                        if f.module_id == module.id:
                            func = f
                            break
                    
                    if not func:
                        continue
                    
                    # Categorize using taxonomy mapper
                    taxonomy_match = self.taxonomy_mapper.get_primary_category(
                        name=func.name,
                        is_method=func.is_method,
                        is_async=func.is_async,
                        parent_class=parent_name,
                        decorators=None  # TODO: Extract decorators from pyclbr if available
                    )
                    
                    if taxonomy_match:
                        # Create taxonomy entity
                        taxonomy_entity = create_taxonomy_entity(taxonomy_match)
                        
                        # Check if this taxonomy already exists
                        existing_taxonomies = uow.repositories['taxonomy'].get_all()
                        existing = None
                        for t in existing_taxonomies:
                            if (t.category == taxonomy_entity.category and 
                                t.subcategory == taxonomy_entity.subcategory and
                                t.pattern == taxonomy_entity.pattern):
                                existing = t
                                break
                        
                        if existing:
                            taxonomy_id = existing.id
                        else:
                            uow.repositories['taxonomy'].add(taxonomy_entity)
                            uow.commit()
                            taxonomy_id = taxonomy_entity.id
                        
                        # Create relationship: function -> taxonomy
                        relationship = Relationship(
                            from_type='function',
                            from_id=func.id,
                            to_type='taxonomy',
                            to_id=taxonomy_id,
                            relationship_type='categorized_as'
                        )
                        uow.repositories['relationship'].add(relationship)
                
                # Track import relationships
                imports = getattr(module_result, 'imports', [])
                if imports:
                    for import_name in imports:
                        # Find imported module in database
                        imported_module = uow.repositories['module'].get_by_name(import_name)
                        if imported_module:
                            relationship = Relationship(
                                from_type='module',
                                from_id=module.id,
                                to_type='module',
                                to_id=imported_module.id,
                                relationship_type='imports'
                            )
                            uow.repositories['relationship'].add(relationship)
                
                # Commit all changes
                uow.commit()
            
            # Calculate duration and notify
            duration = (datetime.utcnow() - start_time).total_seconds()
            self.notify_processing_complete(module_name, worker_id, duration)
            
            return True
        
        except Exception as e:
            error_msg = str(e)
            self.notify_processing_error(module_name, worker_id, error_msg)
            return True  # Still processed (with error)


# ============================================================================
# Worker: Async worker that processes queue items
# ============================================================================

class Worker:
    """
    Async worker that continuously processes queue items.
    
    Dependency Injection:
    - worker_id: Unique worker identifier
    - processor: QueueProcessor instance
    - observers: List of worker observers
    """
    
    def __init__(
        self,
        worker_id: int,
        processor: QueueProcessor,
        observers: Optional[List[WorkerObserver]] = None,
        poll_interval: float = 0.1
    ):
        self.worker_id = worker_id
        self.processor = processor
        self.observers = observers or []
        self.poll_interval = poll_interval
        self.running = False
        self.task: Optional[asyncio.Task] = None
    
    def notify_started(self):
        """Notify observers worker started"""
        for observer in self.observers:
            observer.on_worker_started(self.worker_id)
    
    def notify_stopped(self):
        """Notify observers worker stopped"""
        for observer in self.observers:
            observer.on_worker_stopped(self.worker_id)
    
    async def run(self):
        """Run worker loop"""
        self.running = True
        self.notify_started()
        
        try:
            while self.running:
                # Try to process one item
                processed = await self.processor.process_one(self.worker_id)
                
                if not processed:
                    # Queue empty, wait before polling again
                    await asyncio.sleep(self.poll_interval)
        
        finally:
            self.notify_stopped()
    
    def start(self) -> asyncio.Task:
        """Start worker as async task"""
        self.task = asyncio.create_task(self.run())
        return self.task
    
    def stop(self):
        """Stop worker gracefully"""
        self.running = False
    
    async def wait_until_stopped(self):
        """Wait for worker to stop"""
        if self.task:
            await self.task


# ============================================================================
# Worker Pool: Manage multiple concurrent workers
# ============================================================================

class WorkerPool:
    """
    Manages pool of async workers.
    
    Dependency Injection:
    - queue_strategy: Queue to process
    - db_factory: Database factory
    - num_workers: Number of concurrent workers
    - observers: List of worker observers
    """
    
    def __init__(
        self,
        queue_strategy: QueueStrategy,
        db_factory: DatabaseSessionFactory,
        num_workers: int = 4,
        observers: Optional[List[WorkerObserver]] = None,
        taxonomy_mapper: Optional[TaxonomyMapper] = None
    ):
        self.queue_strategy = queue_strategy
        self.db_factory = db_factory
        self.num_workers = num_workers
        self.observers = observers or []
        self.taxonomy_mapper = taxonomy_mapper or TaxonomyMapper()
        
        # Create processor
        self.processor = QueueProcessor(
            queue_strategy=queue_strategy,
            db_factory=db_factory,
            observers=observers,
            taxonomy_mapper=self.taxonomy_mapper
        )
        
        # Create workers
        self.workers: List[Worker] = []
        for i in range(num_workers):
            worker = Worker(
                worker_id=i,
                processor=self.processor,
                observers=observers
            )
            self.workers.append(worker)
    
    def start(self):
        """Start all workers"""
        print(f"🚀 Starting worker pool with {self.num_workers} workers...")
        for worker in self.workers:
            worker.start()
    
    def stop(self):
        """Stop all workers gracefully"""
        print(f"🛑 Stopping worker pool...")
        for worker in self.workers:
            worker.stop()
    
    async def wait_until_stopped(self):
        """Wait for all workers to stop"""
        await asyncio.gather(*[worker.wait_until_stopped() for worker in self.workers])
    
    async def process_until_empty(self):
        """Process queue until empty, then stop"""
        self.start()
        
        # Wait until queue is empty
        while not self.queue_strategy.is_empty():
            await asyncio.sleep(0.5)
        
        # Give workers time to finish current items
        await asyncio.sleep(1)
        
        self.stop()
        await self.wait_until_stopped()


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    import sys
    from pathlib import Path
    
    # Add project root
    sys.path.insert(0, str(Path(__file__).parent))
    
    from api import InMemoryQueueStrategy
    
    print("=" * 60)
    print(" Async Workers Example")
    print("=" * 60)
    
    # Setup: Dependency Injection
    queue_strategy = InMemoryQueueStrategy(maxsize=100)
    
    db_factory = DatabaseSessionFactory(
        connection_string="sqlite:///test_workers.db",
        echo=False
    )
    db_factory.create_tables()
    
    observers = [
        LoggingWorkerObserver(),
        MetricsWorkerObserver()
    ]
    
    # Add test data to queue
    print("\n📤 Adding test modules to queue...")
    for i in range(5):
        test_module = ModuleDiscoveryResult(
            module_name=f'test_module_{i}',
            filepath=f'/test/module_{i}.py',
            is_package=False,
            classes=[{'name': f'TestClass{i}', 'lineno': 10}],
            functions=[{'name': f'test_func{i}', 'lineno': 20}],
            imports=['sys'],
            checksum=f'hash{i}',
            discovered_at=datetime.utcnow().isoformat(),
            scanner_version='1.0.0'
        )
        queue_strategy.enqueue(test_module, priority=1)
    
    print(f"✅ Added 5 modules to queue")
    
    # Create worker pool
    pool = WorkerPool(
        queue_strategy=queue_strategy,
        db_factory=db_factory,
        num_workers=2,
        observers=observers
    )
    
    # Process queue
    print("\n⚙️  Starting worker pool...")
    asyncio.run(pool.process_until_empty())
    
    # Show metrics
    metrics_observer = next(o for o in observers if isinstance(o, MetricsWorkerObserver))
    metrics = metrics_observer.get_metrics()
    
    print("\n" + "=" * 60)
    print(" Processing Complete")
    print("=" * 60)
    print(f"Total processed: {metrics['total_processed']}")
    print(f"Total errors: {metrics['total_errors']}")
    print(f"Average duration: {metrics['avg_duration']:.2f}s")
    print("=" * 60)
