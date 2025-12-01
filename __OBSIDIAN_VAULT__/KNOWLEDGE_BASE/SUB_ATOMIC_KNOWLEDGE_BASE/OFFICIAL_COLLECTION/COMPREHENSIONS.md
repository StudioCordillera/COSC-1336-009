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

