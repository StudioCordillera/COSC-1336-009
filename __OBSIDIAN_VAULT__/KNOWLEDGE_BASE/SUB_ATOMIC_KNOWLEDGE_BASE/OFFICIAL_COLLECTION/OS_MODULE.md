# OS_MODULE

## Core Definition
**os module** provides portable way to use operating system dependent functionality. Essential for file/directory operations, path manipulation, environment variables, and process management.

**Tags**: #os #module #file-system #path #environment #process

---

## COMPLETE OS MODULE QUICK REFERENCE

### OS MODULE METHODS - Target | Operation | Output

```python
import os

# ═══════════════════════════════════════════════════════════════════════════
# DIRECTORY OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
os.getcwd()                  # None | Get current working directory | Returns absolute path string
os.chdir(path)               # Path string | Change working directory | Returns None (or raises OSError)
os.mkdir(path)               # Path string | Create single directory | Returns None (or raises FileExistsError)
os.mkdir(path, mode=0o777)   # Path + permissions | Create dir with perms | Returns None
os.makedirs(path)            # Path string | Create nested directories | Returns None (creates all parents)
os.makedirs(path, exist_ok=True) # Path | Create if not exists | Returns None (no error if exists)
os.rmdir(path)               # Path string | Remove empty directory | Returns None (or raises OSError)
os.removedirs(path)          # Path string | Remove nested empty dirs | Returns None (removes parents too)
os.listdir(path='.')         # Path string | List directory contents | Returns list of names (strings)
os.scandir(path='.')         # Path string | Iterate directory entries | Returns iterator of DirEntry objects
os.walk(top)                 # Path string | Walk directory tree | Yields (dirpath, dirnames, filenames) tuples
os.walk(top, topdown=False)  # Path string | Walk bottom-up | Yields tuples bottom-up

# ═══════════════════════════════════════════════════════════════════════════
# FILE OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
os.remove(path)              # File path | Delete file | Returns None (or raises FileNotFoundError)
os.unlink(path)              # File path | Delete file (alias) | Returns None
os.rename(src, dst)          # Two paths | Rename/move file/dir | Returns None (or raises OSError)
os.replace(src, dst)         # Two paths | Rename/move (overwrite) | Returns None (works cross-platform)
os.stat(path)                # Path string | Get file/dir info | Returns os.stat_result object
os.path.getsize(path)        # File path | Get file size | Returns int (bytes)
os.path.getmtime(path)       # Path string | Get modification time | Returns float (timestamp)
os.path.getatime(path)       # Path string | Get access time | Returns float (timestamp)
os.path.getctime(path)       # Path string | Get creation time | Returns float (timestamp)
os.access(path, mode)        # Path + mode | Check file permissions | Returns True/False
os.chmod(path, mode)         # Path + mode | Change file permissions | Returns None
os.chown(path, uid, gid)     # Path + IDs | Change owner (Unix) | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# PATH CHECKING OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
os.path.exists(path)         # Path string | Check if exists | Returns True/False
os.path.isfile(path)         # Path string | Check if regular file | Returns True/False
os.path.isdir(path)          # Path string | Check if directory | Returns True/False
os.path.islink(path)         # Path string | Check if symbolic link | Returns True/False
os.path.isabs(path)          # Path string | Check if absolute path | Returns True/False
os.path.ismount(path)        # Path string | Check if mount point | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# PATH MANIPULATION OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
os.path.join(path1, path2, ...) # Path parts | Join path components | Returns combined path string
os.path.split(path)          # Path string | Split into dir + file | Returns (head, tail) tuple
os.path.splitext(path)       # Path string | Split extension | Returns (root, ext) tuple
os.path.splitdrive(path)     # Path string | Split drive letter | Returns (drive, tail) tuple
os.path.dirname(path)        # Path string | Get directory name | Returns directory path string
os.path.basename(path)       # Path string | Get file/dir name | Returns name string
os.path.abspath(path)        # Path string | Get absolute path | Returns absolute path string
os.path.relpath(path, start) # Two paths | Get relative path | Returns relative path string
os.path.realpath(path)       # Path string | Resolve symbolic links | Returns resolved absolute path
os.path.normpath(path)       # Path string | Normalize path | Returns normalized path string
os.path.normcase(path)       # Path string | Normalize case | Returns case-normalized path
os.path.expanduser(path)     # Path string | Expand ~ to home dir | Returns expanded path string
os.path.expandvars(path)     # Path string | Expand env variables | Returns expanded path string
os.path.commonpath(paths)    # List of paths | Find common base path | Returns common path string
os.path.commonprefix(paths)  # List of paths | Find common prefix | Returns prefix string

# ═══════════════════════════════════════════════════════════════════════════
# ENVIRONMENT VARIABLES
# ═══════════════════════════════════════════════════════════════════════════
os.environ                   # None | Access all env vars | Returns dict-like object
os.environ['VAR']            # Var name | Get env variable | Returns value string (or KeyError)
os.environ.get('VAR')        # Var name | Get env var safely | Returns value or None
os.environ.get('VAR', default) # Var name + default | Get with fallback | Returns value or default
os.getenv('VAR')             # Var name | Get env variable | Returns value or None
os.getenv('VAR', default)    # Var name + default | Get with fallback | Returns value or default
os.environ['VAR'] = 'value'  # Var name + value | Set env variable | Returns None
os.putenv('VAR', 'value')    # Var name + value | Set env var (legacy) | Returns None
os.unsetenv('VAR')           # Var name | Remove env variable | Returns None
os.environb                  # None | Access env vars as bytes | Returns dict-like bytes object

# ═══════════════════════════════════════════════════════════════════════════
# PROCESS OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
os.system(command)           # Command string | Execute shell command | Returns exit code int
os.getpid()                  # None | Get current process ID | Returns int PID
os.getppid()                 # None | Get parent process ID | Returns int PID
os.kill(pid, signal)         # PID + signal | Send signal to process | Returns None
os._exit(n)                  # Exit code | Exit immediately | Does not return (exits)
os.abort()                   # None | Generate SIGABRT | Does not return (aborts)

# ═══════════════════════════════════════════════════════════════════════════
# SYSTEM INFORMATION
# ═══════════════════════════════════════════════════════════════════════════
os.name                      # None | Get OS name | Returns 'posix', 'nt', 'java'
os.uname()                   # None (Unix) | Get system info | Returns uname_result tuple
os.cpu_count()               # None | Get CPU count | Returns int or None
os.getlogin()                # None | Get login name | Returns string username
os.sep                       # None | Get path separator | Returns '/' or '\\'
os.pathsep                   # None | Get PATH separator | Returns ':' or ';'
os.linesep                   # None | Get line separator | Returns '\n' or '\r\n'
os.devnull                   # None | Get null device path | Returns '/dev/null' or 'nul'
os.curdir                    # None | Get current dir symbol | Returns '.'
os.pardir                    # None | Get parent dir symbol | Returns '..'

# ═══════════════════════════════════════════════════════════════════════════
# FILE DESCRIPTOR OPERATIONS (Lower Level)
# ═══════════════════════════════════════════════════════════════════════════
os.open(path, flags)         # Path + flags | Open file (low level) | Returns int file descriptor
os.close(fd)                 # File descriptor | Close file | Returns None
os.read(fd, n)               # FD + bytes | Read n bytes | Returns bytes object
os.write(fd, data)           # FD + bytes | Write bytes | Returns int bytes written
os.lseek(fd, pos, how)       # FD + position | Seek in file | Returns new position int
os.dup(fd)                   # File descriptor | Duplicate FD | Returns new FD int
os.dup2(fd, fd2)             # Two FDs | Duplicate to specific FD | Returns None
os.pipe()                    # None | Create pipe | Returns (read_fd, write_fd) tuple
os.fsync(fd)                 # File descriptor | Force write to disk | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# PERMISSION & MODE CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════
os.F_OK                      # Constant | Check existence | Value 0
os.R_OK                      # Constant | Check read permission | Value 4
os.W_OK                      # Constant | Check write permission | Value 2
os.X_OK                      # Constant | Check execute permission | Value 1
os.O_RDONLY                  # Constant | Open read-only | Flag value
os.O_WRONLY                  # Constant | Open write-only | Flag value
os.O_RDWR                    # Constant | Open read-write | Flag value
os.O_CREAT                   # Constant | Create if not exists | Flag value
os.O_EXCL                    # Constant | Fail if exists | Flag value
os.O_TRUNC                   # Constant | Truncate to zero | Flag value
os.O_APPEND                  # Constant | Append mode | Flag value

# ═══════════════════════════════════════════════════════════════════════════
# STAT RESULT ATTRIBUTES
# ═══════════════════════════════════════════════════════════════════════════
stat_result.st_mode          # stat_result | File mode/permissions | Returns int
stat_result.st_ino           # stat_result | Inode number | Returns int
stat_result.st_dev           # stat_result | Device ID | Returns int
stat_result.st_nlink         # stat_result | Number of hard links | Returns int
stat_result.st_uid           # stat_result | User ID of owner | Returns int
stat_result.st_gid           # stat_result | Group ID of owner | Returns int
stat_result.st_size          # stat_result | File size in bytes | Returns int
stat_result.st_atime         # stat_result | Last access time | Returns float timestamp
stat_result.st_mtime         # stat_result | Last modification time | Returns float timestamp
stat_result.st_ctime         # stat_result | Creation/change time | Returns float timestamp

# ═══════════════════════════════════════════════════════════════════════════
# CSV FILE I/O WITH DICTIONARIES (import csv)
# ═══════════════════════════════════════════════════════════════════════════
csv.DictReader(file)         # File object | Read CSV as dictionaries | Returns iterator of dicts (row dicts)
csv.DictWriter(file, fields) # File + fields | Write dicts to CSV | Returns DictWriter object
csv.reader(file)             # File object | Read CSV as lists | Returns iterator of lists
csv.writer(file)             # File object | Write lists to CSV | Returns writer object
writer.writeheader()         # DictWriter | Write header row | Returns None
writer.writerow(dict)        # DictWriter + dict | Write single row | Returns None
writer.writerows(dicts)      # DictWriter + list | Write multiple rows | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# JSON FILE I/O WITH DICTIONARIES (import json)
# ═══════════════════════════════════════════════════════════════════════════
json.load(file)              # File object | Read JSON to dict/list | Returns Python object
json.loads(string)           # JSON string | Parse JSON string | Returns Python object
json.dump(obj, file)         # Object + file | Write object to JSON | Returns None
json.dump(obj, file, indent=2) # Object + file | Write formatted JSON | Returns None
json.dumps(obj)              # Python object | Convert to JSON string | Returns JSON string
json.dumps(obj, indent=2)    # Object + indent | Format JSON string | Returns formatted string

# ═══════════════════════════════════════════════════════════════════════════
# TEXT FILE I/O PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
open(path, 'r')              # Path + mode | Open for reading | Returns file object
open(path, 'w')              # Path + mode | Open for writing (overwrite) | Returns file object
open(path, 'a')              # Path + mode | Open for appending | Returns file object
open(path, 'r+')             # Path + mode | Open for read/write | Returns file object
file.read()                  # File object | Read entire file | Returns string
file.readline()              # File object | Read single line | Returns string
file.readlines()             # File object | Read all lines | Returns list of strings
file.write(text)             # File + text | Write string to file | Returns int (chars written)
file.writelines(lines)       # File + list | Write list of strings | Returns None
with open(path) as f:        # Context manager | Auto-close file | Yields file object

# ═══════════════════════════════════════════════════════════════════════════
# FILE I/O INTEGRATION PATTERNS (Covered in Detail Below)
# ═══════════════════════════════════════════════════════════════════════════
# Pattern: Read CSV → Dictionary (by ID key)
# Pattern: Write Dictionary → CSV file
# Pattern: Append to CSV file
# Pattern: Read/Write JSON ↔ Dictionary
# Pattern: Merge multiple JSON files
# Pattern: Process multiple text files in loop
# Pattern: Read all files in directory → Dictionary
# Pattern: Write dictionary entries → Separate files
# Pattern: Batch process files with custom function
# Pattern: Recursive file tree → Nested dictionary
# Pattern: Student database (load/save/search/update)
# Pattern: Log file operations (append/parse/rotate)
# Pattern: Config file management (read/write key=value)
# Pattern: Project structure validation
```

### COMMON OPERATION EXAMPLES

```python
import os

# Current directory
os.getcwd()                  # → "C:\\Users\\name\\project"

# Directory operations
os.mkdir("new_folder")
os.makedirs("path/to/nested/folder", exist_ok=True)
os.listdir(".")              # → ['file1.txt', 'folder1', 'file2.py']

# Path operations
os.path.join("folder", "file.txt")  # → "folder\\file.txt" (Windows) or "folder/file.txt" (Unix)
os.path.exists("file.txt")   # → True/False
os.path.isfile("data.csv")   # → True
os.path.isdir("folder")      # → True

# Path manipulation
os.path.split("C:\\folder\\file.txt")     # → ("C:\\folder", "file.txt")
os.path.splitext("data.csv")              # → ("data", ".csv")
os.path.basename("C:\\folder\\file.txt")  # → "file.txt"
os.path.dirname("C:\\folder\\file.txt")   # → "C:\\folder"

# Environment variables
os.environ['PATH']           # → "C:\\Windows\\system32;..."
os.getenv('USERNAME')        # → "YourUsername"
os.environ['MY_VAR'] = 'value'

# File info
os.path.getsize("file.txt")  # → 1024 (bytes)
stat_info = os.stat("file.txt")
stat_info.st_size            # → 1024
```

---

## DETAILED OS OPERATIONS

### 1. DIRECTORY NAVIGATION & MANAGEMENT

```python
import os

# Get current directory
current_dir = os.getcwd()
print(current_dir)           # → "C:\\Users\\name\\project"

# Change directory
os.chdir("C:\\Users\\name\\Documents")
os.chdir("..")               # Go up one level
os.chdir("subfolder")        # Go into subfolder

# Create directories
os.mkdir("new_folder")       # Single directory
os.makedirs("path/to/nested/folders")  # Create all intermediate dirs

# Create directory if not exists (no error)
if not os.path.exists("output"):
    os.mkdir("output")

# Better way (Python 3.2+)
os.makedirs("output", exist_ok=True)

# Remove directories
os.rmdir("empty_folder")     # Remove empty directory only
os.removedirs("path/to/empty/folders")  # Remove empty nested dirs

# List directory contents
files = os.listdir(".")      # Returns ['file1.txt', 'folder1', 'file2.py']
files = os.listdir("C:\\Users")  # List specific directory

# Filter listings
files = [f for f in os.listdir(".") if f.endswith('.txt')]
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
```

### 2. PATH MANIPULATION

```python
import os

# Join paths (cross-platform)
path = os.path.join("folder", "subfolder", "file.txt")
# Windows: "folder\\subfolder\\file.txt"
# Unix:    "folder/subfolder/file.txt"

# Split paths
directory, filename = os.path.split("C:\\folder\\file.txt")
# directory → "C:\\folder"
# filename → "file.txt"

# Split extension
name, ext = os.path.splitext("data.csv")
# name → "data"
# ext → ".csv"

# Split drive (Windows)
drive, path = os.path.splitdrive("C:\\folder\\file.txt")
# drive → "C:"
# path → "\\folder\\file.txt"

# Get components
os.path.basename("C:\\folder\\file.txt")  # → "file.txt"
os.path.dirname("C:\\folder\\file.txt")   # → "C:\\folder"

# Absolute path
rel_path = "subfolder/file.txt"
abs_path = os.path.abspath(rel_path)
# → "C:\\Users\\name\\project\\subfolder\\file.txt"

# Normalize paths
os.path.normpath("folder/../file.txt")    # → "file.txt"
os.path.normpath("folder/./subfolder")    # → "folder\\subfolder"

# Expand user home directory
os.path.expanduser("~/documents")
# Windows: "C:\\Users\\username\\documents"
# Unix:    "/home/username/documents"

# Relative path
os.path.relpath("C:\\Users\\name\\docs\\file.txt", "C:\\Users\\name")
# → "docs\\file.txt"
```

### 3. PATH CHECKING

```python
import os

# Check existence
if os.path.exists("file.txt"):
    print("File exists")

# Check type
if os.path.isfile("data.csv"):
    print("Is a file")

if os.path.isdir("folder"):
    print("Is a directory")

if os.path.islink("symlink"):
    print("Is a symbolic link")

# Check if absolute path
os.path.isabs("C:\\folder\\file.txt")  # → True (Windows)
os.path.isabs("folder/file.txt")       # → False (relative)

# Check permissions
if os.access("file.txt", os.R_OK):
    print("Readable")

if os.access("file.txt", os.W_OK):
    print("Writable")

if os.access("script.py", os.X_OK):
    print("Executable")

# Combined check
if os.access("file.txt", os.R_OK | os.W_OK):
    print("Read and write access")
```

### 4. FILE OPERATIONS

```python
import os

# Get file info
size = os.path.getsize("file.txt")  # Bytes
mtime = os.path.getmtime("file.txt")  # Modification timestamp
atime = os.path.getatime("file.txt")  # Access timestamp
ctime = os.path.getctime("file.txt")  # Creation timestamp

# Convert timestamp to readable format
from datetime import datetime
mtime = os.path.getmtime("file.txt")
readable = datetime.fromtimestamp(mtime)
print(readable)  # → "2025-01-15 14:30:00"

# Detailed file info
stat_info = os.stat("file.txt")
print(f"Size: {stat_info.st_size} bytes")
print(f"Modified: {datetime.fromtimestamp(stat_info.st_mtime)}")
print(f"Owner UID: {stat_info.st_uid}")
print(f"Permissions: {oct(stat_info.st_mode)}")

# Rename/Move file
os.rename("old_name.txt", "new_name.txt")
os.rename("file.txt", "backup/file.txt")  # Move to different folder

# Replace (overwrites destination)
os.replace("source.txt", "destination.txt")

# Delete file
os.remove("file.txt")
os.unlink("file.txt")  # Same as remove

# Delete file safely
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
```

### 5. DIRECTORY WALKING

```python
import os

# Walk directory tree (top-down)
for dirpath, dirnames, filenames in os.walk("project"):
    print(f"Directory: {dirpath}")
    print(f"  Subdirectories: {dirnames}")
    print(f"  Files: {filenames}")
    
# Example output:
# Directory: project
#   Subdirectories: ['src', 'tests']
#   Files: ['README.md', 'main.py']
# Directory: project/src
#   Subdirectories: []
#   Files: ['module1.py', 'module2.py']

# Find all Python files
python_files = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename.endswith('.py'):
            full_path = os.path.join(dirpath, filename)
            python_files.append(full_path)

# Walk bottom-up (process files before directories)
for dirpath, dirnames, filenames in os.walk("project", topdown=False):
    # Process files first, then directories
    for filename in filenames:
        print(os.path.join(dirpath, filename))

# Skip certain directories
for dirpath, dirnames, filenames in os.walk("."):
    # Remove directories you want to skip (modifies dirnames in-place)
    dirnames[:] = [d for d in dirnames if d not in ['__pycache__', '.git', 'venv']]
    
    for filename in filenames:
        print(os.path.join(dirpath, filename))

# Using scandir (more efficient for large directories)
with os.scandir(".") as entries:
    for entry in entries:
        if entry.is_file():
            print(f"File: {entry.name}, Size: {entry.stat().st_size}")
        elif entry.is_dir():
            print(f"Directory: {entry.name}")
```

### 6. ENVIRONMENT VARIABLES

```python
import os

# Access all environment variables (dict-like)
env = os.environ
print(type(env))  # → <class 'os._Environ'>

# Get specific variable
path = os.environ['PATH']
user = os.environ['USERNAME']  # Windows
user = os.environ['USER']      # Unix/Linux

# Get safely (no KeyError)
home = os.environ.get('HOME')  # Returns None if not exists
home = os.environ.get('HOME', '/default/home')  # With default

# Using getenv (preferred)
python_path = os.getenv('PYTHONPATH')
python_path = os.getenv('PYTHONPATH', 'default/path')

# Set environment variable
os.environ['MY_APP_CONFIG'] = '/path/to/config'
os.environ['DEBUG'] = 'True'

# Check if variable exists
if 'VIRTUAL_ENV' in os.environ:
    print("Running in virtual environment")

# Remove environment variable
if 'TEMP_VAR' in os.environ:
    del os.environ['TEMP_VAR']

# Iterate all environment variables
for key, value in os.environ.items():
    print(f"{key} = {value}")

# Common environment variables
print(os.getenv('HOME'))       # Home directory
print(os.getenv('PATH'))       # Executable search path
print(os.getenv('PYTHONPATH')) # Python module search path
print(os.getenv('TEMP'))       # Temp directory (Windows)
print(os.getenv('TMP'))        # Temp directory (Unix)
```

### 7. SYSTEM INFORMATION

```python
import os

# Operating system name
print(os.name)
# 'posix' → Unix/Linux/MacOS
# 'nt' → Windows
# 'java' → Jython

# Platform-specific code
if os.name == 'nt':
    # Windows-specific code
    print("Running on Windows")
else:
    # Unix/Linux/Mac code
    print("Running on Unix-like system")

# Path separator
print(os.sep)
# Windows: '\\'
# Unix: '/'

# PATH environment variable separator
print(os.pathsep)
# Windows: ';'
# Unix: ':'

# Line separator
print(repr(os.linesep))
# Windows: '\r\n'
# Unix: '\n'

# Current and parent directory symbols
print(os.curdir)   # → '.'
print(os.pardir)   # → '..'

# Null device
print(os.devnull)
# Windows: 'nul'
# Unix: '/dev/null'

# CPU count
cpu_count = os.cpu_count()
print(f"CPU cores: {cpu_count}")

# Process ID
pid = os.getpid()
ppid = os.getppid()
print(f"Current PID: {pid}")
print(f"Parent PID: {ppid}")

# Login name
username = os.getlogin()
print(f"Logged in as: {username}")

# Unix system info (Unix only)
if os.name == 'posix':
    info = os.uname()
    print(f"System: {info.sysname}")
    print(f"Node: {info.nodename}")
    print(f"Release: {info.release}")
    print(f"Version: {info.version}")
    print(f"Machine: {info.machine}")
```

### 8. EXECUTING SYSTEM COMMANDS

```python
import os

# Execute shell command (simple)
exit_code = os.system('dir')  # Windows
exit_code = os.system('ls')   # Unix

# Check exit code
if exit_code == 0:
    print("Command succeeded")
else:
    print(f"Command failed with code {exit_code}")

# Execute multiple commands
os.system('cd folder && dir')  # Windows
os.system('cd folder && ls')   # Unix

# Better way: use subprocess module (preferred)
import subprocess

# Run command and capture output
result = subprocess.run(['python', '--version'], capture_output=True, text=True)
print(result.stdout)

# Run command with shell
subprocess.run('dir *.txt', shell=True)

# Run and get output
output = subprocess.check_output(['python', '--version'], text=True)
print(output)
```

---

## PRACTICAL PROJECT PATTERNS

### Pattern 1: File Organization Script
```python
import os

def organize_files_by_extension(directory):
    """Organize files into folders by extension"""
    os.chdir(directory)
    
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            # Get extension
            name, ext = os.path.splitext(filename)
            
            if ext:
                # Create folder for extension
                folder = ext[1:]  # Remove the dot
                os.makedirs(folder, exist_ok=True)
                
                # Move file
                new_path = os.path.join(folder, filename)
                os.rename(filename, new_path)
                print(f"Moved {filename} to {folder}/")

# Usage
organize_files_by_extension("C:\\Downloads")
```

### Pattern 2: Find Files Recursively
```python
import os

def find_files(directory, extension):
    """Find all files with specific extension"""
    found_files = []
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                full_path = os.path.join(dirpath, filename)
                found_files.append(full_path)
    
    return found_files

# Find all Python files
py_files = find_files("C:\\Projects", ".py")
for file in py_files:
    print(file)

# Find multiple extensions
def find_files_multi(directory, extensions):
    """Find files with multiple extensions"""
    found_files = []
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                full_path = os.path.join(dirpath, filename)
                found_files.append(full_path)
    
    return found_files

# Usage
data_files = find_files_multi("C:\\Project", [".csv", ".json", ".xlsx"])
```

### Pattern 3: Safe File Operations
```python
import os

def safe_delete(filepath):
    """Safely delete file with confirmation"""
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
    
    if not os.path.isfile(filepath):
        print(f"Not a file: {filepath}")
	        return False
    
    try:
        os.remove(filepath)
        print(f"Deleted: {filepath}")
        return True
    except PermissionError:
        print(f"Permission denied: {filepath}")
        return False
    except Exception as e:
        print(f"Error deleting {filepath}: {e}")
        return False

def safe_create_directory(directory):
    """Create directory if not exists"""
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except PermissionError:
        print(f"Permission denied: {directory}")
        return False
    except Exception as e:
        print(f"Error creating {directory}: {e}")
        return False
```

### Pattern 4: Path Building
```python
import os

def build_project_path(*parts):
    """Build path relative to project root"""
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Build path
    full_path = os.path.join(script_dir, *parts)
    
    # Normalize
    full_path = os.path.normpath(full_path)
    
    return full_path

# Usage
data_file = build_project_path("data", "students.csv")
output_dir = build_project_path("output", "reports")

# Ensure directories exist
os.makedirs(os.path.dirname(data_file), exist_ok=True)
```

### Pattern 5: File Statistics
```python
import os
from datetime import datetime

def get_file_stats(filepath):
    """Get detailed file statistics"""
    if not os.path.exists(filepath):
        return None
    
    stat_info = os.stat(filepath)
    
    stats = {
        'path': os.path.abspath(filepath),
        'name': os.path.basename(filepath),
        'size': stat_info.st_size,
        'size_kb': stat_info.st_size / 1024,
        'size_mb': stat_info.st_size / (1024 * 1024),
        'modified': datetime.fromtimestamp(stat_info.st_mtime),
        'created': datetime.fromtimestamp(stat_info.st_ctime),
        'accessed': datetime.fromtimestamp(stat_info.st_atime),
        'is_file': os.path.isfile(filepath),
        'is_dir': os.path.isdir(filepath),
        'readable': os.access(filepath, os.R_OK),
        'writable': os.access(filepath, os.W_OK),
        'executable': os.access(filepath, os.X_OK)
    }
    
    return stats

# Usage
stats = get_file_stats("data.csv")
if stats:
    print(f"File: {stats['name']}")
    print(f"Size: {stats['size_kb']:.2f} KB")
    print(f"Modified: {stats['modified']}")
```

### Pattern 6: Directory Size Calculator
```python
import os

def get_directory_size(directory):
    """Calculate total size of directory"""
    total_size = 0
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            
            # Skip if symbolic link
            if not os.path.islink(filepath):
                total_size += os.path.getsize(filepath)
    
    return total_size

def format_size(bytes):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

# Usage
size = get_directory_size("C:\\Projects")
print(f"Total size: {format_size(size)}")
```

### Pattern 7: Cross-Platform Path Handling
```python
import os

def get_data_directory():
    """Get platform-specific data directory"""
    if os.name == 'nt':  # Windows
        base = os.environ.get('APPDATA', os.path.expanduser('~'))
        return os.path.join(base, 'MyApp', 'data')
    else:  # Unix/Linux/Mac
        base = os.path.expanduser('~')
        return os.path.join(base, '.myapp', 'data')

def get_config_file():
    """Get platform-specific config file path"""
    if os.name == 'nt':  # Windows
        base = os.environ.get('APPDATA', os.path.expanduser('~'))
        config_dir = os.path.join(base, 'MyApp')
    else:  # Unix/Linux/Mac
        config_dir = os.path.expanduser('~/.config/myapp')
    
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, 'config.ini')

# Build paths correctly for any OS
def join_path(*parts):
    """Join path parts using correct separator"""
    return os.path.join(*parts)

# Usage
path = join_path("data", "students", "records.csv")
# Windows: "data\\students\\records.csv"
# Unix: "data/students/records.csv"
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: FileNotFoundError
```python
# WRONG - no error checking
os.remove("nonexistent.txt")  # FileNotFoundError

# RIGHT - check first
if os.path.exists("file.txt"):
    os.remove("file.txt")

# OR - use try/except
try:
    os.remove("file.txt")
except FileNotFoundError:
    print("File not found")
```

### Error 2: PermissionError
```python
# WRONG - no permission check
os.mkdir("C:\\Windows\\new_folder")  # PermissionError

# RIGHT - check permissions
if os.access("folder", os.W_OK):
    os.mkdir("folder/subfolder")

# OR - handle error
try:
    os.mkdir("folder")
except PermissionError:
    print("Permission denied")
```

### Error 3: FileExistsError
```python
# WRONG - creates error if exists
os.mkdir("existing_folder")  # FileExistsError

# RIGHT - check first
if not os.path.exists("folder"):
    os.mkdir("folder")

# BETTER - use exist_ok
os.makedirs("folder", exist_ok=True)
```

### Error 4: OSError with rmdir
```python
# WRONG - can't remove non-empty directory
os.rmdir("folder_with_files")  # OSError

# RIGHT - check if empty
if os.path.isdir("folder"):
    if not os.listdir("folder"):  # Empty
        os.rmdir("folder")

# OR - use shutil for non-empty
import shutil
shutil.rmtree("folder")  # Removes everything
```

### Error 5: Path Separator Issues
```python
# WRONG - hardcoded separator
path = "folder\\subfolder\\file.txt"  # Fails on Unix

# RIGHT - use os.path.join
path = os.path.join("folder", "subfolder", "file.txt")

# OR - use forward slashes (work on both)
path = "folder/subfolder/file.txt"  # Works on Windows too
```

---

## PERFORMANCE TIPS

1. **Use os.scandir() instead of os.listdir() for large directories**
   ```python
   # SLOW - creates stat objects for everything
   for name in os.listdir(large_dir):
       path = os.path.join(large_dir, name)
       if os.path.isfile(path):
           process(path)
   
   # FAST - scandir caches stat info
   with os.scandir(large_dir) as entries:
       for entry in entries:
           if entry.is_file():
               process(entry.path)
   ```

2. **Use os.path.exists() once instead of multiple type checks**
   ```python
   # SLOWER
   if os.path.isfile(path):
       process_file(path)
   elif os.path.isdir(path):
       process_dir(path)
   
   # FASTER
   if os.path.exists(path):
       if os.path.isfile(path):
           process_file(path)
       else:
           process_dir(path)
   ```

3. **Cache os.path operations in loops**
   ```python
   # SLOW
   for item in items:
       path = os.path.join(base_dir, item)
       process(path)
   
   # FASTER
   join = os.path.join  # Cache function
   for item in items:
       path = join(base_dir, item)
       process(path)
   ```

4. **Use os.walk() instead of recursive os.listdir()**
   ```python
   # SLOW - manual recursion
   def list_files(directory):
       result = []
       for item in os.listdir(directory):
           path = os.path.join(directory, item)
           if os.path.isdir(path):
               result.extend(list_files(path))
           else:
               result.append(path)
       return result
   
   # FAST - use os.walk
   def list_files(directory):
       result = []
       for dirpath, _, filenames in os.walk(directory):
           for filename in filenames:
               result.append(os.path.join(dirpath, filename))
       return result
   ```

---

---

## FILE I/O INTEGRATION WITH OS MODULE

### 1. CSV FILE OPERATIONS WITH DICTIONARIES

```python
import os
import csv

# Pattern 1: Read CSV into dictionary (by ID)
def read_csv_to_dict(filepath):
    """Read CSV file into dictionary with ID as key"""
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found")
        return {}
    
    students = {}
    
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_id = row['ID']
                students[student_id] = {
                    'name': row['Name'],
                    'gpa': float(row['GPA']),
                    'major': row['Major']
                }
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return {}
    
    return students

# Usage
data_path = os.path.join("data", "students.csv")
students = read_csv_to_dict(data_path)
print(f"Loaded {len(students)} students")

# Pattern 2: Read CSV into list of dictionaries
def read_csv_to_list(filepath):
    """Read CSV file into list of dictionaries"""
    if not os.path.exists(filepath):
        return []
    
    records = []
    
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(dict(row))
    
    return records

# Pattern 3: Write dictionary to CSV
def write_dict_to_csv(data_dict, filepath):
    """Write dictionary to CSV file"""
    # Ensure directory exists
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)
    
    if not data_dict:
        print("No data to write")
        return
    
    # Get first record to determine headers
    first_key = next(iter(data_dict))
    headers = ['ID'] + list(data_dict[first_key].keys())
    
    try:
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            
            for student_id, info in data_dict.items():
                row = [student_id] + list(info.values())
                writer.writerow(row)
        
        print(f"Wrote {len(data_dict)} records to {filepath}")
    except Exception as e:
        print(f"Error writing CSV: {e}")

# Pattern 4: Append to CSV file
def append_to_csv(record, filepath):
    """Append single record to CSV file"""
    # Check if file exists to determine if we need headers
    file_exists = os.path.exists(filepath)
    
    # Ensure directory exists
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)
    
    with open(filepath, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=record.keys())
        
        # Write header if new file
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(record)

# Pattern 5: Read CSV with validation
def read_csv_validated(filepath, required_fields):
    """Read CSV with field validation"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    records = []
    errors = []
    
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        
        # Validate headers
        if not all(field in reader.fieldnames for field in required_fields):
            missing = set(required_fields) - set(reader.fieldnames)
            raise ValueError(f"Missing required fields: {missing}")
        
        for line_num, row in enumerate(reader, start=2):  # Start at 2 (header is line 1)
            # Check for missing values
            if all(row[field] for field in required_fields):
                records.append(row)
            else:
                errors.append(f"Line {line_num}: Missing required field")
    
    if errors:
        print(f"Found {len(errors)} errors")
        for error in errors[:5]:  # Show first 5 errors
            print(f"  {error}")
    
    return records

# Usage
records = read_csv_validated(
    os.path.join("data", "students.csv"),
    required_fields=['ID', 'Name', 'GPA']
)
```

### 2. JSON FILE OPERATIONS WITH DICTIONARIES

```python
import os
import json

# Pattern 1: Read JSON into dictionary
def read_json_to_dict(filepath):
    """Read JSON file into dictionary"""
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found")
        return {}
    
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

# Usage
config_path = os.path.join("config", "settings.json")
config = read_json_to_dict(config_path)

# Pattern 2: Write dictionary to JSON
def write_dict_to_json(data, filepath, indent=2):
    """Write dictionary to JSON file with formatting"""
    # Ensure directory exists
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)
    
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=indent)
        print(f"Wrote data to {filepath}")
    except Exception as e:
        print(f"Error writing JSON: {e}")

# Usage
students = {
    "12345": {"name": "Alice", "gpa": 3.8, "major": "CS"},
    "67890": {"name": "Bob", "gpa": 3.5, "major": "Math"}
}
write_dict_to_json(students, os.path.join("output", "students.json"))

# Pattern 3: Update existing JSON file
def update_json_file(filepath, key, value):
    """Update specific key in JSON file"""
    # Read existing data
    if os.path.exists(filepath):
        data = read_json_to_dict(filepath)
    else:
        data = {}
    
    # Update
    data[key] = value
    
    # Write back
    write_dict_to_json(data, filepath)

# Pattern 4: Merge multiple JSON files
def merge_json_files(directory, output_file):
    """Merge all JSON files in directory into one"""
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return
    
    merged_data = {}
    
    # Walk through directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            data = read_json_to_dict(filepath)
            
            # Merge data
            if isinstance(data, dict):
                merged_data.update(data)
    
    # Write merged data
    write_dict_to_json(merged_data, output_file)
    print(f"Merged {len(os.listdir(directory))} files")

# Pattern 5: JSON with backup
def write_json_with_backup(data, filepath):
    """Write JSON file and create backup of old version"""
    # Create backup if file exists
    if os.path.exists(filepath):
        backup_path = filepath + '.bak'
        os.replace(filepath, backup_path)
        print(f"Created backup: {backup_path}")
    
    # Write new data
    write_dict_to_json(data, filepath)
```

### 3. TEXT FILE OPERATIONS IN LOOPS

```python
import os

# Pattern 1: Process multiple files in directory
def process_text_files(directory):
    """Process all text files in directory"""
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return
    
    results = {}
    
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            
            # Read and process
            with open(filepath, 'r') as file:
                content = file.read()
                word_count = len(content.split())
                line_count = content.count('\n') + 1
            
            results[filename] = {
                'words': word_count,
                'lines': line_count,
                'size': os.path.getsize(filepath)
            }
    
    return results

# Usage
stats = process_text_files("documents")
for filename, info in stats.items():
    print(f"{filename}: {info['words']} words, {info['lines']} lines")

# Pattern 2: Read files into dictionary by name
def read_files_to_dict(directory, extension='.txt'):
    """Read all files with extension into dictionary"""
    if not os.path.isdir(directory):
        return {}
    
    files_dict = {}
    
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r') as file:
                # Use filename without extension as key
                name = os.path.splitext(filename)[0]
                files_dict[name] = file.read()
    
    return files_dict

# Pattern 3: Write dictionary entries to separate files
def write_dict_to_files(data_dict, directory, extension='.txt'):
    """Write each dictionary entry to separate file"""
    os.makedirs(directory, exist_ok=True)
    
    for key, content in data_dict.items():
        filename = f"{key}{extension}"
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w') as file:
            file.write(str(content))
    
    print(f"Wrote {len(data_dict)} files to {directory}")

# Pattern 4: Batch file processing with error handling
def batch_process_files(input_dir, output_dir, process_func):
    """Process all files in directory with custom function"""
    if not os.path.isdir(input_dir):
        print(f"Input directory not found: {input_dir}")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    
    processed = 0
    errors = 0
    
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        
        # Skip directories
        if os.path.isdir(input_path):
            continue
        
        output_path = os.path.join(output_dir, filename)
        
        try:
            # Read
            with open(input_path, 'r') as file:
                content = file.read()
            
            # Process
            result = process_func(content)
            
            # Write
            with open(output_path, 'w') as file:
                file.write(result)
            
            processed += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            errors += 1
    
    print(f"Processed: {processed}, Errors: {errors}")

# Usage example
def uppercase_processor(text):
    """Example processing function"""
    return text.upper()

batch_process_files("input", "output", uppercase_processor)

# Pattern 5: Read files recursively into nested dictionary
def read_directory_tree(root_dir):
    """Read all files in directory tree into nested dictionary"""
    tree = {}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Get relative path from root
        rel_path = os.path.relpath(dirpath, root_dir)
        
        # Build nested dict structure
        current = tree
        if rel_path != '.':
            parts = rel_path.split(os.sep)
            for part in parts:
                current = current.setdefault(part, {})
        
        # Add files
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r') as file:
                    current[filename] = file.read()
            except:
                current[filename] = None  # Mark unreadable files
    
    return tree
```

### 4. STUDENT RECORD SYSTEM (COMPLETE EXAMPLE)

```python
import os
import csv

class StudentDatabase:
    """Complete student database with file operations"""
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.csv_path = os.path.join(data_dir, "students.csv")
        self.students = {}
        
        # Ensure data directory exists
        os.makedirs(data_dir, exist_ok=True)
        
        # Load existing data
        self.load_from_csv()
    
    def load_from_csv(self):
        """Load students from CSV file into dictionary"""
        if not os.path.exists(self.csv_path):
            print("No existing database found. Starting fresh.")
            return
        
        try:
            with open(self.csv_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_id = row['ID']
                    self.students[student_id] = {
                        'name': row['Name'],
                        'gpa': float(row['GPA']),
                        'major': row['Major'],
                        'credits': int(row['Credits'])
                    }
            
            print(f"Loaded {len(self.students)} students from {self.csv_path}")
        except Exception as e:
            print(f"Error loading database: {e}")
    
    def save_to_csv(self):
        """Save students dictionary to CSV file"""
        if not self.students:
            print("No students to save")
            return
        
        try:
            with open(self.csv_path, 'w', newline='') as file:
                # Define headers
                headers = ['ID', 'Name', 'GPA', 'Major', 'Credits']
                writer = csv.writer(file)
                writer.writerow(headers)
                
                # Write each student
                for student_id, info in self.students.items():
                    row = [
                        student_id,
                        info['name'],
                        info['gpa'],
                        info['major'],
                        info['credits']
                    ]
                    writer.writerow(row)
            
            print(f"Saved {len(self.students)} students to {self.csv_path}")
        except Exception as e:
            print(f"Error saving database: {e}")
    
    def add_student(self, student_id, name, gpa, major, credits=0):
        """Add new student to dictionary"""
        if student_id in self.students:
            print(f"Student {student_id} already exists")
            return False
        
        self.students[student_id] = {
            'name': name,
            'gpa': float(gpa),
            'major': major,
            'credits': int(credits)
        }
        
        # Auto-save after adding
        self.save_to_csv()
        return True
    
    def find_student(self, student_id):
        """Find student by ID"""
        return self.students.get(student_id)
    
    def update_student(self, student_id, **kwargs):
        """Update student information"""
        if student_id not in self.students:
            print(f"Student {student_id} not found")
            return False
        
        # Update only provided fields
        for key, value in kwargs.items():
            if key in self.students[student_id]:
                self.students[student_id][key] = value
        
        self.save_to_csv()
        return True
    
    def delete_student(self, student_id):
        """Delete student from dictionary"""
        if student_id in self.students:
            del self.students[student_id]
            self.save_to_csv()
            return True
        return False
    
    def search_by_major(self, major):
        """Search students by major"""
        results = {}
        for student_id, info in self.students.items():
            if info['major'].lower() == major.lower():
                results[student_id] = info
        return results
    
    def get_statistics(self):
        """Get database statistics"""
        if not self.students:
            return None
        
        gpas = [s['gpa'] for s in self.students.values()]
        
        stats = {
            'total_students': len(self.students),
            'average_gpa': sum(gpas) / len(gpas),
            'highest_gpa': max(gpas),
            'lowest_gpa': min(gpas),
            'file_size': os.path.getsize(self.csv_path) if os.path.exists(self.csv_path) else 0
        }
        
        return stats
    
    def export_by_major(self, output_dir="exports"):
        """Export students to separate CSV files by major"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Group by major
        by_major = {}
        for student_id, info in self.students.items():
            major = info['major']
            if major not in by_major:
                by_major[major] = {}
            by_major[major][student_id] = info
        
        # Write separate file for each major
        for major, students in by_major.items():
            filename = f"{major.replace(' ', '_')}_students.csv"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', newline='') as file:
                headers = ['ID', 'Name', 'GPA', 'Credits']
                writer = csv.writer(file)
                writer.writerow(headers)
                
                for student_id, info in students.items():
                    row = [student_id, info['name'], info['gpa'], info['credits']]
                    writer.writerow(row)
            
            print(f"Exported {len(students)} {major} students to {filepath}")
    
    def create_backup(self):
        """Create backup of database"""
        if not os.path.exists(self.csv_path):
            print("No database to backup")
            return
        
        # Create backup directory
        backup_dir = os.path.join(self.data_dir, "backups")
        os.makedirs(backup_dir, exist_ok=True)
        
        # Create timestamp for backup filename
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"students_backup_{timestamp}.csv"
        backup_path = os.path.join(backup_dir, backup_filename)
        
        # Copy file
        with open(self.csv_path, 'r') as source:
            with open(backup_path, 'w') as dest:
                dest.write(source.read())
        
        print(f"Backup created: {backup_path}")
        return backup_path

# Usage Example
def main():
    # Initialize database
    db = StudentDatabase("data")
    
    # Add students
    db.add_student("12345", "Alice Smith", 3.8, "Computer Science", 60)
    db.add_student("67890", "Bob Jones", 3.5, "Mathematics", 45)
    db.add_student("11111", "Carol White", 3.9, "Computer Science", 90)
    
    # Find student
    student = db.find_student("12345")
    if student:
        print(f"Found: {student['name']}, GPA: {student['gpa']}")
    
    # Search by major
    cs_students = db.search_by_major("Computer Science")
    print(f"Found {len(cs_students)} CS students")
    
    # Update student
    db.update_student("12345", gpa=3.9, credits=75)
    
    # Get statistics
    stats = db.get_statistics()
    print(f"Average GPA: {stats['average_gpa']:.2f}")
    print(f"Total students: {stats['total_students']}")
    
    # Export by major
    db.export_by_major("exports")
    
    # Create backup
    db.create_backup()

if __name__ == "__main__":
    main()
```

### 5. LOG FILE PROCESSING

```python
import os
from datetime import datetime

# Pattern 1: Append to log file
def log_message(message, log_file="app.log", log_dir="logs"):
    """Append message to log file with timestamp"""
    os.makedirs(log_dir, exist_ok=True)
    
    log_path = os.path.join(log_dir, log_file)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(log_path, 'a') as file:
        file.write(log_entry)

# Pattern 2: Read log file into dictionary by date
def parse_log_file(log_path):
    """Parse log file into dictionary grouped by date"""
    if not os.path.exists(log_path):
        return {}
    
    logs_by_date = {}
    
    with open(log_path, 'r') as file:
        for line in file:
            if line.startswith('['):
                # Extract timestamp and message
                parts = line.split('] ', 1)
                if len(parts) == 2:
                    timestamp = parts[0][1:]  # Remove '['
                    message = parts[1].strip()
                    
                    # Get date
                    date = timestamp.split(' ')[0]
                    
                    # Add to dictionary
                    if date not in logs_by_date:
                        logs_by_date[date] = []
                    logs_by_date[date].append({
                        'time': timestamp,
                        'message': message
                    })
    
    return logs_by_date

# Pattern 3: Rotate log files
def rotate_log_file(log_file="app.log", log_dir="logs", max_size_mb=10):
    """Rotate log file if exceeds size limit"""
    log_path = os.path.join(log_dir, log_file)
    
    if not os.path.exists(log_path):
        return
    
    # Check file size
    size_mb = os.path.getsize(log_path) / (1024 * 1024)
    
    if size_mb >= max_size_mb:
        # Create archive directory
        archive_dir = os.path.join(log_dir, "archive")
        os.makedirs(archive_dir, exist_ok=True)
        
        # Generate archive filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_name = f"{os.path.splitext(log_file)[0]}_{timestamp}.log"
        archive_path = os.path.join(archive_dir, archive_name)
        
        # Move current log to archive
        os.rename(log_path, archive_path)
        print(f"Rotated log to: {archive_path}")

# Pattern 4: Clean old log files
def clean_old_logs(log_dir="logs", days_to_keep=30):
    """Delete log files older than specified days"""
    if not os.path.isdir(log_dir):
        return
    
    import time
    current_time = time.time()
    cutoff_time = current_time - (days_to_keep * 24 * 60 * 60)
    
    deleted_count = 0
    
    for filename in os.listdir(log_dir):
        if filename.endswith('.log'):
            filepath = os.path.join(log_dir, filename)
            
            # Get file modification time
            if os.path.getmtime(filepath) < cutoff_time:
                os.remove(filepath)
                deleted_count += 1
                print(f"Deleted old log: {filename}")
    
    print(f"Cleaned {deleted_count} old log files")
```

### 6. CONFIG FILE MANAGEMENT

```python
import os

# Pattern 1: Read config file into dictionary
def read_config(config_path="config.txt"):
    """Read key=value config file into dictionary"""
    if not os.path.exists(config_path):
        return {}
    
    config = {}
    
    with open(config_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Parse key=value
            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    
    return config

# Pattern 2: Write dictionary to config file
	def write_config(config_dict, config_path="config.txt"):
	    """Write dictionary to config file"""
	    directory = os.path.dirname(config_path)
	    if directory:
	        os.makedirs(directory, exist_ok=True)
	    
	    with open(config_path, 'w') as file:
	        for key, value in config_dict.items():
	            file.write(f"{key}={value}\n")

# Pattern 3: Update single config value
def update_config_value(key, value, config_path="config.txt"):
    """Update single config value in file"""
    # Read existing config
    config = read_config(config_path)
    
    # Update value
    config[key] = value
    
    # Write back
    write_config(config, config_path)

# Usage
config_path = os.path.join("config", "settings.txt")
settings = read_config(config_path)

# Update setting
update_config_value("debug", "true", config_path)
```

### 7. DATA VALIDATION WITH FILE CHECKS

```python
import os

def validate_project_structure(project_dir):
    """Validate required project files and directories exist"""
    required_structure = {
        'directories': ['data', 'output', 'logs'],
        'files': ['main.py', 'config.txt']
    }
    
    errors = []
    warnings = []
    
    # Check directories
    for dirname in required_structure['directories']:
        dirpath = os.path.join(project_dir, dirname)
        if not os.path.exists(dirpath):
            errors.append(f"Missing directory: {dirname}")
        elif not os.path.isdir(dirpath):
            errors.append(f"Not a directory: {dirname}")
    
    # Check files
    for filename in required_structure['files']:
        filepath = os.path.join(project_dir, filename)
        if not os.path.exists(filepath):
            errors.append(f"Missing file: {filename}")
        elif not os.path.isfile(filepath):
            errors.append(f"Not a file: {filename}")
        else:
            # Check if file is empty
            if os.path.getsize(filepath) == 0:
                warnings.append(f"Empty file: {filename}")
    
    # Report results
    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    if not errors and not warnings:
        print("✓ Project structure validated successfully")
    
    return len(errors) == 0

def create_project_structure(project_dir):
    """Create standard project structure"""
    structure = {
        'data': ['students.csv', 'config.json'],
        'output': [],
        'logs': ['app.log'],
        'src': ['main.py', 'utils.py']
    }
    
    for dirname, files in structure.items():
        dirpath = os.path.join(project_dir, dirname)
        os.makedirs(dirpath, exist_ok=True)
        print(f"Created directory: {dirpath}")
        
        # Create empty files
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            if not os.path.exists(filepath):
                open(filepath, 'w').close()
                print(f"Created file: {filepath}")
```

---

## OS MODULE vs PATHLIB

**When to use os module:**
- Working with environment variables
- Process operations
- Low-level file operations
- System information
- Legacy code compatibility

**When to use pathlib (Python 3.4+):**
- Modern path manipulation
- Object-oriented path handling
- Cleaner, more readable code

```python
# OS module approach
import os
path = os.path.join("folder", "file.txt")
if os.path.exists(path):
    size = os.path.getsize(path)

# Pathlib approach (modern)
from pathlib import Path
path = Path("folder") / "file.txt"
if path.exists():
    size = path.stat().st_size
```
