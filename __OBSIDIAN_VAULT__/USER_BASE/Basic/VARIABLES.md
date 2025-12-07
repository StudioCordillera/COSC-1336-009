# Domain: Variables

## Overview
Variables are containers for storing data values. In Python, you don't need to declare the type - Python figures it out automatically based on the value you assign. Variables are created the moment you assign a value to them.

---

## Core Concepts

### Creating Variables
**What it is**: Assigning a value to a name using the `=` operator.

**Syntax**: `variable_name = value`

**Examples**:
```python
# Simple assignment
x = 5
name = "Alice"
is_active = True

# Python figures out the type automatically
number = 10        # int
price = 19.99      # float
greeting = "Hi"    # str
items = [1, 2, 3]  # list

# Variables can change type
x = 5          # x is int
x = "Hello"    # now x is str (perfectly fine!)

# No need for type declarations
# Unlike Java: int x = 5;
# Python: x = 5  (that's it!)
```

**Rules**:
```python
# Valid variable names
my_variable = 1
_private = 2
myVar = 3
CONSTANT = 4
var123 = 5

# Invalid variable names (will cause errors)
# 2var = 1        # Can't start with number
# my-var = 1      # No hyphens
# my var = 1      # No spaces
# class = 1       # Can't use reserved keywords
```

---

### Naming Rules and Conventions

**Required Rules** (will error if violated):
```python
# 1. Must start with letter (a-z, A-Z) or underscore (_)
name = "Valid"
_name = "Valid"
# 1name = "Invalid"  # Error!

# 2. Can only contain letters, numbers, and underscores
my_var_123 = "Valid"
# my-var = "Invalid"   # Error!
# my var = "Invalid"   # Error!
# my@var = "Invalid"   # Error!

# 3. Case-sensitive (Age and age are different)
Age = 25
age = 30
print(Age)  # 25
print(age)  # 30

# 4. Cannot be Python keywords
# if = 5      # Error!
# for = 10    # Error!
# class = 20  # Error!

# Check all keywords
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', ...]
```

**Style Conventions** (best practices):
```python
# 1. snake_case for regular variables (recommended)
first_name = "John"
total_price = 99.99
is_valid = True

# 2. UPPER_CASE for constants
MAX_SIZE = 100
PI = 3.14159
API_KEY = "abc123"

# 3. _leading_underscore for "private" variables
_internal_value = 42
_helper_function = lambda x: x * 2

# 4. Descriptive names (readable > short)
# Good
user_age = 25
total_price = 19.99
is_logged_in = True

# Bad (too short/unclear)
a = 25
tp = 19.99
flag = True

# 5. Avoid single letters (except in loops or math)
# Good for loops
for i in range(10):
    print(i)

# Good for coordinates
x = 10
y = 20

# Bad for regular variables
n = "John"  # What is n?
```

---

### Variable Types

**Python determines type automatically**:
```python
# Check type with type()
x = 5
print(type(x))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>

price = 19.99
print(type(price))  # <class 'float'>

# Common types
integer = 42                    # int
floating = 3.14                 # float
string = "Hello"                # str
boolean = True                  # bool
list_var = [1, 2, 3]           # list
tuple_var = (1, 2, 3)          # tuple
dict_var = {"key": "value"}    # dict
set_var = {1, 2, 3}            # set
none_var = None                # NoneType
```

**Type Checking**:
```python
# Check if variable is specific type
age = 25

# Method 1: type()
if type(age) == int:
    print("age is an integer")

# Method 2: isinstance() (preferred)
if isinstance(age, int):
    print("age is an integer")

# Check multiple types
value = "123"
if isinstance(value, (int, float)):
    print("Number")
elif isinstance(value, str):
    print("String")  # This prints

# Real-world example
def process_input(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return data * 2
    elif isinstance(data, list):
        return len(data)
    else:
        return None

print(process_input("hello"))    # "HELLO"
print(process_input(5))          # 10
print(process_input([1, 2, 3]))  # 3
```

---

### Multiple Assignment

**Assign to multiple variables at once**:
```python
# 1. Same value to multiple variables
x = y = z = 100
print(x, y, z)  # 100 100 100

# 2. Different values to multiple variables (unpacking)
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3

# 3. Unpack from list/tuple
numbers = [10, 20, 30]
x, y, z = numbers
print(x)  # 10

# 4. Swap variables (no temp needed!)
x = 5
y = 10
x, y = y, x  # Swap
print(x, y)  # 10 5

# 5. Unpack with * (rest)
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# 6. Ignore values with _
name, _, age = ["Alice", "Smith", 25]
print(name)  # "Alice"
print(age)   # 25
# (ignored "Smith")
```

**Real-world Examples**:
```python
# Parse coordinates
point = (100, 200)
x, y = point
print(f"X: {x}, Y: {y}")

# Parse CSV line
csv_line = "John,30,Engineer"
name, age, job = csv_line.split(",")
print(f"{name} is a {age}-year-old {job}")

# Function returning multiple values
def get_user():
    return "Alice", 25, "alice@example.com"

name, age, email = get_user()
print(f"User: {name}, {age}, {email}")

# Dictionary unpacking
data = {"name": "Bob", "age": 30}
name, age = data.values()
print(name, age)  # Bob 30

# Loop with unpacking
users = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

for name, age in users:
    print(f"{name} is {age} years old")
```

---

### Variable Scope

**Where variables can be accessed**:

```python
# 1. Local Scope (inside function)
def my_function():
    local_var = "I'm local"
    print(local_var)  # Works

my_function()
# print(local_var)  # Error! Not accessible outside

# 2. Global Scope (outside all functions)
global_var = "I'm global"

def my_function():
    print(global_var)  # Works - can read global

my_function()
print(global_var)  # Works

# 3. Modifying global from inside function
counter = 0

def increment():
    global counter  # Must declare global to modify
    counter += 1

increment()
print(counter)  # 1

# Without global keyword
count = 0

def bad_increment():
    count = count + 1  # Error! Can't modify without 'global'

# 4. Nested function scope
def outer():
    outer_var = "Outer"
    
    def inner():
        inner_var = "Inner"
        print(outer_var)  # Can access outer
        print(inner_var)  # Can access own
    
    inner()
    # print(inner_var)  # Error! Can't access inner

outer()

# 5. nonlocal keyword (for nested functions)
def outer():
    count = 0
    
    def inner():
        nonlocal count  # Modify outer function's variable
        count += 1
    
    inner()
    print(count)  # 1

outer()
```

**Best Practices**:
```python
# Minimize global variables
# BAD
score = 0

def update_score():
    global score
    score += 10

# GOOD - pass and return
def update_score(score):
    return score + 10

score = 0
score = update_score(score)

# Use function parameters instead
# BAD
user_name = "Alice"

def greet():
    global user_name
    print(f"Hello, {user_name}")

# GOOD
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
```

---

### Variable Assignment Patterns

**Common patterns for assigning variables**:

```python
# 1. Conditional assignment
age = 25
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"

# 2. Default values
user_input = None
name = user_input or "Guest"  # Use "Guest" if user_input is falsy
print(name)  # "Guest"

# With None specifically
result = None
value = result if result is not None else 0
print(value)  # 0

# 3. Walrus operator := (Python 3.8+)
# Assign AND use in same expression
if (length := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is long: {length} items")
# List is long: 5 items

# 4. Multiple assignment from function
def get_stats():
    return 100, 75, 92  # min, max, avg

min_val, max_val, avg_val = get_stats()

# 5. Dictionary unpacking for assignment
config = {"host": "localhost", "port": 8080}
host = config.get("host")
port = config.get("port")

# Or use unpacking
host, port = config["host"], config["port"]

# 6. Increment/Decrement
count = 10
count += 5   # count = count + 5 (now 15)
count -= 3   # count = count - 3 (now 12)
count *= 2   # count = count * 2 (now 24)
count //= 4  # count = count // 4 (now 6)

# 7. Chained comparison assignment
x = 15
result = 0 < x < 20  # True (x is between 0 and 20)
```

---

### Variable Deletion

**Removing variables from memory**:

```python
# Delete variable with del
x = 5
print(x)  # 5

del x
# print(x)  # Error! Variable doesn't exist anymore

# Delete multiple variables
a, b, c = 1, 2, 3
del a, b, c

# Delete list items
numbers = [1, 2, 3, 4, 5]
del numbers[0]  # Remove first item
print(numbers)  # [2, 3, 4, 5]

del numbers[1:3]  # Remove slice
print(numbers)  # [2, 5]

# Delete dictionary items
data = {"a": 1, "b": 2, "c": 3}
del data["b"]
print(data)  # {"a": 1, "c": 3}

# When to use del
# 1. Free memory for large objects
large_data = [i for i in range(1000000)]
# ... use large_data ...
del large_data  # Free memory immediately

# 2. Remove unwanted variables
temp = calculate_something()
result = process(temp)
del temp  # Don't need temp anymore
```

---

### String Variables (Special Operations)

**String-specific variable operations**:

```python
# 1. Multi-line strings
message = """
This is a
multi-line
string
"""

# 2. String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # "John Doe"

# 3. f-strings (formatted string literals)
name = "Alice"
age = 25
info = f"{name} is {age} years old"
print(info)  # "Alice is 25 years old"

# With expressions
price = 19.99
tax = 0.08
total = f"Total: ${price * (1 + tax):.2f}"
print(total)  # "Total: $21.59"

# 4. Raw strings (for paths, regex)
path = r"C:\Users\Documents\file.txt"
print(path)  # C:\Users\Documents\file.txt

# 5. String multiplication
separator = "-" * 50
print(separator)  # --------------------------------------------------

# 6. String methods
text = "  hello world  "
cleaned = text.strip().title()
print(cleaned)  # "Hello World"
```

---

### Numeric Variables (Special Operations)

**Number-specific operations**:

```python
# 1. Integer operations
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7 (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division)
print(a // b)  # 3 (floor division)
print(a % b)   # 1 (modulo/remainder)
print(a ** b)  # 1000 (exponent)

# 2. Float operations
price = 19.99
quantity = 3
total = price * quantity
print(f"${total:.2f}")  # $59.97

# 3. Type mixing (int + float = float)
x = 5      # int
y = 2.5    # float
z = x + y  # 7.5 (float)
print(type(z))  # <class 'float'>

# 4. Division always returns float
result = 10 / 2
print(result)       # 5.0
print(type(result)) # <class 'float'>

# 5. Complex numbers
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0

# 6. Number formatting
num = 1234567.89
print(f"{num:,.2f}")  # 1,234,567.89
print(f"{num:.2e}")   # 1.23e+06
```

---

### Collection Variables (Lists, Tuples, etc.)

**Working with collection variables**:

```python
# 1. Lists (mutable)
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10  # Can modify
numbers.append(6)  # Can add
print(numbers)  # [10, 2, 3, 4, 5, 6]

# 2. Tuples (immutable)
coordinates = (10, 20)
# coordinates[0] = 15  # Error! Can't modify

# 3. Sets (unique values)
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print(unique_numbers)  # {1, 2, 3, 4, 5}

# 4. Dictionaries (key-value pairs)
user = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}
print(user["name"])  # "Alice"
user["age"] = 26  # Can modify

# 5. List comprehensions
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 6. Nested collections
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 6
```

---

### Boolean Variables

**Working with True/False values**:

```python
# 1. Boolean values
is_active = True
is_admin = False

# 2. Boolean operations
has_permission = is_active and is_admin
can_view = is_active or is_admin

# 3. Comparison results are booleans
age = 25
is_adult = age >= 18
print(is_adult)  # True

# 4. Truthy and Falsy values
# Falsy: False, None, 0, 0.0, "", [], {}, ()
# Everything else is Truthy

empty_list = []
if not empty_list:
    print("List is empty")  # This prints

# 5. Boolean conversion
value = "Hello"
is_empty = not bool(value)
print(is_empty)  # False

# 6. Short-circuit evaluation
def expensive_check():
    print("Running expensive check")
    return True

active = False
result = active and expensive_check()
# expensive_check() never runs because active is False
```

---

### None Type

**The special None value**:

```python
# 1. None represents absence of value
result = None
user_input = None

# 2. Function returns None by default
def no_return():
    print("Hello")

value = no_return()
print(value)  # None

# 3. Checking for None
value = None

# Use 'is' for None (not ==)
if value is None:
    print("Value is None")  # This prints

if value is not None:
    print("Value exists")

# 4. None in dictionaries
user = {"name": "Alice", "age": None}
if user["age"] is None:
    print("Age not provided")

# 5. Default None parameters
def greet(name=None):
    if name is None:
        name = "Guest"
    print(f"Hello, {name}")

greet()        # "Hello, Guest"
greet("Alice") # "Hello, Alice"

# 6. None vs empty
empty_list = []
none_list = None

print(empty_list == None)  # False
print(none_list is None)   # True
```

---

### Constants

**Values that shouldn't change** (by convention):

```python
# 1. Use UPPER_CASE for constants
MAX_CONNECTIONS = 100
API_URL = "https://api.example.com"
TAX_RATE = 0.08
PI = 3.14159

# 2. Python doesn't enforce constants
# This is just a convention
MAX_SIZE = 100
MAX_SIZE = 200  # Legal, but shouldn't do this

# 3. Group related constants
# colors.py
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# config.py
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_NAME = "myapp"

# 4. Use in calculations
SALES_TAX = 0.08

def calculate_total(subtotal):
    return subtotal * (1 + SALES_TAX)

# 5. Enum for related constants (Python 3.4+)
from enum import Enum

class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

order_status = Status.PENDING
print(order_status.value)  # 1
```

---

## Common Patterns and Best Practices

### 1. Naming Patterns
```python
# Boolean variables: use is_, has_, can_, should_
is_valid = True
has_permission = False
can_edit = True
should_update = False

# Counters and indexes
count = 0
index = 0
total = 0

# Collections (plural names)
users = ["Alice", "Bob"]
numbers = [1, 2, 3]
items = ["apple", "banana"]

# Single items (singular names)
user = "Alice"
number = 42
item = "apple"
```

### 2. Avoiding Common Mistakes
```python
# Mistake 1: Mutable default arguments
# BAD
def add_item(item, items=[]):
    items.append(item)
    return items

# GOOD
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Mistake 2: Reusing variable names
# BAD
list = [1, 2, 3]  # Shadows built-in 'list'

# GOOD
numbers = [1, 2, 3]

# Mistake 3: Not using meaningful names
# BAD
x = 123  # What is x?
temp = "John"  # temp for what?

# GOOD
user_id = 123
first_name = "John"
```

### 3. Variable Organization
```python
# Group related variables
# User information
user_name = "Alice"
user_age = 25
user_email = "alice@example.com"

# Or use dictionary
user = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

# Or use a class
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

user = User("Alice", 25, "alice@example.com")
```

---

## Quick Reference

### Variable Creation
```python
# Basic
x = 5
name = "Alice"

# Multiple
x = y = z = 0
a, b, c = 1, 2, 3

# Type check
type(x)
isinstance(x, int)
```

### Naming Rules
```python
# Valid
my_var, _private, myVar, VAR123

# Invalid
2var, my-var, my var, class
```

### Scope
```python
# Local: inside function
# Global: outside functions
# Use 'global' to modify global from function
# Use 'nonlocal' for nested functions
```

### Assignment Operators
```python
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
x //= 2  # x = x // 2
x %= 3   # x = x % 3
x **= 2  # x = x ** 2
```

### Common Patterns
```python
# Swap
x, y = y, x

# Conditional
status = "Yes" if condition else "No"

# Default
value = user_input or "default"

# None check
if value is None:
    pass
```

