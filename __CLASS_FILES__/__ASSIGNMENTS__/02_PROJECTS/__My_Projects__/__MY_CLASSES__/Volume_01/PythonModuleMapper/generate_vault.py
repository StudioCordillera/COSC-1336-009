"""
Vault Generator Script

Generates the full Obsidian vault from the database.
Uses ObsidianMCPVaultBuilder to generate content and writes directly to the file system.
"""

import os
from pathlib import Path
from obsidian_mcp_vault import ObsidianMCPVaultBuilder
from models import DatabaseSessionFactory, UnitOfWork
from canvas_builder import CanvasBuilder, CanvasLayout
from logger_config import get_logger

logger = get_logger("generate_vault")

def main(db_path: Path = None, vault_root: Path = None):
    # Configuration
    if db_path is None:
        db_path = Path("python_modules.db")
    
    if vault_root is None:
        # Default to local PythonModules directory in the project folder
        vault_root = Path(__file__).parent / "PythonModules"
    
    logger.info(f"Database: {db_path}")
    logger.info(f"Vault Root: {vault_root}")
    
    if not db_path.exists():
        logger.error("Error: Database not found!")
        return

    # Create vault directories
    for subdir in ["Modules", "Classes", "Functions", "Taxonomy"]:
        (vault_root / subdir).mkdir(parents=True, exist_ok=True)
        
    # Initialize builder
    db_url = f"sqlite:///{db_path}"
    session_factory = DatabaseSessionFactory(db_url)
    builder = ObsidianMCPVaultBuilder(session_factory)
    
    # Define Module Categories for Layout
    MODULE_CATEGORIES = {
        "Text Processing": ["string", "re", "difflib", "textwrap", "unicodedata", "stringprep", "readline", "rlcompleter"],
        "Binary Data": ["struct", "codecs"],
        "Data Types": ["datetime", "calendar", "collections", "heapq", "bisect", "array", "weakref", "types", "copy", "pprint", "reprlib", "enum"],
        "Numeric": ["numbers", "math", "cmath", "decimal", "fractions", "random", "statistics"],
        "Functional": ["itertools", "functools", "operator"],
        "Files": ["pathlib", "os.path", "fileinput", "stat", "filecmp", "tempfile", "glob", "fnmatch", "linecache", "shutil"],
        "Persistence": ["pickle", "copyreg", "shelve", "marshal", "dbm", "sqlite3"],
        "Compression": ["zlib", "gzip", "bz2", "lzma", "zipfile", "tarfile"],
        "File Formats": ["csv", "configparser", "netrc", "xdrlib", "plistlib"],
        "Crypto": ["hashlib", "hmac", "secrets"],
        "System": ["os", "io", "time", "argparse", "getopt", "logging", "getpass", "curses", "platform", "errno", "ctypes", "sys", "sysconfig", "builtins", "warnings", "dataclasses", "contextlib", "abc", "atexit", "traceback", "future_builtins", "gc", "inspect", "site"],
        "Concurrency": ["threading", "multiprocessing", "concurrent", "subprocess", "sched", "queue", "contextvars"],
        "Networking": ["asyncio", "socket", "ssl", "select", "selectors", "asyncore", "asynchat", "signal", "mmap", "ipaddress"],
        "Internet Data": ["email", "json", "mailcap", "mailbox", "mimetypes", "base64", "binhex", "binascii", "quopri", "uu"],
        "Markup": ["html", "xml"],
        "Internet Protocols": ["webbrowser", "cgi", "cgitb", "wsgiref", "urllib", "http", "ftplib", "poplib", "imaplib", "nntplib", "smtplib", "smtpd", "telnetlib", "uuid", "socketserver", "xmlrpc"],
        "Multimedia": ["audioop", "aifc", "sunau", "wave", "chunk", "colorsys", "imghdr", "sndhdr", "ossaudiodev"],
        "I18n": ["gettext", "locale"],
        "Frameworks": ["turtle", "cmd", "shlex"],
        "GUI": ["tkinter"],
        "Dev Tools": ["typing", "pydoc", "doctest", "unittest", "test"],
        "Debug": ["bdb", "faulthandler", "pdb", "timeit", "trace", "tracemalloc"],
        "Distribution": ["distutils", "ensurepip", "venv", "zipapp"],
        "Interpreters": ["code", "codeop"],
        "Importing": ["zipimport", "pkgutil", "modulefinder", "runpy", "importlib"],
        "Language": ["parser", "ast", "symtable", "symbol", "token", "keyword", "tokenize", "tabnanny", "pyclbr", "py_compile", "compileall", "dis", "pickletools"]
    }
    
    # Reverse map for easy lookup
    MODULE_TO_CATEGORY = {}
    for cat, mods in MODULE_CATEGORIES.items():
        for mod in mods:
            MODULE_TO_CATEGORY[mod] = cat
            # Also handle submodules roughly
            MODULE_TO_CATEGORY[mod.split('.')[0]] = cat

    # Generate notes
    logger.info("Generating notes...")
    all_notes = builder.get_all_notes()
    
    # Write notes to disk using MCP/API integration
    total_written = 0
    total_failed = 0
    
    def write_locally(filename, content):
        try:
            full_path = vault_root / filename
            full_path.parent.mkdir(parents=True, exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            logger.error(f"Failed to write {filename}: {e}")
            return False

    for category, notes in all_notes.items():
        logger.info(f"Writing {category}...")
        for note in notes:
            # note is a dict with 'filename', 'content', 'name'
            # filename is relative, e.g., "Modules/math.md"
            
            # Write directly to disk
            if write_locally(note['filename'], note['content']):
                total_written += 1
            else:
                total_failed += 1
                
    logger.info(f"\nSuccess! Written {total_written} notes to {vault_root}")
    if total_failed > 0:
        logger.warning(f"Failed to write {total_failed} notes")

    # Generate Canvases
    logger.info("\nGenerating Canvases...")
    
    # 1. Overview Canvas (All Modules)
    logger.info("Generating Overview.canvas...")
    overview_builder = CanvasBuilder()
    
    with UnitOfWork(session_factory) as uow:
        modules = uow.repositories['module'].get_all()
        
        # Group modules by category
        grouped_modules = {}
        for module in modules:
            # Find category
            cat = "Uncategorized"
            # Try exact match
            if module.name in MODULE_TO_CATEGORY:
                cat = MODULE_TO_CATEGORY[module.name]
            else:
                # Try prefix match
                parts = module.name.split('.')
                if parts[0] in MODULE_TO_CATEGORY:
                    cat = MODULE_TO_CATEGORY[parts[0]]
            
            if cat not in grouped_modules:
                grouped_modules[cat] = []
            grouped_modules[cat].append(module)
            
        # Layout groups
        # We'll place groups in a grid, and modules inside groups in a grid
        
        group_cols = 4
        group_width = 1500
        group_height = 1000
        group_padding = 200
        
        current_group_idx = 0
        
        for category, cat_modules in grouped_modules.items():
            # Calculate group position
            gx = (current_group_idx % group_cols) * (group_width + group_padding)
            gy = (current_group_idx // group_cols) * (group_height + group_padding)
            
            # Create a group node (Canvas doesn't strictly have "Group" nodes in the JSON spec exposed here easily, 
            # but we can simulate it by placing a text node or just clustering)
            # Actually, Canvas DOES have group nodes, but our builder might not support it yet.
            # Let's just place a big label node
            
            label_id = overview_builder.add_text_node(f"# {category}", gx, gy - 100, width=group_width, height=80)
            
            # Layout modules within this group area
            # Simple grid within the group box
            mod_cols = 3
            mod_w = 400
            mod_h = 200
            mod_pad = 50
            
            for i, module in enumerate(cat_modules):
                mx = gx + (i % mod_cols) * (mod_w + mod_pad)
                my = gy + (i // mod_cols) * (mod_h + mod_pad)
                
                file_path = f"Modules/{module.name}.md"
                node_id = overview_builder.add_file_node(file_path, mx, my, width=mod_w, height=mod_h)
            
            current_group_idx += 1
            
        # Add edges for imports
        relationships = uow.repositories['relationship'].get_all()
        for rel in relationships:
            if rel.relationship_type == 'imports' and rel.from_type == 'module' and rel.to_type == 'module':
                from_mod = uow.repositories['module'].get_by_id(rel.from_id)
                to_mod = uow.repositories['module'].get_by_id(rel.to_id)
                
                if from_mod and to_mod:
                    from_path = f"Modules/{from_mod.name}.md"
                    to_path = f"Modules/{to_mod.name}.md"
                    
                    from_id = overview_builder.get_node_id(from_path)
                    to_id = overview_builder.get_node_id(to_path)
                    
                    if from_id and to_id:
                        overview_builder.add_edge(from_id, to_id, label="imports", color="#888888")
    
    # Write Overview Canvas
    # Use API to write canvas
    overview_content = overview_builder.to_json()
    if write_locally("Overview.canvas", overview_content):
        logger.info(f"[OK] Written Overview.canvas")
    else:
        logger.error(f"[FAIL] Failed to write Overview.canvas")

    # 2. Module Detail Canvases
    logger.info("Generating Module Canvases...")
    count = 0
    
    with UnitOfWork(session_factory) as uow:
        modules = uow.repositories['module'].get_all()
        
        for module in modules:
            mod_builder = CanvasBuilder()
            
            # Center: Module Note
            mod_path = f"Modules/{module.name}.md"
            center_id = mod_builder.add_file_node(mod_path, 0, 0, width=600, height=400, color="#2c3e50")
            
            # Surrounding: Classes
            classes = uow.repositories['class'].get_by_module(module.id)
            if classes:
                class_positions = CanvasLayout.circle(0, 0, radius=800, count=len(classes))
                
                for i, cls in enumerate(classes):
                    pos = class_positions[i]
                    cls_path = f"Classes/{cls.name}.md"
                    cls_id = mod_builder.add_file_node(cls_path, pos['x'], pos['y'], width=400, height=300, color="#e67e22")
                    
                    # Link Module -> Class
                    mod_builder.add_edge(center_id, cls_id, label="defines")
                    
                    # Methods for this class
                    methods = uow.repositories['function'].get_by_class(cls.id)
                    if methods:
                        # Place methods in a smaller circle around the class
                        # This might get crowded, so let's just list them or place them below
                        # For now, let's skip methods on the canvas to avoid clutter, 
                        # or maybe just add the first few
                        pass

            # Functions (standalone)
            functions = [f for f in uow.repositories['function'].get_by_module(module.id) if not f.class_id]
            if functions:
                # Place functions in a circle further out or in a separate cluster
                func_positions = CanvasLayout.circle(0, 0, radius=1200, count=len(functions))
                
                for i, func in enumerate(functions):
                    pos = func_positions[i]
                    func_path = f"Functions/{func.name}_{func.id}.md"
                    func_id = mod_builder.add_file_node(func_path, pos['x'], pos['y'], width=400, height=200, color="#27ae60")
                    
                    # Link Module -> Function
                    mod_builder.add_edge(center_id, func_id, label="defines")

            # Write Module Canvas
            canvas_filename = f"Modules/{module.name}.canvas"
            canvas_content = mod_builder.to_json()
            
            if write_locally(canvas_filename, canvas_content):
                count += 1
            else:
                logger.error(f"Failed to write canvas for {module.name}")
            
    logger.info(f"[OK] Written {count} module canvases")

if __name__ == "__main__":
    main()
