# DICTIONARY_OPERATIONS

## Core Definition
**Dictionaries** are mutable key-value pair collections with O(1) lookup. Keys must be immutable (strings, numbers, tuples); values can be any type.

**Tags**: #dictionary #key-value #dict-methods #nested #iteration #enumerate

---

## COMPLETE METHODS QUICK REFERENCE

### DICTIONARY METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# ACCESS METHODS
# ═══════════════════════════════════════════════════════════════════════════
dict[key]                    # Dict depth 1 | Access value by key | Returns value or KeyError
dict.get(key)                # Dict depth 1 | Safe access by key | Returns value or None
dict.get(key, default)       # Dict depth 1 | Safe access with fallback | Returns value or default
dict.keys()                  # Dict depth 1 | Get all keys | Returns dict_keys view object
dict.values()                # Dict depth 1 | Get all values | Returns dict_values view object
dict.items()                 # Dict depth 1 | Get key-value pairs | Returns dict_items of (key, val) tuples
dict.setdefault(key, default)# Dict depth 1 | Get or set default | Returns value or sets/returns default

# ═══════════════════════════════════════════════════════════════════════════
# MODIFICATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
dict[key] = value            # Dict depth 1 | Add/update key | Modifies dict, returns None
dict.update(other_dict)      # Dict depth 1 | Merge dictionaries | Modifies dict, returns None
dict.update(key=value)       # Dict depth 1 | Update with kwargs | Modifies dict, returns None
dict.update([(k,v), ...])    # Dict depth 1 | Update from list of tuples | Modifies dict, returns None
dict.pop(key)                # Dict depth 1 | Remove key return value | Returns value or KeyError
dict.pop(key, default)       # Dict depth 1 | Remove key with fallback | Returns value or default
dict.popitem()               # Dict depth 1 | Remove last item (LIFO) | Returns (key, value) tuple
del dict[key]                # Dict depth 1 | Delete specific key | Deletes key or KeyError
dict.clear()                 # Dict depth 1 | Remove all items | Empties dict, returns None

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY METHODS
# ═══════════════════════════════════════════════════════════════════════════
len(dict)                    # Dict any depth | Count key-value pairs | Returns int count
key in dict                  # Dict depth 1 | Check key membership | Returns True/False
key not in dict              # Dict depth 1 | Check key absence | Returns True/False
dict.copy()                  # Dict any depth | Shallow copy dict | Returns new dict (same refs)
dict.fromkeys(keys, value)   # Class method | Create dict from keys | Returns new dict with default vals
type(dict)                   # Any object | Check object type | Returns <class 'dict'>
bool(dict)                   # Dict any depth | Check if empty | Returns False if empty, else True
str(dict)                    # Dict any depth | Convert to string | Returns string representation
sorted(dict)                 # Dict depth 1 | Sort keys | Returns sorted list of keys
sorted(dict.items())         # Dict depth 1 | Sort by keys | Returns sorted list of (key, val) tuples
sorted(dict.values())        # Dict depth 1 | Sort values | Returns sorted list of values
max(dict)                    # Dict depth 1 | Find max key | Returns key with max value
min(dict)                    # Dict depth 1 | Find min key | Returns key with min value
sum(dict.values())           # Dict depth 1 | Sum numeric values | Returns sum of all values
all(dict.values())           # Dict depth 1 | Check all truthy | Returns True if all values truthy
any(dict.values())           # Dict depth 1 | Check any truthy | Returns True if any value truthy
list(dict)                   # Dict depth 1 | Convert keys to list | Returns list of keys
list(dict.keys())            # Dict depth 1 | Convert keys to list | Returns list of keys
list(dict.values())          # Dict depth 1 | Convert values to list | Returns list of values
list(dict.items())           # Dict depth 1 | Convert items to list | Returns list of (key, val) tuples
tuple(dict)                  # Dict depth 1 | Convert keys to tuple | Returns tuple of keys
set(dict)                    # Dict depth 1 | Convert keys to set | Returns set of keys

# ═══════════════════════════════════════════════════════════════════════════
# ITERATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
for key in dict:             # Dict depth 1 | Iterate keys | Yields each key
for key in dict.keys():      # Dict depth 1 | Iterate keys explicitly | Yields each key
for value in dict.values():  # Dict depth 1 | Iterate values | Yields each value
for k, v in dict.items():    # Dict depth 1 | Iterate pairs | Yields (key, value) tuples
enumerate(dict)              # Dict depth 1 | Index + iterate keys | Yields (index, key) tuples
enumerate(dict.keys())       # Dict depth 1 | Index + iterate keys | Yields (index, key) tuples
enumerate(dict.values())     # Dict depth 1 | Index + iterate values | Yields (index, value) tuples
enumerate(dict.items())      # Dict depth 1 | Index + iterate pairs | Yields (index, (key, val)) tuples
enumerate(dict, start=1)     # Dict depth 1 | Index from start + keys | Yields (index, key) from start
zip(dict1, dict2)            # Multiple dicts | Pair keys together | Yields tuples of paired keys
zip(dict.keys(), dict.values()) # Dict depth 1 | Pair keys with values | Yields (key, value) tuples
reversed(dict)               # Dict depth 1 | Reverse iteration (3.8+) | Yields keys in reverse order
iter(dict)                   # Dict depth 1 | Create iterator | Returns iterator over keys
next(iter(dict))             # Dict iterator | Get next item | Returns next key from iterator

# ═══════════════════════════════════════════════════════════════════════════
# COMPREHENSION PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
{k: v for k, v in items}     # Iterable pairs | Create dict | Returns new dict from pairs
{k: expr for k in iterable}  # Iterable | Create with expression | Returns new dict with computed values
{k: v for k, v in d.items() if cond} # Dict + condition | Filter dict | Returns new filtered dict
{v: k for k, v in d.items()} # Dict depth 1 | Swap keys/values | Returns new inverted dict
{k: d[k] for k in keys}      # Dict + key list | Extract subset | Returns new dict with selected keys

# ═══════════════════════════════════════════════════════════════════════════
# DICTIONARY CREATION
# ═══════════════════════════════════════════════════════════════════════════
{}                           # Literal | Create empty | Returns empty dict
{'a': 1, 'b': 2}            # Literal | Create with items | Returns dict with specified pairs
dict()                       # Constructor | Create empty | Returns empty dict
dict(a=1, b=2)              # Constructor + kwargs | Create from keywords | Returns dict with keyword pairs
dict([('a', 1), ('b', 2)])  # Constructor + list | Create from pairs | Returns dict from list of tuples
dict(zip(keys, vals))        # Constructor + zip | Create from lists | Returns dict pairing keys with values
dict.fromkeys(['a','b'], 0)  # Class method | Create with default | Returns dict with keys all set to default
{**dict1, **dict2}           # Unpacking | Merge dicts (3.5+) | Returns new merged dict
dict1 | dict2                # Union operator (3.9+) | Merge dicts | Returns new merged dict

# ═══════════════════════════════════════════════════════════════════════════
# NESTED DICTIONARY ACCESS
# ═══════════════════════════════════════════════════════════════════════════
dict[key1][key2]             # Dict depth 2 | Access nested value | Returns nested value or KeyError
dict.get(k1, {}).get(k2)     # Dict depth 2 | Safe nested access | Returns nested value or None
dict[key1][key2][key3]       # Dict depth 3 | Access deep nested | Returns deep value or KeyError
dict.get(k1,{}).get(k2,{}).get(k3) # Dict depth 3 | Safe deep access | Returns deep value or None

# ═══════════════════════════════════════════════════════════════════════════
# COMPARISON & EQUALITY
# ═══════════════════════════════════════════════════════════════════════════
dict1 == dict2               # Two dicts | Check equality | Returns True if same key-value pairs
dict1 != dict2               # Two dicts | Check inequality | Returns True if different
dict1.keys() == dict2.keys() # Two dicts | Compare keys only | Returns True if same keys
dict1.items() <= dict2.items() # Two dicts | Check subset | Returns True if dict1 is subset
```

### COMMON OPERATION EXAMPLES

```python
# Example dictionary
student = {'name': 'John', 'id': 'S001', 'gpa': 3.8}

# Access
student['name']              # → 'John'
student.get('age', 0)        # → 0 (key doesn't exist)
list(student.keys())         # → ['name', 'id', 'gpa']

# Modify
student['age'] = 20          # Adds new key 'age'
student.update({'major': 'CS'}) # Adds 'major'
student.pop('age')           # Removes 'age', returns 20

# Iterate
for k, v in student.items(): # Loop through pairs
    print(f"{k}: {v}")

for i, k in enumerate(student): # With index
    print(f"{i}: {k}")

# Check
'name' in student            # → True
len(student)                 # → 3
```

---

## ACCESSING KEYS, VALUES, AND KEY NAMES

### Method 1: Direct Key Access
```python
student = {'name': 'John', 'id': 'S001', 'gpa': 3.8}

# Access value by key (raises KeyError if missing)
name = student['name']        # 'John'

# Get key name from iteration
for key in student:
    print(key)                # Prints: name, id, gpa
```

### Method 2: Using .get() - Safe Access
```python
# Returns None if key doesn't exist (no error)
age = student.get('age')      # None

# Returns default value if key doesn't exist
age = student.get('age', 0)   # 0
email = student.get('email', 'No email')  # 'No email'
```

### Method 3: Getting All Keys
```python
# .keys() returns dict_keys view object
keys = student.keys()         # dict_keys(['name', 'id', 'gpa'])

# Convert to list for indexing
keys_list = list(student.keys())  # ['name', 'id', 'gpa']
first_key = keys_list[0]      # 'name'

# Iterate through keys
for key in student.keys():
    print(f"Key: {key}")
```

### Method 4: Getting All Values
```python
# .values() returns dict_values view object
values = student.values()     # dict_values(['John', 'S001', 3.8])

# Convert to list
values_list = list(student.values())  # ['John', 'S001', 3.8]

# Iterate through values (no keys available here)
for value in student.values():
    print(f"Value: {value}")
```

### Method 5: Getting Key-Value Pairs with .items()
```python
# .items() returns dict_items of (key, value) tuples
items = student.items()       
# dict_items([('name', 'John'), ('id', 'S001'), ('gpa', 3.8)])

# Unpack tuples in loop
for key, value in student.items():
    print(f"{key}: {value}")
    # name: John
    # id: S001
    # gpa: 3.8

# Access tuple directly
for item in student.items():
    key = item[0]
    value = item[1]
    print(f"{key} = {value}")
```

### Method 6: Check Key Existence
```python
# Best practice: check before accessing
if 'name' in student:
    print(student['name'])    # John

# Check for missing key
if 'phone' not in student:
    print("No phone number")  # Prints this

# Use with get() for default
phone = student['phone'] if 'phone' in student else 'Not provided'
```

---

## ENUMERATE WITH DICTIONARIES

### enumerate() on Keys (Default Iteration)
```python
student = {'name': 'John', 'id': 'S001', 'gpa': 3.8}

# enumerate gives (index, key)
for index, key in enumerate(student):
    print(f"{index}: {key} = {student[key]}")
# 0: name = John
# 1: id = S001
# 2: gpa = 3.8

# Start index at 1
for index, key in enumerate(student, start=1):
    print(f"{index}. {key}")
# 1. name
# 2. id
# 3. gpa
```

### enumerate() on .keys()
```python
# Explicitly enumerate keys
for index, key in enumerate(student.keys()):
    print(f"[{index}] {key}: {student[key]}")
# [0] name: John
# [1] id: S001
# [2] gpa: 3.8
```

### enumerate() on .values()
```python
# Enumerate values only (no key information)
for index, value in enumerate(student.values()):
    print(f"Value #{index}: {value}")
# Value #0: John
# Value #1: S001
# Value #2: 3.8
```

### enumerate() on .items()
```python
# Enumerate (key, value) tuples
for index, (key, value) in enumerate(student.items()):
    print(f"{index + 1}. {key} = {value}")
# 1. name = John
# 2. id = S001
# 3. gpa = 3.8

# Access as tuple instead of unpacking
for index, item in enumerate(student.items()):
    print(f"{index}: key={item[0]}, value={item[1]}")
```

### enumerate() on Nested Dictionaries
```python
students = {
    'S001': {'name': 'John', 'gpa': 3.8},
    'S002': {'name': 'Alice', 'gpa': 3.9}
}

# Enumerate outer dictionary
for index, (student_id, info) in enumerate(students.items(), 1):
    print(f"\n{index}. Student ID: {student_id}")
    # Enumerate inner dictionary
    for i, (key, value) in enumerate(info.items()):
        print(f"   {i + 1}. {key}: {value}")

# Output:
# 1. Student ID: S001
#    1. name: John
#    2. gpa: 3.8
# 2. Student ID: S002
#    1. name: Alice
#    2. gpa: 3.9
```

---

## LOOPING PATTERNS

### Pattern 1: Loop Through Keys (Default)
```python
student = {'name': 'John', 'id': 'S001', 'gpa': 3.8}

# Default iteration - keys only
for key in student:
    print(f"{key}: {student[key]}")
```

### Pattern 2: Loop Through Values Only
```python
# When you don't need keys
for value in student.values():
    print(value)
# John
# S001
# 3.8
```

### Pattern 3: Loop Through Key-Value Pairs
```python
# Most common pattern - access both
for key, value in student.items():
    print(f"{key} = {value}")
```

### Pattern 4: Loop with Index
```python
# When you need position/counter
for index, key in enumerate(student):
    print(f"{index}: {key} = {student[key]}")
```

### Pattern 5: Conditional Looping
```python
# Filter while iterating
for key, value in student.items():
    if isinstance(value, (int, float)):
        print(f"{key}: {value}")
# gpa: 3.8
```

### Pattern 6: Loop and Modify (Safe Pattern)
```python
# WRONG: Don't modify dict while iterating
# for key in student:
#     del student[key]  # RuntimeError!

# CORRECT: Create list of keys first
for key in list(student.keys()):
    if key == 'gpa':
        del student[key]

# BETTER: Use comprehension to create new dict
student = {k: v for k, v in student.items() if k != 'gpa'}
```

---

## NESTED DICTIONARIES IN DETAIL

### Level 1: Simple Nested Dictionary
```python
students = {
    'S001': {
        'name': 'John',
        'age': 20,
        'gpa': 3.8
    },
    'S002': {
        'name': 'Alice',
        'age': 22,
        'gpa': 3.9
    }
}

# Access nested values
john_name = students['S001']['name']        # 'John'
alice_gpa = students['S002']['gpa']         # 3.9

# Modify nested values
students['S001']['gpa'] = 3.9
students['S002']['age'] = 23

# Add new nested key
students['S001']['major'] = 'CS'
```

### Level 2: Iterating Nested Dictionaries
```python
# Loop through outer dictionary
for student_id, student_info in students.items():
    print(f"\nStudent ID: {student_id}")
    
    # Loop through inner dictionary
    for key, value in student_info.items():
        print(f"  {key}: {value}")

# Output:
# Student ID: S001
#   name: John
#   age: 20
#   gpa: 3.8
```

### Level 3: Nested Dictionaries with Lists
```python
course = {
    'COSC1336': {
        'title': 'Programming I',
        'credits': 3,
        'students': ['S001', 'S002', 'S003'],
        'grades': {
            'S001': 92,
            'S002': 88,
            'S003': 95
        }
    }
}

# Access list within nested dict
students_in_course = course['COSC1336']['students']  # ['S001', 'S002', 'S003']

# Access dict within nested dict
s001_grade = course['COSC1336']['grades']['S001']    # 92

# Loop through list in nested dict
for student_id in course['COSC1336']['students']:
    grade = course['COSC1336']['grades'][student_id]
    print(f"{student_id}: {grade}")
```

### Level 4: Triple-Nested Dictionary
```python
database = {
    'colleges': {
        'CS': {
            'courses': {
                'COSC1336': {
                    'title': 'Programming I',
                    'students': ['S001', 'S002']
                }
            }
        }
    }
}

# Access deeply nested value
course_title = database['colleges']['CS']['courses']['COSC1336']['title']
# 'Programming I'

# Safer access with .get()
title = (database.get('colleges', {})
                 .get('CS', {})
                 .get('courses', {})
                 .get('COSC1336', {})
                 .get('title', 'Not found'))
```

### Level 5: Nested Dictionary with Mixed Types
```python
employee = {
    'E001': {
        'name': 'John Smith',
        'department': 'Engineering',
        'salary': 75000,
        'skills': ['Python', 'Java', 'SQL'],
        'projects': {
            'P01': {'name': 'Web App', 'hours': 120},
            'P02': {'name': 'Database', 'hours': 80}
        },
        'active': True
    }
}

# Access list in nested dict
skills = employee['E001']['skills']          # ['Python', 'Java', 'SQL']
first_skill = employee['E001']['skills'][0]  # 'Python'

# Loop through nested dict of dicts
for proj_id, proj_info in employee['E001']['projects'].items():
    print(f"{proj_id}: {proj_info['name']} - {proj_info['hours']} hours")
# P01: Web App - 120 hours
# P02: Database - 80 hours

# Add to nested list
employee['E001']['skills'].append('JavaScript')

# Add to nested dict
employee['E001']['projects']['P03'] = {'name': 'API', 'hours': 60}
```

### Nested Dict Iteration Patterns
```python
# Pattern 1: Enumerate nested with counting
for i, (outer_key, outer_val) in enumerate(students.items(), 1):
    print(f"\n{i}. {outer_key}")
    for j, (inner_key, inner_val) in enumerate(outer_val.items(), 1):
        print(f"   {i}.{j} {inner_key}: {inner_val}")

# Pattern 2: Build nested dict from flat data
raw_data = [
    ('S001', 'name', 'John'),
    ('S001', 'gpa', 3.8),
    ('S002', 'name', 'Alice'),
    ('S002', 'gpa', 3.9)
]

nested = {}
for student_id, key, value in raw_data:
    if student_id not in nested:
        nested[student_id] = {}
    nested[student_id][key] = value

# Result: {'S001': {'name': 'John', 'gpa': 3.8}, ...}

# Pattern 3: Flatten nested dict
def flatten_dict(nested_dict, parent_key='', sep='_'):
    items = []
    for k, v in nested_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flat = flatten_dict({'a': {'b': 1, 'c': 2}})
# {'a_b': 1, 'a_c': 2}
```

---

## DICTIONARY COMPREHENSIONS

### Basic Comprehension
```python
# Create dict from range
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create dict from lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}
```

### Conditional Comprehension
```python
# Filter with condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transform existing dict
prices = {'apple': 2.5, 'banana': 1.5}
discounted = {k: v * 0.9 for k, v in prices.items()}
# {'apple': 2.25, 'banana': 1.35}

# Filter existing dict
passing = {k: v for k, v in grades.items() if v >= 70}
```

### Advanced Comprehensions
```python
# Swap keys and values
original = {'a': 1, 'b': 2}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b'}

# Nested comprehension
matrix = {i: {j: i*j for j in range(3)} for i in range(3)}
# {0: {0: 0, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, ...}
```

---

## COMMON PATTERNS FOR PROJECTS

### Pattern 1: Student Lookup System (Project 8 Style)
```python
def readData(filename):
    """Read student data from file into dictionary"""
    students = {}
    with open(filename, 'r') as file:
        for line in file:
            student_id, name = line.strip().split(',')
            students[student_id] = name
    return students

def search_student(students, student_id):
    """Search for student with safe access"""
    if student_id in students:
        return True, students[student_id]
    else:
        return False, "Student Not Found"

# Usage
students = readData('data.txt')
found, name = search_student(students, 'A007')
if found:
    print(f"Name: {name}")
else:
    print(name)
```

### Pattern 2: Menu Options Dictionary
```python
menu_options = {
    'W': 'Withdraw',
    'D': 'Deposit',
    'B': 'Balance',
    'Q': 'Quit'
}

# Display menu
for code, description in menu_options.items():
    print(f"{code} - {description}")

# Validate choice
choice = input("Enter choice: ").upper()
if choice in menu_options:
    print(f"Selected: {menu_options[choice]}")
else:
    print("Invalid choice")
```

### Pattern 3: Counting/Frequency
```python
# Count occurrences
text = "hello world"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ...}

# Or with setdefault
for char in text:
    frequency.setdefault(char, 0)
    frequency[char] += 1
```

### Pattern 4: Grouping Data
```python
students = [
    {'name': 'John', 'grade': 'A'},
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'}
]

# Group by grade
by_grade = {}
for student in students:
    grade = student['grade']
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student['name'])

# {'A': ['John', 'Alice'], 'B': ['Bob']}
```

### Pattern 5: Configuration Storage
```python
config = {
    'app_name': 'Student Manager',
    'version': '1.0',
    'settings': {
        'max_students': 100,
        'auto_save': True,
        'theme': 'dark'
    }
}

# Access nested config
max_students = config['settings']['max_students']

# Update config
config['settings'].update({'theme': 'light', 'font_size': 12})
```

---

## ERROR HANDLING

### KeyError Prevention
```python
student = {'name': 'John', 'id': 'S001'}

# WRONG: Direct access can raise KeyError
try:
    age = student['age']  # KeyError!
except KeyError:
    age = 0

# CORRECT: Use .get() with default
age = student.get('age', 0)  # 0

# CORRECT: Check key exists
if 'age' in student:
    age = student['age']
else:
    age = 0
```

### Safe Nested Access
```python
data = {'user': {'profile': {'name': 'John'}}}

# WRONG: Can raise KeyError at any level
name = data['user']['profile']['name']

# CORRECT: Check each level
if 'user' in data and 'profile' in data['user']:
    name = data['user']['profile'].get('name', 'Unknown')

# BETTER: Use .get() chain
name = data.get('user', {}).get('profile', {}).get('name', 'Unknown')
```

---

## QUICK EXAMPLES

### Create and Access
```python
# Create
student = {'name': 'John', 'id': 'S001', 'gpa': 3.8}

# Access
name = student['name']                    # 'John'
age = student.get('age', 0)              # 0
keys = list(student.keys())              # ['name', 'id', 'gpa']
```

### Modify
```python
# Add/Update
student['age'] = 20
student.update({'major': 'CS', 'year': 2})

# Remove
student.pop('age')
del student['major']
```

### Iterate
```python
# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key-Value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# With enumerate
for i, (key, value) in enumerate(student.items(), 1):
    print(f"{i}. {key}: {value}")
```

### Nested
```python
# Create nested
students = {
    'S001': {'name': 'John', 'gpa': 3.8},
    'S002': {'name': 'Alice', 'gpa': 3.9}
}

# Access nested
john_gpa = students['S001']['gpa']       # 3.8

# Iterate nested
for sid, info in students.items():
    for key, value in info.items():
        print(f"{sid} {key}: {value}")
```

---

*Last Updated: November 30, 2025*
*Focus: Methods-first, looping patterns, nested dictionaries, enumerate integration*