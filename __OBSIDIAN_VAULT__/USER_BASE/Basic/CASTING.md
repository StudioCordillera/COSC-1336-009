# Domain: Casting (Type Conversion)

## Overview
Casting is the process of converting one data type to another. Python provides built-in functions to convert between types. Understanding casting is essential for data manipulation, user input processing, and working with different data formats.

---

## Why Cast Types?

**Common scenarios**:
```python
# 1. User input (always string, need to convert)
age_str = input("Enter age: ")  # Returns string "25"
age = int(age_str)              # Convert to integer 25

# 2. Math with different types
text_num = "100"
result = int(text_num) + 50  # Convert then add: 150

# 3. String formatting
count = 42
message = "Count: " + str(count)  # Convert int to string

# 4. Data cleaning
values = ["1", "2", "3", "4", "5"]
numbers = [int(v) for v in values]  # Convert all to int

# 5. API responses (JSON strings to proper types)
price_str = "19.99"
price = float(price_str)  # Convert for calculations
```

---

## String Conversions

### To String (str)
**Convert any type to string**:

```python
# Numbers to string
x = str(123)        # "123"
y = str(45.67)      # "45.67"
z = str(3 + 4j)     # "(3+4j)"

# Boolean to string
a = str(True)       # "True"
b = str(False)      # "False"

# Collections to string
list_str = str([1, 2, 3])              # "[1, 2, 3]"
dict_str = str({"name": "Alice"})      # "{'name': 'Alice'}"
set_str = str({1, 2, 3})               # "{1, 2, 3}"

# None to string
none_str = str(None)  # "None"

# Use in concatenation
age = 25
message = "Age: " + str(age)  # "Age: 25"

# F-strings (automatic conversion)
message = f"Age: {age}"  # "Age: 25" (no str() needed!)

# Format method
message = "Age: {}".format(age)  # "Age: 25"

# Real-world example
def format_user_info(name, age, score):
    return f"{name} (age {age}) scored {score} points"

print(format_user_info("Alice", 25, 95.5))
# "Alice (age 25) scored 95.5 points"
```

### From String
**Convert string to other types**:

```python
# String to int
x = int("123")      # 123
y = int("-50")      # -50

# Error cases
# int("45.6")       # ValueError! Has decimal
# int("abc")        # ValueError! Not a number
# int("12.34")      # ValueError! Has decimal

# String to float
x = float("123")    # 123.0
y = float("45.67")  # 45.67
z = float("-3.14")  # -3.14
a = float("3.14e-2")  # 0.0314 (scientific notation)

# String to boolean
# Note: bool() doesn't parse "True"/"False" strings properly
x = bool("True")    # True (any non-empty string is True!)
y = bool("False")   # True (also True, because non-empty!)
z = bool("")        # False (only empty string is False)

# Proper string to boolean conversion
def str_to_bool(s):
    return s.lower() in ['true', '1', 'yes', 'y']

print(str_to_bool("True"))   # True
print(str_to_bool("False"))  # False
print(str_to_bool("yes"))    # True

# String to list (splits into characters)
chars = list("Hello")  # ['H', 'e', 'l', 'l', 'o']

# String to list (split by delimiter)
csv = "apple,banana,cherry"
items = csv.split(",")  # ['apple', 'banana', 'cherry']

# Real-world example: Parse user input
def parse_numbers(text):
    """Convert comma-separated numbers to list of integers."""
    parts = text.split(",")
    numbers = []
    for part in parts:
        try:
            numbers.append(int(part.strip()))
        except ValueError:
            pass  # Skip invalid numbers
    return numbers

print(parse_numbers("1, 2, 3, 4, 5"))  # [1, 2, 3, 4, 5]
print(parse_numbers("1, abc, 3"))      # [1, 3]
```

---

## Number Conversions

### Integer (int)
**Convert to integer**:

```python
# Float to int (truncates decimal, doesn't round!)
x = int(45.9)      # 45 (not 46!)
y = int(-3.7)      # -3 (not -4!)
z = int(0.999)     # 0

# To round before converting
import math
x = int(round(45.9))    # 46
y = int(math.ceil(45.1))   # 46 (always round up)
z = int(math.floor(45.9))  # 45 (always round down)

# String to int
x = int("123")     # 123
y = int("-456")    # -456

# String with base (binary, octal, hex)
binary = int("1010", 2)      # 10 (from binary)
octal = int("12", 8)         # 10 (from octal)
hex_num = int("FF", 16)      # 255 (from hexadecimal)
hex_alt = int("0xFF", 16)    # 255 (with 0x prefix)

# Boolean to int
x = int(True)      # 1
y = int(False)     # 0

# Complex to int (Error!)
# z = int(3 + 4j)  # TypeError! Can't convert complex directly

# Extract real part first
c = 3 + 4j
x = int(c.real)    # 3

# List/Dict to int (Error!)
# x = int([1, 2, 3])  # TypeError!

# Error handling
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("123"))    # 123
print(safe_int("abc"))    # 0 (default)
print(safe_int(45.7))     # 45
print(safe_int(None))     # 0 (default)

# Real-world: Parse user age
age_input = input("Enter age: ")
try:
    age = int(age_input)
    if age < 0:
        print("Age cannot be negative")
    else:
        print(f"Age: {age}")
except ValueError:
    print("Invalid age - must be a number")
```

### Float (float)
**Convert to float**:

```python
# Int to float
x = float(123)     # 123.0
y = float(-456)    # -456.0

# String to float
x = float("123")       # 123.0
y = float("45.67")     # 45.67
z = float("-3.14")     # -3.14
a = float("3.14e-2")   # 0.0314 (scientific notation)

# Special values
inf = float('inf')     # Infinity
neg_inf = float('-inf')  # Negative infinity
nan = float('nan')     # Not a Number

# Boolean to float
x = float(True)    # 1.0
y = float(False)   # 0.0

# Complex to float (Error!)
# z = float(3 + 4j)  # TypeError!

# Extract real or imaginary part
c = 3 + 4j
real = float(c.real)    # 3.0
imag = float(c.imag)    # 4.0

# Error handling
def safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

print(safe_float("3.14"))   # 3.14
print(safe_float("abc"))    # 0.0
print(safe_float(None))     # 0.0

# Real-world: Parse price
price_input = "$19.99"
# Remove $ and convert
price_clean = price_input.replace("$", "").replace(",", "")
try:
    price = float(price_clean)
    tax = price * 0.08
    total = price + tax
    print(f"Total: ${total:.2f}")
except ValueError:
    print("Invalid price format")
```

### Complex (complex)
**Convert to complex**:

```python
# Create from int/float
x = complex(5)         # (5+0j)
y = complex(3, 4)      # (3+4j)
z = complex(1.5, 2.5)  # (1.5+2.5j)

# String to complex
x = complex("3+4j")    # (3+4j)
y = complex("5-2j")    # (5-2j)

# Note: No spaces in string!
# complex("3 + 4j")    # ValueError!

# From other complex
c1 = 3 + 4j
c2 = complex(c1)       # (3+4j)

# Boolean to complex
x = complex(True)      # (1+0j)
y = complex(False)     # 0j

# Real-world use (rare in general programming)
# Electrical engineering
impedance = complex(50, 30)  # 50Ω resistance, 30Ω reactance
print(f"Impedance: {impedance}")
print(f"Magnitude: {abs(impedance):.2f}Ω")
```

---

## Collection Conversions

### List (list)
**Convert to list**:

```python
# String to list (characters)
x = list("Hello")           # ['H', 'e', 'l', 'l', 'o']

# Tuple to list
x = list((1, 2, 3))         # [1, 2, 3]

# Set to list
x = list({1, 2, 3})         # [1, 2, 3] (order may vary)

# Range to list
x = list(range(5))          # [0, 1, 2, 3, 4]

# Dictionary to list (keys only)
d = {"a": 1, "b": 2, "c": 3}
keys = list(d)              # ['a', 'b', 'c']
values = list(d.values())   # [1, 2, 3]
items = list(d.items())     # [('a', 1), ('b', 2), ('c', 3)]

# Generator to list
squares = (x**2 for x in range(5))
x = list(squares)           # [0, 1, 4, 9, 16]

# Number to list (Error!)
# x = list(123)             # TypeError!

# Split string into list
text = "apple,banana,cherry"
fruits = text.split(",")    # ['apple', 'banana', 'cherry']

# List comprehension (convert types)
strings = ["1", "2", "3", "4", "5"]
numbers = [int(s) for s in strings]  # [1, 2, 3, 4, 5]

# Real-world: Parse CSV line
csv_line = "John,30,Engineer,New York"
data = csv_line.split(",")
name, age, job, city = data
age = int(age)  # Convert age to int
print(f"{name}, {age}, {job}, {city}")
```

### Tuple (tuple)
**Convert to tuple**:

```python
# List to tuple
x = tuple([1, 2, 3])        # (1, 2, 3)

# String to tuple (characters)
x = tuple("Hello")          # ('H', 'e', 'l', 'l', 'o')

# Set to tuple
x = tuple({1, 2, 3})        # (1, 2, 3)

# Range to tuple
x = tuple(range(5))         # (0, 1, 2, 3, 4)

# Dictionary to tuple (keys)
d = {"a": 1, "b": 2}
x = tuple(d)                # ('a', 'b')

# Why convert to tuple?
# - Immutability (can't be changed)
# - Can be dictionary keys
# - Slightly faster than lists
# - Less memory usage

# Real-world: Function returning multiple values
def get_coordinates():
    return (10, 20, 30)  # Return tuple

x, y, z = get_coordinates()
print(f"X: {x}, Y: {y}, Z: {z}")

# Tuple as dictionary key
locations = {}
point1 = tuple([10, 20])
point2 = tuple([30, 40])
locations[point1] = "Home"
locations[point2] = "Work"
print(locations[(10, 20)])  # "Home"
```

### Set (set)
**Convert to set (removes duplicates)**:

```python
# List to set (removes duplicates)
x = set([1, 2, 2, 3, 3, 3])     # {1, 2, 3}

# String to set (unique characters)
x = set("Hello")                 # {'H', 'e', 'l', 'o'}

# Tuple to set
x = set((1, 2, 3))              # {1, 2, 3}

# Range to set
x = set(range(5))               # {0, 1, 2, 3, 4}

# Dictionary to set (keys)
d = {"a": 1, "b": 2}
x = set(d)                      # {'a', 'b'}

# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))     # [1, 2, 3, 4, 5] (order may change!)

# Keep order while removing duplicates
def unique_ordered(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(unique_ordered(numbers))  # [1, 2, 3, 4, 5] (order preserved!)

# Real-world: Find unique words
text = "hello world hello python world"
words = text.split()
unique_words = set(words)
print(f"Unique words: {unique_words}")
# {'hello', 'world', 'python'}

# Count unique values
emails = ["a@test.com", "b@test.com", "a@test.com", "c@test.com"]
unique_count = len(set(emails))
print(f"Unique emails: {unique_count}")  # 3
```

### Dictionary (dict)
**Convert to dictionary**:

```python
# List of tuples to dict
x = dict([("a", 1), ("b", 2), ("c", 3)])
print(x)  # {'a': 1, 'b': 2, 'c': 3}

# Two lists to dict (zip)
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
x = dict(zip(keys, values))
print(x)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Using dict() constructor
x = dict(name="Alice", age=25, city="NYC")
print(x)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# List of lists to dict
data = [["a", 1], ["b", 2], ["c", 3]]
x = dict(data)
print(x)  # {'a': 1, 'b': 2, 'c': 3}

# Dictionary comprehension
keys = ["a", "b", "c"]
x = {k: i for i, k in enumerate(keys)}
print(x)  # {'a': 0, 'b': 1, 'c': 2}

# Real-world: Parse query string
query = "name=Alice&age=25&city=NYC"
params = {}
for pair in query.split("&"):
    key, value = pair.split("=")
    params[key] = value
print(params)
# {'name': 'Alice', 'age': '25', 'city': 'NYC'}

# CSV to dict
csv_data = """name,age,city
Alice,25,NYC
Bob,30,LA"""

lines = csv_data.strip().split("\n")
headers = lines[0].split(",")
rows = []
for line in lines[1:]:
    values = line.split(",")
    row = dict(zip(headers, values))
    rows.append(row)

print(rows)
# [{'name': 'Alice', 'age': '25', 'city': 'NYC'},
#  {'name': 'Bob', 'age': '30', 'city': 'LA'}]
```

---

## Boolean Conversions

### To Boolean (bool)
**Convert to True or False**:

```python
# Falsy values (convert to False)
print(bool(False))      # False
print(bool(None))       # False
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(0j))         # False
print(bool(""))         # False
print(bool([]))         # False
print(bool(()))         # False
print(bool({}))         # False
print(bool(set()))      # False

# Truthy values (everything else = True)
print(bool(True))       # True
print(bool(1))          # True
print(bool(-1))         # True
print(bool(0.1))        # True
print(bool("Hello"))    # True
print(bool(" "))        # True (space is not empty!)
print(bool([1]))        # True
print(bool([0]))        # True (list with 0 is not empty!)
print(bool({"a": 0}))   # True

# String to boolean (careful!)
# Any non-empty string is True
print(bool("True"))     # True
print(bool("False"))    # True (also True!)
print(bool("0"))        # True (also True!)

# Proper string to boolean conversion
def parse_bool(s):
    s = str(s).lower().strip()
    if s in ['true', '1', 'yes', 'y', 'on']:
        return True
    elif s in ['false', '0', 'no', 'n', 'off']:
        return False
    else:
        raise ValueError(f"Cannot convert '{s}' to boolean")

print(parse_bool("True"))    # True
print(parse_bool("false"))   # False
print(parse_bool("1"))       # True
print(parse_bool("0"))       # False
print(parse_bool("yes"))     # True

# Use in conditionals
user_input = ""
if user_input:  # Checks bool(user_input)
    print("Has input")
else:
    print("No input")  # This prints

# Real-world: Validate required fields
def validate_form(data):
    required = ["name", "email", "message"]
    for field in required:
        if not data.get(field):  # bool() check
            return False, f"{field} is required"
    return True, "Valid"

form1 = {"name": "Alice", "email": "alice@test.com", "message": "Hi"}
form2 = {"name": "Bob", "email": "", "message": "Hello"}

print(validate_form(form1))  # (True, 'Valid')
print(validate_form(form2))  # (False, 'email is required')
```

---

## Implicit vs Explicit Casting

### Implicit (Automatic)
**Python automatically converts types**:

```python
# Int + Float = Float
x = 5       # int
y = 2.5     # float
z = x + y   # 7.5 (automatically converted to float)
print(type(z))  # <class 'float'>

# Int to Float in division
result = 10 / 2  # 5.0 (automatically float)
print(type(result))  # <class 'float'>

# Boolean to Int
result = True + 5  # 6 (True = 1)
print(result)

# In comparisons
print(5 == 5.0)  # True (values compared, not types)
print(1 == True)  # True
print(0 == False)  # True

# Real-world: Mixed type calculations
price = 19.99    # float
quantity = 3     # int
total = price * quantity  # 59.97 (float)
# No manual casting needed!
```

### Explicit (Manual)
**You specify the conversion**:

```python
# When you need specific type
x = 5.7
y = int(x)  # Explicitly convert to int (5)

# User input (always string)
age = int(input("Age: "))  # Must explicitly convert

# String concatenation
count = 42
message = "Count: " + str(count)  # Must convert to string

# Ensure type for function
def calculate_tax(price: float) -> float:
    return price * 0.08

# Explicitly convert to ensure correct type
user_input = "19.99"
tax = calculate_tax(float(user_input))

# Real-world: Data cleaning
data = ["1", "2", "3", "4", "5"]
# Explicitly convert all to int
numbers = [int(x) for x in data]

# API response (JSON strings to proper types)
json_data = {
    "user_id": "12345",
    "price": "19.99",
    "quantity": "3",
    "active": "true"
}

# Explicitly convert each field
user_id = int(json_data["user_id"])
price = float(json_data["price"])
quantity = int(json_data["quantity"])
active = json_data["active"].lower() == "true"
```

---

## Error Handling

### Try-Except for Conversions
```python
# Safe conversion function
def safe_cast(value, cast_type, default=None):
    try:
        return cast_type(value)
    except (ValueError, TypeError):
        return default

# Usage
print(safe_cast("123", int))       # 123
print(safe_cast("abc", int))       # None
print(safe_cast("abc", int, 0))    # 0 (custom default)
print(safe_cast("3.14", float))    # 3.14
print(safe_cast(None, str, ""))    # ""

# Multiple conversion attempts
def flexible_int(value):
    """Try to convert to int, trying multiple strategies."""
    # Already int
    if isinstance(value, int):
        return value
    
    # Try direct conversion
    try:
        return int(value)
    except (ValueError, TypeError):
        pass
    
    # Try float first (handles "3.14" strings)
    try:
        return int(float(value))
    except (ValueError, TypeError):
        pass
    
    # Give up
    raise ValueError(f"Cannot convert {value} to int")

print(flexible_int(42))          # 42
print(flexible_int("42"))        # 42
print(flexible_int("42.7"))      # 42
print(flexible_int(42.7))        # 42
# print(flexible_int("abc"))     # ValueError

# Validation before conversion
def validated_int(value, min_val=None, max_val=None):
    """Convert to int with validation."""
    try:
        num = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid integer: {value}")
    
    if min_val is not None and num < min_val:
        raise ValueError(f"Value {num} below minimum {min_val}")
    
    if max_val is not None and num > max_val:
        raise ValueError(f"Value {num} above maximum {max_val}")
    
    return num

# Usage
age = validated_int(input("Age (0-120): "), min_val=0, max_val=120)
```

---

## Real-World Examples

### Form Data Processing
```python
def process_registration(form_data):
    """Process user registration form."""
    try:
        # Extract and convert fields
        username = str(form_data.get("username", "")).strip()
        email = str(form_data.get("email", "")).strip()
        age = int(form_data.get("age", 0))
        subscribe = str(form_data.get("subscribe", "false")).lower() == "true"
        
        # Validate
        if not username:
            return False, "Username required"
        if not email:
            return False, "Email required"
        if age < 13:
            return False, "Must be 13 or older"
        
        # Create user dict
        user = {
            "username": username,
            "email": email,
            "age": age,
            "subscribe": subscribe
        }
        
        return True, user
    
    except ValueError as e:
        return False, f"Invalid data: {e}"

# Test
form = {
    "username": "alice123",
    "email": "alice@example.com",
    "age": "25",
    "subscribe": "true"
}

success, result = process_registration(form)
if success:
    print(f"Registered: {result}")
else:
    print(f"Error: {result}")
```

### CSV Data Import
```python
def import_csv_data(csv_text):
    """Import CSV and convert to proper types."""
    lines = csv_text.strip().split("\n")
    headers = lines[0].split(",")
    
    data = []
    for line in lines[1:]:
        values = line.split(",")
        row = {}
        
        for header, value in zip(headers, values):
            # Try to convert to appropriate type
            value = value.strip()
            
            # Try int
            try:
                row[header] = int(value)
                continue
            except ValueError:
                pass
            
            # Try float
            try:
                row[header] = float(value)
                continue
            except ValueError:
                pass
            
            # Try boolean
            if value.lower() in ["true", "false"]:
                row[header] = value.lower() == "true"
                continue
            
            # Keep as string
            row[header] = value
        
        data.append(row)
    
    return data

csv = """name,age,score,active
Alice,25,95.5,true
Bob,30,87.3,false
Charlie,22,92.1,true"""

result = import_csv_data(csv)
for row in result:
    print(row)
# {'name': 'Alice', 'age': 25, 'score': 95.5, 'active': True}
# {'name': 'Bob', 'age': 30, 'score': 87.3, 'active': False}
# {'name': 'Charlie', 'age': 22, 'score': 92.1, 'active': True}
```

---

## Quick Reference

### Conversion Functions
```python
str(x)      # To string
int(x)      # To integer
float(x)    # To float
complex(x)  # To complex
bool(x)     # To boolean
list(x)     # To list
tuple(x)    # To tuple
set(x)      # To set
dict(x)     # To dictionary
```

### Common Patterns
```python
# String to number
int("123")
float("3.14")

# Number to string
str(123)

# Remove duplicates
list(set(items))

# Safe conversion
try:
    x = int(value)
except ValueError:
    x = default
```

### Falsy Values
```python
False, None, 0, 0.0, "", [], {}, ()
# Everything else is truthy
```

