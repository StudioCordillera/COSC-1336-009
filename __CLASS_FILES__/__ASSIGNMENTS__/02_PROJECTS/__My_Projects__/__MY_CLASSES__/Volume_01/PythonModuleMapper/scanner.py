# Recursive Module Scanner using Command Pattern
# Sends discovered modules to API queue for processing

import pyclbr
import sys
import ast
from pathlib import Path
from typing import List, Set, Optional, Callable
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
import hashlib
from logger_config import get_logger

logger = get_logger("scanner")


# Command Pattern: Abstract command for module operations
class ModuleCommand(ABC):
    """Abstract command for module operations"""
    
    @abstractmethod
    def execute(self) -> dict:
        """Execute the command"""
        pass
    
    @abstractmethod
    def undo(self):
        """Undo the command if possible"""
        pass


@dataclass
class ModuleDiscoveryResult:
    """Result of module discovery"""
    module_name: str
    filepath: str
    is_package: bool
    discovered_at: datetime
    checksum: str
    classes: List[dict] = field(default_factory=list)
    functions: List[dict] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    docstring: Optional[str] = None
    error: Optional[str] = None


class ImportVisitor(ast.NodeVisitor):
    """AST Visitor to extract imports"""
    def __init__(self):
        self.imports = []

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module:
            self.imports.append(node.module)
        self.generic_visit(node)


class RichMetadataVisitor(ast.NodeVisitor):
    """AST Visitor to extract rich metadata (docstrings, args, decorators)"""
    def __init__(self):
        self.classes = {}
        self.functions = {}
        self.module_docstring = None
        self.current_class = None

    def visit_Module(self, node):
        self.module_docstring = ast.get_docstring(node)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.classes[node.name] = {
            'docstring': ast.get_docstring(node),
            'decorators': [self._get_decorator_name(d) for d in node.decorator_list],
            'lineno': node.lineno,
            'methods': {}
        }
        old_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = old_class

    def visit_FunctionDef(self, node):
        self._process_function(node)
        # Don't visit children to avoid processing nested functions as top-level
        # self.generic_visit(node) 

    def visit_AsyncFunctionDef(self, node):
        self._process_function(node, is_async=True)
        # Don't visit children to avoid processing nested functions as top-level
        # self.generic_visit(node)

    def _process_function(self, node, is_async=False):
        args = []
        # Handle positional args
        for arg in node.args.args:
            arg_data = {'name': arg.arg}
            if arg.annotation:
                arg_data['type'] = self._get_annotation_name(arg.annotation)
            args.append(arg_data)
            
        # Handle return annotation
        returns = self._get_annotation_name(node.returns) if node.returns else None

        func_data = {
            'docstring': ast.get_docstring(node),
            'decorators': [self._get_decorator_name(d) for d in node.decorator_list],
            'args': args,
            'returns': returns,
            'is_async': is_async,
            'lineno': node.lineno
        }
        
        if self.current_class:
            if self.current_class in self.classes:
                self.classes[self.current_class]['methods'][node.name] = func_data
        else:
            self.functions[node.name] = func_data

    def _get_decorator_name(self, node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_decorator_name(node.value)}.{node.attr}"
        elif isinstance(node, ast.Call):
            return self._get_decorator_name(node.func)
        return "unknown_decorator"

    def _get_annotation_name(self, node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_annotation_name(node.value)}.{node.attr}"
        elif isinstance(node, ast.Subscript):
            return f"{self._get_annotation_name(node.value)}[{self._get_annotation_name(node.slice)}]"
        elif isinstance(node, ast.Constant):
            return str(node.value)
        return "Any"


class ScanModuleCommand(ModuleCommand):
    """Command to scan a specific module"""
    
    def __init__(
        self,
        module_name: str,
        search_paths: Optional[List[Path]] = None,
        callback: Optional[Callable] = None
    ):
        """
        Initialize scan command with dependency injection
        
        Args:
            module_name: Name of module to scan
            search_paths: Optional custom search paths
            callback: Optional callback for results
        """
        self.module_name = module_name
        self.search_paths = [str(p) for p in search_paths] if search_paths else None
        self.callback = callback
        self.result: Optional[ModuleDiscoveryResult] = None
    
    def _extract_metadata(self, filepath: str) -> dict:
        """Extract rich metadata using AST"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                tree = ast.parse(content, filename=filepath)
            
            # Extract imports
            import_visitor = ImportVisitor()
            import_visitor.visit(tree)
            
            # Extract rich metadata
            meta_visitor = RichMetadataVisitor()
            meta_visitor.visit(tree)
            
            return {
                'imports': list(set(import_visitor.imports)),
                'classes': meta_visitor.classes,
                'functions': meta_visitor.functions,
                'module_docstring': meta_visitor.module_docstring
            }
        except Exception as e:
            logger.warning(f"Failed to parse metadata from {filepath}: {e}")
            return {'imports': [], 'classes': {}, 'functions': {}, 'module_docstring': None}

    def execute(self) -> dict:
        """Execute module scan"""
        logger.debug(f"Scanning module: {self.module_name}")
        try:
            # Use pyclbr to safely read module without importing
            data = pyclbr.readmodule_ex(self.module_name, path=self.search_paths)
            
            # Extract file path
            filepath = None
            is_package = '__path__' in data
            
            # Get filepath from an item that belongs to this module
            for item in data.values():
                if hasattr(item, 'file') and hasattr(item, 'module') and item.module == self.module_name:
                    filepath = item.file
                    break
            
            # Fallback: use importlib to find file if pyclbr didn't give us a clear one
            if not filepath:
                import importlib.util
                try:
                    spec = importlib.util.find_spec(self.module_name)
                    if spec and spec.origin:
                        filepath = spec.origin
                except ImportError:
                    pass
            
            # Calculate checksum
            checksum = self._calculate_checksum(filepath) if filepath else None
            
            # Extract metadata if we have a file
            metadata = {'imports': [], 'classes': {}, 'functions': {}, 'module_docstring': None}
            if filepath:
                metadata = self._extract_metadata(filepath)

            # Extract classes
            classes = []
            functions = []
            
            for name, descriptor in data.items():
                if name == '__path__':
                    continue
                
                if isinstance(descriptor, pyclbr.Class):
                    # Merge pyclbr data with AST metadata
                    ast_data = metadata['classes'].get(name, {})
                    
                    classes.append({
                        'name': name,
                        'lineno': descriptor.lineno,
                        'methods': list(descriptor.methods.keys()),
                        'bases': [
                            b.name if isinstance(b, pyclbr.Class) else str(b)
                            for b in descriptor.super
                        ],
                        'parent': descriptor.parent.name if descriptor.parent else None,
                        'docstring': ast_data.get('docstring'),
                        'decorators': ast_data.get('decorators', [])
                    })
                    
                    # Also process methods as functions
                    for method_name, method_lineno in descriptor.methods.items():
                        method_ast_data = ast_data.get('methods', {}).get(method_name, {})
                        
                        func_data = {
                            'name': method_name,
                            'lineno': method_lineno,
                            'parent': name, # Parent is the class name
                            'docstring': method_ast_data.get('docstring'),
                            'decorators': method_ast_data.get('decorators', []),
                            'args': method_ast_data.get('args', []),
                            'returns': method_ast_data.get('returns'),
                            'is_async': method_ast_data.get('is_async', False)
                        }
                        functions.append(func_data)
                
                elif isinstance(descriptor, pyclbr.Function):
                    # Merge pyclbr data with AST metadata
                    # Note: pyclbr returns top-level functions and methods.
                    # AST visitor stores functions by name.
                    # If it's a method, it might not be in metadata['functions'] if we only visit top-level.
                    # But here we are iterating pyclbr results which are top-level or nested classes.
                    # pyclbr.Function is for top-level functions.
                    
                    ast_data = metadata['functions'].get(name, {})
                    
                    # If AST didn't find it (maybe because of some dynamic creation or complex structure),
                    # we might still want to keep it, but without rich metadata.
                    
                    func_data = {
                        'name': name,
                        'lineno': descriptor.lineno,
                        'parent': descriptor.parent.name if descriptor.parent else None,
                        'docstring': ast_data.get('docstring'),
                        'decorators': ast_data.get('decorators', []),
                        'args': ast_data.get('args', []),
                        'returns': ast_data.get('returns')
                    }
                    
                    # Add async flag if Python 3.10+
                    if sys.version_info >= (3, 10):
                        func_data['is_async'] = getattr(descriptor, 'is_async', False)
                    
                    functions.append(func_data)
            
            # Create result
            self.result = ModuleDiscoveryResult(
                module_name=self.module_name,
                filepath=filepath or 'unknown',
                is_package=is_package,
                discovered_at=datetime.utcnow(),
                checksum=checksum or 'unknown',
                classes=classes,
                functions=functions,
                imports=metadata['imports'],
                docstring=metadata['module_docstring']
            )
            
            # Call callback if provided
            if self.callback:
                self.callback(self.result)
            
            logger.debug(f"Successfully scanned {self.module_name}")
            return {
                'success': True,
                'module_name': self.module_name,
                'data': self.result.__dict__
            }
        
        except Exception as e:
            logger.error(f"Failed to scan {self.module_name}: {e}")
            self.result = ModuleDiscoveryResult(
                module_name=self.module_name,
                filepath='unknown',
                is_package=False,
                discovered_at=datetime.utcnow(),
                checksum='error',
                error=str(e)
            )
            
            return {
                'success': False,
                'module_name': self.module_name,
                'error': str(e)
            }
    
    def undo(self):
        """Cannot undo a scan operation"""
        pass
    
    def _calculate_checksum(self, filepath: str) -> str:
        """Calculate MD5 checksum of file"""
        try:
            with open(filepath, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception:
            return 'unknown'


# Strategy Pattern: Different scanning strategies
class ScanStrategy(ABC):
    """Abstract scanning strategy"""
    
    @abstractmethod
    def scan(self, root_path: Path) -> List[str]:
        """Scan for modules and return module names"""
        pass


class RecursiveScanStrategy(ScanStrategy):
    """Recursively scan directory for Python modules"""
    
    def __init__(
        self,
        max_depth: int = 10,
        excluded_patterns: Optional[List[str]] = None
    ):
        """
        Initialize recursive scanner
        
        Args:
            max_depth: Maximum recursion depth
            excluded_patterns: Patterns to exclude (e.g., ['test_*', '*_test.py'])
        """
        self.max_depth = max_depth
        self.excluded_patterns = excluded_patterns or []
    
    def scan(self, root_path: Path) -> List[str]:
        """Recursively scan for Python modules"""
        modules = []
        
        def _scan_recursive(path: Path, depth: int = 0, prefix: str = ''):
            if depth > self.max_depth:
                return
            
            if not path.is_dir():
                return
            
            # Check for __init__.py to identify package
            init_file = path / '__init__.py'
            is_package = init_file.exists()
            
            if is_package:
                module_name = prefix.rstrip('.')
                if module_name and not self._is_excluded(module_name):
                    modules.append(module_name)
            
            # Scan Python files
            for item in path.iterdir():
                if item.name.startswith('_') and item.name != '__init__.py':
                    continue
                
                if item.is_file() and item.suffix == '.py' and item.name != '__init__.py':
                    module_name = f"{prefix}{item.stem}"
                    if not self._is_excluded(module_name):
                        modules.append(module_name)
                
                elif item.is_dir() and not item.name.startswith('.'):
                    new_prefix = f"{prefix}{item.name}."
                    _scan_recursive(item, depth + 1, new_prefix)
        
        _scan_recursive(root_path)
        return modules
    
    def _is_excluded(self, module_name: str) -> bool:
        """Check if module matches exclusion patterns"""
        import fnmatch
        for pattern in self.excluded_patterns:
            if fnmatch.fnmatch(module_name, pattern):
                return True
        return False


class SysPathScanStrategy(ScanStrategy):
    """Scan sys.path for importable modules"""
    
    def scan(self, root_path: Optional[Path] = None) -> List[str]:
        """Scan sys.path for modules"""
        import pkgutil
        
        modules = []
        for importer, modname, ispkg in pkgutil.iter_modules():
            if not modname.startswith('_'):
                modules.append(modname)
        
        return modules


# Iterator Pattern: Iterate through discovered modules
class ModuleIterator:
    """Iterator for discovered modules"""
    
    def __init__(self, modules: List[str]):
        self._modules = modules
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> str:
        if self._index >= len(self._modules):
            raise StopIteration
        
        module = self._modules[self._index]
        self._index += 1
        return module
    
    def has_next(self) -> bool:
        """Check if more modules available"""
        return self._index < len(self._modules)
    
    def reset(self):
        """Reset iterator to beginning"""
        self._index = 0


# Observer Pattern: Notify when modules are discovered
class ScanObserver(ABC):
    """Abstract observer for scan events"""
    
    @abstractmethod
    def on_module_discovered(self, module_name: str):
        """Called when module is discovered"""
        pass
    
    @abstractmethod
    def on_scan_complete(self, total_modules: int):
        """Called when scan completes"""
        pass
    
    @abstractmethod
    def on_scan_error(self, error: str):
        """Called when scan encounters error"""
        pass


class APISubmitObserver(ScanObserver):
    """
    Observer that submits discovered modules to API
    
    Integrates with api_client.APIClient for HTTP submission.
    Accumulates modules for batch submission on scan_complete.
    """
    
    def __init__(self, api_client, enable_batch: bool = True):
        """
        Initialize with API client dependency injection
        
        Args:
            api_client: api_client.APIClient instance for HTTP submission
            enable_batch: If True, accumulate and batch submit on completion
        """
        self.api_client = api_client
        self.enable_batch = enable_batch
        self.pending_submissions = []
        self.submitted_count = 0
        self.error_count = 0
    
    def on_module_discovered(self, module_name: str):
        """
        Queue module for submission
        
        If batch mode enabled, adds to pending list.
        Otherwise, submits immediately.
        """
        if self.enable_batch:
            # Create module discovery command and queue for batch
            command = ScanModuleCommand(module_name)
            self.pending_submissions.append(command)
        else:
            # Immediate submission
            self._submit_single(module_name)
    
    def on_scan_complete(self, total_modules: int):
        """
        Submit all pending modules in batch when scan completes
        
        Executes all pending ScanModuleCommands to extract module data,
        then submits batch to API via api_client.submit_batch()
        """
        if self.enable_batch and self.pending_submissions:
            print(f"Executing {len(self.pending_submissions)} scan commands...")
            
            # Execute all commands to get ModuleDiscoveryResult objects
            module_results = []
            for cmd in self.pending_submissions:
                try:
                    result = cmd.execute()
                    if result.get('success'):
                        # Convert to format expected by API
                        module_data = {
                            'module_name': result['module_name'],
                            'filepath': result.get('filepath', 'unknown'),
                            'is_package': result.get('is_package', False),
                            'classes': result.get('classes', []),
                            'functions': result.get('functions', []),
                            'imports': result.get('imports', []),
                            'checksum': result.get('checksum', 'unknown'),
                            'discovered_at': datetime.utcnow().isoformat(),
                            'scanner_version': '1.0.0'
                        }
                        module_results.append(module_data)
                except Exception as e:
                    print(f"Error executing command for {cmd.module_name}: {e}")
                    self.error_count += 1
            
            # Submit batch to API
            if module_results:
                print(f"Submitting batch of {len(module_results)} modules to API...")
                try:
                    batch_result = self.api_client.submit_batch(module_results)
                    self.submitted_count = batch_result['successful']
                    self.error_count += batch_result['failed']
                    
                    print(f"✅ Batch submission complete:")
                    print(f"   Success: {batch_result['successful']}/{batch_result['total']}")
                    print(f"   Failed: {batch_result['failed']}/{batch_result['total']}")
                except Exception as e:
                    print(f"❌ Batch submission error: {e}")
                    self.error_count += len(module_results)
            
            # Clear pending
            self.pending_submissions = []
        
        print(f"Scan complete: {total_modules} modules discovered, {self.submitted_count} submitted to API")
    
    def on_scan_error(self, error: str):
        """Log scan error"""
        print(f"❌ Scan error: {error}")
    
    def _submit_single(self, module_name: str):
        """Submit single module immediately (non-batch mode)"""
        try:
            # Execute scan command
            command = ScanModuleCommand(module_name)
            result = command.execute()
            
            if result.get('success'):
                # Submit to API
                module_data = {
                    'module_name': result['module_name'],
                    'filepath': result.get('filepath', 'unknown'),
                    'is_package': result.get('is_package', False),
                    'classes': result.get('classes', []),
                    'functions': result.get('functions', []),
                    'imports': result.get('imports', []),
                    'checksum': result.get('checksum', 'unknown'),
                    'discovered_at': datetime.utcnow().isoformat(),
                    'scanner_version': '1.0.0'
                }
                
                response = self.api_client.submit_module(module_data)
                self.submitted_count += 1
                print(f"✅ Submitted {module_name} (queue_id: {response.get('queue_id')})")
        except Exception as e:
            print(f"❌ Error submitting {module_name}: {e}")
            self.error_count += 1


# Main Scanner using composite pattern
class ModuleScanner:
    """Main module scanner with dependency injection"""
    
    def __init__(
        self,
        scan_strategy: ScanStrategy,
        observers: Optional[List[ScanObserver]] = None,
        batch_size: int = 50
    ):
        """
        Initialize scanner with dependencies
        
        Args:
            scan_strategy: Strategy for scanning modules
            observers: List of observers to notify
            batch_size: Number of modules to batch before processing
        """
        self.scan_strategy = scan_strategy
        self.observers = observers or []
        self.batch_size = batch_size
        self.discovered_modules: Set[str] = set()
    
    def add_observer(self, observer: ScanObserver):
        """Add observer"""
        self.observers.append(observer)
    
    def remove_observer(self, observer: ScanObserver):
        """Remove observer"""
        self.observers.remove(observer)
    
    def notify_module_discovered(self, module_name: str):
        """Notify all observers of module discovery"""
        for observer in self.observers:
            observer.on_module_discovered(module_name)
    
    def notify_scan_complete(self, total_modules: int):
        """Notify all observers of scan completion"""
        for observer in self.observers:
            observer.on_scan_complete(total_modules)
    
    def notify_scan_error(self, error: str):
        """Notify all observers of scan error"""
        for observer in self.observers:
            observer.on_scan_error(error)
    
    def scan(self, root_path: Path) -> List[str]:
        """
        Scan for modules using configured strategy
        
        Args:
            root_path: Root path to scan
            
        Returns:
            List of discovered module names
        """
        try:
            # Use strategy to discover modules
            modules = self.scan_strategy.scan(root_path)
            
            # Notify observers in batches
            batch = []
            for module_name in modules:
                if module_name not in self.discovered_modules:
                    self.discovered_modules.add(module_name)
                    batch.append(module_name)
                    
                    if len(batch) >= self.batch_size:
                        self._process_batch(batch)
                        batch = []
            
            # Process remaining batch
            if batch:
                self._process_batch(batch)
            
            # Notify completion
            self.notify_scan_complete(len(modules))
            
            return modules
        
        except Exception as e:
            self.notify_scan_error(str(e))
            raise
    
    def _process_batch(self, batch: List[str]):
        """Process a batch of modules"""
        for module_name in batch:
            self.notify_module_discovered(module_name)
    
    def create_scan_commands(
        self,
        modules: List[str],
        search_paths: Optional[List[Path]] = None,
        callback: Optional[Callable] = None
    ) -> List[ScanModuleCommand]:
        """
        Create scan commands for discovered modules
        
        Args:
            modules: List of module names
            search_paths: Optional custom search paths
            callback: Optional callback for results
            
        Returns:
            List of scan commands ready to execute
        """
        return [
            ScanModuleCommand(module, search_paths, callback)
            for module in modules
        ]


# Example usage
if __name__ == '__main__':
    # OPTION 1: Use with real API client
    print("=" * 60)
    print("Example 1: Scanner with API Integration")
    print("=" * 60)
    
    try:
        from api_client import APIClient
        
        # Create API client with dependency injection
        api_client = APIClient(
            base_url="http://localhost:8000",
            timeout=30,
            retry_attempts=3
        )
        
        # Check if API is available
        try:
            health = api_client.health_check()
            print(f"✅ API is available: {health['status']}")
        except Exception as e:
            print(f"⚠️  API not available: {e}")
            print("   Start API server: python api_server.py")
            sys.exit(1)
        
        # Create scanning strategy
        strategy = RecursiveScanStrategy(
            max_depth=3,
            excluded_patterns=['test_*', '*_test', '__pycache__']
        )
        
        # Create observer with API client
        observer = APISubmitObserver(
            api_client=api_client,
            enable_batch=True  # Use batch submission
        )
        
        # Create scanner with dependencies
        scanner = ModuleScanner(
            scan_strategy=strategy,
            observers=[observer],
            batch_size=20
        )
        
        # Scan current directory
        print(f"\nScanning: {Path.cwd()}")
        modules = scanner.scan(Path('.'))
        print(f"\n✅ Discovered {len(modules)} total modules")
        
        # Get final metrics
        metrics = api_client.get_metrics()
        print(f"\n📊 API Queue Metrics:")
        print(f"   Queue size: {metrics['queue']['size']}")
        print(f"   Total enqueued: {metrics['queue']['total_enqueued']}")
        
        api_client.close()
        
    except ImportError as e:
        print(f"❌ Cannot import api_client: {e}")
        print("\n" + "=" * 60)
        print("Example 2: Scanner with Mock Client (No API)")
        print("=" * 60)
        
        # OPTION 2: Use with mock client for testing without API
        class MockAPIClient:
            def submit_module(self, module_data):
                return {'status': 'success', 'queue_id': 'mock_123', 'module': module_data['module_name']}
            
            def submit_batch(self, module_results):
                return {
                    'total': len(module_results),
                    'successful': len(module_results),
                    'failed': 0,
                    'details': [{'module': m['module_name'], 'status': 'success'} for m in module_results]
                }
        
        strategy = RecursiveScanStrategy(
            max_depth=2,
            excluded_patterns=['test_*', '*_test', '__pycache__']
        )
        
        observer = APISubmitObserver(
            api_client=MockAPIClient(),
            enable_batch=True
        )
        
        scanner = ModuleScanner(
            scan_strategy=strategy,
            observers=[observer],
            batch_size=10
        )
        
        print(f"Scanning: {Path.cwd()}")
        modules = scanner.scan(Path('.'))
        print(f"\n✅ Discovered {len(modules)} modules (mock submission)")
