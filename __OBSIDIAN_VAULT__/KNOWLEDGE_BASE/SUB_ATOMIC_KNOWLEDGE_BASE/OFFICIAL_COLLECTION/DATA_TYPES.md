# DATA_TYPES

## Node Metadata
- **Node Type**: Sub-Atomic Fundamental Concept
- **Knowledge Family**: Programming Foundations → Data Representation → Type Systems
- **W3Schools Reference**: Python Data Types (Primary Source - https://www.w3schools.com/python/python_datatypes.asp)
- **Python Docs**: Built-in Types (https://docs.python.org/3/library/stdtypes.html)
- **Textbook Coverage**: Gaddis Chapter 2 - Input, Processing, and Output (Data Types Section)
- **Course Competency**: Type Classification, Type Conversion, Type Operations, Built-in Types

## Tags
#data-types #type-systems #integers #floats #strings #booleans #lists #dictionaries #tuples #sets #w3schools-primary #type-conversion #built-in-types #type-checking #data-representation

## Family Relationships
### Parent Concepts
- [[VARIABLES]] - Variables store data of specific types
- Programming Fundamentals - Data types are core programming concepts
- Computer Memory - Types determine memory allocation and representation

### Child Concepts  
- Numeric Types (int, float, complex)
- Sequence Types (str, list, tuple, range)
- Mapping Types (dict)
- Set Types (set, frozenset)
- Boolean Type (bool)
- Binary Types (bytes, bytearray, memoryview)

### Sibling Concepts
- [[VARIABLES]] - Variables must have compatible data types
- [[INPUT_OUTPUT_OPERATIONS]] - I/O operations involve type conversion
- [[FUNCTIONS]] - Functions accept and return specific data types
- [[CONTROL_STRUCTURES]] - Control structures evaluate boolean data types

### Dependencies
- **Requires**: Basic programming concepts, variable understanding
- **Enables**: Type-safe programming, data manipulation, function parameters
- **Supports**: All programming operations, memory management, performance optimization

## Core Definition
**Data Types** specify the kind of value a variable can hold and determine what operations can be performed on that data. Python's built-in data types include numeric types (integers, floats), sequence types (strings, lists, tuples), mapping types (dictionaries), set types, and boolean types. Each data type has specific characteristics, methods, and memory requirements that influence program behavior and performance.

### Essential Characteristics
1. **Type Classification**: Categories like numeric, sequence, mapping, set, and boolean
2. **Mutability**: Whether data can be changed after creation (mutable vs immutable)
3. **Operations**: Specific operations and methods available for each type
4. **Memory Usage**: How different types are stored and accessed in memory
5. **Type Conversion**: Ability to convert between compatible data types

## Professor Implementation Requirements
- Demonstrate understanding of all built-in Python data types
- Use appropriate data type for specific programming scenarios
- Implement type conversion between compatible types
- Show knowledge of mutable vs immutable type differences
- Apply type-specific methods and operations correctly
- Handle type-related errors and exceptions appropriately

## Textbook Integration - Gaddis Chapter 2
### Key Learning Objectives
- Understand difference between numeric data types (int vs float)
- Work with string data type and string operations
- Use boolean data type in conditional expressions
- Apply appropriate data type for specific data storage needs
- Perform type conversion using built-in conversion functions

### Textbook Data Type Coverage
```python
# Basic data type examples from Gaddis
age = 25              # Integer type
price = 19.95         # Float type  
name = "John Smith"   # String type
is_student = True     # Boolean type
```

## W3Schools Integration (Primary Source)
### W3Schools Data Type Hierarchy Structure
1. **Text Type**: str (string)
2. **Numeric Types**: int (integer), float, complex
3. **Sequence Types**: list, tuple, range
4. **Mapping Type**: dict (dictionary)
5. **Set Types**: set, frozenset
6. **Boolean Type**: bool
7. **Binary Types**: bytes, bytearray, memoryview
8. **None Type**: NoneType

### W3Schools Core Examples
```python
# Text Type (W3Schools Primary)
x = "Hello World"                    # str
print(type(x))

# Numeric Types (W3Schools Primary)
x = 20                               # int
y = 20.5                            # float
z = 1j                              # complex

# Sequence Types (W3Schools Primary)
x = ["apple", "banana", "cherry"]    # list
y = ("apple", "banana", "cherry")    # tuple
z = range(6)                        # range

# Mapping Type (W3Schools Primary)
x = {"name" : "John", "age" : 36}   # dict

# Set Types (W3Schools Primary)
x = {"apple", "banana", "cherry"}    # set
y = frozenset({"apple", "banana", "cherry"})  # frozenset

# Boolean Type (W3Schools Primary)
x = True                            # bool
y = False                          # bool

# None Type (W3Schools Primary)
x = None                           # NoneType
```

### W3Schools Learning Path
- **Beginner**: Basic types (str, int, float, bool), type() function
- **Intermediate**: Collections (list, dict, tuple), type conversion
- **Advanced**: Set types, binary types, complex numbers, type checking

## Implementation Patterns

### Type Identification and Conversion
```python
# Type checking using type() and isinstance()
def identify_data_type(value):
    """
    Identify and display data type information
    
    Parameters:
    value: Any Python value
    """
    print(f"Value: {value}")
    print(f"Type: {type(value)}")
    print(f"Type name: {type(value).__name__}")
    
    # Type checking examples
    if isinstance(value, str):
        print("This is a string type")
    elif isinstance(value, (int, float)):
        print("This is a numeric type")
    elif isinstance(value, list):
        print("This is a list type")
    elif isinstance(value, dict):
        print("This is a dictionary type")

# Example usage
identify_data_type("Hello World")
identify_data_type(42)
identify_data_type([1, 2, 3])
identify_data_type({"name": "John", "age": 30})
```

### Type Conversion Patterns
```python
# Numeric type conversions
def demonstrate_type_conversion():
    """
    Show various type conversion techniques
    """
    # String to numeric conversions
    str_num = "123"
    int_value = int(str_num)         # String to integer
    float_value = float(str_num)     # String to float
    
    print(f"Original: {str_num} (type: {type(str_num)})")
    print(f"Integer: {int_value} (type: {type(int_value)})")
    print(f"Float: {float_value} (type: {type(float_value)})")
    
    # Numeric to string conversion
    number = 456.789
    str_value = str(number)          # Number to string
    print(f"Number: {number} (type: {type(number)})")
    print(f"String: {str_value} (type: {type(str_value)})")
    
    # Boolean conversions
    bool_from_int = bool(1)          # Non-zero integers are True
    bool_from_zero = bool(0)         # Zero is False
    bool_from_string = bool("text")  # Non-empty strings are True
    bool_from_empty = bool("")       # Empty strings are False
    
    print(f"bool(1): {bool_from_int}")
    print(f"bool(0): {bool_from_zero}")
    print(f"bool('text'): {bool_from_string}")
    print(f"bool(''): {bool_from_empty}")

demonstrate_type_conversion()
```

### Collection Data Types Implementation
```python
# Working with different collection types
def collection_type_examples():
    """
    Demonstrate usage of collection data types
    """
    # List (mutable sequence)
    fruits_list = ["apple", "banana", "cherry"]
    fruits_list.append("orange")    # Lists are mutable
    print(f"List: {fruits_list}")
    
    # Tuple (immutable sequence) 
    coordinates = (10, 20)
    # coordinates.append(30)        # This would cause error - tuples are immutable
    print(f"Tuple: {coordinates}")
    
    # Dictionary (key-value mapping)
    student_info = {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science"
    }
    student_info["gpa"] = 3.8       # Dictionaries are mutable
    print(f"Dictionary: {student_info}")
    
    # Set (unique elements)
    unique_numbers = {1, 2, 3, 2, 1}  # Duplicates automatically removed
    unique_numbers.add(4)            # Sets are mutable
    print(f"Set: {unique_numbers}")
    
    # Range (numeric sequence)
    number_range = range(5)          # 0, 1, 2, 3, 4
    range_list = list(number_range)  # Convert to list for display
    print(f"Range: {range_list}")

collection_type_examples()
```

## Advanced Techniques

### Type Annotations and Hints
```python
from typing import List, Dict, Tuple, Optional, Union

def process_student_data(
    name: str, 
    age: int, 
    grades: List[float], 
    info: Dict[str, str]
) -> Tuple[str, float]:
    """
    Process student data with type annotations
    
    Args:
        name (str): Student's full name
        age (int): Student's age in years
        grades (List[float]): List of numeric grades
        info (Dict[str, str]): Additional student information
        
    Returns:
        Tuple[str, float]: Student summary and average grade
    """
    average_grade = sum(grades) / len(grades) if grades else 0.0
    summary = f"{name} (age {age}): {len(grades)} grades recorded"
    
    return summary, average_grade

# Usage with proper types
student_grades = [85.5, 92.0, 78.5, 88.0]
student_info = {"major": "CS", "year": "sophomore"}
result = process_student_data("John Doe", 20, student_grades, student_info)
print(result)
```

### Custom Type Checking and Validation
```python
def validate_data_types(data_dict):
    """
    Validate data types in a dictionary with specific requirements
    
    Parameters:
    data_dict (dict): Dictionary with data to validate
    
    Returns:
    tuple: (is_valid, error_messages)
    """
    required_types = {
        'name': str,
        'age': int,  
        'salary': (int, float),  # Accept either int or float
        'active': bool,
        'skills': list
    }
    
    errors = []
    
    for key, expected_type in required_types.items():
        if key not in data_dict:
            errors.append(f"Missing required field: {key}")
            continue
            
        value = data_dict[key]
        
        if isinstance(expected_type, tuple):
            # Multiple acceptable types
            if not isinstance(value, expected_type):
                errors.append(f"{key} must be one of {expected_type}, got {type(value)}")
        else:
            # Single expected type
            if not isinstance(value, expected_type):
                errors.append(f"{key} must be {expected_type}, got {type(value)}")
    
    return len(errors) == 0, errors

# Example validation
employee_data = {
    'name': 'Alice Johnson',
    'age': 28,
    'salary': 75000.50,
    'active': True,
    'skills': ['Python', 'SQL', 'Git']
}

is_valid, validation_errors = validate_data_types(employee_data)
if is_valid:
    print("Data validation passed!")
else:
    print("Validation errors:")
    for error in validation_errors:
        print(f"  - {error}")
```

### Memory-Efficient Type Usage
```python
import sys
from decimal import Decimal

def compare_type_memory_usage():
    """
    Compare memory usage of different data types
    """
    # Integer vs Float memory comparison
    int_value = 42
    float_value = 42.0
    
    print(f"Integer {int_value}: {sys.getsizeof(int_value)} bytes")
    print(f"Float {float_value}: {sys.getsizeof(float_value)} bytes")
    
    # String vs Bytes comparison
    text_string = "Hello World"
    text_bytes = b"Hello World"
    
    print(f"String '{text_string}': {sys.getsizeof(text_string)} bytes")
    print(f"Bytes {text_bytes}: {sys.getsizeof(text_bytes)} bytes")
    
    # List vs Tuple comparison (same data)
    data_list = [1, 2, 3, 4, 5]
    data_tuple = (1, 2, 3, 4, 5)
    
    print(f"List {data_list}: {sys.getsizeof(data_list)} bytes")
    print(f"Tuple {data_tuple}: {sys.getsizeof(data_tuple)} bytes")
    
    # Set vs List for unique values
    unique_list = [1, 2, 3, 4, 5]
    unique_set = {1, 2, 3, 4, 5}
    
    print(f"List {unique_list}: {sys.getsizeof(unique_list)} bytes")
    print(f"Set {unique_set}: {sys.getsizeof(unique_set)} bytes")

compare_type_memory_usage()
```

## Quality Assessment

### Type-Related Testing Strategy
```python
def test_data_type_operations():
    """
    Comprehensive testing for data type operations
    """
    # Test numeric operations
    assert isinstance(5 + 3, int)           # Integer arithmetic
    assert isinstance(5.0 + 3, float)       # Float arithmetic
    assert isinstance(5 / 2, float)         # Division always returns float
    assert isinstance(5 // 2, int)          # Floor division returns int
    
    # Test string operations
    assert isinstance("Hello" + " World", str)
    assert isinstance("test" * 3, str)
    assert len("Python") == 6
    
    # Test list operations
    test_list = [1, 2, 3]
    test_list.append(4)
    assert len(test_list) == 4
    assert isinstance(test_list, list)
    
    # Test dictionary operations
    test_dict = {"key": "value"}
    test_dict["new_key"] = "new_value"
    assert len(test_dict) == 2
    assert isinstance(test_dict, dict)
    
    # Test type conversion accuracy
    assert int("123") == 123
    assert float("123.45") == 123.45
    assert str(456) == "456"
    assert bool(1) == True
    assert bool(0) == False
    
    print("All data type tests passed!")

test_data_type_operations()
```

### Common Type Errors and Debugging
```python
def handle_common_type_errors():
    """
    Demonstrate common type errors and their solutions
    """
    try:
        # Type conversion errors
        invalid_int = int("12.5")  # ValueError: invalid literal
    except ValueError as e:
        print(f"Type conversion error: {e}")
        # Solution: Use float() first, then int()
        correct_int = int(float("12.5"))
        print(f"Correct conversion: {correct_int}")
    
    try:
        # Unsupported operation errors
        result = "Hello" + 5  # TypeError: can't concatenate str and int
    except TypeError as e:
        print(f"Operation error: {e}")
        # Solution: Convert types for compatibility
        result = "Hello" + str(5)
        print(f"Correct operation: {result}")
    
    try:
        # Index errors with sequences
        data = [1, 2, 3]
        value = data[5]  # IndexError: list index out of range
    except IndexError as e:
        print(f"Index error: {e}")
        # Solution: Check bounds before accessing
        if 5 < len(data):
            value = data[5]
        else:
            print("Index out of range, using default")
            value = None

handle_common_type_errors()
```

### Performance Considerations
```python
import timeit

def performance_type_comparisons():
    """
    Compare performance of different data type operations
    """
    # List vs Tuple access performance
    test_list = list(range(1000))
    test_tuple = tuple(range(1000))
    
    list_time = timeit.timeit(lambda: test_list[500], number=1000000)
    tuple_time = timeit.timeit(lambda: test_tuple[500], number=1000000)
    
    print(f"List access time: {list_time:.6f} seconds")
    print(f"Tuple access time: {tuple_time:.6f} seconds")
    
    # Set vs List membership testing
    test_set = set(range(1000))
    test_list = list(range(1000))
    
    set_membership = timeit.timeit(lambda: 500 in test_set, number=100000)
    list_membership = timeit.timeit(lambda: 500 in test_list, number=100000)
    
    print(f"Set membership test: {set_membership:.6f} seconds")
    print(f"List membership test: {list_membership:.6f} seconds")

performance_type_comparisons()
```

## Backlink Reference System

### Incoming Links (Concepts that reference Data Types)
- [[VARIABLES]] → Variables must be declared with appropriate data types
- [[INPUT_OUTPUT_OPERATIONS]] → I/O operations involve data type conversion and validation
- [[FUNCTIONS]] → Functions accept parameters and return values of specific data types
- [[CONTROL_STRUCTURES]] → Conditional statements evaluate boolean data types
- Memory Management → Data types determine memory allocation and storage requirements
- Error Handling → Type errors are common programming issues requiring proper handling

### Outgoing Links (Concepts Data Types reference)
- [[VARIABLES]] ← Data types determine what values variables can store
- Type Conversion ← Converting between compatible data types for operations
- Memory Allocation ← Different types require different memory management strategies
- Performance Optimization ← Type choice affects program speed and memory usage
- Data Validation ← Ensuring data matches expected types for reliability
- Object-Oriented Programming ← Classes create custom data types with methods

### Cross-Reference Networks  
- **Programming Fundamentals**: Data types form the foundation of all programming concepts
- **Software Engineering**: Type systems enable code reliability, maintainability, and debugging
- **Computer Science Theory**: Data types connect to formal type theory and language design
- **Performance Engineering**: Type selection affects memory usage, speed, and scalability

## Integration Points

### Course Integration
- **Project Applications**: All programming projects require appropriate data type selection
- **Exam Preparation**: Data type questions appear in type conversion, operations, and debugging problems
- **Lab Exercises**: Weekly practice with type operations, conversions, and error handling
- **Problem Solving**: Data type understanding essential for algorithm implementation and data structure selection

### Professional Development Connections
- **Software Engineering**: Type systems enable large-scale software development and maintenance
- **Database Design**: Data types map to database column types and constraints
- **API Development**: Type definitions enable clear interfaces and data contracts
- **Performance Optimization**: Type selection directly impacts application performance and memory usage

### Advanced Programming Pathways
- **Static Type Checking**: Type hints and mypy for improved code reliability
- **Functional Programming**: Algebraic data types and type composition techniques  
- **Systems Programming**: Low-level data types and memory management considerations
- **Data Science**: Specialized data types for numerical computing and data analysis

---
*Last Updated: Current Session - Sub-Atomic Node with W3Schools Primary Source Integration*
*Node Family: Programming Foundations → Data Representation → Type Systems*  
*Cross-Reference Capacity: 15+ interconnected concepts with comprehensive backlinking*