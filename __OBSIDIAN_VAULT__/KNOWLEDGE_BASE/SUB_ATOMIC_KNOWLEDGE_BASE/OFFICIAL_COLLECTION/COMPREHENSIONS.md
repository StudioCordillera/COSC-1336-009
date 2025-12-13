# COMPREHENSIONS - COMPREHENSIVE REFERENCE

## QUICK REFERENCE - ALL COMPREHENSIONS

```python
# ═══════════════════════════════════════════════════════════════════════════
# LIST COMPREHENSIONS [result]
# ═══════════════════════════════════════════════════════════════════════════
[x for x in iterable]              # Iterable | Copy all elements | Returns list
[expr for x in iterable]           # Iterable + expr | Transform each | Returns list
[x for x in iterable if condition] # Iterable + filter | Filtered elements | Returns list
[expr for x in iterable if cond]   # Transform + filter | Filtered & transformed | Returns list
[x for row in matrix for x in row] # Nested iteration | Flatten 2D | Returns list
[expr for x in iter1 for y in iter2] # Cartesian product | All combinations | Returns list
[expr if cond else alt for x in iter] # Conditional expr | Ternary in comprehension | Returns list

# ═══════════════════════════════════════════════════════════════════════════
# SET COMPREHENSIONS {result}
# ═══════════════════════════════════════════════════════════════════════════
{x for x in iterable}              # Iterable | Unique elements | Returns set
{expr for x in iterable}           # Iterable + expr | Transform unique | Returns set
{x for x in iterable if condition} # Iterable + filter | Filtered unique | Returns set
{x.lower() for x in strings}       # Transform strings | Lowercase unique | Returns set
{x**2 for x in range(n) if x%2==0} # Filter + transform | Even squares | Returns set

# ═══════════════════════════════════════════════════════════════════════════
# DICT COMPREHENSIONS {key: value}
# ═══════════════════════════════════════════════════════════════════════════
{k: v for k, v in pairs}           # Pairs | Create dict | Returns dict
{k: expr for k, v in pairs}        # Transform values | Modified dict | Returns dict
{expr: v for k, v in pairs}        # Transform keys | Modified keys | Returns dict
{k: v for k, v in pairs if cond}   # Filter pairs | Filtered dict | Returns dict
{x: x**2 for x in range(n)}        # Generate pairs | Number→square | Returns dict
{v: k for k, v in dict.items()}    # Reverse dict | Swap keys/values | Returns dict
{k: dict[k] for k in keys}         # Select keys | Extract subset | Returns dict

# ═══════════════════════════════════════════════════════════════════════════
# GENERATOR EXPRESSIONS (result) - Lazy evaluation
# ═══════════════════════════════════════════════════════════════════════════
(x for x in iterable)              # Iterable | Lazy iterator | Returns generator
(expr for x in iterable)           # Iterable + expr | Transform lazy | Returns generator
(x for x in iterable if condition) # Iterable + filter | Filtered lazy | Returns generator
sum(x for x in range(n))           # Generator | Direct to function | Returns result
list(x for x in iterable)          # Generator → list | Convert to list | Returns list
tuple(x for x in iterable)         # Generator → tuple | Convert to tuple | Returns tuple
any(condition for x in iterable)   # Generator + any | Check if any True | Returns bool
all(condition for x in iterable)   # Generator + all | Check if all True | Returns bool
max(expr for x in iterable)        # Generator + max | Find maximum | Returns max value
min(expr for x in iterable)        # Generator + min | Find minimum | Returns min value

# ═══════════════════════════════════════════════════════════════════════════
# NESTED COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════════════════
[[y for y in row] for row in matrix] # 2D copy | Copy matrix | Returns list of lists
[x for row in matrix for x in row]   # Flatten | 1D from 2D | Returns list
[[f(x,y) for x in range(n)] for y in range(m)] # Generate 2D | Create matrix | Returns list of lists
{(x,y) for x in range(n) for y in range(m)} # Nested set | Coordinate pairs | Returns set
{x: [y for y in range(m)] for x in range(n)} # Dict of lists | Nested structure | Returns dict

# ═══════════════════════════════════════════════════════════════════════════
# CONDITIONAL EXPRESSIONS IN COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════════════════
[x if x > 0 else 0 for x in nums]  # Ternary | Replace negatives with 0 | Returns list
[x if cond else y for x in iter]   # Conditional expr | Choose value | Returns list
[x for x in iter if cond]          # Filter | Keep matching only | Returns list
# NOTE: Filter uses 'if' at END, ternary uses 'if...else' in EXPRESSION

# ═══════════════════════════════════════════════════════════════════════════
# COMPREHENSION WITH MULTIPLE CONDITIONS
# ═══════════════════════════════════════════════════════════════════════════
[x for x in iter if cond1 if cond2] # Multiple filters | AND conditions | Returns list
[x for x in iter if cond1 and cond2] # Combined filter | AND conditions | Returns list
[x for x in iter if cond1 or cond2]  # Combined filter | OR conditions | Returns list

# ═══════════════════════════════════════════════════════════════════════════
# COMPREHENSION WITH ENUMERATE, ZIP, RANGE
# ═══════════════════════════════════════════════════════════════════════════
[i for i, x in enumerate(lst)]     # Enumerate | Get indices | Returns list of ints
[x for i, x in enumerate(lst) if i%2==0] # Enumerate + filter | Even indices | Returns list
[(x, y) for x, y in zip(l1, l2)]   # Zip | Pair elements | Returns list of tuples
[x+y for x, y in zip(l1, l2)]      # Zip + combine | Sum pairs | Returns list
[i*j for i in range(n) for j in range(m)] # Nested range | Multiplication table | Returns list
```

---

## LIST COMPREHENSIONS - CORE CONCEPT

List comprehensions provide a concise way to create lists based on existing iterables.

### Basic Syntax:
```python
# General form
[expression for item in iterable]

# With filter
[expression for item in iterable if condition]

# Example - squares
squares = [x**2 for x in range(10)]
# → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Equivalent to:
squares = []
for x in range(10):
    squares.append(x**2)
```

### Simple Transformations:
```python
# Convert to uppercase
words = ['hello', 'world', 'python']
upper = [word.upper() for word in words]
# → ['HELLO', 'WORLD', 'PYTHON']

# Get lengths
lengths = [len(word) for word in words]
# → [5, 5, 6]

# Multiply each by 2
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
# → [2, 4, 6, 8, 10]

# Convert types
strings = ['1', '2', '3', '4', '5']
integers = [int(s) for s in strings]
# → [1, 2, 3, 4, 5]

# Extract attributes
students = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 21}
]
names = [student['name'] for student in students]
# → ['Alice', 'Bob', 'Charlie']
```

### With Filtering (if clause):
```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
# → [2, 4, 6, 8, 10]

# Filter positive numbers
values = [5, -2, 8, -7, 3, -1, 9]
positives = [x for x in values if x > 0]
# → [5, 8, 3, 9]

# Filter by length
words = ['hi', 'hello', 'hey', 'goodbye']
long_words = [w for w in words if len(w) > 3]
# → ['hello', 'goodbye']

# Filter by type
mixed = [1, 'hello', 2.5, 'world', 3, None]
strings_only = [x for x in mixed if isinstance(x, str)]
# → ['hello', 'world']

# Filter with method
emails = ['test@gmail.com', 'user@yahoo.com', 'admin@gmail.com']
gmail_only = [e for e in emails if e.endswith('@gmail.com')]
# → ['test@gmail.com', 'admin@gmail.com']
```

### Multiple Conditions:
```python
numbers = range(1, 21)

# AND conditions (both must be true)
filtered = [x for x in numbers if x % 2 == 0 if x > 10]
# → [12, 14, 16, 18, 20]

# Same as:
filtered = [x for x in numbers if x % 2 == 0 and x > 10]

# OR conditions
filtered = [x for x in numbers if x < 5 or x > 15]
# → [1, 2, 3, 4, 16, 17, 18, 19, 20]

# Complex conditions
filtered = [x for x in numbers if (x % 3 == 0 or x % 5 == 0) and x < 15]
# → [3, 5, 6, 9, 10, 12]
```

### Conditional Expressions (Ternary):
```python
# Replace negatives with 0
numbers = [5, -2, 8, -7, 3, -1]
non_negative = [x if x >= 0 else 0 for x in numbers]
# → [5, 0, 8, 0, 3, 0]

# Categorize as 'even' or 'odd'
numbers = [1, 2, 3, 4, 5]
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
# → ['odd', 'even', 'odd', 'even', 'odd']

# Pass/Fail based on score
scores = [85, 92, 67, 78, 95]
results = ['Pass' if score >= 70 else 'Fail' for score in scores]
# → ['Pass', 'Pass', 'Fail', 'Pass', 'Pass']

# Clamp values to range
values = [5, 15, 25, 35, 45]
clamped = [x if x <= 30 else 30 for x in values]
# → [5, 15, 25, 30, 30]
```

### Nested Comprehensions:
```python
# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# → [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Equivalent to:
flat = []
for row in matrix:
    for num in row:
        flat.append(num)

# Cartesian product
colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
# → [('red', 'S'), ('red', 'M'), ('red', 'L'),
#    ('green', 'S'), ('green', 'M'), ('green', 'L'),
#    ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

# Multiplication table
table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
# → [[1,2,3,...,10], [2,4,6,...,20], ..., [10,20,30,...,100]]

# Nested with filter
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix for num in row if num % 2 == 0]
# → [2, 4, 6, 8]
```

### With enumerate():
```python
fruits = ['apple', 'banana', 'cherry']

# Get indices
indices = [i for i, fruit in enumerate(fruits)]
# → [0, 1, 2]

# Get values at even indices
even_indexed = [fruit for i, fruit in enumerate(fruits) if i % 2 == 0]
# → ['apple', 'cherry']

# Format with index
formatted = [f"{i+1}. {fruit}" for i, fruit in enumerate(fruits)]
# → ['1. apple', '2. banana', '3. cherry']

# Filter by both index and value
numbers = [10, 20, 30, 40, 50]
result = [num for i, num in enumerate(numbers) if i > 1 and num < 45]
# → [30, 40]
```

### With zip():
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

# Combine into tuples
combined = [(name, age) for name, age in zip(names, ages)]
# → [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Combine three lists
full_info = [(n, a, c) for n, a, c in zip(names, ages, cities)]
# → [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]

# Sum corresponding elements
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = [a + b for a, b in zip(list1, list2)]
# → [11, 22, 33, 44]

# Compare two lists
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 4, 3, 2, 5]
differences = [abs(a - b) for a, b in zip(nums1, nums2)]
# → [0, 2, 0, 2, 0]
```

---

## SET COMPREHENSIONS - UNIQUE VALUES

Set comprehensions create sets (unique, unordered collections).

### Basic Syntax:
```python
# General form
{expression for item in iterable}

# With filter
{expression for item in iterable if condition}

# Example - unique squares
squares = {x**2 for x in range(-5, 6)}
# → {0, 1, 4, 9, 16, 25} (duplicates removed)

# Unique first letters
words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
first_letters = {word[0] for word in words}
# → {'a', 'b', 'c'}
```

### Remove Duplicates:
```python
# From list with duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unique = {x for x in numbers}
# → {1, 2, 3, 4, 5}

# Unique word lengths
text = "the quick brown fox jumps over the lazy dog"
word_lengths = {len(word) for word in text.split()}
# → {3, 4, 5} (unique lengths only)

# Unique email domains
emails = ['a@gmail.com', 'b@yahoo.com', 'c@gmail.com', 'd@hotmail.com']
domains = {email.split('@')[1] for email in emails}
# → {'gmail.com', 'yahoo.com', 'hotmail.com'}
```

### Case-Insensitive Uniqueness:
```python
words = ['Hello', 'world', 'HELLO', 'World', 'Python']
unique_lower = {word.lower() for word in words}
# → {'hello', 'world', 'python'}

# Unique names (case-insensitive)
names = ['Alice', 'bob', 'ALICE', 'Bob', 'charlie']
unique_names = {name.lower() for name in names}
# → {'alice', 'bob', 'charlie'}
```

### With Filtering:
```python
# Unique even numbers
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_evens = {x for x in numbers if x % 2 == 0}
# → {2, 4, 6}

# Unique positive values
values = [5, -2, 8, -7, 3, -1, 8, 5]
unique_positives = {x for x in values if x > 0}
# → {5, 8, 3}

# Unique valid IDs
ids = [101, 102, 0, 103, -1, 102, 104, 0]
valid_ids = {id for id in ids if id > 0}
# → {101, 102, 103, 104}
```

### Nested Set Comprehensions:
```python
# Unique values from 2D structure
matrix = [[1, 2, 2], [3, 3, 4], [4, 5, 5]]
unique_values = {num for row in matrix for num in row}
# → {1, 2, 3, 4, 5}

# Unique coordinate pairs
coordinates = {(x, y) for x in range(3) for y in range(3)}
# → {(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}
```

---

## DICT COMPREHENSIONS - KEY-VALUE PAIRS

Dict comprehensions create dictionaries from iterables.

### Basic Syntax:
```python
# General form
{key_expr: value_expr for item in iterable}

# With filter
{key_expr: value_expr for item in iterable if condition}

# Example - number to square mapping
squares = {x: x**2 for x in range(6)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Word to length mapping
words = ['apple', 'banana', 'cherry']
lengths = {word: len(word) for word in words}
# → {'apple': 5, 'banana': 6, 'cherry': 6}
```

### From Lists/Tuples:
```python
# From list of tuples
pairs = [('a', 1), ('b', 2), ('c', 3)]
dictionary = {k: v for k, v in pairs}
# → {'a': 1, 'b': 2, 'c': 3}

# From two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
person = {k: v for k, v in zip(keys, values)}
# → {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# From single list (value as key)
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers}
# → {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Transform Existing Dict:
```python
original = {'a': 1, 'b': 2, 'c': 3}

# Double all values
doubled = {k: v * 2 for k, v in original.items()}
# → {'a': 2, 'b': 4, 'c': 6}

# Uppercase all keys
upper_keys = {k.upper(): v for k, v in original.items()}
# → {'A': 1, 'B': 2, 'C': 3}

# Swap keys and values
swapped = {v: k for k, v in original.items()}
# → {1: 'a', 2: 'b', 3: 'c'}

# Transform both
transformed = {k.upper(): v**2 for k, v in original.items()}
# → {'A': 1, 'B': 4, 'C': 9}
```

### Filtering:
```python
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}

# Filter by value
passing = {name: score for name, score in scores.items() if score >= 80}
# → {'Alice': 85, 'Bob': 92, 'Diana': 95}

# Filter by key
filtered = {name: score for name, score in scores.items() if name.startswith('A')}
# → {'Alice': 85}

# Filter by both
high_scorers_a = {name: score for name, score in scores.items() 
                  if score >= 90 and name.startswith(('A', 'B'))}
# → {'Bob': 92}
```

### Conditional Values:
```python
numbers = {'a': 5, 'b': -2, 'c': 8, 'd': -7}

# Replace negative values with 0
non_negative = {k: (v if v >= 0 else 0) for k, v in numbers.items()}
# → {'a': 5, 'b': 0, 'c': 8, 'd': 0}

# Categorize values
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 65}
grades = {name: ('Pass' if score >= 70 else 'Fail') 
          for name, score in scores.items()}
# → {'Alice': 'Pass', 'Bob': 'Pass', 'Charlie': 'Fail'}
```

### Nested Dict Comprehensions:
```python
# Create grade book
students = ['Alice', 'Bob', 'Charlie']
subjects = ['Math', 'English', 'Science']
gradebook = {student: {subject: 0 for subject in subjects} 
             for student in students}
# → {'Alice': {'Math': 0, 'English': 0, 'Science': 0},
#    'Bob': {'Math': 0, 'English': 0, 'Science': 0},
#    'Charlie': {'Math': 0, 'English': 0, 'Science': 0}}

# Group by category
items = [('fruit', 'apple'), ('fruit', 'banana'), 
         ('veggie', 'carrot'), ('veggie', 'celery')]
grouped = {category: [item for cat, item in items if cat == category]
           for category in {'fruit', 'veggie'}}
# → {'fruit': ['apple', 'banana'], 'veggie': ['carrot', 'celery']}
```

---

## GENERATOR EXPRESSIONS - LAZY EVALUATION

Generator expressions are like list comprehensions but use () instead of []. They generate values on-demand (lazy evaluation).

### Basic Syntax:
```python
# General form
(expression for item in iterable)

# Example
gen = (x**2 for x in range(10))
# → <generator object> (not a list!)

# Convert to list to see values
list(gen)  # → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Memory Efficiency:
```python
# List comprehension - creates entire list in memory
list_comp = [x**2 for x in range(1000000)]  # Uses ~8MB memory

# Generator expression - creates values on demand
gen_expr = (x**2 for x in range(1000000))   # Uses minimal memory

# Iterate through generator (values created as needed)
for value in gen_expr:
    print(value)  # Values generated one at a time
```

### Direct Use in Functions:
```python
# Sum of squares (no need for list())
total = sum(x**2 for x in range(100))
# → 328350

# Max value
maximum = max(x**2 for x in range(10))
# → 81

# Any/All
has_even = any(x % 2 == 0 for x in range(10))
# → True

all_positive = all(x > 0 for x in range(1, 10))
# → True

# Join strings
text = ', '.join(str(x) for x in range(5))
# → '0, 1, 2, 3, 4'
```

### With Filtering:
```python
# Even numbers only
evens_gen = (x for x in range(20) if x % 2 == 0)
list(evens_gen)  # → [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Sum of even squares
total = sum(x**2 for x in range(10) if x % 2 == 0)
# → 120 (0 + 4 + 16 + 36 + 64)
```

### Generator vs List Comprehension:
```python
# List comprehension - all values created immediately
list_result = [x**2 for x in range(10)]
print(list_result)  # → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator expression - values created on demand
gen_result = (x**2 for x in range(10))
print(gen_result)   # → <generator object>
print(list(gen_result))  # → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Can only iterate once
gen = (x for x in range(5))
list(gen)  # → [0, 1, 2, 3, 4]
list(gen)  # → [] (exhausted!)
```

### Chaining Generators:
```python
# Multiple transformations
numbers = range(20)
evens = (x for x in numbers if x % 2 == 0)
squares = (x**2 for x in evens)
large = (x for x in squares if x > 50)
result = list(large)  # → [64, 100, 144, 196, 256, 324]

# All computed lazily, minimal memory usage
```

---

## GENERATORS WITH ANY() AND ALL() - BOOLEAN CHECKING

### Using any() with Generator Expressions:
```python
# Check if ANY element matches condition
numbers = [1, 3, 5, 7, 8, 9]

# Check if any even number exists
has_even = any(x % 2 == 0 for x in numbers)
# → True (8 is even)

# Check if any negative exists
has_negative = any(x < 0 for x in numbers)
# → False

# Check if any string starts with 'A'
words = ['hello', 'world', 'apple', 'python']
starts_with_a = any(word.startswith('A') for word in words)
# → False (case-sensitive)

starts_with_a = any(word.lower().startswith('a') for word in words)
# → True (apple)

# Check in nested dictionaries
OPTIONS = {
    'L': {'OPTION': 'L', 'PROMPT': 'Enter length', 'COMPLETED': False},
    'S': {'OPTION': 'S', 'PROMPT': 'Enter surgery', 'COMPLETED': False},
    'P': {'OPTION': 'P', 'PROMPT': 'Enter pharmacy', 'COMPLETED': True},
}

# Check if ANY item is incomplete
has_incomplete = any(not item['COMPLETED'] for item in OPTIONS.values())
# → True (L and S are not completed)

# Alternative syntax
has_incomplete = any(item['COMPLETED'] == False for item in OPTIONS.values())
# → True

# Check if any value exceeds threshold
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
has_high_score = any(score > 90 for score in scores.values())
# → True (Bob: 92)

# Check if any key matches pattern
has_admin = any('admin' in key.lower() for key in {'user1', 'Admin_User', 'guest'})
# → True
```

### Using all() with Generator Expressions:
```python
# Check if ALL elements match condition
numbers = [2, 4, 6, 8, 10]

# Check if all are even
all_even = all(x % 2 == 0 for x in numbers)
# → True

# Check if all are positive
all_positive = all(x > 0 for x in numbers)
# → True

# Check if all strings are uppercase
words = ['HELLO', 'WORLD', 'PYTHON']
all_upper = all(word.isupper() for word in words)
# → True

# Check in nested dictionaries
OPTIONS = {
    'L': {'OPTION': 'L', 'COMPLETED': True},
    'S': {'OPTION': 'S', 'COMPLETED': True},
    'P': {'OPTION': 'P', 'COMPLETED': True},
}

# Check if ALL items are completed
all_completed = all(item['COMPLETED'] for item in OPTIONS.values())
# → True

# Check if all students passed
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
all_passed = all(score >= 70 for score in scores.values())
# → True

# Check if all values are strings
data = ['hello', 'world', 'python']
all_strings = all(isinstance(x, str) for x in data)
# → True

# Validate all required fields exist
required_fields = ['name', 'email', 'age']
user_data = {'name': 'Alice', 'email': 'alice@test.com', 'age': 25}
has_all_fields = all(field in user_data for field in required_fields)
# → True
```

### Combining any() and all():
```python
# Check if all pass OR any get extra credit
students = [
    {'name': 'Alice', 'score': 85, 'extra': False},
    {'name': 'Bob', 'score': 92, 'extra': True},
    {'name': 'Charlie', 'score': 78, 'extra': False}
]

all_pass = all(s['score'] >= 70 for s in students)
any_extra = any(s['extra'] for s in students)

if all_pass and any_extra:
    print("Everyone passed and someone got extra credit!")
# → Prints the message

# Validate: all fields present AND no empty values
form_data = {'name': 'Alice', 'email': 'alice@test.com', 'phone': '555-1234'}
required = ['name', 'email', 'phone']

is_valid = all(field in form_data for field in required) and \
           all(form_data[field] for field in required)
# → True (all fields exist and are non-empty)

# Check if NOT all are complete (at least one incomplete)
tasks = [
    {'name': 'Task 1', 'done': True},
    {'name': 'Task 2', 'done': False},
    {'name': 'Task 3', 'done': True}
]

has_incomplete = not all(task['done'] for task in tasks)
# → True (same as: any(not task['done'] for task in tasks))
```

### Short-Circuit Evaluation:
```python
# any() stops at first True
def check(x):
    print(f"Checking {x}")
    return x > 5

numbers = [1, 2, 8, 10, 15]
result = any(check(x) for x in numbers)
# Prints: Checking 1, Checking 2, Checking 8
# Stops at 8 (first True), doesn't check 10 or 15
# → True

# all() stops at first False
def check_even(x):
    print(f"Checking {x}")
    return x % 2 == 0

numbers = [2, 4, 7, 8, 10]
result = all(check_even(x) for x in numbers)
# Prints: Checking 2, Checking 4, Checking 7
# Stops at 7 (first False), doesn't check 8 or 10
# → False
```

### Practical Use Cases:
```python
# Use Case 1: Form validation
form = {'name': '', 'email': 'user@test.com', 'age': 25}

# Check if any field is empty
has_empty_field = any(not value for value in form.values())
# → True (name is empty)

# Use Case 2: Permission checking
user_permissions = {'read': True, 'write': False, 'delete': False}

# Check if user can do anything
can_do_anything = any(user_permissions.values())
# → True (has read permission)

# Check if user has full access
has_full_access = all(user_permissions.values())
# → False (missing write and delete)

# Use Case 3: Data quality check
records = [
    {'id': 1, 'value': 100},
    {'id': 2, 'value': 200},
    {'id': 3, 'value': 150}
]

# Check if all records have positive values
all_positive = all(record['value'] > 0 for record in records)
# → True

# Check if any record exceeds threshold
has_outlier = any(record['value'] > 180 for record in records)
# → True (200 exceeds 180)

# Use Case 4: Game state checking
OPTIONS = {
    'L': {'OPTION': 'L', 'COMPLETED': False},
    'S': {'OPTION': 'S', 'COMPLETED': False},
    'P': {'OPTION': 'P', 'COMPLETED': False}
}

# Check if game can continue (has incomplete tasks)
can_continue = any(not opt['COMPLETED'] for opt in OPTIONS.values())
# → True

# Check if game is finished (all tasks complete)
is_finished = all(opt['COMPLETED'] for opt in OPTIONS.values())
# → False

# Use Case 5: Multi-level validation
data = {
    'users': [
        {'name': 'Alice', 'active': True},
        {'name': 'Bob', 'active': True}
    ]
}

# Check if any user is inactive
has_inactive = any(not user['active'] for user in data.get('users', []))
# → False

# Check if all users have names
all_named = all(user.get('name') for user in data.get('users', []))
# → True
```

### any() vs or, all() vs and:
```python
# Using 'or' - evaluates all conditions even if True found early
result = (1 > 5) or (2 > 5) or (3 > 5) or (8 > 5)
# All comparisons evaluated

# Using any() - stops at first True (more efficient)
result = any(x > 5 for x in [1, 2, 3, 8, 10, 15])
# Stops at 8, doesn't evaluate 10 or 15

# Using 'and' - evaluates all conditions even if False found
result = (2 % 2 == 0) and (4 % 2 == 0) and (7 % 2 == 0) and (8 % 2 == 0)
# All comparisons evaluated

# Using all() - stops at first False (more efficient)  
result = all(x % 2 == 0 for x in [2, 4, 7, 8, 10])
# Stops at 7, doesn't evaluate 8 or 10

# any() and all() work with any iterable
result = any(char.isdigit() for char in "hello123")  # → True
result = all(char.isalpha() for char in "hello")     # → True
```

---

## GENERATORS WITH OTHER BUILT-IN FUNCTIONS

### Using sum() with Generators:
```python
# Sum of squares
total = sum(x**2 for x in range(10))
# → 285

# Sum with filtering
even_sum = sum(x for x in range(20) if x % 2 == 0)
# → 90 (0+2+4+6+8+10+12+14+16+18)

# Sum values from dict
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
total_score = sum(score for score in scores.values())
# → 255

# Sum with transformation
prices = [10.50, 20.00, 15.75]
total_with_tax = sum(price * 1.08 for price in prices)
# → 49.95

# Count matching items (True=1, False=0)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = sum(1 for x in numbers if x % 2 == 0)
# → 5 (five even numbers)
```

### Using max() and min() with Generators:
```python
# Find maximum
numbers = [1, 5, 3, 9, 2]
maximum = max(x for x in numbers)
# → 9

# Max with transformation
words = ['hi', 'hello', 'hey', 'goodbye']
longest = max(len(word) for word in words)
# → 7 (length of 'goodbye')

# Max from dict values
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
highest_score = max(score for score in scores.values())
# → 92

# Min with filtering
numbers = [10, -5, 20, -3, 15]
min_positive = min(x for x in numbers if x > 0)
# → 10

# Max with default for empty sequences
empty = []
result = max((x for x in empty), default=0)
# → 0 (avoids ValueError)
```

### Using sorted() with Generators:
```python
# Sort transformed values
numbers = [3, 1, 4, 1, 5, 9]
sorted_squares = sorted(x**2 for x in numbers)
# → [1, 1, 9, 16, 25, 81]

# Sort filtered values
sorted_evens = sorted(x for x in range(10) if x % 2 == 0)
# → [0, 2, 4, 6, 8]
```

### Using enumerate() with Generators:
```python
# Enumerate in comprehension
items = ['apple', 'banana', 'cherry']
indexed = [(i, item) for i, item in enumerate(items)]
# → [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# Filter by index
even_indices = [item for i, item in enumerate(items) if i % 2 == 0]
# → ['apple', 'cherry']
```

### Using zip() with Generators:
```python
# Zip multiple sequences
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
combined = list((name, score) for name, score in zip(names, scores))
# → [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Sum parallel lists
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = [a + b for a, b in zip(list1, list2)]
# → [11, 22, 33, 44]
```

### Using filter() vs Generator with if:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() (returns filter object)
evens = filter(lambda x: x % 2 == 0, numbers)
list(evens)  # → [2, 4, 6, 8, 10]

# Using generator with if (more Pythonic)
evens = (x for x in numbers if x % 2 == 0)
list(evens)  # → [2, 4, 6, 8, 10]

# List comprehension (if need list immediately)
evens = [x for x in numbers if x % 2 == 0]
# → [2, 4, 6, 8, 10]
```

### Using map() vs Generator Expression:
```python
numbers = [1, 2, 3, 4, 5]

# Using map() (returns map object)
squares = map(lambda x: x**2, numbers)
list(squares)  # → [1, 4, 9, 16, 25]

# Using generator expression (more readable)
squares = (x**2 for x in numbers)
list(squares)  # → [1, 4, 9, 16, 25]

# List comprehension (if need list immediately)
squares = [x**2 for x in numbers]
# → [1, 4, 9, 16, 25]
```

---

## WALRUS OPERATOR IN COMPREHENSIONS (Python 3.8+)

The walrus operator `:=` allows assignment within expressions, useful in comprehensions to avoid redundant calculations.

### Basic Walrus in Comprehensions:
```python
# Without walrus - function called twice
data = [1, 2, 3, 4, 5]
result = [expensive_func(x) for x in data if expensive_func(x) > 10]

# With walrus - function called once, value reused
result = [y for x in data if (y := expensive_func(x)) > 10]

# Example with actual function
def square(x):
    print(f"Computing square of {x}")
    return x ** 2

# Without walrus - computes twice
numbers = [1, 2, 3, 4, 5]
result = [square(x) for x in numbers if square(x) > 10]
# Prints "Computing..." 10 times (2x for each element)

# With walrus - computes once
result = [y for x in numbers if (y := square(x)) > 10]
# Prints "Computing..." 5 times (1x for each element)
# → [16, 25]
```

### Walrus with String Methods:
```python
# Process only non-empty stripped strings
lines = ['  hello  ', '', '  world  ', '   ']

# Without walrus - strip called twice
cleaned = [line.strip() for line in lines if line.strip()]

# With walrus - strip called once
cleaned = [stripped for line in lines if (stripped := line.strip())]
# → ['hello', 'world']

# Complex string processing
data = ['  HELLO  ', 'world', '  PYTHON  ']
result = [lower for text in data 
          if len(lower := text.strip().lower()) > 4]
# → ['hello', 'python']
```

### Walrus with Regex:
```python
import re

# Extract and use regex matches
texts = ['Price: $100', 'Cost: $50', 'No price', 'Value: $200']

# Without walrus
prices = [float(re.search(r'\$(\d+)', text).group(1)) 
          for text in texts if re.search(r'\$(\d+)', text)]

# With walrus - regex called once per item
prices = [float(match.group(1)) 
          for text in texts 
          if (match := re.search(r'\$(\d+)', text))]
# → [100.0, 50.0, 200.0]

# Extract email domains
emails = ['user@gmail.com', 'admin@yahoo.com', 'invalid', 'test@outlook.com']
domains = [match.group(1) 
           for email in emails 
           if (match := re.search(r'@([a-z]+\.[a-z]+)', email))]
# → ['gmail.com', 'yahoo.com', 'outlook.com']
```

### Walrus in Nested Comprehensions:
```python
# Process matrix with intermediate calculations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Calculate and use row sum
result = [[val / row_sum 
           for val in row] 
          for row in matrix 
          if (row_sum := sum(row)) > 10]
# Normalizes only rows with sum > 10

# Filter and transform with walrus
data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result = [[x * mult for x in row]
          for row in data
          if (mult := len(row)) > 2]
# → [[3, 6, 9], [24, 28, 32, 36]]
```

### Walrus with Dictionary Access:
```python
# Safe dictionary access with walrus
users = [
    {'name': 'Alice', 'age': 25, 'city': 'NYC'},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35, 'city': 'LA'}
]

# Get names of users with city
names_with_city = [user['name'] 
                   for user in users 
                   if (city := user.get('city'))]
# → ['Alice', 'Charlie']

# Get city or default
cities = [city if (city := user.get('city')) else 'Unknown' 
          for user in users]
# → ['NYC', 'Unknown', 'LA']
```

### Walrus with File Processing:
```python
# Read and process file lines (pseudocode)
# with open('data.txt') as f:
#     # Without walrus - reads twice
#     lines = [line for line in f if line.strip()]
#     
#     # With walrus - reads once
#     lines = [stripped for line in f if (stripped := line.strip())]

# Process CSV-like data
data = ['name,age', 'Alice,25', 'Bob,30', '']
result = [parts for line in data 
          if (parts := line.split(',')) and len(parts) == 2]
# → [['name', 'age'], ['Alice', '25'], ['Bob', '30']]
```

### Practical Walrus Examples:
```python
# Example 1: Validation with reuse
inputs = ['123', 'abc', '456', '789']
valid_numbers = [num for text in inputs 
                 if (text.isdigit()) and (num := int(text)) > 200]
# → [456, 789]

# Example 2: Complex filtering
products = [
    {'name': 'Apple', 'price': 1.50},
    {'name': 'Banana', 'price': 0.75},
    {'name': 'Cherry', 'price': 3.00}
]

# Filter and apply discount
discounted = [{'name': p['name'], 'discounted_price': disc_price}
              for p in products
              if (disc_price := p['price'] * 0.9) > 1.0]
# → [{'name': 'Apple', 'discounted_price': 1.35}, 
#    {'name': 'Cherry', 'discounted_price': 2.7}]

# Example 3: API response processing (pseudocode)
# responses = [fetch_api(url) for url in urls]
# valid = [data for resp in responses 
#          if (data := resp.json()).get('status') == 'success']
```

### When to Use Walrus:
```python
# ✅ GOOD - Avoids redundant expensive operations
result = [val for x in data if (val := expensive_func(x)) > threshold]

# ✅ GOOD - Avoids redundant method calls
cleaned = [s for line in lines if (s := line.strip())]

# ✅ GOOD - Reuses regex match
matches = [m.group(1) for text in texts if (m := re.search(pattern, text))]

# ❌ AVOID - Doesn't save computation
result = [x for x in data if (y := x) > 10]  # Unnecessary, just use x

# ❌ AVOID - Makes code less readable without benefit
result = [(y := x * 2) for x in data]  # Just do: [x * 2 for x in data]
```

---

## ADVANCED COMPREHENSION PATTERNS

### Pattern 1: Flatten Nested Structures
```python
# Flatten list of lists
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
# → [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Flatten with filtering
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_evens = [x for sublist in nested for x in sublist if x % 2 == 0]
# → [2, 4, 6, 8]

# Flatten dict of lists
data = {'group1': [1, 2, 3], 'group2': [4, 5], 'group3': [6, 7, 8]}
all_values = [val for vals in data.values() for val in vals]
# → [1, 2, 3, 4, 5, 6, 7, 8]

# Flatten deeply nested (recursive approach needed for arbitrary depth)
nested = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
flat = [item for sublist1 in nested for sublist2 in sublist1 for item in sublist2]
# → [1, 2, 3, 4, 5, 6, 7, 8]
```

### Pattern 2: Transpose Matrix
```python
# Transpose 2D matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using list comprehension with zip
transposed = [list(row) for row in zip(*matrix)]
# → [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Alternative without zip
transposed = [[matrix[j][i] for j in range(len(matrix))] 
              for i in range(len(matrix[0]))]
# → [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Pattern 3: Group By Category
```python
# Group items by category (manual)
items = [
    {'name': 'apple', 'category': 'fruit'},
    {'name': 'carrot', 'category': 'veggie'},
    {'name': 'banana', 'category': 'fruit'},
    {'name': 'celery', 'category': 'veggie'}
]

# Get unique categories first
categories = {item['category'] for item in items}

# Group by category
grouped = {cat: [item['name'] for item in items if item['category'] == cat]
           for cat in categories}
# → {'fruit': ['apple', 'banana'], 'veggie': ['carrot', 'celery']}

# Using dict.setdefault (alternative)
grouped = {}
for item in items:
    grouped.setdefault(item['category'], []).append(item['name'])
# → {'fruit': ['apple', 'banana'], 'veggie': ['carrot', 'celery']}
```

### Pattern 4: Sliding Window
```python
# Create sliding windows
data = [1, 2, 3, 4, 5, 6, 7, 8]
window_size = 3

# Sliding window of size 3
windows = [data[i:i+window_size] for i in range(len(data) - window_size + 1)]
# → [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]

# Sum of each window
window_sums = [sum(data[i:i+window_size]) 
               for i in range(len(data) - window_size + 1)]
# → [6, 9, 12, 15, 18, 21]

# Pairs (consecutive elements)
pairs = [(data[i], data[i+1]) for i in range(len(data) - 1)]
# → [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
```

### Pattern 5: Conditional Nested Structure
```python
# Create nested structure based on conditions
numbers = range(1, 11)

# Group by even/odd
grouped = {
    'even': [x for x in numbers if x % 2 == 0],
    'odd': [x for x in numbers if x % 2 != 0]
}
# → {'even': [2, 4, 6, 8, 10], 'odd': [1, 3, 5, 7, 9]}

# Categorize by range
categorized = {
    'small': [x for x in numbers if x < 4],
    'medium': [x for x in numbers if 4 <= x <= 7],
    'large': [x for x in numbers if x > 7]
}
# → {'small': [1, 2, 3], 'medium': [4, 5, 6, 7], 'large': [8, 9, 10]}
```

### Pattern 6: Multi-level Dict Comprehension
```python
# Create nested dictionary structure
students = ['Alice', 'Bob', 'Charlie']
subjects = ['Math', 'English', 'Science']

# Initialize gradebook with nested dicts
gradebook = {
    student: {subject: 0 for subject in subjects}
    for student in students
}
# → {'Alice': {'Math': 0, 'English': 0, 'Science': 0},
#    'Bob': {'Math': 0, 'English': 0, 'Science': 0},
#    'Charlie': {'Math': 0, 'English': 0, 'Science': 0}}

# Create grid coordinates
grid = {
    (x, y): f"Cell({x},{y})"
    for x in range(3)
    for y in range(3)
}
# → {(0,0): 'Cell(0,0)', (0,1): 'Cell(0,1)', ...}
```

### Pattern 7: Conditional Dict Building
```python
# Build dict with conditional inclusion
data = {'a': 1, 'b': None, 'c': 3, 'd': 0, 'e': 5}

# Filter out None and zero values
filtered = {k: v for k, v in data.items() if v}
# → {'a': 1, 'c': 3, 'e': 5}

# Include only if value meets criteria
high_values = {k: v for k, v in data.items() if v and v > 2}
# → {'c': 3, 'e': 5}

# Transform based on condition
transformed = {k: (v * 2 if v > 2 else v) for k, v in data.items() if v}
# → {'a': 1, 'c': 6, 'e': 10}
```

### Pattern 8: Cartesian Product Variations
```python
# Basic cartesian product
letters = ['A', 'B']
numbers = [1, 2, 3]
combos = [(letter, number) for letter in letters for number in numbers]
# → [('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3)]

# Filtered cartesian product
combos = [(l, n) for l in letters for n in numbers if n > 1]
# → [('A', 2), ('A', 3), ('B', 2), ('B', 3)]

# Three-way cartesian product
sizes = ['S', 'M']
colors = ['Red', 'Blue']
types = ['Cotton', 'Polyester']
products = [(size, color, type_) 
            for size in sizes 
            for color in colors 
            for type_ in types]
# → [('S', 'Red', 'Cotton'), ('S', 'Red', 'Polyester'), ...]
```

### Pattern 9: Inverse/Reverse Mappings
```python
# Reverse a dictionary
original = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original.items()}
# → {1: 'a', 2: 'b', 3: 'c'}

# Group by value (if values can repeat)
data = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
# Get unique values
values = set(data.values())
# Group keys by value
grouped = {val: [k for k, v in data.items() if v == val] 
           for val in values}
# → {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}
```

### Pattern 10: Counting and Frequency
```python
# Count occurrences (manual)
items = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
unique = set(items)
counts = {item: sum(1 for x in items if x == item) for item in unique}
# → {'a': 3, 'b': 2, 'c': 1, 'd': 1}

# Alternative using count method
counts = {item: items.count(item) for item in set(items)}
# → {'a': 3, 'b': 2, 'c': 1, 'd': 1}

# Count by condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parity_count = {
    'even': sum(1 for x in numbers if x % 2 == 0),
    'odd': sum(1 for x in numbers if x % 2 != 0)
}
# → {'even': 5, 'odd': 5}
```

---

## COMPARISON: LIST VS SET VS DICT VS GENERATOR

```python
iterable = range(10)

# List comprehension []
list_comp = [x**2 for x in iterable]
# → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Type: list, Ordered: Yes, Duplicates: Yes, Memory: All at once

# Set comprehension {}
set_comp = {x**2 for x in iterable}
# → {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
# Type: set, Ordered: No, Duplicates: No (unique), Memory: All at once

# Dict comprehension {key: value}
dict_comp = {x: x**2 for x in iterable}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# Type: dict, Ordered: Yes (3.7+), Duplicates: No (keys unique), Memory: All at once

# Generator expression ()
gen_expr = (x**2 for x in iterable)
# → <generator object>
# Type: generator, Ordered: Yes, Duplicates: Yes, Memory: Lazy (one at a time)
```

---

## PRACTICAL PROJECT PATTERNS

### Pattern 1: Data Cleaning
```python
# Remove empty strings and whitespace
raw_data = ['  hello  ', '', 'world', '  ', 'python']
cleaned = [s.strip() for s in raw_data if s.strip()]
# → ['hello', 'world', 'python']

# Convert and validate numbers
strings = ['10', '20', 'abc', '30', 'xyz']
numbers = [int(s) for s in strings if s.isdigit()]
# → [10, 20, 30]

# Clean and normalize emails
emails = ['  ALICE@TEST.COM  ', 'bob@test.com', 'CHARLIE@TEST.COM']
normalized = {email.strip().lower() for email in emails}
# → {'alice@test.com', 'bob@test.com', 'charlie@test.com'}
```

### Pattern 2: Student Data Processing
```python
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'Diana', 'score': 95}
]

# Extract names
names = [s['name'] for s in students]
# → ['Alice', 'Bob', 'Charlie', 'Diana']

# Filter passing students
passing = [s for s in students if s['score'] >= 80]
# → [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 92}, {'name': 'Diana', 'score': 95}]

# Create name → score mapping
score_dict = {s['name']: s['score'] for s in students}
# → {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95}

# Assign letter grades
grades = {s['name']: ('A' if s['score'] >= 90 else 'B' if s['score'] >= 80 else 'C')
          for s in students}
# → {'Alice': 'B', 'Bob': 'A', 'Charlie': 'C', 'Diana': 'A'}
```

### Pattern 3: File Processing
```python
# Extract file extensions
files = ['doc1.txt', 'image.png', 'data.csv', 'script.py']
extensions = {f.split('.')[-1] for f in files}
# → {'txt', 'png', 'csv', 'py'}

# Filter by extension
text_files = [f for f in files if f.endswith('.txt')]
# → ['doc1.txt']

# Create filename → extension mapping
file_map = {f: f.split('.')[-1] for f in files}
# → {'doc1.txt': 'txt', 'image.png': 'png', 'data.csv': 'csv', 'script.py': 'py'}
```

### Pattern 4: Matrix Operations
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten matrix
flat = [num for row in matrix for num in row]
# → [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get diagonal
diagonal = [matrix[i][i] for i in range(len(matrix))]
# → [1, 5, 9]

# Transpose matrix
transposed = [[matrix[j][i] for j in range(len(matrix))] 
              for i in range(len(matrix[0]))]
# → [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Filter even numbers
evens = [[num for num in row if num % 2 == 0] for row in matrix]
# → [[], [4, 6], [8]]
```

### Pattern 5: String Processing
```python
text = "The quick brown fox jumps over the lazy dog"

# Word lengths
word_lengths = [len(word) for word in text.split()]
# → [3, 5, 5, 3, 5, 4, 3, 4, 3]

# Words longer than 3 characters
long_words = [word for word in text.split() if len(word) > 3]
# → ['quick', 'brown', 'jumps', 'over', 'lazy']

# Unique word lengths
unique_lengths = {len(word) for word in text.split()}
# → {3, 4, 5}

# Word → length mapping
word_map = {word: len(word) for word in text.split()}
# → {'The': 3, 'quick': 5, 'brown': 5, ...}
```

### Pattern 6: Data Aggregation
```python
sales = [
    {'item': 'apple', 'price': 1.50, 'qty': 10},
    {'item': 'banana', 'price': 0.75, 'qty': 15},
    {'item': 'apple', 'price': 1.50, 'qty': 5},
    {'item': 'cherry', 'price': 2.00, 'qty': 8}
]

# Calculate totals
totals = [sale['price'] * sale['qty'] for sale in sales]
# → [15.0, 11.25, 7.5, 16.0]

# Grand total
grand_total = sum(sale['price'] * sale['qty'] for sale in sales)
# → 49.75

# Unique items
unique_items = {sale['item'] for sale in sales}
# → {'apple', 'banana', 'cherry'}

# Item → total price mapping
item_totals = {sale['item']: sale['price'] * sale['qty'] for sale in sales}
# → {'apple': 7.5, 'banana': 11.25, 'cherry': 16.0}
# Note: apple appears twice but dict only keeps last value
```

### Pattern 7: Filtering and Categorizing
```python
numbers = range(-10, 11)

# Separate into categories
negatives = [x for x in numbers if x < 0]
zeros = [x for x in numbers if x == 0]
positives = [x for x in numbers if x > 0]

# Categorize all at once
categories = {
    'negative': [x for x in numbers if x < 0],
    'zero': [x for x in numbers if x == 0],
    'positive': [x for x in numbers if x > 0]
}

# Or using dict comprehension
categories = {
    'negative': list(x for x in numbers if x < 0),
    'zero': list(x for x in numbers if x == 0),
    'positive': list(x for x in numbers if x > 0)
}
```

### Pattern 8: Create Lookup Tables
```python
# Roman numeral lookup
roman_values = {
    symbol: value for symbol, value in [
        ('I', 1), ('V', 5), ('X', 10), 
        ('L', 50), ('C', 100), ('D', 500), ('M', 1000)
    ]
}
# → {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Reverse lookup
value_to_roman = {v: k for k, v in roman_values.items()}
# → {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

# ASCII lookup
ascii_map = {chr(i): i for i in range(65, 91)}  # A-Z
# → {'A': 65, 'B': 66, ..., 'Z': 90}
```

---

## PERFORMANCE CONSIDERATIONS

### When to Use Each Type:

#### List Comprehension []:
- **Use when**: Need ordered collection, allow duplicates, need indexing
- **Memory**: Creates entire list immediately
- **Speed**: Fast, but uses more memory
```python
# Good for: collecting results, preserving order, needing index access
results = [process(x) for x in data]
```

#### Set Comprehension {}:
- **Use when**: Need unique values, don't care about order
- **Memory**: Creates entire set immediately
- **Speed**: Automatic deduplication, fast membership testing
```python
# Good for: removing duplicates, checking membership
unique_ids = {item['id'] for item in records}
```

#### Dict Comprehension {k:v}:
- **Use when**: Need key-value mapping
- **Memory**: Creates entire dict immediately
- **Speed**: O(1) lookups
```python
# Good for: lookups, mapping relationships
lookup = {item['id']: item for item in records}
```

#### Generator Expression ():
- **Use when**: Processing large datasets, only iterate once
- **Memory**: Minimal - values created on demand
- **Speed**: Slower per-item, but memory efficient
```python
# Good for: large datasets, streaming data, single-pass processing
total = sum(x**2 for x in huge_dataset)
```

### Memory Comparison:
```python
import sys

# List comprehension
list_comp = [x for x in range(1000)]
print(sys.getsizeof(list_comp))  # ~9024 bytes

# Generator expression
gen_expr = (x for x in range(1000))
print(sys.getsizeof(gen_expr))   # ~128 bytes (much smaller!)

# But generator values computed each time accessed
# List values stored and reusable
```

---

## COMMON MISTAKES & SOLUTIONS

### Mistake 1: Generator Exhaustion
```python
# ❌ Wrong - generator can only be used once
gen = (x for x in range(5))
list1 = list(gen)  # [0, 1, 2, 3, 4]
list2 = list(gen)  # [] - empty! Generator exhausted

# ✅ Correct - use list comprehension if need multiple uses
lst = [x for x in range(5)]
list1 = list(lst)  # [0, 1, 2, 3, 4]
list2 = list(lst)  # [0, 1, 2, 3, 4]
```

### Mistake 2: {} Creates Dict, Not Set
```python
# ❌ Wrong - empty {} is a dict!
empty = {}
print(type(empty))  # <class 'dict'>

# ✅ Correct - use set() for empty set
empty = set()
print(type(empty))  # <class 'set'>

# Set comprehension works for non-empty
non_empty = {x for x in range(5)}  # {0, 1, 2, 3, 4}
```

### Mistake 3: Filter vs Conditional Expression
```python
numbers = [1, 2, 3, 4, 5]

# Filter (if at end) - removes elements
evens_only = [x for x in numbers if x % 2 == 0]
# → [2, 4]

# Conditional expression (if...else in middle) - transforms elements
even_or_zero = [x if x % 2 == 0 else 0 for x in numbers]
# → [0, 2, 0, 4, 0]

# ❌ Wrong - can't use if without else in expression position
# wrong = [x if x % 2 == 0 for x in numbers]  # SyntaxError
```

### Mistake 4: Nested Loop Order
```python
# Order matters in nested comprehensions!
matrix = [[1, 2], [3, 4], [5, 6]]

# ✅ Correct - reads naturally left to right
flat = [num for row in matrix for num in row]
# → [1, 2, 3, 4, 5, 6]

# Equivalent to:
flat = []
for row in matrix:      # First loop
    for num in row:     # Second loop
        flat.append(num)
```

### Mistake 5: Modifying While Iterating
```python
# ❌ Wrong - don't modify list being iterated
numbers = [1, 2, 3, 4, 5]
# for x in numbers:
#     if x % 2 == 0:
#         numbers.remove(x)  # Dangerous!

# ✅ Correct - create new list with comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [x for x in numbers if x % 2 != 0]
# → [1, 3, 5]
```

---

## SUMMARY - KEY TAKEAWAYS

1. **List Comprehension []**: Ordered, allows duplicates, creates full list
2. **Set Comprehension {}**: Unordered, unique values, creates full set
3. **Dict Comprehension {k:v}**: Key-value pairs, unique keys
4. **Generator Expression ()**: Lazy evaluation, memory efficient, single-use

5. **Syntax patterns**:
   - Transform: `[expr for x in iter]`
   - Filter: `[x for x in iter if cond]`
   - Both: `[expr for x in iter if cond]`
   - Conditional: `[x if cond else y for x in iter]`
   - Nested: `[x for outer in iter1 for x in outer]`

6. **Use generators** for large datasets or single-pass processing
7. **Use list/set/dict comprehensions** for reusable collections
8. **Remember**: Filter uses `if` at end, ternary uses `if...else` in expression
9. **Comprehensions are Pythonic** - preferred over manual loops when appropriate
10. **Keep comprehensions readable** - use regular loops if comprehension becomes too complex

