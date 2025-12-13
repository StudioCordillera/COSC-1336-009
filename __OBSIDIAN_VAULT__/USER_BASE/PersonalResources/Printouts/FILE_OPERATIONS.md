# FILE_OPERATIONS

## Core Definition
**File operations** enable reading from and writing to files on disk. Essential for data persistence, configuration management, and processing external data sources. Files must be opened, operated on, then properly closed to prevent data loss.

**Tags**: #file-io #data-persistence #file-handling #error-handling #context-manager

---

## COMPLETE FILE OPERATIONS QUICK REFERENCE

### FILE OPERATIONS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# FILE OPENING & CLOSING
# ═══════════════════════════════════════════════════════════════════════════
open(filename, mode)         # Filename + mode | Open file | Returns file object
open(filename, 'r')          # Filename | Open for reading (default) | Returns file object
open(filename, 'w')          # Filename | Open for writing (overwrites) | Returns file object
open(filename, 'a')          # Filename | Open for appending | Returns file object
open(filename, 'x')          # Filename | Create new file (fails if exists) | Returns file object
open(filename, 'r+')         # Filename | Open for read/write | Returns file object
open(filename, 'w+')         # Filename | Open for write/read (overwrites) | Returns file object
open(filename, 'a+')         # Filename | Open for append/read | Returns file object
open(filename, mode, encoding='utf-8') # Filename + encoding | Open with encoding | Returns file object
file.close()                 # File object | Close file | Returns None
with open(filename, mode) as file: # Filename | Auto-closing context | File auto-closed after block

# ═══════════════════════════════════════════════════════════════════════════
# FILE READING METHODS
# ═══════════════════════════════════════════════════════════════════════════
file.read()                  # File object | Read entire file | Returns string with full content
file.read(size)              # File object | Read size bytes | Returns string with size bytes
file.readline()              # File object | Read one line | Returns string with line (includes \n)
file.readlines()             # File object | Read all lines | Returns list of strings (lines)
for line in file:            # File object | Iterate lines | Yields each line as string
next(file)                   # File object | Read next line | Returns next line or StopIteration

# ═══════════════════════════════════════════════════════════════════════════
# FILE WRITING METHODS
# ═══════════════════════════════════════════════════════════════════════════
file.write(string)           # File object + string | Write string to file | Returns number of chars written
file.writelines(list)        # File object + list | Write list of strings | Returns None
file.flush()                 # File object | Force write buffer to disk | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# FILE POSITION & INFO
# ═══════════════════════════════════════════════════════════════════════════
file.tell()                  # File object | Get current position | Returns int byte offset
file.seek(offset)            # File object + offset | Move to position | Returns new position
file.seek(offset, whence)    # File object + offset + origin | Move relative | Returns new position (0=start, 1=current, 2=end)
file.name                    # File object | Get filename | Returns string filename
file.mode                    # File object | Get file mode | Returns string mode
file.closed                  # File object | Check if closed | Returns True/False
file.readable()              # File object | Check if readable | Returns True/False
file.writable()              # File object | Check if writable | Returns True/False
file.seekable()              # File object | Check if seekable | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# OS PATH OPERATIONS (import os)
# ═══════════════════════════════════════════════════════════════════════════
os.path.exists(path)         # Path | Check if exists | Returns True/False
os.path.isfile(path)         # Path | Check if file | Returns True/False
os.path.isdir(path)          # Path | Check if directory | Returns True/False
os.path.getsize(path)        # Path | Get file size | Returns int bytes
os.path.abspath(path)        # Path | Get absolute path | Returns string absolute path
os.path.dirname(path)        # Path | Get directory name | Returns string directory
os.path.basename(path)       # Path | Get filename | Returns string filename
os.path.split(path)          # Path | Split dir and file | Returns (dir, filename) tuple
os.path.splitext(path)       # Path | Split name and extension | Returns (name, ext) tuple
os.path.join(path1, path2)   # Path parts | Join paths | Returns string combined path
os.remove(path)              # Path | Delete file | Returns None
os.rename(old, new)          # Old + new paths | Rename file | Returns None
os.getcwd()                  # None | Get current directory | Returns string current dir
os.chdir(path)               # Path | Change directory | Returns None
os.listdir(path)             # Path | List directory contents | Returns list of filenames
os.mkdir(path)               # Path | Create directory | Returns None
os.makedirs(path)            # Path | Create nested directories | Returns None
os.rmdir(path)               # Path | Remove empty directory | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# FILE MODE FLAGS
# ═══════════════════════════════════════════════════════════════════════════
'r'                          # Mode | Read (default) | Opens for reading, fails if not exists
'w'                          # Mode | Write | Opens for writing, creates new/overwrites
'a'                          # Mode | Append | Opens for appending, creates if not exists
'x'                          # Mode | Exclusive create | Creates new file, fails if exists
'b'                          # Mode flag | Binary mode | Combine with r/w/a for binary
't'                          # Mode flag | Text mode (default) | Combine with r/w/a for text
'+'                          # Mode flag | Update (read+write) | Combine with r/w/a

# ═══════════════════════════════════════════════════════════════════════════
# ERROR HANDLING FOR FILES
# ═══════════════════════════════════════════════════════════════════════════
FileNotFoundError            # Exception | File doesn't exist | Raised when file not found
PermissionError              # Exception | Access denied | Raised when lacking permissions
IsADirectoryError            # Exception | Path is directory | Raised when expecting file
FileExistsError              # Exception | File already exists | Raised with 'x' mode
IOError                      # Exception | General I/O error | Raised on I/O operation failure
```

### COMMON OPERATION EXAMPLES

```python
# Safe file reading with context manager
with open("data.txt", "r") as file:
    content = file.read()                      # → Full file as string

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())                    # → Each line without newline

# Read all lines into list
with open("data.txt", "r") as file:
    lines = file.readlines()                   # → ['line1\n', 'line2\n', ...]

# Write to file
with open("output.txt", "w") as file:
    file.write("Hello World\n")                # → Writes and returns char count

# Append to file
with open("log.txt", "a") as file:
    file.write("New log entry\n")              # → Appends to end

# Check if file exists
import os
if os.path.exists("data.txt"):
    print("File exists")                       # → True/False

# Get file size
size = os.path.getsize("data.txt")             # → Size in bytes

# Join paths safely
path = os.path.join("folder", "file.txt")      # → "folder/file.txt" (OS-appropriate)
```

---

## DETAILED FILE OPERATIONS

### 1. FILE OPENING PATTERNS

```python
# Manual file opening (NOT RECOMMENDED)
file = open("filename.txt", "r")               # Open for reading
try:
    content = file.read()
finally:
    file.close()                               # Must manually close

# BEST PRACTICE: Context manager (with statement)
with open("filename.txt", "r") as file:
    content = file.read()
# File automatically closed, even if error occurs

# Multiple files simultaneously
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())

# File modes
# 'r'  = Read (default), fails if not exists
# 'w'  = Write, creates/overwrites
# 'a'  = Append, creates if not exists
# 'x'  = Exclusive create, fails if exists
# 'r+' = Read+Write, fails if not exists
# 'w+' = Write+Read, creates/overwrites
# 'a+' = Append+Read, creates if not exists
# 'b'  = Binary mode (add to mode: 'rb', 'wb')
```

### 2. READING FILE PATTERNS

```python
text = "data.txt"

# Read entire file at once
with open(text, "r") as file:
    content = file.read()                      # → Full file as single string

# Read with size limit
with open(text, "r") as file:
    chunk = file.read(100)                     # → First 100 bytes

# Read line by line (memory efficient)
with open(text, "r") as file:
    for line in file:
        print(line.strip())                    # → Each line, newline removed

# Read all lines into list
with open(text, "r") as file:
    lines = file.readlines()                   # → ['line1\n', 'line2\n', ...]

# Read lines without newlines
with open(text, "r") as file:
    lines = [line.strip() for line in file]    # → ['line1', 'line2', ...]

# Read one line at a time
with open(text, "r") as file:
    first_line = file.readline()               # → First line with \n
    second_line = file.readline()              # → Second line with \n

# Read non-empty lines only
with open(text, "r") as file:
    lines = [line.strip() for line in file if line.strip()]
```

### 3. WRITING FILE PATTERNS

```python
# Write single string
with open("output.txt", "w") as file:
    file.write("Hello World\n")                # → Returns 12 (chars written)

# Write multiple strings
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# Write list of strings
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)                     # → Writes all lines

# Append to existing file
with open("log.txt", "a") as file:
    file.write("New log entry\n")              # → Adds to end

# Write formatted data
data = {"name": "Alice", "age": 30, "city": "NYC"}
with open("data.txt", "w") as file:
    for key, value in data.items():
        file.write(f"{key}: {value}\n")

# Write numbers
numbers = [1, 2, 3, 4, 5]
with open("numbers.txt", "w") as file:
    for num in numbers:
        file.write(f"{num}\n")
    # OR
    file.write('\n'.join(map(str, numbers)) + '\n')
```

### 4. ERROR HANDLING PATTERNS

```python
# Basic error handling
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")

# Check if file exists first
import os
if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        content = file.read()
else:
    print("File does not exist")

# Create file if not exists
try:
    with open("output.txt", "x") as file:       # 'x' mode
        file.write("New file\n")
except FileExistsError:
    print("File already exists")

# Safe read with default
def safe_read_file(filename, default=""):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return default
```

### 5. PATH OPERATIONS

```python
import os

# Check existence
os.path.exists("data.txt")                     # → True/False
os.path.isfile("data.txt")                     # → True if file
os.path.isdir("folder")                        # → True if directory

# File information
os.path.getsize("data.txt")                    # → Size in bytes
os.path.getmtime("data.txt")                   # → Last modified timestamp
os.path.getctime("data.txt")                   # → Creation timestamp

# Path manipulation
os.path.abspath("data.txt")                    # → "/full/path/to/data.txt"
os.path.dirname("/path/to/file.txt")           # → "/path/to"
os.path.basename("/path/to/file.txt")          # → "file.txt"
os.path.split("/path/to/file.txt")             # → ("/path/to", "file.txt")
os.path.splitext("file.txt")                   # → ("file", ".txt")

# Join paths (OS-appropriate separator)
os.path.join("folder", "subfolder", "file.txt") # → "folder/subfolder/file.txt"

# Current directory
os.getcwd()                                    # → Current working directory
os.chdir("/new/path")                          # Change directory

# List directory
os.listdir(".")                                # → ['file1.txt', 'file2.txt', ...]
os.listdir("/path/to/dir")                     # → Files in directory

# File operations
os.remove("file.txt")                          # Delete file
os.rename("old.txt", "new.txt")                # Rename file
```

---

## PRACTICAL EXAM PATTERNS

### PATTERN 1: Safe File Reading with Error Handling

```python
def safe_read_file(filename):
    """
    Safely read file with comprehensive error handling.
    Returns list of cleaned lines or empty list on error.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Clean data - remove whitespace and empty lines
        cleaned_lines = []
        for line in lines:
            cleaned = line.strip()
            if cleaned:                            # Skip empty lines
                cleaned_lines.append(cleaned)
        
        return cleaned_lines
        
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found")
        return []
    except PermissionError:
        print(f"ERROR: Permission denied for '{filename}'")
        return []
    except Exception as e:
        print(f"ERROR: {e}")
        return []

# Process mixed data types (numbers + strings)
def process_data_file(filename):
    """Process file with mixed numeric and text data."""
    lines = safe_read_file(filename)
    
    numbers = []
    strings = []
    
    for line in lines:
        try:
            # Try numeric conversion
            if '.' in line:
                numbers.append(float(line))
            else:
                numbers.append(int(line))
        except ValueError:
            # Not a number, store as string
            strings.append(line)
    
    return numbers, strings

# Usage
nums, strs = process_data_file("data1.txt")
print(f"Found {len(nums)} numbers and {len(strs)} strings")
```

### PATTERN 2: Data Analysis with File Output

```python
def analyze_data_file(filename):
    """
    Complete data analysis from file - exam project pattern.
    Reads mixed data, analyzes, and writes results to files.
    """
    print(f"Analyzing: {filename}")
    
    # Read and categorize data
    numbers, strings = process_data_file(filename)
    
    if not numbers and not strings:
        print("No data found")
        return
    
    # Numeric analysis
    if numbers:
        print("\nNumeric Analysis:")
        print(f"  Count: {len(numbers)}")
        print(f"  Sum: {sum(numbers):.2f}")
        print(f"  Average: {sum(numbers)/len(numbers):.2f}")
        print(f"  Max: {max(numbers):.2f}")
        print(f"  Min: {min(numbers):.2f}")
        
        # Save numeric results
        with open("numeric_results.txt", "w") as file:
            file.write("Numeric Analysis Results\n")
            file.write("=" * 30 + "\n")
            file.write(f"Count:   {len(numbers)}\n")
            file.write(f"Sum:     {sum(numbers):.2f}\n")
            file.write(f"Average: {sum(numbers)/len(numbers):.2f}\n")
            file.write(f"Max:     {max(numbers):.2f}\n")
            file.write(f"Min:     {min(numbers):.2f}\n")
            file.write(f"Range:   {max(numbers) - min(numbers):.2f}\n")
    
    # String analysis
    if strings:
        unique = set(strings)
        print("\nString Analysis:")
        print(f"  Count: {len(strings)}")
        print(f"  Unique: {len(unique)}")
        
        # Save string results
        with open("string_results.txt", "w") as file:
            file.write("String Analysis Results\n")
            file.write("=" * 30 + "\n")
            file.write(f"Total:  {len(strings)}\n")
            file.write(f"Unique: {len(unique)}\n\n")
            file.write("All Strings:\n")
            for i, s in enumerate(strings, 1):
                file.write(f"  {i}. {s}\n")

# Usage
analyze_data_file("data1.txt")
```

### PATTERN 3: Interactive User Data Collection

```python
def collect_and_save_data():
    """
    Interactive data collection with file persistence.
    Common exam pattern for user input programs.
    """
    data = []
    
    print("Data Collection System")
    print("Commands: 'save' to save, 'quit' to exit")
    
    while True:
        user_input = input("Enter data: ").strip()
        
        if user_input.lower() == 'save':
            break
        elif user_input.lower() == 'quit':
            print("Exiting without saving")
            return
        elif user_input:
            data.append(user_input)
            print(f"  Added: {user_input}")
    
    if not data:
        print("No data to save")
        return
    
    # Get valid filename
    while True:
        filename = input("Filename (.txt): ")
        if filename.endswith('.txt'):
            break
        print("Must end with .txt")
    
    # Save to file
    try:
        with open(filename, 'w') as file:
            file.write(f"Data Collection Session\n")
            file.write(f"Total items: {len(data)}\n")
            file.write("=" * 30 + "\n\n")
            
            for i, item in enumerate(data, 1):
                file.write(f"{i}. {item}\n")
        
        print(f"Saved to {filename}")
        
    except Exception as e:
        print(f"Error: {e}")

def load_and_display_data():
    """Load and display previously saved file."""
    filename = input("Filename to load: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"\n{'='*40}")
            print(f"Content of {filename}:")
            print('='*40)
            print(content)
            
    except FileNotFoundError:
        print(f"File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")
```

### PATTERN 4: Text File with Comma-Separated Values to Dictionary

```python
def parse_line_to_dict(line, keys):
    """
    Parse line with comma-space separated values into dictionary.
    Splits on ', ' (comma-space) pattern.
    
    Args:
        line: String like "Alice, 30, New York"
        keys: List of key names ["name", "age", "city"]
    
    Returns:
        Dictionary {'name': 'Alice', 'age': '30', 'city': 'New York'}
    """
    values = line.strip().split(', ')
    
    # Pad with empty strings if not enough values
    while len(values) < len(keys):
        values.append('')
    
    # Map keys to values
    return {keys[i]: values[i] for i in range(len(keys))}

# Example: Parse single line
keys = ["name", "age", "city"]
line = "Alice, 30, New York"
person = parse_line_to_dict(line, keys)
print(person)                                  # → {'name': 'Alice', 'age': '30', 'city': 'New York'}

# Example: Load text file into list of dictionaries
def load_txt_as_dicts(filename, keys):
    """
    Read .txt file where each line has comma-space separated values.
    Returns list of dictionaries.
    """
    records = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:                       # Skip empty lines
                    record = parse_line_to_dict(line, keys)
                    records.append(record)
        
        return records
        
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Usage
keys = ["name", "age", "city"]
data = load_txt_as_dicts("people.txt", keys)

# If people.txt contains:
# Alice, 30, New York
# Bob, 25, Los Angeles
# Carol, 35, Chicago

for person in data:
    print(f"{person['name']} is {person['age']} years old")
# Output:
# Alice is 30 years old
# Bob is 25 years old
# Carol is 35 years old

# Example: Load with header line
def load_txt_with_header(filename):
    """
    Load .txt file where first line defines keys.
    Rest of lines are comma-space separated values.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            return []
        
        # First line defines keys
        keys = [k.strip() for k in lines[0].strip().split(', ')]
        
        # Parse remaining lines
        records = []
        for line in lines[1:]:
            line = line.strip()
            if line:
                record = parse_line_to_dict(line, keys)
                records.append(record)
        
        return records
        
    except Exception as e:
        print(f"Error: {e}")
        return []

# Usage
data = load_txt_with_header("data.txt")
# If data.txt contains:
# name, age, city
# Alice, 30, New York
# Bob, 25, Los Angeles

print(data)
# → [{'name': 'Alice', 'age': '30', 'city': 'New York'},
#    {'name': 'Bob', 'age': '25', 'city': 'Los Angeles'}]

# Example: Type conversion after loading
def load_txt_with_types(filename, keys, types):
    """
    Load .txt and convert values to specific types.
    
    Args:
        filename: .txt file path
        keys: List of key names
        types: List of type converters [str, int, str]
    """
    records = load_txt_as_dicts(filename, keys)
    
    # Convert types
    for record in records:
        for i, key in enumerate(keys):
            try:
                record[key] = types[i](record[key])
            except (ValueError, IndexError):
                pass
    
    return records

# Usage with type conversion
keys = ["name", "age", "salary"]
types = [str, int, float]
data = load_txt_with_types("employees.txt", keys, types)

# Now age is int, salary is float
for emp in data:
    print(f"{emp['name']}: ${emp['salary']:.2f}")
```

### PATTERN 5: CSV-Style Data Processing

```python
def process_csv_data(filename, delimiter=','):
    """
    Read CSV-style file and return list of dictionaries.
    First line is treated as header.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            return []
        
        # Parse header
        header = lines[0].strip().split(delimiter)
        
        # Parse data rows
        data_rows = []
        for line in lines[1:]:
            row = line.strip().split(delimiter)
            if len(row) == len(header):
                row_dict = {header[j]: value for j, value in enumerate(row)}
                data_rows.append(row_dict)
        
        return data_rows
        
    except Exception as e:
        print(f"Error: {e}")
        return []

def writeCSVData(filename, data, headers):
    """Write data in CSV format"""
    try:
        with open(filename, 'w') as file:
            # Write header
            file.write(','.join(headers) + '\n')
            
            # Write data
            for row in data:
                values = [str(row.get(header, '')) for header in headers]
                file.write(','.join(values) + '\n')
                
        print(f"CSV data written to {filename}")
        
    except Exception as e:
        print(f"Error writing CSV: {e}")

# Example usage
def gradeBookExample():
    """Example using CSV operations for grade management"""
    # Sample data
    students = [
        {"Name": "Alice", "Math": "95", "Science": "87", "English": "92"},
        {"Name": "Bob", "Math": "78", "Science": "89", "English": "84"},
        {"Name": "Carol", "Math": "92", "Science": "95", "English": "88"}
    ]
    
    headers = ["Name", "Math", "Science", "English"]
    
    # Write to file
    writeCSVData("grades.csv", students, headers)
    
    # Read and process
    loaded_data = processCSVData("grades.csv")
    
    # Calculate averages
    print("\nGrade Analysis:")
    for student in loaded_data:
        name = student["Name"]
        try:
            math_grade = float(student["Math"])
            science_grade = float(student["Science"])
            english_grade = float(student["English"])
            
            average = (math_grade + science_grade + english_grade) / 3
            print(f"{name}: Average = {average:.2f}")
            
        except ValueError:
            print(f"Error calculating average for {name}")
```

### TASK 5: Log File Management

**CONTEXT**: Program monitoring and debugging - useful for exam projects

```python
import datetime

def writeLog(message, log_file="program.log"):
    """
    Write timestamped log entries
    Useful for debugging and program monitoring
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    try:
        with open(log_file, 'a') as file:
            file.write(log_entry)
    except Exception as e:
        print(f"Error writing to log: {e}")

def readLog(log_file="program.log", lines=10):
    """Read last N lines from log file"""
    try:
        with open(log_file, 'r') as file:
            all_lines = file.readlines()
            
        # Get last N lines
        recent_lines = all_lines[-lines:] if len(all_lines) > lines else all_lines
        
        print(f"Last {len(recent_lines)} log entries:")
        for line in recent_lines:
            print(line.strip())
            
    except FileNotFoundError:
        print(f"Log file {log_file} not found")
    except Exception as e:
        print(f"Error reading log: {e}")

# Example usage in exam project
def examProjectWithLogging():
    """Example exam project pattern with logging"""
    writeLog("Program started")
    
    try:
        # Simulate program operations
        data = processDataFile("input.txt")
        writeLog(f"Processed {len(data)} items from input file")
        
        # Perform calculations
        result = sum(data) if data else 0
        writeLog(f"Calculation result: {result}")
        
        # Save results
        with open("results.txt", "w") as file:
            file.write(f"Results: {result}\n")
        writeLog("Results saved to results.txt")
        
    except Exception as e:
        writeLog(f"ERROR: {e}")
        print(f"An error occurred: {e}")
    
    finally:
        writeLog("Program ended")
```

## REAL-WORLD APPLICATIONS

### PROJECT PATTERN: Student Grade Manager

```python
def studentGradeManager():
    """
    Complete grade management system with file persistence
    Demonstrates comprehensive file operations
    """
    GRADES_FILE = "student_grades.txt"
    
    def loadGrades():
        """Load grades from file"""
        grades = {}
        try:
            with open(GRADES_FILE, 'r') as file:
                for line in file:
                    line = line.strip()
                    if ':' in line:
                        name, grade_list = line.split(':', 1)
                        grades[name] = [float(g) for g in grade_list.split(',') if g.strip()]
        except FileNotFoundError:
            print("No existing grades file found. Starting fresh.")
        except Exception as e:
            print(f"Error loading grades: {e}")
        return grades
    
    def saveGrades(grades):
        """Save grades to file"""
        try:
            with open(GRADES_FILE, 'w') as file:
                for name, grade_list in grades.items():
                    grade_str = ','.join(str(g) for g in grade_list)
                    file.write(f"{name}:{grade_str}\n")
            print("Grades saved successfully")
        except Exception as e:
            print(f"Error saving grades: {e}")
    
    def generateReport(grades):
        """Generate comprehensive grade report"""
        report_file = "grade_report.txt"
        try:
            with open(report_file, 'w') as file:
                file.write("STUDENT GRADE REPORT\n")
                file.write("=" * 50 + "\n\n")
                
                for name, grade_list in grades.items():
                    if grade_list:
                        average = sum(grade_list) / len(grade_list)
                        file.write(f"Student: {name}\n")
                        file.write(f"Grades: {', '.join(str(g) for g in grade_list)}\n")
                        file.write(f"Average: {average:.2f}\n")
                        
                        # Letter grade
                        if average >= 90:
                            letter = 'A'
                        elif average >= 80:
                            letter = 'B'
                        elif average >= 70:
                            letter = 'C'
                        elif average >= 60:
                            letter = 'D'
                        else:
                            letter = 'F'
                        
                        file.write(f"Letter Grade: {letter}\n")
                        file.write("-" * 30 + "\n")
                
            print(f"Report generated: {report_file}")
        except Exception as e:
            print(f"Error generating report: {e}")
    
    # Main program
    grades = loadGrades()
    
    while True:
        print("\n=== GRADE MANAGER ===")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student")
        print("4. View All Students")
        print("5. Generate Report")
        print("6. Save and Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            if name not in grades:
                grades[name] = []
                print(f"Added student: {name}")
            else:
                print("Student already exists")
                
        elif choice == '2':
            name = input("Enter student name: ")
            if name in grades:
                try:
                    grade = float(input("Enter grade: "))
                    grades[name].append(grade)
                    print(f"Added grade {grade} for {name}")
                except ValueError:
                    print("Invalid grade format")
            else:
                print("Student not found")
                
        elif choice == '3':
            name = input("Enter student name: ")
            if name in grades:
                grade_list = grades[name]
                if grade_list:
                    average = sum(grade_list) / len(grade_list)
                    print(f"{name}: {grade_list}, Average: {average:.2f}")
                else:
                    print(f"{name}: No grades recorded")
            else:
                print("Student not found")
                
        elif choice == '4':
            if grades:
                for name, grade_list in grades.items():
                    if grade_list:
                        average = sum(grade_list) / len(grade_list)
                        print(f"{name}: Average {average:.2f}")
                    else:
                        print(f"{name}: No grades")
            else:
                print("No students found")
                
        elif choice == '5':
            generateReport(grades)
            
        elif choice == '6':
            saveGrades(grades)
            break
            
        else:
            print("Invalid choice")
```

## COMMON PITFALLS & DEBUGGING

### 1. File Not Closed Properly

```python
# WRONG - File might not close on error
file = open("data.txt", "r")
data = file.read()
# If error occurs here, file stays open
file.close()

# RIGHT - Always use 'with' statement
with open("data.txt", "r") as file:
    data = file.read()
# File automatically closed even if error occurs
```

### 2. Path and Encoding Issues

```python
# Handle different operating systems
import os

# Use os.path.join for cross-platform paths
filename = os.path.join("data", "input.txt")

# Specify encoding for special characters
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Handle current working directory
import os
print(f"Current directory: {os.getcwd()}")

# Use absolute paths when necessary
abs_path = os.path.abspath("data.txt")
```

### 3. Memory Issues with Large Files

```python
# WRONG - Loads entire file into memory
with open("huge_file.txt", "r") as file:
    content = file.read()  # Could cause memory error

# RIGHT - Process line by line
with open("huge_file.txt", "r") as file:
    for line in file:
        process_line(line.strip())  # Process one line at a time

# Or read in chunks
def read_in_chunks(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk
```

## PERFORMANCE TIPS

### 1. Efficient File Reading

```python
# For small files - read all at once
with open("small_file.txt", "r") as file:
    lines = file.readlines()

# For large files - use generator
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage
for line in read_large_file("large_file.txt"):
    process(line)
```

### 2. Batch Writing

```python
# SLOW - Multiple file operations
for item in data:
    with open("output.txt", "a") as file:
        file.write(f"{item}\n")

# FAST - Single file operation
with open("output.txt", "w") as file:
    for item in data:
        file.write(f"{item}\n")

# FASTEST - Join all data first
output_text = '\n'.join(str(item) for item in data) + '\n'
with open("output.txt", "w") as file:
    file.write(output_text)
```

## STUDY CHECKLIST FOR EXAMS

### BASIC LEVEL (MUST KNOW)

- [ ] Open files safely using 'with' statement
- [ ] Read files using read(), readline(), readlines()
- [ ] Write files using write() and writelines()
- [ ] Handle FileNotFoundError with try/except
- [ ] Understand file modes: 'r', 'w', 'a', 'x'
- [ ] Process files line by line in loops
- [ ] Close files properly to prevent data loss

### INTERMEDIATE LEVEL

- [ ] Handle multiple exception types in file operations
- [ ] Process mixed data types from files (numbers and strings)
- [ ] Validate file data and clean input
- [ ] Create structured output files with formatting
- [ ] Use append mode for logging and data collection
- [ ] Check if files exist before operating on them

### ADVANCED LEVEL (BONUS UNDERSTANDING)

- [ ] Process CSV-style structured data
- [ ] Handle large files efficiently (chunk processing)
- [ ] Work with file paths across different operating systems
- [ ] Implement backup and recovery for data files
- [ ] Use file operations in complex program workflows

## QUICK REFERENCE COMMANDS

### Essential File Operations

```python
# Safe file reading
with open("filename.txt", "r") as file:
    content = file.read()

# Safe file writing  
with open("filename.txt", "w") as file:
    file.write("content")

# Line by line processing
with open("filename.txt", "r") as file:
    for line in file:
        print(line.strip())

# Error handling
try:
    with open("filename.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
```

### Data Type Processing

```python
def processFileData(filename):
    """Process mixed data types from file"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():
                    number = int(line)
                    # Process number
                elif line:
                    text = line
                    # Process text
    except FileNotFoundError:
        print(f"File {filename} not found")
```

---

**KEY INSIGHT**: File operations are essential for data persistence and real-world programming. Master safe file handling with proper error management to excel in exam projects and practical applications.

**EXAM STRATEGY**: Always use 'with' statements for file operations, handle exceptions gracefully, and validate data when reading from files. These patterns demonstrate professional programming practices.

**REMEMBER**: Files are external resources that can fail - always anticipate and handle errors. Use try/except blocks and 'with' statements to write robust, reliable file handling code.