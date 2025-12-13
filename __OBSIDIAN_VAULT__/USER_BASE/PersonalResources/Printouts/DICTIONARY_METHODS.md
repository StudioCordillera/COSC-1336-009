 # DICTIONARY_METHODS

## Core Definition
**Dictionaries** are mutable, unordered (insertion-ordered in Python 3.7+) collections of key-value pairs. Support fast lookups, dynamic updates, and flexible data organization using hashable keys.

**Tags**: #dictionary #hash #mapping #key-value #mutable #collection

---

## COMPLETE DICTIONARY METHODS QUICK REFERENCE

### DICTIONARY METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# CORE ACCESS METHODS
# ═══════════════════════════════════════════════════════════════════════════
dict[key]                    # Dict | Access value by key | Returns value or KeyError
dict.get(key)                # Dict | Safe access by key | Returns value or None
dict.get(key, default)       # Dict | Safe access with default | Returns value or default
dict.setdefault(key, default) # Dict | Get or set if missing | Returns value, sets if missing
dict.keys()                  # Dict | Get all keys | Returns dict_keys view
dict.values()                # Dict | Get all values | Returns dict_values view
dict.items()                 # Dict | Get key-value pairs | Returns dict_items view
len(dict)                    # Dict | Get number of items | Returns int count
key in dict                  # Dict | Check key existence | Returns True/False
key not in dict              # Dict | Check key absence | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# MODIFICATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
dict[key] = value            # Dict | Add or update entry | Modifies dict in place
dict.update(other_dict)      # Dict | Merge dictionaries | Modifies dict in place
dict.update(key=value)       # Dict | Update with kwargs | Modifies dict in place
dict.update([(k, v), ...])   # Dict | Update from pairs | Modifies dict in place
dict.pop(key)                # Dict | Remove and return value | Returns value or KeyError
dict.pop(key, default)       # Dict | Remove with default | Returns value or default
dict.popitem()               # Dict | Remove and return last pair | Returns (key, value) tuple
dict.clear()                 # Dict | Remove all items | Empties dict, returns None
del dict[key]                # Dict | Delete key-value pair | Removes entry or KeyError
dict |= other                # Dict (3.9+) | Union update operator | Modifies dict in place

# ═══════════════════════════════════════════════════════════════════════════
# CREATION & COPYING METHODS
# ═══════════════════════════════════════════════════════════════════════════
dict()                       # Constructor | Create empty dict | Returns new empty dict
dict(key=value, ...)         # Constructor | Create from kwargs | Returns new dict
dict([(k, v), ...])          # Constructor | Create from pairs | Returns new dict
dict(mapping)                # Constructor | Create from mapping | Returns new dict
dict.fromkeys(keys)          # Static | Create with keys, None values | Returns new dict
dict.fromkeys(keys, value)   # Static | Create with keys, same value | Returns new dict
dict.copy()                  # Dict | Shallow copy | Returns new dict copy
{k: v for k, v in items}     # Dict comprehension | Build from expression | Returns new dict

# ═══════════════════════════════════════════════════════════════════════════
# COMBINATION METHODS (Python 3.9+)
# ═══════════════════════════════════════════════════════════════════════════
dict1 | dict2                # Two dicts | Union (merge) | Returns new merged dict
dict1 |= dict2               # Two dicts | Union update | Modifies dict1 in place

# ═══════════════════════════════════════════════════════════════════════════
# VIEW OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
dict.keys() & other.keys()   # Two key views | Intersection | Returns set of common keys
dict.keys() | other.keys()   # Two key views | Union | Returns set of all keys
dict.keys() - other.keys()   # Two key views | Difference | Returns set of unique keys
dict.keys() ^ other.keys()   # Two key views | Symmetric diff | Returns set of unique to each

# ═══════════════════════════════════════════════════════════════════════════
# ITERATION PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
for key in dict:             # Dict | Iterate over keys | Yields each key
for key in dict.keys():      # Dict | Explicit key iteration | Yields each key
for value in dict.values():  # Dict | Iterate over values | Yields each value
for key, value in dict.items(): # Dict | Iterate key-value pairs | Yields (key, value) tuples
enumerate(dict)              # Dict | Indexed iteration | Yields (index, key) tuples
enumerate(dict.items())      # Dict | Indexed pair iteration | Yields (index, (key, value))
reversed(dict)               # Dict (3.8+) | Reverse key iteration | Yields keys in reverse
iter(dict)                   # Dict | Create key iterator | Returns iterator over keys
next(iter(dict))             # Dict iterator | Get next key | Returns next key or StopIteration

# ═══════════════════════════════════════════════════════════════════════════
# DICTIONARY UNPACKING
# ═══════════════════════════════════════════════════════════════════════════
{**dict1, **dict2}           # Two dicts | Unpack and merge | Returns new merged dict
func(**dict)                 # Dict | Unpack as kwargs | Passes items as keyword arguments
{k: v, **other}              # Dict + items | Combine with unpacking | Returns new merged dict

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
str(dict)                    # Dict | Convert to string | Returns string representation
repr(dict)                   # Dict | Get repr string | Returns repr string
hash(frozendict)             # Frozen dict | Get hash value | Returns int hash (immutable only)
bool(dict)                   # Dict | Check if non-empty | Returns True if non-empty, False if empty
sorted(dict)                 # Dict | Sort keys | Returns sorted list of keys
sorted(dict.items())         # Dict items | Sort by keys | Returns sorted list of tuples
sorted(dict, key=dict.get)   # Dict | Sort keys by values | Returns list of keys sorted by value
min(dict)                    # Dict | Find minimum key | Returns smallest key
max(dict)                    # Dict | Find maximum key | Returns largest key
sum(dict.values())           # Dict values | Sum all values | Returns sum if numeric
list(dict)                   # Dict | Convert keys to list | Returns list of keys
tuple(dict)                  # Dict | Convert keys to tuple | Returns tuple of keys
set(dict)                    # Dict | Convert keys to set | Returns set of keys

# ═══════════════════════════════════════════════════════════════════════════
# COMPARISON OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
dict1 == dict2               # Two dicts | Check equality | Returns True/False
dict1 != dict2               # Two dicts | Check inequality | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# DICTIONARY LITERALS & CREATION
# ═══════════════════════════════════════════════════════════════════════════
{}                           # Literal | Empty dictionary | Returns empty dict
{'key': 'value'}             # Literal | Dict with items | Returns new dict
{1: 'a', 2: 'b'}             # Literal | Mixed key types | Returns new dict
dict(a=1, b=2)               # Constructor | Keyword arguments | Returns {'a': 1, 'b': 2}
dict([('a', 1), ('b', 2)])   # Constructor | From pairs | Returns {'a': 1, 'b': 2}
{k: v for k, v in pairs}     # Comprehension | From expression | Returns new dict
```

### COMMON OPERATION EXAMPLES

```python
# Create dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Access values
person['name']               # → 'Alice'
person.get('age')            # → 30
person.get('job', 'N/A')     # → 'N/A' (not found, use default)

# Modify dictionary
person['age'] = 31           # Update existing
person['job'] = 'Engineer'   # Add new
person.update({'age': 32, 'country': 'USA'})  # Update multiple

# Remove items
person.pop('city')           # → 'NYC' (removes and returns)
last = person.popitem()      # → ('country', 'USA') (removes last)
del person['job']            # Delete specific key

# Check existence
'name' in person             # → True
'phone' not in person        # → True

# Get keys, values, items
person.keys()                # → dict_keys(['name', 'age'])
person.values()              # → dict_values(['Alice', 32])
person.items()               # → dict_items([('name', 'Alice'), ('age', 32)])

# Iterate
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Copy and merge
backup = person.copy()
more_data = {'email': 'alice@example.com'}
person.update(more_data)

# Comprehension
squares = {x: x**2 for x in range(5)}  # → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## DETAILED DICTIONARY OPERATIONS

### 1. DICTIONARY CREATION PATTERNS

```python
# Empty dictionary
d1 = {}
d2 = dict()

# Literal creation
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'NYC'
}

# From keyword arguments
person = dict(name='Alice', age=30, city='NYC')

# From list of tuples/pairs
pairs = [('a', 1), ('b', 2), ('c', 3)]
d = dict(pairs)              # → {'a': 1, 'b': 2, 'c': 3}

# From two lists using zip
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'NYC']
person = dict(zip(keys, values))

# From keys with default value
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys)      # → {'a': None, 'b': None, 'c': None}
d = dict.fromkeys(keys, 0)   # → {'a': 0, 'b': 0, 'c': 0}

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
evens = {x: x**2 for x in range(10) if x % 2 == 0}

# Nested comprehension
matrix = {(i, j): i*j for i in range(3) for j in range(3)}

# From another dict (shallow copy)
original = {'a': 1, 'b': 2}
copy1 = original.copy()
copy2 = dict(original)
copy3 = {**original}         # Unpacking syntax

# Merging dictionaries (Python 3.9+)
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = d1 | d2             # → {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Merging with unpacking (Python 3.5+)
merged = {**d1, **d2}

# Merging with update (modifies in place)
d1.update(d2)
```

### 2. ACCESSING VALUES SAFELY

```python
data = {'name': 'Bob', 'age': 25}

# Direct access (raises KeyError if missing)
name = data['name']          # → 'Bob'
# email = data['email']      # → KeyError

# Safe access with get()
name = data.get('name')      # → 'Bob'
email = data.get('email')    # → None
email = data.get('email', 'N/A')  # → 'N/A' (custom default)

# setdefault() - get or create with default
email = data.setdefault('email', 'unknown@example.com')
# If 'email' exists: returns existing value
# If 'email' missing: adds 'email' with default, returns default
print(data)                  # → {'name': 'Bob', 'age': 25, 'email': 'unknown@example.com'}

# Check before access
if 'name' in data:
    name = data['name']

# EAFP style (Easier to Ask Forgiveness than Permission)
try:
    email = data['email']
except KeyError:
    email = 'N/A'

# LBYL style (Look Before You Leap)
email = data['email'] if 'email' in data else 'N/A'
```

### 3. MODIFYING DICTIONARIES

```python
data = {'name': 'Charlie', 'age': 35}

# Add or update single item
data['city'] = 'Boston'      # Add new
data['age'] = 36             # Update existing

# Update multiple items
data.update({'age': 37, 'job': 'Engineer'})
data.update([('salary', 75000), ('department', 'IT')])
data.update(country='USA', state='MA')

# Conditional update (only if key doesn't exist)
data.setdefault('email', 'charlie@example.com')
data.setdefault('name', 'David')  # Won't change (name exists)

# Remove items - pop() returns value
age = data.pop('age')        # → 37, removes 'age'
job = data.pop('job', 'N/A') # → 'Engineer', removes 'job'
# missing = data.pop('xyz')  # → KeyError
missing = data.pop('xyz', None)  # → None (safe)

# Remove and return last inserted item (LIFO)
item = data.popitem()        # → ('state', 'MA')

# Remove with del
del data['city']             # Remove 'city' or KeyError

# Clear all items
data.clear()                 # → {} (empties dictionary)

# Increment counter pattern
word_count = {}
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
# → {'apple': 3, 'banana': 2, 'cherry': 1}

# Using setdefault for counter
word_count = {}
for word in words:
    word_count.setdefault(word, 0)
    word_count[word] += 1
```

### 4. ITERATION PATTERNS

```python
data = {'name': 'David', 'age': 28, 'city': 'LA', 'job': 'Designer'}

# Iterate over keys (default)
for key in data:
    print(key)               # → name, age, city, job

# Explicit key iteration
for key in data.keys():
    print(key, data[key])

# Iterate over values
for value in data.values():
    print(value)             # → David, 28, LA, Designer

# Iterate over items (key-value pairs)
for key, value in data.items():
    print(f"{key}: {value}")

# Enumerate for indexed iteration
for index, key in enumerate(data):
    print(f"{index}: {key} = {data[key]}")

for index, (key, value) in enumerate(data.items()):
    print(f"{index}: {key} = {value}")

# Reverse iteration (Python 3.8+)
for key in reversed(data):
    print(key)               # → job, city, age, name

# Iterate with transformation
for key, value in data.items():
    if isinstance(value, str):
        print(f"{key}: {value.upper()}")

# Filter during iteration
for key, value in data.items():
    if isinstance(value, int):
        print(f"{key}: {value}")

# Build list from iteration
keys_list = [key for key in data]
values_list = [value for value in data.values()]
items_list = [(k, v) for k, v in data.items()]

# Iterate with multiple dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

for key in {**dict1, **dict2}:
    print(key)
```

### 5. DICTIONARY COMPREHENSIONS

```python
# Basic comprehension
squares = {x: x**2 for x in range(6)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# → {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From list
words = ['apple', 'banana', 'cherry']
lengths = {word: len(word) for word in words}
# → {'apple': 5, 'banana': 6, 'cherry': 6}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
# → {1: 'a', 2: 'b', 3: 'c'}

# Filter and transform
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v*2 for k, v in data.items() if v > 2}
# → {'c': 6, 'd': 8}

# From two lists
keys = ['name', 'age', 'city']
values = ['Eve', 29, 'Seattle']
person = {k: v for k, v in zip(keys, values)}

# Nested comprehension
matrix = {(i, j): i+j for i in range(3) for j in range(3)}
# → {(0, 0): 0, (0, 1): 1, ..., (2, 2): 4}

# Conditional value
grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
results = {name: 'Pass' if score >= 80 else 'Fail' 
           for name, score in grades.items()}
# → {'Alice': 'Pass', 'Bob': 'Pass', 'Charlie': 'Fail'}

# Case transformation
data = {'Name': 'Frank', 'Age': 30, 'City': 'NYC'}
lowercase = {k.lower(): v for k, v in data.items()}
# → {'name': 'Frank', 'age': 30, 'city': 'NYC'}

# Grouping with comprehension
words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
by_first = {letter: [w for w in words if w[0] == letter] 
            for letter in set(w[0] for w in words)}
# → {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

### 6. MERGING & COMBINING DICTIONARIES

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'b': 20, 'e': 5}

# Using update() - modifies in place
d = dict1.copy()
d.update(dict2)              # → {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Overlapping keys - last wins
d = dict1.copy()
d.update(dict3)              # → {'a': 1, 'b': 20, 'e': 5}

# Using unpacking (Python 3.5+)
merged = {**dict1, **dict2}  # → {'a': 1, 'b': 2, 'c': 3, 'd': 4}
merged = {**dict1, **dict2, **dict3}  # Last dict wins on conflicts

# Using union operator (Python 3.9+)
merged = dict1 | dict2       # → {'a': 1, 'b': 2, 'c': 3, 'd': 4}
merged = dict1 | dict2 | dict3  # Chain multiple

# Union update (Python 3.9+)
d = dict1.copy()
d |= dict2                   # Modifies d in place

# Merge with custom conflict resolution
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

merged = merge_dicts(dict1, dict2, dict3)

# Merge with addition for conflicts
def merge_add(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = merge_add(d1, d2)   # → {'a': 1, 'b': 5, 'c': 4}

# Merge with list accumulation
def merge_lists(dict1, dict2):
    result = {}
    for key in set(dict1) | set(dict2):
        result[key] = dict1.get(key, []) + dict2.get(key, [])
    return result

d1 = {'a': [1], 'b': [2]}
d2 = {'b': [3], 'c': [4]}
merged = merge_lists(d1, d2)  # → {'a': [1], 'b': [2, 3], 'c': [4]}
```

### 7. SORTING DICTIONARIES

```python
data = {'banana': 3, 'apple': 5, 'cherry': 2, 'date': 4}

# Sort by keys (returns list of keys)
sorted_keys = sorted(data)
# → ['apple', 'banana', 'cherry', 'date']

# Sort by keys - create new sorted dict
sorted_dict = {k: data[k] for k in sorted(data)}
# → {'apple': 5, 'banana': 3, 'cherry': 2, 'date': 4}

# Sort by keys using dict()
sorted_dict = dict(sorted(data.items()))

# Sort by values
sorted_by_value = sorted(data.items(), key=lambda item: item[1])
# → [('cherry', 2), ('banana', 3), ('date', 4), ('apple', 5)]

# Sort by values - create dict
sorted_dict = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
# → {'cherry': 2, 'banana': 3, 'date': 4, 'apple': 5}

# Reverse sort
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
# → {'apple': 5, 'date': 4, 'banana': 3, 'cherry': 2}

# Sort keys by their values
sorted_keys_by_value = sorted(data, key=data.get)
# → ['cherry', 'banana', 'date', 'apple']

# Sort by complex criteria
people = {
    'Alice': {'age': 30, 'salary': 70000},
    'Bob': {'age': 25, 'salary': 60000},
    'Charlie': {'age': 35, 'salary': 80000}
}

# Sort by nested value
sorted_by_age = dict(sorted(people.items(), key=lambda x: x[1]['age']))
sorted_by_salary = dict(sorted(people.items(), key=lambda x: x[1]['salary']))

# Multiple sort criteria
sorted_multi = dict(sorted(people.items(), 
                          key=lambda x: (x[1]['age'], x[1]['salary'])))

# Get top N items
top_3 = dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:3])

# Case-insensitive key sort
mixed_case = {'Zebra': 1, 'apple': 2, 'BANANA': 3}
sorted_case = dict(sorted(mixed_case.items(), key=lambda x: x[0].lower()))
```

### 8. FILTERING DICTIONARIES

```python
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Filter by value
filtered = {k: v for k, v in data.items() if v > 2}
# → {'c': 3, 'd': 4, 'e': 5}

# Filter by key
filtered = {k: v for k, v in data.items() if k in ['a', 'c', 'e']}
# → {'a': 1, 'c': 3, 'e': 5}

# Filter by key pattern
filtered = {k: v for k, v in data.items() if k.startswith('a')}

# Filter with function
def is_even(value):
    return value % 2 == 0

filtered = {k: v for k, v in data.items() if is_even(v)}
# → {'b': 2, 'd': 4}

# Remove None values
data_with_none = {'a': 1, 'b': None, 'c': 3, 'd': None}
filtered = {k: v for k, v in data_with_none.items() if v is not None}
# → {'a': 1, 'c': 3}

# Remove empty strings
data_with_empty = {'name': 'Alice', 'email': '', 'city': 'NYC'}
filtered = {k: v for k, v in data_with_empty.items() if v}
# → {'name': 'Alice', 'city': 'NYC'}

# Keep only certain keys
keys_to_keep = ['a', 'c']
filtered = {k: data[k] for k in keys_to_keep if k in data}
# → {'a': 1, 'c': 3}

# Remove certain keys
keys_to_remove = ['b', 'd']
filtered = {k: v for k, v in data.items() if k not in keys_to_remove}
# → {'a': 1, 'c': 3, 'e': 5}

# Filter nested dict
people = {
    'Alice': {'age': 30, 'active': True},
    'Bob': {'age': 25, 'active': False},
    'Charlie': {'age': 35, 'active': True}
}

active_people = {k: v for k, v in people.items() if v['active']}
# → {'Alice': {...}, 'Charlie': {...}}

# Filter with multiple conditions
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
filtered = {k: v for k, v in data.items() if v > 2 and k != 'e'}
# → {'c': 3, 'd': 4, 'f': 6}
```

### 9. NESTED DICTIONARIES

```python
# Create nested structure
company = {
    'employees': {
        'Alice': {'age': 30, 'role': 'Engineer', 'salary': 75000},
        'Bob': {'age': 25, 'role': 'Designer', 'salary': 65000},
        'Charlie': {'age': 35, 'role': 'Manager', 'salary': 85000}
    },
    'departments': {
        'Engineering': ['Alice'],
        'Design': ['Bob'],
        'Management': ['Charlie']
    }
}

# Access nested values
alice_age = company['employees']['Alice']['age']  # → 30

# Safe nested access with get()
age = company.get('employees', {}).get('Alice', {}).get('age')

# Safe access with default
email = company.get('employees', {}).get('Alice', {}).get('email', 'N/A')

# Update nested value
company['employees']['Alice']['salary'] = 80000

# Add to nested dict
company['employees']['David'] = {'age': 28, 'role': 'Analyst', 'salary': 60000}

# Iterate nested dict
for name, info in company['employees'].items():
    print(f"{name}: {info['role']} - ${info['salary']}")

# Flatten nested dict
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

nested = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
flat = flatten_dict(nested)
# → {'a': 1, 'b_c': 2, 'b_d_e': 3}

# Deep copy nested dict
import copy
nested = {'a': {'b': 1}}
shallow = nested.copy()      # Shallow: nested dicts still shared
deep = copy.deepcopy(nested)  # Deep: fully independent copy

# Update nested dict recursively
def deep_update(base_dict, update_dict):
    for key, value in update_dict.items():
        if isinstance(value, dict) and key in base_dict and isinstance(base_dict[key], dict):
            deep_update(base_dict[key], value)
        else:
            base_dict[key] = value
    return base_dict

base = {'a': {'b': 1, 'c': 2}}
update = {'a': {'b': 10, 'd': 3}}
deep_update(base, update)
# → {'a': {'b': 10, 'c': 2, 'd': 3}}

# Search nested dict for value
def find_key_by_value(d, target_value, path=[]):
    for key, value in d.items():
        if value == target_value:
            return path + [key]
        if isinstance(value, dict):
            result = find_key_by_value(value, target_value, path + [key])
            if result:
                return result
    return None

nested = {'a': {'b': {'c': 123}}}
path = find_key_by_value(nested, 123)  # → ['a', 'b', 'c']
```

### 10. DICTIONARY VIEWS AND SET OPERATIONS

```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}

# Get views (dynamic - reflect changes)
keys_view = dict1.keys()     # → dict_keys(['a', 'b', 'c'])
values_view = dict1.values()  # → dict_values([1, 2, 3])
items_view = dict1.items()   # → dict_items([('a', 1), ('b', 2), ('c', 3)])

# Views are dynamic
dict1['d'] = 4
print(keys_view)             # → dict_keys(['a', 'b', 'c', 'd'])

# Convert views to lists
keys_list = list(dict1.keys())
values_list = list(dict1.values())
items_list = list(dict1.items())

# Set operations on keys
common_keys = dict1.keys() & dict2.keys()
# → {'b', 'c'}

all_keys = dict1.keys() | dict2.keys()
# → {'a', 'b', 'c', 'd'}

unique_to_dict1 = dict1.keys() - dict2.keys()
# → {'a'}

unique_to_either = dict1.keys() ^ dict2.keys()
# → {'a', 'd'}

# Filter dict by key operations
common_items = {k: dict1[k] for k in dict1.keys() & dict2.keys()}
# → {'b': 2, 'c': 3}

# Check if key in multiple dicts
if 'b' in dict1.keys() & dict2.keys():
    print("Key exists in both")

# Set operations on items (both key and value must match)
common_items = dict1.items() & dict2.items()
# → {('b', 2), ('c', 3)}

different_items = dict1.items() ^ dict2.items()
# → {('a', 1), ('d', 4)}

# Find dicts with same key but different values
different_values = {k for k in dict1.keys() & dict2.keys() 
                   if dict1[k] != dict2[k]}

# Union of dicts (prefer dict1 values on conflict)
union = {**dict2, **dict1}

# Intersection of dicts (values from dict1)
intersection = {k: dict1[k] for k in dict1.keys() & dict2.keys()}
```

### 11. DEFAULTDICT AND COUNTER PATTERNS

```python
from collections import defaultdict, Counter

# defaultdict - provide default value for missing keys
word_lists = defaultdict(list)
word_lists['a'].append('apple')  # No KeyError, creates empty list first
word_lists['a'].append('apricot')
word_lists['b'].append('banana')
# → defaultdict(<class 'list'>, {'a': ['apple', 'apricot'], 'b': ['banana']})

# defaultdict with int (counter pattern)
word_count = defaultdict(int)
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
for word in words:
    word_count[word] += 1  # No need for get() or setdefault()
# → defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 1})

# defaultdict with set
categories = defaultdict(set)
categories['fruits'].add('apple')
categories['fruits'].add('banana')
categories['vegetables'].add('carrot')

# Counter - specialized dict for counting
from collections import Counter
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counts = Counter(words)
# → Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common items
counts.most_common(2)        # → [('apple', 3), ('banana', 2)]

# Counter operations
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'c', 'c', 'd'])

c1 + c2                      # → Counter({'a': 3, 'c': 3, 'b': 1, 'd': 1})
c1 - c2                      # → Counter({'a': 1, 'b': 1})
c1 & c2                      # → Counter({'a': 1, 'c': 1}) (min)
c1 | c2                      # → Counter({'a': 2, 'c': 2, 'b': 1, 'd': 1}) (max)

# Convert Counter to regular dict
regular_dict = dict(counts)

# Update Counter
counts.update(['apple', 'date'])
counts.subtract(['banana'])  # Can go negative

# Total of all counts
total = sum(counts.values())

# List of elements (repeating by count)
elements = list(counts.elements())
# → ['apple', 'apple', 'apple', 'banana', 'banana', 'cherry']
```

### 12. PERFORMANCE PATTERNS

```python
import sys

# Memory efficient - generator vs dict comprehension
# Generator (lazy evaluation)
gen = ((x, x**2) for x in range(1000000))  # Small memory footprint
# Dict comprehension (immediate)
d = {x: x**2 for x in range(1000000)}  # Consumes full memory

# Fast membership testing
large_dict = {x: x**2 for x in range(10000)}
# O(1) average time
if 5000 in large_dict:  # Very fast
    pass

# Avoid repeated key lookups
data = {'a': 1, 'b': 2, 'c': 3}

# Inefficient - multiple lookups
if 'a' in data:
    x = data['a']
    y = data['a'] * 2
    z = data['a'] + 10

# Efficient - single lookup
if 'a' in data:
    val = data['a']
    x = val
    y = val * 2
    z = val + 10

# Or use EAFP
try:
    val = data['a']
    x = val
    y = val * 2
    z = val + 10
except KeyError:
    pass

# Batch updates faster than individual
data = {}
items = [(i, i**2) for i in range(1000)]

# Slower
for k, v in items:
    data[k] = v

# Faster
data.update(items)

# Faster dict copy for large dicts
original = {x: x**2 for x in range(10000)}
# Fast
copy1 = original.copy()
# Slower
copy2 = dict(original)
# Slower
copy3 = {k: v for k, v in original.items()}

# Memory profiling
d1 = {x: x for x in range(100)}
d2 = dict((x, x) for x in range(100))
print(sys.getsizeof(d1))  # Check memory usage
```

---

## COMMON PATTERNS AND IDIOMS

### Pattern 1: Counter/Frequency Pattern
```python
# Count occurrences
items = ['a', 'b', 'a', 'c', 'b', 'a']
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

# Or with setdefault
counts = {}
for item in items:
    counts.setdefault(item, 0)
    counts[item] += 1

# Or with defaultdict
from collections import defaultdict
counts = defaultdict(int)
for item in items:
    counts[item] += 1

# Or with Counter
from collections import Counter
counts = Counter(items)
```

### Pattern 2: Grouping Pattern
```python
# Group items by property
students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'},
    {'name': 'David', 'grade': 'C'}
]

# Group by grade
by_grade = {}
for student in students:
    grade = student['grade']
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student['name'])

# With setdefault
by_grade = {}
for student in students:
    by_grade.setdefault(student['grade'], []).append(student['name'])

# With defaultdict
from collections import defaultdict
by_grade = defaultdict(list)
for student in students:
    by_grade[student['grade']].append(student['name'])
```

### Pattern 3: Invert Dictionary
```python
# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
# → {1: 'a', 2: 'b', 3: 'c'}

# Handle duplicate values
original = {'a': 1, 'b': 2, 'c': 1}
inverted = {}
for k, v in original.items():
    inverted.setdefault(v, []).append(k)
# → {1: ['a', 'c'], 2: ['b']}
```

### Pattern 4: Dictionary as Switch/Case
```python
# Replace if-elif-else chains
def handle_action(action, data):
    actions = {
        'create': lambda d: print(f"Creating {d}"),
        'update': lambda d: print(f"Updating {d}"),
        'delete': lambda d: print(f"Deleting {d}"),
    }
    
    handler = actions.get(action, lambda d: print(f"Unknown action"))
    handler(data)

handle_action('create', 'record')  # → Creating record
handle_action('unknown', 'test')   # → Unknown action

# With arguments
def operations(op, x, y):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else None,
    }
    return ops.get(op, lambda a, b: None)(x, y)

result = operations('+', 5, 3)     # → 8
```

### Pattern 5: Caching/Memoization
```python
# Simple cache
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

# Or use functools
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Pattern 6: Configuration Management
```python
# Application configuration
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'mydb'
    },
    'api': {
        'base_url': 'https://api.example.com',
        'timeout': 30,
        'retries': 3
    },
    'features': {
        'enable_logging': True,
        'enable_cache': True,
        'debug_mode': False
    }
}

# Access with defaults
db_host = config.get('database', {}).get('host', 'localhost')
debug = config.get('features', {}).get('debug_mode', False)

# Environment overrides
import os
config['database']['host'] = os.getenv('DB_HOST', config['database']['host'])
```

### Pattern 7: Data Transformation Pipeline
```python
# Transform dict structure
raw_data = {'NAME': 'alice', 'AGE': '30', 'CITY': 'nyc'}

# Lowercase keys, convert values
processed = {
    k.lower(): int(v) if v.isdigit() else v.title()
    for k, v in raw_data.items()
}
# → {'name': 'Alice', 'age': 30, 'city': 'Nyc'}

# Filter and rename
mapping = {'NAME': 'name', 'AGE': 'age'}
processed = {
    mapping[k]: v 
    for k, v in raw_data.items() 
    if k in mapping
}
# → {'name': 'alice', 'age': '30'}
```

---

## BEST PRACTICES AND TIPS

### ✓ DO's
1. **Use `.get()` for safe access** - Avoid KeyError with default values
2. **Use `in` for existence checks** - Faster than try/except for simple checks
3. **Use comprehensions** - More readable and often faster than loops
4. **Use `.items()` for iteration** - Clean access to both keys and values
5. **Use `collections.defaultdict`** - Simplify accumulation patterns
6. **Use `collections.Counter`** - Built-in counting functionality
7. **Use meaningful key names** - Self-documenting code
8. **Keep keys hashable** - Use immutable types (str, int, tuple)

### ✗ DON'Ts
1. **Don't modify dict during iteration** - Creates runtime errors
2. **Don't use mutable objects as keys** - Lists/dicts can't be keys
3. **Don't rely on order pre-Python 3.7** - Use OrderedDict if needed
4. **Don't use dict for large datasets** - Consider databases or specialized structures
5. **Don't nest too deeply** - Hard to read and maintain
6. **Don't repeat lookups** - Store value once for multiple uses

### Common Pitfalls
```python
# ❌ Modifying during iteration
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    if key == 'b':
        del d[key]  # RuntimeError!

# ✓ Correct approach
d = {k: v for k, v in d.items() if k != 'b'}

# ❌ Mutable default argument
def add_to_dict(value, d={}):  # Dangerous!
    d[value] = value
    return d

# ✓ Correct approach
def add_to_dict(value, d=None):
    if d is None:
        d = {}
    d[value] = value
    return d

# ❌ Assuming order (Python < 3.7)
# Don't write code that depends on specific key order

# ✓ Explicit ordering
from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2)])

# ❌ Using list as key
# d = {[1, 2]: 'value'}  # TypeError

# ✓ Use tuple instead
d = {(1, 2): 'value'}  # OK

# ❌ Inefficient nested lookup
value = data['level1']['level2']['level3']  # Can raise KeyError

# ✓ Safe nested access
value = data.get('level1', {}).get('level2', {}).get('level3', default)
```

---

## ADVANCED TOPICS

### Working with JSON
```python
import json

# Dict to JSON string
data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
json_string = json.dumps(data)
# → '{"name": "Alice", "age": 30, "city": "NYC"}'

# JSON string to dict
json_string = '{"name": "Bob", "age": 25}'
data = json.loads(json_string)
# → {'name': 'Bob', 'age': 25}

# Write dict to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read JSON file to dict
with open('data.json', 'r') as f:
    data = json.load(f)

# Pretty print
print(json.dumps(data, indent=2, sort_keys=True))
```

### Dictionary Subclassing
```python
# Custom dictionary class
class CaseInsensitiveDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower() if isinstance(key, str) else key, value)
    
    def __getitem__(self, key):
        return super().__getitem__(key.lower() if isinstance(key, str) else key)
    
    def __contains__(self, key):
        return super().__contains__(key.lower() if isinstance(key, str) else key)

d = CaseInsensitiveDict()
d['Name'] = 'Alice'
print(d['name'])  # → 'Alice'
print(d['NAME'])  # → 'Alice'

# Dot notation access
class DotDict(dict):
    """Dictionary with dot notation access"""
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"No attribute '{key}'")
    
    def __setattr__(self, key, value):
        self[key] = value

d = DotDict({'name': 'Bob', 'age': 25})
print(d.name)     # → 'Bob'
d.city = 'NYC'
print(d['city'])  # → 'NYC'
```

### ChainMap for Multiple Contexts
```python
from collections import ChainMap

# Simulate scope resolution (local -> global)
defaults = {'color': 'red', 'user': 'guest'}
overrides = {'user': 'admin'}

combined = ChainMap(overrides, defaults)
print(combined['user'])   # → 'admin' (from overrides)
print(combined['color'])  # → 'red' (from defaults)

# Add new context
local = {'color': 'blue'}
combined = combined.new_child(local)
print(combined['color'])  # → 'blue' (from local)

# Remove context
combined = combined.parents
print(combined['color'])  # → 'red' (local removed)
```

---

## PERFORMANCE COMPARISON

```python
import timeit

# Access time: dict[key] vs dict.get(key)
# dict[key] is slightly faster but can raise KeyError
# dict.get(key) is safer with minimal overhead

# Iteration: for key vs for key in keys()
# Identical performance in Python 3

# Creation: literal {} vs dict()
# Literal {} is faster

# Comprehension vs loop
# Comprehension usually faster and more readable

# Membership test: in vs iteration
# 'in' operator is O(1) average, iteration is O(n)

# Merging: update() vs unpacking vs | operator
# update() fastest for in-place
# | operator cleanest for new dict (Python 3.9+)
```

---

## SUMMARY CHEAT SHEET

```python
# CREATE
d = {}; d = dict(); d = {'k': 'v'}; d = {k: v for k, v in pairs}

# ACCESS
d[k]; d.get(k); d.get(k, default); d.setdefault(k, default)

# MODIFY
d[k] = v; d.update(other); d.pop(k); d.popitem(); del d[k]; d.clear()

# ITERATE
for k in d; for v in d.values(); for k, v in d.items()

# CHECK
k in d; k not in d; len(d); bool(d)

# VIEW
d.keys(); d.values(); d.items()

# COPY/MERGE
d.copy(); {**d1, **d2}; d1 | d2 (3.9+); d1.update(d2)

# COMPREHENSION
{k: v for k, v in items if condition}

# SORT
sorted(d); sorted(d.items()); sorted(d, key=d.get)

# CONVERT
list(d); tuple(d); set(d); str(d); dict(pairs)
```

---

**Reference**: Python Official Documentation - [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

**Last Updated**: December 6, 2025
