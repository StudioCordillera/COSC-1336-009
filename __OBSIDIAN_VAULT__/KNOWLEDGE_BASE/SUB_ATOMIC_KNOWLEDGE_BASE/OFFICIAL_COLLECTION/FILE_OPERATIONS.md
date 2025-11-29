# FILE_OPERATIONS.md

## META-INFORMATION

- **SOURCE**: W3Schools Python File Handling + COSC-1336 Advanced Course Materials
- **FAMILY**: Input/Output Operations & Data Processing
- **CROSS-REFERENCES**: [[LOOPS.md]], [[LIST_OPERATIONS.md]], [[ERROR_HANDLING.md]], [[STRING_METHODS.md]]
- **EXAM_RELEVANCE**: HIGH - File operations critical for data processing projects
- **LAST_UPDATED**: 2025-01-19

## BY YOU FOR YOU: PRACTICAL NOTES

### WHAT IS FILE HANDLING?

File handling is the process of working with files stored on the computer - reading data from files, writing data to files, and managing file operations. It's essential for data persistence and processing.

### WHY FILE OPERATIONS MATTER

From course material analysis (particularly the advanced loop exercises with `data1.txt` processing), file operations enable:

- **Data Persistence**: Save program results and user data permanently
- **Data Processing**: Read and analyze datasets from external files  
- **Input Automation**: Load test data and configuration automatically
- **Report Generation**: Create output files with processed results
- **Real-World Integration**: Work with data from other systems and applications

### CRITICAL PATTERNS FOR EXAM SUCCESS

Based on analysis of course materials (particularly file processing with mixed data types), these patterns are essential:

1. **Safe File Reading**: Always use try/except for file operations
2. **Data Type Handling**: Process mixed numeric and string data from files
3. **Line Processing**: Clean and validate data from each line
4. **Error Recovery**: Handle file not found and permission errors gracefully
5. **Resource Management**: Properly close files to prevent data loss

## W3SCHOOLS INTEGRATION

### 1. OPENING FILES

```python
# Basic file opening
file = open("filename.txt", "r")  # Read mode
file = open("filename.txt", "w")  # Write mode (overwrites)
file = open("filename.txt", "a")  # Append mode
file = open("filename.txt", "x")  # Create mode (fails if exists)

# File modes
# "r" - Read (default)
# "w" - Write (overwrites existing file)
# "a" - Append (adds to end of file)
# "x" - Create (exclusive creation, fails if exists)
# "t" - Text mode (default)
# "b" - Binary mode

# Always close files
file.close()
```

### 2. SAFE FILE HANDLING WITH 'WITH' STATEMENT

```python
# BEST PRACTICE - Automatic file closing
with open("filename.txt", "r") as file:
    content = file.read()
# File automatically closed when leaving 'with' block

# Multiple files
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(processed_data)
```

### 3. READING FILES

```python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()  # Returns string with entire file

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # Remove newline characters

# Read all lines into list
with open("data.txt", "r") as file:
    lines = file.readlines()  # Returns list of lines

# Read one line at a time
with open("data.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
```

### 4. WRITING FILES

```python
# Write string to file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Write list of strings
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Append to existing file
with open("log.txt", "a") as file:
    file.write("New log entry\n")
```

## EXAM-FOCUSED TASK DIRECTIVES

### TASK 1: Safe File Reading with Error Handling

**CONTEXT**: Based on patterns observed in advanced course materials

```python
def safeReadFile(filename):
    """
    Safely read file with comprehensive error handling
    Returns list of cleaned lines or empty list if error
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Clean the data
        cleaned_lines = []
        for line in lines:
            cleaned = line.strip()  # Remove whitespace
            if cleaned:  # Skip empty lines
                cleaned_lines.append(cleaned)
        
        return cleaned_lines
        
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found")
        return []
    except PermissionError:
        print(f"ERROR: Permission denied to read '{filename}'")
        return []
    except Exception as e:
        print(f"ERROR: Unexpected error reading file: {e}")
        return []

# Usage pattern from course materials
def processDataFile(filename):
    """Process file with mixed data types like data1.txt"""
    lines = safeReadFile(filename)
    
    numbers = []
    strings = []
    
    for line in lines:
        # Try to convert to number first
        try:
            if '.' in line:
                numbers.append(float(line))
            else:
                numbers.append(int(line))
        except ValueError:
            # If not a number, treat as string
            strings.append(line)
    
    return numbers, strings
```

### TASK 2: Data Processing with File I/O

**CONTEXT**: Essential pattern for exam projects requiring data analysis

```python
def analyzeDataFile(filename):
    """
    Complete data analysis from file - exam project pattern
    """
    print(f"Analyzing data from: {filename}")
    
    # Read and process data
    numbers, strings = processDataFile(filename)
    
    if not numbers and not strings:
        print("No data found in file")
        return
    
    # Numeric analysis
    if numbers:
        print(f"\nNumeric Data Analysis:")
        print(f"Count: {len(numbers)}")
        print(f"Sum: {sum(numbers):.2f}")
        print(f"Average: {sum(numbers)/len(numbers):.2f}")
        print(f"Maximum: {max(numbers):.2f}")
        print(f"Minimum: {min(numbers):.2f}")
        
        # Write numeric results
        with open("numeric_analysis.txt", "w") as file:
            file.write(f"Numeric Analysis Results\n")
            file.write(f"========================\n")
            file.write(f"Total numbers: {len(numbers)}\n")
            file.write(f"Sum: {sum(numbers):.2f}\n")
            file.write(f"Average: {sum(numbers)/len(numbers):.2f}\n")
            file.write(f"Range: {max(numbers) - min(numbers):.2f}\n")
    
    # String analysis
    if strings:
        print(f"\nString Data Analysis:")
        print(f"Count: {len(strings)}")
        print(f"Unique values: {len(set(strings))}")
        
        # Write string results
        with open("string_analysis.txt", "w") as file:
            file.write(f"String Analysis Results\n")
            file.write(f"=======================\n")
            file.write(f"Total strings: {len(strings)}\n")
            file.write(f"Unique strings: {len(set(strings))}\n")
            file.write(f"All strings:\n")
            for i, s in enumerate(strings, 1):
                file.write(f"{i}. {s}\n")

# Usage
analyzeDataFile("data1.txt")
```

### TASK 3: User Data Collection and File Storage

**CONTEXT**: Interactive programs that save user input - common exam pattern

```python
def collectAndSaveUserData():
    """
    Collect user data and save to file with validation
    Pattern commonly used in exam projects
    """
    data = []
    
    print("Data Collection System")
    print("Enter data (type 'save' to save and exit, 'quit' to exit without saving)")
    
    while True:
        user_input = input("Enter data: ").strip()
        
        if user_input.lower() == 'save':
            break
        elif user_input.lower() == 'quit':
            print("Exiting without saving")
            return
        elif user_input:  # Not empty
            data.append(user_input)
            print(f"Added: {user_input}")
    
    if not data:
        print("No data to save")
        return
    
    # Get filename from user
    while True:
        filename = input("Enter filename to save (with .txt extension): ")
        if filename.endswith('.txt'):
            break
        print("Filename must end with .txt")
    
    # Save data
    try:
        with open(filename, 'w') as file:
            file.write(f"Data Collection Session\n")
            file.write(f"Total items: {len(data)}\n")
            file.write(f"{'='*30}\n")
            
            for i, item in enumerate(data, 1):
                file.write(f"{i}. {item}\n")
        
        print(f"Data saved successfully to {filename}")
        
    except Exception as e:
        print(f"Error saving file: {e}")

def loadAndDisplayData():
    """Load previously saved data file"""
    filename = input("Enter filename to load: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"\nContent of {filename}:")
            print("=" * 40)
            print(content)
            
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error loading file: {e}")
```

### TASK 4: CSV-Style Data Processing

**CONTEXT**: Structured data handling for advanced projects

```python
def processCSVData(filename, delimiter=','):
    """
    Process CSV-style data files
    Advanced pattern for structured data
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            print("File is empty")
            return []
        
        # Process header
        header = lines[0].strip().split(delimiter)
        print(f"Columns found: {header}")
        
        # Process data rows
        data_rows = []
        for i, line in enumerate(lines[1:], 2):  # Start from line 2
            row = line.strip().split(delimiter)
            
            if len(row) == len(header):
                # Create dictionary for each row
                row_dict = {}
                for j, value in enumerate(row):
                    row_dict[header[j]] = value
                data_rows.append(row_dict)
            else:
                print(f"Warning: Line {i} has {len(row)} columns, expected {len(header)}")
        
        return data_rows
        
    except Exception as e:
        print(f"Error processing CSV: {e}")
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