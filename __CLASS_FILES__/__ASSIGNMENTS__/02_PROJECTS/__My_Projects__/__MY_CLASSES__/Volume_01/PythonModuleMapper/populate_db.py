"""
Database Populator Script

Scans standard library modules and populates the database.
Bypasses the API/Queue system for direct population.
"""

import asyncio
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, Dict, Any

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from scanner import ScanModuleCommand
from workers import QueueProcessor, QueueStrategy, WorkerObserver
from models import DatabaseSessionFactory, UnitOfWork
from api import ModuleDiscoveryResult
from logger_config import get_logger

logger = get_logger("populate_db")

class DirectQueueStrategy(QueueStrategy):
    """Simple queue strategy for direct processing"""
    def __init__(self):
        self.items = []
        
    def enqueue(self, item: ModuleDiscoveryResult, priority: int = 1) -> str:
        self.items.append(item)
        return "direct_id"
        
    def dequeue(self) -> Optional[Tuple[ModuleDiscoveryResult, str]]:
        if not self.items:
            return None
        return (self.items.pop(0), "direct_id")
        
    def remove(self, queue_id: str) -> bool:
        return False
        
    def peek(self) -> Optional[ModuleDiscoveryResult]:
        if not self.items:
            return None
        return self.items[0]
        
    def get_stats(self) -> Dict[str, Any]:
        return {"size": len(self.items)}
        
    def is_empty(self) -> bool:
        return len(self.items) == 0

class LoggingObserver(WorkerObserver):
    def on_processing_start(self, module_name: str, worker_id: int):
        logger.debug(f"[Worker {worker_id}] Starting {module_name}")
    
    def on_processing_complete(self, module_name: str, worker_id: int, duration: float):
        logger.info(f"[Worker {worker_id}] Completed {module_name} in {duration:.2f}s")
    
    def on_processing_error(self, module_name: str, worker_id: int, error: str):
        logger.error(f"[Worker {worker_id}] Error processing {module_name}: {error}")
        
    def on_worker_started(self, worker_id: int): pass
    def on_worker_stopped(self, worker_id: int): pass

async def populate(db_path: Path = None):
    if db_path is None:
        db_path = Path("python_modules.db")
        
    logger.info(f"Populating database: {db_path}")
    
    # Setup components
    db_url = f"sqlite:///{db_path}"
    session_factory = DatabaseSessionFactory(db_url)
    
    # Create tables explicitly
    logger.info("Creating tables...")
    session_factory.create_tables()
    
    queue = DirectQueueStrategy()
    worker = QueueProcessor(queue, session_factory, observers=[LoggingObserver()])
    
    # Initialize DB tables
    # (DatabaseSessionFactory creates tables on init if using SQLite)
    
    # Scan modules
    # Comprehensive list of Standard Library modules
    modules_to_scan = [
        # Text Processing
        "string", "re", "difflib", "textwrap", "unicodedata", "stringprep", "readline", "rlcompleter",
        
        # Binary Data
        "struct", "codecs",
        
        # Data Types
        "datetime", "calendar", "collections", "heapq", "bisect", "array", "weakref", "types", "copy", "pprint", "reprlib", "enum",
        
        # Numeric and Math
        "numbers", "math", "cmath", "decimal", "fractions", "random", "statistics",
        
        # Functional Programming
        "itertools", "functools", "operator",
        
        # File and Directory Access
        "pathlib", "os.path", "fileinput", "stat", "filecmp", "tempfile", "glob", "fnmatch", "linecache", "shutil",
        
        # Data Persistence
        "pickle", "copyreg", "shelve", "marshal", "dbm", "sqlite3",
        
        # Data Compression
        "zlib", "gzip", "bz2", "lzma", "zipfile", "tarfile",
        
        # File Formats
        "csv", "configparser", "netrc", "xdrlib", "plistlib",
        
        # Cryptographic Services
        "hashlib", "hmac", "secrets",
        
        # Generic Operating System Services
        "os", "io", "time", "argparse", "getopt", "logging", "getpass", "curses", "platform", "errno", "ctypes",
        
        # Concurrent Execution
        "threading", "multiprocessing", "concurrent.futures", "subprocess", "sched", "queue", "contextvars",
        
        # Networking and Interprocess Communication
        "asyncio", "socket", "ssl", "select", "selectors", "asyncore", "asynchat", "signal", "mmap",
        
        # Internet Data Handling
        "email", "json", "mailcap", "mailbox", "mimetypes", "base64", "binhex", "binascii", "quopri", "uu",
        
        # Structured Markup Processing
        "html", "xml",
        
        # Internet Protocols
        "webbrowser", "cgi", "cgitb", "wsgiref", "urllib", "http", "ftplib", "poplib", "imaplib", "nntplib", "smtplib", "smtpd", "telnetlib", "uuid", "socketserver", "xmlrpc", "ipaddress",
        
        # Multimedia Services
        "audioop", "aifc", "sunau", "wave", "chunk", "colorsys", "imghdr", "sndhdr", "ossaudiodev",
        
        # Internationalization
        "gettext", "locale",
        
        # Program Frameworks
        "turtle", "cmd", "shlex",
        
        # Graphical User Interfaces with Tk
        "tkinter",
        
        # Development Tools
        "typing", "pydoc", "doctest", "unittest", "test",
        
        # Debugging and Profiling
        "bdb", "faulthandler", "pdb", "timeit", "trace", "tracemalloc",
        
        # Software Packaging and Distribution
        "distutils", "ensurepip", "venv", "zipapp",
        
        # Python Runtime Services
        "sys", "sysconfig", "builtins", "warnings", "dataclasses", "contextlib", "abc", "atexit", "traceback", "future_builtins", "gc", "inspect", "site",
        
        # Custom Python Interpreters
        "code", "codeop",
        
        # Importing Modules
        "zipimport", "pkgutil", "modulefinder", "runpy", "importlib",
        
        # Python Language Services
        "parser", "ast", "symtable", "symbol", "token", "keyword", "tokenize", "tabnanny", "pyclbr", "py_compile", "compileall", "dis", "pickletools"
    ]
    
    logger.info(f"Scanning {len(modules_to_scan)} standard library modules...")
    
    for mod_name in modules_to_scan:
        logger.info(f"Scanning {mod_name}...")
        command = ScanModuleCommand(mod_name)
        result = command.execute()
        
        if not result['success']:
            logger.error(f"Error scanning {mod_name}: {result.get('error')}")
            continue
            
        data = result['data']
        
        # Create ModuleDiscoveryResult
        discovery = ModuleDiscoveryResult(
            module_name=data['module_name'],
            filepath=data['filepath'],
            is_package=data['is_package'],
            discovered_at=str(data['discovered_at']),
            checksum=data['checksum'],
            classes=data['classes'],
            functions=data['functions'],
            imports=data.get('imports', []), # Use extracted imports
            scanner_version="1.0.0", # Default version
            docstring=data.get('docstring')
        )
        
        # Add to queue
        queue.enqueue(discovery)
        
    # Process queue
    logger.info("Processing results...")
    count = 0
    while True:
        processed = await worker.process_one(worker_id=1)
        if not processed:
            break
        count += 1
        logger.info(f"Processed module {count}")
        
    logger.info(f"Done! Populated {count} modules.")

if __name__ == "__main__":
    asyncio.run(populate())
