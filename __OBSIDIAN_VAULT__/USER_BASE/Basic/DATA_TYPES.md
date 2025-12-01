# Domain: Data Types

## Overview
Python has several built-in data types that determine what kind of values a variable can hold and what operations can be performed on them. Python automatically assigns the type based on the value.

---

## All Python Data Types

### Text Type
- **str** (String): Text data enclosed in quotes

### Numeric Types
- **int** (Integer): Whole numbers
- **float** (Float): Decimal numbers
- **complex** (Complex): Numbers with real and imaginary parts

### Sequence Types
- **list** (List): Ordered, mutable collection
- **tuple** (Tuple): Ordered, immutable collection
- **range** (Range): Sequence of numbers

### Mapping Type
- **dict** (Dictionary): Key-value pairs

### Set Types
- **set** (Set): Unordered collection of unique values
- **frozenset** (Frozen Set): Immutable set

### Boolean Type
- **bool** (Boolean): True or False

### Binary Types
- **bytes** (Bytes): Immutable byte sequence
- **bytearray** (Byte Array): Mutable byte sequence
- **memoryview** (Memory View): Memory view object

### None Type
- **NoneType** (None): Represents absence of value

---

## Getting Data Type

**Check type with type()**:
```python
x = 5
print(type(x))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>

items = [1, 2, 3]
print(type(items))  # <class 'list'>

# Get type name as string
print(type(x).__name__)  # 'int'

# Check if specific type
if type(x) == int:
    print("x is an integer")

# Better way: use isinstance()
if isinstance(x, int):
    print("x is an integer")

# Check multiple types
value = "123"
if isinstance(value, (int, float, str)):
    print("value is int, float, or str")
```

---

## Setting Data Types

**Python assigns type automatically**:

### String
```python
# All create strings
x = "Hello"
x = 'Hello'
x = """Hello"""

print(type(x))  # <class 'str'>

# Examples
name = "Alice"
message = 'Welcome!'
paragraph = """This is
a multi-line
string"""

# Empty string
empty = ""
print(len(empty))  # 0
```

### Numeric Types
```python
# Integer
x = 20
x = -100
x = 0
print(type(x))  # <class 'int'>

# Float
x = 20.5
x = -15.7
x = 3.14
print(type(x))  # <class 'float'>

# Complex
x = 1j
x = 3 + 4j
x = complex(2, 5)
print(type(x))  # <class 'complex'>
```

### Sequence Types
```python
# List
x = ["apple", "banana", "cherry"]
x = [1, 2, 3, 4, 5]
x = []  # Empty list
print(type(x))  # <class 'list'>

# Tuple
x = ("apple", "banana", "cherry")
x = (1, 2, 3)
x = ()  # Empty tuple
x = (1,)  # Single item tuple (note the comma!)
print(type(x))  # <class 'tuple'>

# Range
x = range(6)  # 0, 1, 2, 3, 4, 5
x = range(2, 10)  # 2, 3, 4, 5, 6, 7, 8, 9
x = range(0, 10, 2)  # 0, 2, 4, 6, 8
print(type(x))  # <class 'range'>
```

### Mapping Type
```python
# Dictionary
x = {"name": "Alice", "age": 25}
x = {}  # Empty dict
x = dict(name="Bob", age=30)
print(type(x))  # <class 'dict'>

# Examples
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Nested dictionaries
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
```

### Set Types
```python
# Set
x = {"apple", "banana", "cherry"}
x = set()  # Empty set (can't use {})
print(type(x))  # <class 'set'>

# Frozenset (immutable)
x = frozenset({"apple", "banana", "cherry"})
print(type(x))  # <class 'frozenset'>

# Note: {} creates dict, not set
empty_dict = {}
empty_set = set()
```

### Boolean Type
```python
# Boolean
x = True
x = False
print(type(x))  # <class 'bool'>

# From comparisons
x = 10 > 5  # True
x = 5 == 3  # False

# From bool() function
x = bool(1)      # True
x = bool(0)      # False
x = bool("Hi")   # True
x = bool("")     # False
```

### Binary Types
```python
# Bytes (immutable)
x = b"Hello"
x = bytes(5)  # 5 zero bytes
print(type(x))  # <class 'bytes'>

# Bytearray (mutable)
x = bytearray(5)  # 5 zero bytes
x = bytearray(b"Hello")
print(type(x))  # <class 'bytearray'>

# Memoryview
x = memoryview(bytes(5))
print(type(x))  # <class 'memoryview'>
```

### None Type
```python
# None
x = None
print(type(x))  # <class 'NoneType'>

# Common uses
def no_return():
    print("Hello")

result = no_return()
print(result)  # None

# Default parameter
def greet(name=None):
    if name is None:
        name = "Guest"
    print(f"Hello, {name}")
```

---

## Type Conversion (Casting)

### To String (str)
```python
# Numbers to string
x = str(123)      # "123"
x = str(45.6)     # "45.6"
x = str(3 + 4j)   # "(3+4j)"

# Collections to string
x = str([1, 2, 3])           # "[1, 2, 3]"
x = str({"a": 1, "b": 2})    # "{'a': 1, 'b': 2}"

# Boolean to string
x = str(True)     # "True"
x = str(False)    # "False"

# Format conversion
num = 42
text = f"Number: {num}"  # "Number: 42"
```

### To Integer (int)
```python
# String to int
x = int("123")    # 123
# x = int("45.6")  # Error! Can't convert float string directly

# Float to int (truncates)
x = int(45.9)     # 45 (not 46!)
x = int(-3.7)     # -3

# Boolean to int
x = int(True)     # 1
x = int(False)    # 0

# From different bases
x = int("1010", 2)   # 10 (binary)
x = int("FF", 16)    # 255 (hex)
x = int("12", 8)     # 10 (octal)
```

### To Float (float)
```python
# String to float
x = float("123")      # 123.0
x = float("45.6")     # 45.6
x = float("3.14e-2")  # 0.0314

# Integer to float
x = float(123)        # 123.0

# Boolean to float
x = float(True)       # 1.0
x = float(False)      # 0.0

# Special values
x = float('inf')      # inf
x = float('-inf')     # -inf
x = float('nan')      # nan
```

### To List (list)
```python
# String to list (characters)
x = list("Hello")     # ['H', 'e', 'l', 'l', 'o']

# Tuple to list
x = list((1, 2, 3))   # [1, 2, 3]

# Range to list
x = list(range(5))    # [0, 1, 2, 3, 4]

# Set to list
x = list({1, 2, 3})   # [1, 2, 3]

# Dictionary to list (keys only)
d = {"a": 1, "b": 2}
x = list(d)           # ['a', 'b']
x = list(d.values())  # [1, 2]
x = list(d.items())   # [('a', 1), ('b', 2)]
```

### To Tuple (tuple)
```python
# List to tuple
x = tuple([1, 2, 3])   # (1, 2, 3)

# String to tuple
x = tuple("Hello")     # ('H', 'e', 'l', 'l', 'o')

# Range to tuple
x = tuple(range(5))    # (0, 1, 2, 3, 4)
```

### To Set (set)
```python
# List to set (removes duplicates)
x = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# String to set (unique characters)
x = set("Hello")      # {'H', 'e', 'l', 'o'}

# Tuple to set
x = set((1, 2, 3))    # {1, 2, 3}
```

### To Dictionary (dict)
```python
# List of tuples to dict
x = dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}

# Two lists to dict
keys = ["name", "age"]
values = ["Alice", 25]
x = dict(zip(keys, values))  # {'name': 'Alice', 'age': 25}

# Using dict() constructor
x = dict(name="Alice", age=25)  # {'name': 'Alice', 'age': 25}
```

### To Boolean (bool)
```python
# Falsy values (convert to False)
print(bool(False))     # False
print(bool(None))      # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(""))        # False
print(bool([]))        # False
print(bool({}))        # False
print(bool(()))        # False

# Truthy values (everything else = True)
print(bool(True))      # True
print(bool(1))         # True
print(bool(-1))        # True
print(bool("Hello"))   # True
print(bool([1]))       # True
print(bool({"a": 1}))  # True
```

---

## Mutable vs Immutable

### Immutable (Cannot Change)
**Once created, the value cannot be modified**:

```python
# Immutable types
# - int, float, complex
# - str
# - tuple
# - frozenset
# - bytes

# Example: String (immutable)
text = "Hello"
# text[0] = "J"  # Error! Can't modify

# Must create new string
text = "J" + text[1:]  # "Jello"

# Example: Tuple (immutable)
coords = (10, 20)
# coords[0] = 15  # Error! Can't modify

# Must create new tuple
coords = (15, 20)

# Example: Integer (immutable)
x = 5
x = x + 1  # Creates NEW integer object (6)
# Doesn't modify the original 5

# Consequences
a = "Hello"
b = a
a = a + " World"
print(a)  # "Hello World"
print(b)  # "Hello" (unchanged)
```

### Mutable (Can Change)
**Can be modified after creation**:

```python
# Mutable types
# - list
# - dict
# - set
# - bytearray

# Example: List (mutable)
numbers = [1, 2, 3]
numbers[0] = 10  # Works! Modifies list
numbers.append(4)  # Adds to same list
print(numbers)  # [10, 2, 3, 4]

# Example: Dictionary (mutable)
person = {"name": "Alice", "age": 25}
person["age"] = 26  # Modifies dict
person["city"] = "NYC"  # Adds to dict
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'NYC'}

# Example: Set (mutable)
items = {1, 2, 3}
items.add(4)  # Modifies set
items.remove(1)  # Modifies set
print(items)  # {2, 3, 4}

# Consequences (be careful!)
list1 = [1, 2, 3]
list2 = list1  # Both point to SAME list!
list1.append(4)
print(list1)  # [1, 2, 3, 4]
print(list2)  # [1, 2, 3, 4] (also changed!)

# To avoid, make a copy
list1 = [1, 2, 3]
list2 = list1.copy()  # or list(list1) or list1[:]
list1.append(4)
print(list1)  # [1, 2, 3, 4]
print(list2)  # [1, 2, 3] (unchanged)
```

---

## Common Type Operations

### Check Type
```python
# type() function
x = 5
print(type(x))  # <class 'int'>
print(type(x) == int)  # True

# isinstance() function (better for checking)
x = 5
print(isinstance(x, int))  # True

# Check multiple types
value = "123"
if isinstance(value, (int, float)):
    print("Number")
elif isinstance(value, str):
    print("String")  # This prints

# Check inheritance
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))     # True
print(isinstance(d, Animal))  # True (Dog is Animal)
print(type(d) == Animal)      # False (exact type is Dog)
```

### Type Comparison
```python
# Using type()
x = 5
y = 5.0

print(type(x) == type(y))  # False (int vs float)
print(x == y)              # True (values equal)

# Using isinstance()
print(isinstance(x, int))    # True
print(isinstance(y, float))  # True

# Check for number types
import numbers
print(isinstance(5, numbers.Number))    # True
print(isinstance(5.0, numbers.Number))  # True
print(isinstance(3+4j, numbers.Number)) # True
```

### Type Safety
```python
# Type hints (Python 3.5+)
def greet(name: str) -> str:
    return f"Hello, {name}"

# Type checking at runtime
def add_numbers(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be int or float")
    return a + b

# Safe conversion
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("123"))   # 123
print(safe_int("abc"))   # 0
print(safe_int(None))    # 0
```

---

## Real-World Examples

### Data Validation
```python
def validate_user_data(data):
    # Check types
    if not isinstance(data, dict):
        return False, "Data must be dictionary"
    
    # Check required fields
    if "name" not in data or not isinstance(data["name"], str):
        return False, "Name must be string"
    
    if "age" not in data or not isinstance(data["age"], int):
        return False, "Age must be integer"
    
    if "email" not in data or not isinstance(data["email"], str):
        return False, "Email must be string"
    
    return True, "Valid"

# Test
user1 = {"name": "Alice", "age": 25, "email": "alice@example.com"}
user2 = {"name": "Bob", "age": "30", "email": "bob@example.com"}

print(validate_user_data(user1))  # (True, 'Valid')
print(validate_user_data(user2))  # (False, 'Age must be integer')
```

### Type-Based Processing
```python
def process_data(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return data * 2
    elif isinstance(data, list):
        return len(data)
    elif isinstance(data, dict):
        return list(data.keys())
    else:
        return None

print(process_data("hello"))       # "HELLO"
print(process_data(5))             # 10
print(process_data([1, 2, 3]))     # 3
print(process_data({"a": 1}))      # ['a']
```

### Safe Type Conversion
```python
def convert_to_type(value, target_type):
    """Safely convert value to target type."""
    try:
        if target_type == 'int':
            return int(value)
        elif target_type == 'float':
            return float(value)
        elif target_type == 'str':
            return str(value)
        elif target_type == 'bool':
            return bool(value)
        elif target_type == 'list':
            return list(value)
        else:
            return None
    except (ValueError, TypeError):
        return None

# Test
print(convert_to_type("123", 'int'))    # 123
print(convert_to_type("3.14", 'float')) # 3.14
print(convert_to_type(42, 'str'))       # "42"
print(convert_to_type("abc", 'int'))    # None (conversion failed)
```

---

## Quick Reference

### All Types
```python
str:       "Hello"
int:       42
float:     3.14
complex:   3+4j
list:      [1, 2, 3]
tuple:     (1, 2, 3)
range:     range(5)
dict:      {"key": "value"}
set:       {1, 2, 3}
frozenset: frozenset({1, 2, 3})
bool:      True/False
bytes:     b"Hello"
bytearray: bytearray(5)
memoryview: memoryview(bytes(5))
NoneType:  None
```

### Type Checking
```python
type(x)           # Get type
isinstance(x, t)  # Check type
type(x) == type(y)  # Compare types
```

### Conversion
```python
str(x)    # To string
int(x)    # To integer
float(x)  # To float
list(x)   # To list
tuple(x)  # To tuple
set(x)    # To set
dict(x)   # To dictionary
bool(x)   # To boolean
```

### Mutability
```python
# Immutable: int, float, str, tuple, frozenset
# Mutable: list, dict, set, bytearray
```

