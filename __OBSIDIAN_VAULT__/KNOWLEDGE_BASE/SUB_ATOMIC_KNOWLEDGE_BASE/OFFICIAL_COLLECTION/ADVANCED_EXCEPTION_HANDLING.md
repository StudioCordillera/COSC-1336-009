# EXCEPTION_HANDLING.md

## META-INFORMATION

- **SOURCE**: W3Schools Python Exception Handling + COSC-1336 Exam Project Patterns
- **FAMILY**: Error Management & Program Reliability
- **CROSS-REFERENCES**: [[INPUT_OUTPUT_OPERATIONS.md]], [[FILE_OPERATIONS.md]], [[FUNCTIONS.md]], [[LOOPS.md]]
- **EXAM_RELEVANCE**: CRITICAL - Exception handling essential for robust programs
- **LAST_UPDATED**: 2025-01-19

## BY YOU FOR YOU: PRACTICAL NOTES

### WHAT IS EXCEPTION HANDLING?

Exception handling is the process of responding to exceptional circumstances during program execution. It prevents programs from crashing when unexpected errors occur and provides graceful error recovery.

### WHY EXCEPTION HANDLING MATTERS

From exam starter file analysis (particularly the `getIntegerData()` and `getFloatData()` functions), exception handling enables:

- **Input Validation**: Handle invalid user input gracefully
- **File Operation Safety**: Manage file errors without program crashes  
- **Data Type Conversion**: Safely convert between data types
- **User Experience**: Provide helpful error messages instead of cryptic crashes
- **Program Reliability**: Keep programs running despite unexpected issues
- **Professional Quality**: Demonstrate proper error management skills

### CRITICAL PATTERNS FOR EXAM SUCCESS

Based on exam starter file patterns, these exception handling approaches are essential:

1. **Input Validation Loops**: Continuously prompt until valid input received
2. **Try-Except Blocks**: Catch specific exceptions and provide recovery
3. **User-Friendly Messages**: Clear error messages that guide users
4. **Graceful Degradation**: Program continues operating after errors
5. **Resource Protection**: Ensure files and resources are properly managed

## W3SCHOOLS INTEGRATION

### 1. BASIC TRY-EXCEPT STRUCTURE

```python
# Basic exception handling
try:
    # Code that might raise an exception
    risky_operation()
except ExceptionType:
    # Handle the exception
    print("An error occurred")

# Handle multiple exception types
try:
    result = int(input("Enter a number: "))
    answer = 10 / result
except ValueError:
    print("Invalid input - not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catch all exceptions
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
```

### 2. COMMON EXCEPTION TYPES

```python
# ValueError - Invalid value for operation
try:
    number = int("not_a_number")
except ValueError:
    print("Cannot convert to integer")

# TypeError - Wrong data type
try:
    result = "hello" + 5
except TypeError:
    print("Cannot add string and integer")

# FileNotFoundError - File doesn't exist
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")

# IndexError - List index out of range
try:
    my_list = [1, 2, 3]
    item = my_list[10]
except IndexError:
    print("Index out of range")

# KeyError - Dictionary key doesn't exist
try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]
except KeyError:
    print("Key not found in dictionary")
```

### 3. ELSE AND FINALLY CLAUSES

```python
# else - Runs if no exception occurred
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print(f"You entered: {number}")

# finally - Always runs (cleanup code)
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed")

# Complete structure
try:
    # Risky code
    result = perform_operation()
except SpecificError:
    # Handle specific error
    handle_error()
except Exception as e:
    # Handle any other error
    print(f"Unexpected error: {e}")
else:
    # Runs if no exception
    print("Operation successful")
finally:
    # Always runs
    cleanup_resources()
```

### 4. RAISING CUSTOM EXCEPTIONS

```python
# Raise built-in exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# Create custom exception classes
class CustomError(Exception):
    """Custom exception for specific situations"""
    pass

class InvalidGradeError(Exception):
    """Raised when grade is outside valid range"""
    def __init__(self, grade, message="Grade must be between 0 and 100"):
        self.grade = grade
        self.message = message
        super().__init__(self.message)

def validate_grade(grade):
    if not 0 <= grade <= 100:
        raise InvalidGradeError(grade)
    return grade
```

## EXAM-FOCUSED TASK DIRECTIVES

### TASK 1: Input Validation Functions (Exam Starter Pattern)

**CONTEXT**: Direct implementation of exam starter file patterns with enhanced error handling

```python
def getIntegerData(prompt):
    """
    Enhanced version of exam starter getIntegerData function
    Continuously prompts until valid integer is entered
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message. Enter numbers ONLY!')
        except KeyboardInterrupt:
            print("\n\t\tOperation cancelled by user")
            return None
        except Exception as e:
            print(f'\t\tUnexpected error: {e}')

def getFloatData(prompt):
    """
    Enhanced version of exam starter getFloatData function
    Handles floating point input with comprehensive validation
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message. Enter numbers ONLY!')
        except KeyboardInterrupt:
            print("\n\t\tOperation cancelled by user")
            return None
        except Exception as e:
            print(f'\t\tUnexpected error: {e}')

def getStringData(prompt, min_length=1, max_length=100):
    """
    Enhanced string input with validation
    """
    while True:
        try:
            value = input(prompt).strip()
            
            if len(value) < min_length:
                print(f'\t\tError: Input too short (minimum {min_length} characters)')
                continue
            
            if len(value) > max_length:
                print(f'\t\tError: Input too long (maximum {max_length} characters)')
                continue
                
            return value
            
        except KeyboardInterrupt:
            print("\n\t\tOperation cancelled by user")
            return None
        except Exception as e:
            print(f'\t\tUnexpected error: {e}')

def getCharData(prompt, valid_chars):
    """
    Enhanced version of exam starter getCharData function
    Accepts list of valid characters for flexibility
    """
    while True:
        try:
            value = input(prompt).upper().strip()
            
            if not value:
                print('\t\tError: Please enter a value')
                continue
            
            if len(value) != 1:
                print('\t\tError: Please enter exactly one character')
                continue
            
            if value not in valid_chars:
                valid_str = ', '.join(valid_chars)
                print(f'\t\tERROR Message: Wrong selection. Choose from: {valid_str}')
                continue
                
            return value
            
        except KeyboardInterrupt:
            print("\n\t\tOperation cancelled by user")
            return None
        except Exception as e:
            print(f'\t\tUnexpected error: {e}')

# Usage examples matching exam patterns
def examInputExample():
    """Demonstrate exam-style input validation"""
    print("Exam Project Input Validation Demo")
    
    # Get integer with validation
    age = getIntegerData("Enter your age: ")
    if age is None:
        return  # User cancelled
    
    # Get float with validation
    gpa = getFloatData("Enter your GPA: ")
    if gpa is None:
        return
    
    # Get string with validation
    name = getStringData("Enter your name: ", min_length=2, max_length=50)
    if name is None:
        return
    
    # Get character choice (exam pattern)
    grade_level = getCharData("Enter grade level (F/S/J/R): ", ['F', 'S', 'J', 'R'])
    if grade_level is None:
        return
    
    # Display results
    print(f"\nStudent Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"GPA: {gpa:.2f}")
    print(f"Grade Level: {grade_level}")
```

### TASK 2: File Operations with Exception Handling

**CONTEXT**: Safe file operations essential for exam projects involving data processing

```python
def safeFileRead(filename):
    """
    Safely read file with comprehensive exception handling
    Returns content or None if error occurs
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Successfully read {len(content)} characters from {filename}")
        return content
        
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found")
        print("Please check the filename and try again")
        return None
        
    except PermissionError:
        print(f"ERROR: Permission denied accessing '{filename}'")
        print("You may not have permission to read this file")
        return None
        
    except IsADirectoryError:
        print(f"ERROR: '{filename}' is a directory, not a file")
        return None
        
    except UnicodeDecodeError:
        print(f"ERROR: Cannot decode '{filename}' - file may be binary")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except:
            return None
            
    except Exception as e:
        print(f"ERROR: Unexpected error reading '{filename}': {e}")
        return None

def safeFileWrite(filename, content):
    """
    Safely write to file with exception handling
    Returns True if successful, False otherwise
    """
    try:
        # Create backup if file exists
        import os
        if os.path.exists(filename):
            backup_name = filename + ".backup"
            with open(filename, 'r') as original:
                with open(backup_name, 'w') as backup:
                    backup.write(original.read())
            print(f"Created backup: {backup_name}")
        
        # Write new content
        with open(filename, 'w') as file:
            file.write(content)
        
        print(f"Successfully wrote {len(content)} characters to {filename}")
        return True
        
    except PermissionError:
        print(f"ERROR: Permission denied writing to '{filename}'")
        return False
        
    except OSError as e:
        print(f"ERROR: System error writing to '{filename}': {e}")
        return False
        
    except Exception as e:
        print(f"ERROR: Unexpected error writing to '{filename}': {e}")
        return False

def processDataFileWithExceptions(filename):
    """
    Process data file with comprehensive error handling
    Demonstrates exam-level file processing
    """
    print(f"Processing data file: {filename}")
    
    # Read file safely
    content = safeFileRead(filename)
    if content is None:
        return None
    
    # Process data with exception handling
    processed_data = {
        'numbers': [],
        'strings': [],
        'errors': []
    }
    
    try:
        lines = content.strip().split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            if not line:  # Skip empty lines
                continue
            
            # Try to process as number
            try:
                if '.' in line:
                    number = float(line)
                else:
                    number = int(line)
                processed_data['numbers'].append(number)
                
            except ValueError:
                # Not a number, treat as string
                processed_data['strings'].append(line)
                
            except Exception as e:
                error_info = f"Line {line_num}: {e}"
                processed_data['errors'].append(error_info)
                print(f"Warning - {error_info}")
        
        # Generate summary
        print(f"Processing complete:")
        print(f"  Numbers found: {len(processed_data['numbers'])}")
        print(f"  Strings found: {len(processed_data['strings'])}")
        print(f"  Errors found: {len(processed_data['errors'])}")
        
        return processed_data
        
    except Exception as e:
        print(f"ERROR: Failed to process file content: {e}")
        return None
```

### TASK 3: Calculator with Exception Handling

**CONTEXT**: Comprehensive calculator demonstrating multiple exception types

```python
def safeCalculator():
    """
    Calculator with comprehensive exception handling
    Demonstrates professional error management
    """
    
    def getNumber(prompt):
        """Get number with validation"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number")
            except KeyboardInterrupt:
                print("\nOperation cancelled")
                return None
    
    def performOperation(num1, operator, num2):
        """Perform calculation with exception handling"""
        try:
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                return num1 / num2
            elif operator == '**':
                return num1 ** num2
            elif operator == '%':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot perform modulo by zero")
                return num1 % num2
            else:
                raise ValueError(f"Unknown operator: {operator}")
                
        except OverflowError:
            raise OverflowError("Result is too large to calculate")
        except Exception as e:
            raise Exception(f"Calculation error: {e}")
    
    # Main calculator loop
    print("Safe Calculator - Enter 'quit' to exit")
    
    while True:
        try:
            # Get first number
            print("\nEnter calculation (or 'quit' to exit)")
            first_input = input("First number: ").strip()
            
            if first_input.lower() == 'quit':
                print("Calculator closed")
                break
            
            num1 = float(first_input)
            
            # Get operator
            operator = input("Operator (+, -, *, /, **, %): ").strip()
            valid_operators = ['+', '-', '*', '/', '**', '%']
            
            if operator not in valid_operators:
                print(f"Invalid operator. Use: {', '.join(valid_operators)}")
                continue
            
            # Get second number
            num2 = getNumber("Second number: ")
            if num2 is None:
                continue
            
            # Perform calculation
            result = performOperation(num1, operator, num2)
            print(f"Result: {num1} {operator} {num2} = {result}")
            
            # Save to history (with exception handling)
            try:
                with open("calculator_history.txt", "a") as file:
                    file.write(f"{num1} {operator} {num2} = {result}\n")
            except Exception as e:
                print(f"Warning: Could not save to history: {e}")
            
        except ValueError as e:
            print(f"Input Error: {e}")
        except ZeroDivisionError as e:
            print(f"Math Error: {e}")
        except OverflowError as e:
            print(f"Overflow Error: {e}")
        except KeyboardInterrupt:
            print("\nCalculator interrupted by user")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again")
```

### TASK 4: Data Validation Class

**CONTEXT**: Object-oriented approach to validation for advanced projects

```python
class DataValidator:
    """
    Comprehensive data validation class
    Demonstrates advanced exception handling patterns
    """
    
    @staticmethod
    def validateAge(age):
        """Validate age with custom exceptions"""
        try:
            age = int(age)
            if age < 0:
                raise ValueError("Age cannot be negative")
            if age > 150:
                raise ValueError("Age must be realistic (0-150)")
            return age
        except ValueError as e:
            if "invalid literal" in str(e):
                raise ValueError("Age must be a whole number")
            else:
                raise
    
    @staticmethod
    def validateGrade(grade):
        """Validate grade (0-100)"""
        try:
            grade = float(grade)
            if not 0 <= grade <= 100:
                raise ValueError("Grade must be between 0 and 100")
            return grade
        except ValueError as e:
            if "invalid literal" in str(e):
                raise ValueError("Grade must be a number")
            else:
                raise
    
    @staticmethod
    def validateEmail(email):
        """Basic email validation"""
        try:
            if not isinstance(email, str):
                raise TypeError("Email must be a string")
            
            email = email.strip()
            
            if not email:
                raise ValueError("Email cannot be empty")
            
            if '@' not in email:
                raise ValueError("Email must contain @ symbol")
            
            parts = email.split('@')
            if len(parts) != 2:
                raise ValueError("Email must have exactly one @ symbol")
            
            username, domain = parts
            if not username or not domain:
                raise ValueError("Email must have username and domain")
            
            if '.' not in domain:
                raise ValueError("Email domain must contain a dot")
            
            return email
            
        except Exception as e:
            raise ValueError(f"Invalid email format: {e}")
    
    @staticmethod
    def validatePhone(phone):
        """Validate phone number format"""
        try:
            # Remove common separators
            clean_phone = ''.join(c for c in phone if c.isdigit())
            
            if len(clean_phone) not in [10, 11]:
                raise ValueError("Phone must be 10 or 11 digits")
            
            # Format as (XXX) XXX-XXXX
            if len(clean_phone) == 11 and clean_phone[0] == '1':
                clean_phone = clean_phone[1:]
            
            formatted = f"({clean_phone[:3]}) {clean_phone[3:6]}-{clean_phone[6:]}"
            return formatted
            
        except Exception as e:
            raise ValueError(f"Invalid phone format: {e}")

def demonstrateValidation():
    """Demonstrate validation with exception handling"""
    validator = DataValidator()
    
    test_data = [
        ("Age", "25", validator.validateAge),
        ("Age", "-5", validator.validateAge),
        ("Grade", "95.5", validator.validateGrade),
        ("Grade", "150", validator.validateGrade),
        ("Email", "test@example.com", validator.validateEmail),
        ("Email", "invalid-email", validator.validateEmail),
        ("Phone", "1234567890", validator.validatePhone),
        ("Phone", "123-456-7890", validator.validatePhone),
    ]
    
    print("Validation Test Results:")
    print("=" * 40)
    
    for data_type, value, validator_func in test_data:
        try:
            result = validator_func(value)
            print(f"✓ {data_type}: '{value}' → '{result}'")
        except Exception as e:
            print(f"✗ {data_type}: '{value}' → ERROR: {e}")
```

### TASK 5: Robust Program Template

**CONTEXT**: Complete program template demonstrating professional exception handling

```python
def robustProgramTemplate():
    """
    Template for robust programs with comprehensive exception handling
    Use this pattern for exam projects
    """
    
    def initialize():
        """Initialize program with error handling"""
        try:
            print("Initializing program...")
            # Setup configuration, load files, etc.
            config = loadConfiguration()
            return config
        except Exception as e:
            print(f"Initialization failed: {e}")
            return None
    
    def loadConfiguration():
        """Load program configuration"""
        try:
            # Try to load config file
            with open("config.txt", "r") as file:
                config = {}
                for line in file:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        config[key] = value
                return config
        except FileNotFoundError:
            # Use default configuration
            print("Config file not found, using defaults")
            return {"default": "true"}
        except Exception as e:
            print(f"Error loading config: {e}")
            return {}
    
    def mainLoop(config):
        """Main program loop with exception handling"""
        try:
            while True:
                print("\n=== MAIN MENU ===")
                print("1. Process Data")
                print("2. Generate Report")
                print("3. Save Results")
                print("4. Exit")
                
                choice = input("Enter choice (1-4): ").strip()
                
                if choice == '1':
                    processData()
                elif choice == '2':
                    generateReport()
                elif choice == '3':
                    saveResults()
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter 1-4.")
                    
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
        except Exception as e:
            print(f"Error in main loop: {e}")
            print("Program will continue...")
    
    def processData():
        """Process data with error handling"""
        try:
            filename = input("Enter data filename: ")
            
            # Validate file exists
            import os
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File {filename} does not exist")
            
            # Process file
            result = processDataFileWithExceptions(filename)
            if result:
                print("Data processing completed successfully")
            else:
                print("Data processing failed")
                
        except Exception as e:
            print(f"Error processing data: {e}")
    
    def generateReport():
        """Generate report with error handling"""
        try:
            print("Generating report...")
            # Report generation logic here
            print("Report generated successfully")
        except Exception as e:
            print(f"Error generating report: {e}")
    
    def saveResults():
        """Save results with error handling"""
        try:
            filename = input("Enter output filename: ")
            success = safeFileWrite(filename, "Sample results data")
            if success:
                print("Results saved successfully")
            else:
                print("Failed to save results")
        except Exception as e:
            print(f"Error saving results: {e}")
    
    def cleanup():
        """Cleanup resources"""
        try:
            print("Cleaning up resources...")
            # Close files, save data, etc.
            print("Cleanup completed")
        except Exception as e:
            print(f"Error during cleanup: {e}")
    
    # Main program execution
    try:
        config = initialize()
        if config is None:
            print("Program cannot start due to initialization errors")
            return
        
        mainLoop(config)
        
    except Exception as e:
        print(f"Fatal program error: {e}")
        
    finally:
        cleanup()
        print("Program terminated")

# Run the template
if __name__ == "__main__":
    robustProgramTemplate()
```

## REAL-WORLD APPLICATIONS

### PROJECT PATTERN: Student Information System

```python
class StudentInformationSystem:
    """
    Complete student system demonstrating comprehensive exception handling
    """
    
    def __init__(self):
        self.students = {}
        self.data_file = "students.txt"
        self.loadStudents()
    
    def loadStudents(self):
        """Load students from file with exception handling"""
        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    try:
                        parts = line.strip().split('|')
                        if len(parts) >= 3:
                            student_id = parts[0]
                            name = parts[1]
                            grades = [float(g) for g in parts[2:] if g]
                            self.students[student_id] = {
                                'name': name,
                                'grades': grades
                            }
                    except ValueError as e:
                        print(f"Error parsing line: {line.strip()}: {e}")
                        
        except FileNotFoundError:
            print(f"Student file {self.data_file} not found. Starting with empty database.")
        except Exception as e:
            print(f"Error loading students: {e}")
    
    def saveStudents(self):
        """Save students to file"""
        try:
            with open(self.data_file, 'w') as file:
                for student_id, info in self.students.items():
                    grades_str = '|'.join(str(g) for g in info['grades'])
                    file.write(f"{student_id}|{info['name']}|{grades_str}\n")
            return True
        except Exception as e:
            print(f"Error saving students: {e}")
            return False
    
    def addStudent(self):
        """Add student with validation"""
        try:
            student_id = input("Enter student ID: ").strip()
            
            if not student_id:
                raise ValueError("Student ID cannot be empty")
            
            if student_id in self.students:
                raise ValueError("Student ID already exists")
            
            name = input("Enter student name: ").strip()
            if not name:
                raise ValueError("Student name cannot be empty")
            
            self.students[student_id] = {
                'name': name,
                'grades': []
            }
            
            print(f"Student {name} added successfully")
            
        except ValueError as e:
            print(f"Error adding student: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def addGrade(self):
        """Add grade with validation"""
        try:
            student_id = input("Enter student ID: ").strip()
            
            if student_id not in self.students:
                raise KeyError("Student ID not found")
            
            grade_input = input("Enter grade (0-100): ")
            grade = float(grade_input)
            
            if not 0 <= grade <= 100:
                raise ValueError("Grade must be between 0 and 100")
            
            self.students[student_id]['grades'].append(grade)
            name = self.students[student_id]['name']
            print(f"Grade {grade} added for {name}")
            
        except KeyError as e:
            print(f"Student not found: {e}")
        except ValueError as e:
            print(f"Invalid grade: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def generateTranscript(self):
        """Generate transcript with error handling"""
        try:
            student_id = input("Enter student ID: ").strip()
            
            if student_id not in self.students:
                raise KeyError("Student ID not found")
            
            student = self.students[student_id]
            name = student['name']
            grades = student['grades']
            
            if not grades:
                print(f"No grades recorded for {name}")
                return
            
            # Calculate statistics
            average = sum(grades) / len(grades)
            highest = max(grades)
            lowest = min(grades)
            
            # Generate transcript file
            transcript_file = f"transcript_{student_id}.txt"
            
            with open(transcript_file, 'w') as file:
                file.write(f"STUDENT TRANSCRIPT\n")
                file.write(f"==================\n\n")
                file.write(f"Student ID: {student_id}\n")
                file.write(f"Name: {name}\n\n")
                file.write(f"Grades: {', '.join(str(g) for g in grades)}\n")
                file.write(f"Average: {average:.2f}\n")
                file.write(f"Highest: {highest}\n")
                file.write(f"Lowest: {lowest}\n")
                file.write(f"Grade Count: {len(grades)}\n")
            
            print(f"Transcript generated: {transcript_file}")
            
        except KeyError as e:
            print(f"Student not found: {e}")
        except Exception as e:
            print(f"Error generating transcript: {e}")
    
    def run(self):
        """Main system loop"""
        try:
            while True:
                print("\n=== STUDENT INFORMATION SYSTEM ===")
                print("1. Add Student")
                print("2. Add Grade")
                print("3. Generate Transcript")
                print("4. Save and Exit")
                
                choice = input("Enter choice (1-4): ").strip()
                
                if choice == '1':
                    self.addStudent()
                elif choice == '2':
                    self.addGrade()
                elif choice == '3':
                    self.generateTranscript()
                elif choice == '4':
                    if self.saveStudents():
                        print("Data saved successfully")
                    break
                else:
                    print("Invalid choice")
                    
        except KeyboardInterrupt:
            print("\nSystem interrupted")
            if self.saveStudents():
                print("Data saved before exit")
        except Exception as e:
            print(f"System error: {e}")
```

## COMMON PITFALLS & DEBUGGING

### 1. Catching Too Broad Exceptions

```python
# WRONG - Catches everything, hard to debug
try:
    risky_operation()
except Exception:
    print("Something went wrong")

# RIGHT - Catch specific exceptions
try:
    risky_operation()
except ValueError:
    print("Invalid value provided")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 2. Not Providing Recovery Options

```python
# WRONG - Just prints error and continues
try:
    process_file("data.txt")
except FileNotFoundError:
    print("File not found")

# RIGHT - Provides recovery options
try:
    process_file("data.txt")
except FileNotFoundError:
    print("File 'data.txt' not found")
    alternative = input("Enter alternative filename: ")
    if alternative:
        try:
            process_file(alternative)
        except Exception as e:
            print(f"Could not process {alternative}: {e}")
```

### 3. Ignoring Finally Clause Importance

```python
# WRONG - Resource might not be cleaned up
try:
    file = open("data.txt", "r")
    process_file(file)
    file.close()
except Exception:
    print("Error occurred")
    # File never closed if error happens!

# RIGHT - Use finally or with statement
try:
    file = open("data.txt", "r")
    process_file(file)
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()

# BETTER - Use with statement
try:
    with open("data.txt", "r") as file:
        process_file(file)
except Exception as e:
    print(f"Error: {e}")
```

## PERFORMANCE TIPS

### 1. Exception Handling Performance

```python
# SLOW - Using exceptions for control flow
def slow_number_check(value):
    try:
        return int(value)
    except ValueError:
        return None

# FAST - Check before converting
def fast_number_check(value):
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        return int(value)
    return None
```

### 2. Efficient Validation

```python
# SLOW - Multiple try/except blocks
def validate_data_slow(data):
    results = []
    for item in data:
        try:
            num = int(item)
            results.append(num)
        except ValueError:
            try:
                num = float(item)
                results.append(num)
            except ValueError:
                results.append(item)
    return results

# FAST - Single validation function
def validate_item(item):
    try:
        if '.' in item:
            return float(item)
        else:
            return int(item)
    except ValueError:
        return item

def validate_data_fast(data):
    return [validate_item(item) for item in data]
```

## STUDY CHECKLIST FOR EXAMS

### BASIC LEVEL (MUST KNOW)

- [ ] Use try/except blocks for error handling
- [ ] Handle ValueError for invalid input conversions
- [ ] Handle FileNotFoundError for missing files
- [ ] Provide user-friendly error messages
- [ ] Use while loops with exception handling for input validation
- [ ] Understand when exceptions occur (division by zero, invalid input)
- [ ] Know the difference between syntax errors and runtime errors

### INTERMEDIATE LEVEL

- [ ] Handle multiple exception types in single try block
- [ ] Use else clause for code that runs when no exception occurs
- [ ] Use finally clause for cleanup code
- [ ] Create input validation functions like exam starter patterns
- [ ] Handle KeyboardInterrupt for user cancellation
- [ ] Validate data ranges (age 0-150, grades 0-100)

### ADVANCED LEVEL (BONUS UNDERSTANDING)

- [ ] Create custom exception classes
- [ ] Raise exceptions with custom messages
- [ ] Chain exceptions with proper error context
- [ ] Implement comprehensive error logging
- [ ] Design graceful degradation strategies
- [ ] Use exception handling in object-oriented programs

## QUICK REFERENCE COMMANDS

### Essential Exception Patterns

```python
# Basic input validation (exam pattern)
def getValidInput(prompt, data_type=str):
    while True:
        try:
            if data_type == int:
                return int(input(prompt))
            elif data_type == float:
                return float(input(prompt))
            else:
                return input(prompt).strip()
        except ValueError:
            print("Invalid input, try again")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            return None

# Safe file operations
try:
    with open("filename.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")

# Multiple exception handling
try:
    result = risky_operation()
except (ValueError, TypeError) as e:
    print(f"Input error: {e}")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Validation Functions

```python
def validate_range(value, min_val, max_val, name):
    """Generic range validation"""
    if not min_val <= value <= max_val:
        raise ValueError(f"{name} must be between {min_val} and {max_val}")
    return value

def safe_convert(value, target_type, default=None):
    """Safely convert value to target type"""
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default
```

---

**KEY INSIGHT**: Exception handling is essential for creating robust, professional programs. Master try/except patterns to handle user input, file operations, and data processing errors gracefully.

**EXAM STRATEGY**: Always validate user input with appropriate exception handling. Use the exam starter file patterns as templates for input validation functions. Provide clear, helpful error messages.

**REMEMBER**: Exceptions are not failures - they're opportunities to handle unexpected situations gracefully and keep your program running smoothly. Good exception handling separates amateur code from professional code.
