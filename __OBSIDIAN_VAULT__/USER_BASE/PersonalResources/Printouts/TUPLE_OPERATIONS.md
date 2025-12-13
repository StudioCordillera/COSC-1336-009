# TUPLE OPERATIONS - COMPREHENSIVE REFERENCE

## QUICK REFERENCE - TUPLE OPERATIONS

```python
# ═══════════════════════════════════════════════════════════════════════════
# TUPLE CREATION
# ═══════════════════════════════════════════════════════════════════════════
()                           # Empty | Create empty tuple | Returns ()
(item,)                      # Single item | Create 1-element tuple | Returns (item,)
(1, 2, 3)                    # Multiple items | Create tuple | Returns (1, 2, 3)
tuple()                      # Empty | Create empty tuple | Returns ()
tuple(iterable)              # Iterable | Convert to tuple | Returns tuple
1, 2, 3                      # Multiple items | Tuple packing | Returns (1, 2, 3)

# ═══════════════════════════════════════════════════════════════════════════
# TUPLE METHODS (Only 2!)
# ═══════════════════════════════════════════════════════════════════════════
t.count(value)               # Tuple + value | Count occurrences | Returns int
t.index(value)               # Tuple + value | Find first index | Returns int
t.index(value, start)        # Tuple + value + start | Find from position | Returns int
t.index(value, start, end)   # Tuple + value + range | Find in slice | Returns int

# ═══════════════════════════════════════════════════════════════════════════
# TUPLE ACCESS & SLICING
# ═══════════════════════════════════════════════════════════════════════════
t[i]                         # Tuple + index | Get element | Returns element
t[-1]                        # Tuple | Get last element | Returns element
t[start:end]                 # Tuple + range | Slice tuple | Returns new tuple
t[start:end:step]            # Tuple + range + step | Slice with step | Returns new tuple
t[::-1]                      # Tuple | Reverse tuple | Returns reversed tuple
len(t)                       # Tuple | Get length | Returns int
min(t)                       # Tuple | Get minimum | Returns min value
max(t)                       # Tuple | Get maximum | Returns max value
sum(t)                       # Tuple of numbers | Get sum | Returns sum

# ═══════════════════════════════════════════════════════════════════════════
# TUPLE UNPACKING
# ═══════════════════════════════════════════════════════════════════════════
a, b = (1, 2)                # Tuple | Unpack to variables | Assigns a=1, b=2
a, b, c = (1, 2, 3)          # Tuple | Unpack 3 values | Assigns a=1, b=2, c=3
a, *rest = (1, 2, 3, 4)      # Tuple | Unpack with rest | Assigns a=1, rest=[2,3,4]
*first, last = (1, 2, 3, 4)  # Tuple | Unpack head/tail | Assigns first=[1,2,3], last=4
a, *mid, z = (1, 2, 3, 4, 5) # Tuple | Unpack edges/middle | Assigns a=1, mid=[2,3,4], z=5
x, y = y, x                  # Tuples | Swap variables | Swaps values
	
# ═══════════════════════════════════════════════════════════════════════════
# TUPLE OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
t1 + t2                      # Two tuples | Concatenate | Returns new tuple
t * n                        # Tuple + int | Repeat tuple | Returns new tuple
item in t                    # Item + tuple | Check membership | Returns bool
item not in t                # Item + tuple | Check non-membership | Returns bool
for item in t:               # Tuple | Iterate elements | Yields each element
enumerate(t)                 # Tuple | Get (index, value) pairs | Returns iterator
enumerate(t, start=1)        # Tuple + start | Custom index start | Returns iterator

# ═══════════════════════════════════════════════════════════════════════════
# TUPLE COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
t1 == t2                     # Two tuples | Check equality | Returns bool
t1 != t2                     # Two tuples | Check inequality | Returns bool
t1 < t2                      # Two tuples | Lexicographic less than | Returns bool
t1 <= t2                     # Two tuples | Lexicographic less/equal | Returns bool
t1 > t2                      # Two tuples | Lexicographic greater than | Returns bool
t1 >= t2                     # Two tuples | Lexicographic greater/equal | Returns bool

# ═══════════════════════════════════════════════════════════════════════════
# NAMED TUPLES (from collections import namedtuple)
# ═══════════════════════════════════════════════════════════════════════════
namedtuple(name, fields)     # Name + fields | Create named tuple class | Returns class
Point = namedtuple('Point', ['x', 'y'])  # Create Point class
p = Point(1, 2)              # Create instance | p.x=1, p.y=2
p.x, p.y                     # Access by name | Returns values
p[0], p[1]                   # Access by index | Returns values
p._asdict()                  # Named tuple | Convert to dict | Returns OrderedDict
p._replace(x=10)             # Named tuple + kwargs | Create modified copy | Returns new tuple
p._fields                    # Named tuple | Get field names | Returns tuple of strings

# ═══════════════════════════════════════════════════════════════════════════
# TUPLE COMPREHENSIONS (Returns generator, convert with tuple())
# ═══════════════════════════════════════════════════════════════════════════
tuple(x for x in range(5))   # Generator → tuple | Create from expression | Returns tuple
tuple(x**2 for x in range(5)) # Generator → tuple | Squared values | Returns tuple
tuple(x for x in lst if x>0) # Filtered generator | Positive values only | Returns tuple
```

---

## TUPLE IMMUTABILITY - KEY CONCEPT

**Tuples are IMMUTABLE** - once created, they cannot be modified.

### What You CANNOT Do:
```python
t = (1, 2, 3)
t[0] = 10        # ❌ TypeError: 'tuple' object does not support item assignment
t.append(4)      # ❌ AttributeError: 'tuple' object has no attribute 'append'
t.remove(1)      # ❌ AttributeError: 'tuple' object has no attribute 'remove'
del t[0]         # ❌ TypeError: 'tuple' object doesn't support item deletion
```

### What You CAN Do:
```python
# Create NEW tuples from existing ones
t = (1, 2, 3)
t = t + (4, 5)           # Concatenation creates new tuple → (1, 2, 3, 4, 5)
t = (0,) + t             # Add to front → (0, 1, 2, 3, 4, 5)
t = t * 2                # Repetition → (0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5)

# Slice to get new tuples
first_three = t[:3]      # → (0, 1, 2)
last_two = t[-2:]        # → (4, 5)
reversed_t = t[::-1]     # → (5, 4, 3, 2, 1, 0)
```

### Tuple vs List Comparison:
| Feature | Tuple | List |
|---------|-------|------|
| **Mutability** | Immutable (cannot change) | Mutable (can change) |
| **Syntax** | `(1, 2, 3)` | `[1, 2, 3]` |
| **Methods** | Only 2: `count()`, `index()` | 11 methods: `append()`, `extend()`, etc. |
| **Performance** | Faster (less memory) | Slower (more memory) |
| **Use Case** | Fixed data, function returns, dict keys | Dynamic data, needs modification |
| **Hash** | Hashable (can be dict key) | Not hashable |

---

## TUPLE CREATION PATTERNS

### Basic Creation:
```python
# Empty tuple
empty = ()
empty = tuple()

# Single element tuple (COMMA REQUIRED!)
single = (1,)        # ✅ Correct - tuple with one element
wrong = (1)          # ❌ Wrong - this is just int 1, not a tuple

# Multiple elements
coords = (10, 20)
rgb = (255, 128, 0)
point3d = (1.5, 2.7, 3.2)

# Without parentheses (tuple packing)
values = 1, 2, 3     # Same as (1, 2, 3)
x = 10, 20, 30       # Same as (10, 20, 30)
```

### Converting to Tuple:
```python
# From list
lst = [1, 2, 3, 4, 5]
t = tuple(lst)                    # → (1, 2, 3, 4, 5)

# From string
chars = tuple("hello")            # → ('h', 'e', 'l', 'l', 'o')

# From range
numbers = tuple(range(5))         # → (0, 1, 2, 3, 4)

# From dictionary (gets keys)
d = {'a': 1, 'b': 2, 'c': 3}
keys = tuple(d)                   # → ('a', 'b', 'c')
values = tuple(d.values())        # → (1, 2, 3)
items = tuple(d.items())          # → (('a', 1), ('b', 2), ('c', 3))

# From set
s = {3, 1, 4, 1, 5}
t = tuple(s)                      # → (1, 3, 4, 5) - sorted, no duplicates
```

---

## TUPLE METHODS (Only 2!)

### 1. count() - Count Occurrences
```python
t = (1, 2, 2, 3, 2, 4, 2)

# Count specific value
count_2 = t.count(2)              # → 4
count_3 = t.count(3)              # → 1
count_5 = t.count(5)              # → 0 (not found)

# Count with different types
mixed = (1, 'a', 2, 'a', 3, 'a')
print(mixed.count('a'))           # → 3
print(mixed.count(1))             # → 1
```

**Use Cases:**
- Frequency counting
- Checking duplicates
- Data validation

### 2. index() - Find First Index
```python
t = (10, 20, 30, 20, 40, 20)

# Basic index finding
pos = t.index(20)                 # → 1 (first occurrence)
pos = t.index(40)                 # → 4

# Search in range
pos = t.index(20, 2)              # → 3 (start from index 2)
pos = t.index(20, 4, 6)           # → 5 (search between 4 and 6)

# Not found raises ValueError
try:
    pos = t.index(99)
except ValueError:
    print("Value not found")      # → "Value not found"

# Safe index finding
value = 50
if value in t:
    pos = t.index(value)
else:
    pos = -1                      # Use -1 to indicate not found
```

---

## TUPLE ACCESS & SLICING

### Index Access:
```python
coordinates = (10, 20, 30, 40, 50)

# Positive indexing (from start)
first = coordinates[0]            # → 10
second = coordinates[1]           # → 20
third = coordinates[2]            # → 30

# Negative indexing (from end)
last = coordinates[-1]            # → 50
second_last = coordinates[-2]     # → 40
third_last = coordinates[-3]      # → 30
```

### Slicing:
```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing [start:end]
slice1 = numbers[2:5]             # → (2, 3, 4)
slice2 = numbers[0:3]             # → (0, 1, 2)
slice3 = numbers[7:10]            # → (7, 8, 9)

# Omitting start or end
from_start = numbers[:4]          # → (0, 1, 2, 3)
to_end = numbers[6:]              # → (6, 7, 8, 9)
full_copy = numbers[:]            # → (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing with step [start:end:step]
evens = numbers[0:10:2]           # → (0, 2, 4, 6, 8)
odds = numbers[1:10:2]            # → (1, 3, 5, 7, 9)
every_third = numbers[::3]        # → (0, 3, 6, 9)

# Reverse slicing
reversed_all = numbers[::-1]      # → (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
reversed_part = numbers[7:2:-1]   # → (7, 6, 5, 4, 3)

# Negative indices in slicing
last_three = numbers[-3:]         # → (7, 8, 9)
all_but_last = numbers[:-1]       # → (0, 1, 2, 3, 4, 5, 6, 7, 8)
middle = numbers[3:-3]            # → (3, 4, 5, 6)
```

### Built-in Functions:
```python
values = (5, 2, 8, 1, 9, 3, 7)

# Length
length = len(values)              # → 7

# Min/Max
minimum = min(values)             # → 1
maximum = max(values)             # → 9

# Sum
total = sum(values)               # → 35
average = sum(values) / len(values)  # → 5.0

# Sorted (returns LIST, not tuple!)
sorted_list = sorted(values)      # → [1, 2, 3, 5, 7, 8, 9] (list!)
sorted_tuple = tuple(sorted(values))  # → (1, 2, 3, 5, 7, 8, 9) (tuple)
reverse_sorted = tuple(sorted(values, reverse=True))  # → (9, 8, 7, 5, 3, 2, 1)

# Any/All
has_positive = any(x > 0 for x in values)    # → True
all_positive = all(x > 0 for x in values)    # → True
has_negative = any(x < 0 for x in values)    # → False
```

---

## TUPLE UNPACKING - POWERFUL FEATURE

### Basic Unpacking:
```python
# Simple unpacking
point = (10, 20)
x, y = point                      # x=10, y=20

# Multiple values
rgb = (255, 128, 0)
red, green, blue = rgb            # red=255, green=128, blue=0

# From function return
def get_user():
    return "Alice", 25, "Engineer"

name, age, job = get_user()       # name="Alice", age=25, job="Engineer"

# Swapping variables (VERY USEFUL!)
a = 5
b = 10
a, b = b, a                       # Now a=10, b=5 (swapped!)
```

### Extended Unpacking with * (Python 3+):
```python
# Unpack first, collect rest
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers            # first=1, rest=[2, 3, 4, 5]

# Unpack last, collect beginning
*beginning, last = numbers        # beginning=[1, 2, 3, 4], last=5

# Unpack first and last, collect middle
first, *middle, last = numbers    # first=1, middle=[2, 3, 4], last=5

# Multiple collection points
a, b, *mid, y, z = (1, 2, 3, 4, 5, 6, 7)  # a=1, b=2, mid=[3,4,5], y=6, z=7

# Ignoring values with underscore
x, _, z = (1, 2, 3)               # x=1, z=3 (ignore middle value)
first, *_, last = (1, 2, 3, 4, 5) # first=1, last=5 (ignore middle values)
```

### Unpacking in Loops:
```python
# List of tuples
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

for name, score in students:
    print(f"{name}: {score}")
# Output:
# Alice: 85
# Bob: 92
# Charlie: 78

# Dictionary items
grades = {'Math': 95, 'English': 88, 'Science': 91}
for subject, grade in grades.items():
    print(f"{subject}: {grade}")

# Enumerate with unpacking
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(f"{index}: {color}")
# Output:
# 0: red
# 1: green
# 2: blue

# Nested tuple unpacking
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"Point({x}, {y})")
```

---

## TUPLE OPERATIONS

### Concatenation (+):
```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

combined = t1 + t2                # → (1, 2, 3, 4, 5, 6)

# Add single element (remember comma!)
t = (1, 2, 3)
t = t + (4,)                      # → (1, 2, 3, 4)

# Add to beginning
t = (0,) + t                      # → (0, 1, 2, 3, 4)

# Chain multiple tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)
all_together = t1 + t2 + t3       # → (1, 2, 3, 4, 5, 6)
```

### Repetition (*):
```python
t = (1, 2, 3)

doubled = t * 2                   # → (1, 2, 3, 1, 2, 3)
tripled = t * 3                   # → (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Create tuple with repeated value
zeros = (0,) * 5                  # → (0, 0, 0, 0, 0)
stars = ('*',) * 10               # → ('*', '*', '*', '*', '*', '*', '*', '*', '*', '*')

# Initialize tuple
empty_slots = (None,) * 3         # → (None, None, None)
```

### Membership Testing:
```python
fruits = ('apple', 'banana', 'cherry', 'date')

# Check if exists
has_apple = 'apple' in fruits     # → True
has_grape = 'grape' in fruits     # → False

# Check if doesn't exist
no_grape = 'grape' not in fruits  # → True

# Use in conditions
fruit = 'banana'
if fruit in fruits:
    print(f"{fruit} found!")      # → "banana found!"

# Count membership in list of tuples
points = [(1, 2), (3, 4), (5, 6)]
if (3, 4) in points:
    print("Point found!")         # → "Point found!"
```

### Iteration:
```python
colors = ('red', 'green', 'blue', 'yellow')

# Simple iteration
for color in colors:
    print(color)
# Output: red, green, blue, yellow

# With enumerate (get index)
for i, color in enumerate(colors):
    print(f"{i}: {color}")
# Output:
# 0: red
# 1: green
# 2: blue
# 3: yellow

# With enumerate (custom start)
for num, color in enumerate(colors, start=1):
    print(f"{num}. {color}")
# Output:
# 1. red
# 2. green
# 3. blue
# 4. yellow

# Iterate with index manually
for i in range(len(colors)):
    print(f"colors[{i}] = {colors[i]}")
```

---

## TUPLE COMPARISON

### Equality:
```python
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)

print(t1 == t2)                   # → True (same values)
print(t1 == t3)                   # → False (different values)
print(t1 != t3)                   # → True (not equal)

# Order matters
t4 = (3, 2, 1)
print(t1 == t4)                   # → False (different order)
```

### Lexicographic Comparison:
```python
# Compares element by element, left to right
t1 = (1, 2, 3)
t2 = (1, 2, 4)
t3 = (1, 3, 1)

print(t1 < t2)                    # → True (3 < 4 at position 2)
print(t1 < t3)                    # → True (2 < 3 at position 1)
print(t2 > t1)                    # → True

# Different lengths
short = (1, 2)
long = (1, 2, 3)
print(short < long)               # → True (shorter is less if prefix matches)

# String comparison
words1 = ('apple', 'banana')
words2 = ('apple', 'cherry')
print(words1 < words2)            # → True ('banana' < 'cherry')
```

### Sorting Tuples:
```python
# List of tuples - sort by first element
points = [(3, 2), (1, 5), (2, 1)]
sorted_points = sorted(points)    # → [(1, 5), (2, 1), (3, 2)]

# Sort by second element
sorted_by_y = sorted(points, key=lambda p: p[1])  # → [(2, 1), (3, 2), (1, 5)]

# Student records - sort by grade
students = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 78)
]
by_grade = sorted(students, key=lambda s: s[1], reverse=True)
# → [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Sort by multiple criteria
data = [
    ('Math', 'Alice', 85),
    ('Math', 'Bob', 92),
    ('English', 'Alice', 88),
    ('English', 'Bob', 85)
]
# Sort by subject, then by grade
sorted_data = sorted(data, key=lambda x: (x[0], x[2]))
```

---

## NAMED TUPLES - Enhanced Tuples

Named tuples provide field names and are more readable than regular tuples.

```python
from collections import namedtuple

# Define a named tuple class
Point = namedtuple('Point', ['x', 'y'])
Student = namedtuple('Student', ['name', 'age', 'major', 'gpa'])

# Create instances
p1 = Point(10, 20)
p2 = Point(x=5, y=15)

student = Student('Alice', 20, 'Computer Science', 3.8)

# Access by name (readable!)
print(p1.x)                       # → 10
print(p1.y)                       # → 20
print(student.name)               # → 'Alice'
print(student.gpa)                # → 3.8

# Access by index (still works)
print(p1[0])                      # → 10
print(student[2])                 # → 'Computer Science'

# Unpack like regular tuple
x, y = p1
name, age, major, gpa = student

# Get field names
print(Point._fields)              # → ('x', 'y')
print(Student._fields)            # → ('name', 'age', 'major', 'gpa')

# Convert to dictionary
print(p1._asdict())               # → {'x': 10, 'y': 20}
print(student._asdict())          # → {'name': 'Alice', 'age': 20, ...}

# Create modified copy
p3 = p1._replace(x=30)            # → Point(x=30, y=20)
student2 = student._replace(gpa=3.9)  # → New student with gpa=3.9
```

### Practical Named Tuple Examples:
```python
from collections import namedtuple

# Employee record system
Employee = namedtuple('Employee', ['id', 'name', 'department', 'salary'])

employees = [
    Employee(101, 'Alice', 'Engineering', 85000),
    Employee(102, 'Bob', 'Sales', 65000),
    Employee(103, 'Charlie', 'Engineering', 90000)
]

# Process employees
for emp in employees:
    print(f"{emp.name} ({emp.department}): ${emp.salary:,}")

# Filter engineers
engineers = [e for e in employees if e.department == 'Engineering']

# RGB color system
Color = namedtuple('Color', ['red', 'green', 'blue'])

white = Color(255, 255, 255)
black = Color(0, 0, 0)
red = Color(255, 0, 0)

def lighten(color, amount=20):
    return Color(
        min(255, color.red + amount),
        min(255, color.green + amount),
        min(255, color.blue + amount)
    )

# Coordinate system
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])

locations = {
    'New York': Coordinate(40.7128, -74.0060),
    'London': Coordinate(51.5074, -0.1278),
    'Tokyo': Coordinate(35.6762, 139.6503)
}

for city, coord in locations.items():
    print(f"{city}: {coord.latitude}°N, {coord.longitude}°E")
```

---

## WHEN TO USE TUPLES VS LISTS

### Use TUPLES when:
1. **Data should not change** (immutable)
   ```python
   RGB_RED = (255, 0, 0)        # Color constants
   ORIGIN = (0, 0)              # Fixed coordinate
   ```

2. **Returning multiple values from function**
   ```python
   def get_stats(numbers):
       return min(numbers), max(numbers), sum(numbers)
   
   min_val, max_val, total = get_stats([1, 2, 3, 4, 5])
   ```

3. **Dictionary keys** (must be hashable)
   ```python
   # Tuples can be dict keys, lists cannot
   grid = {
       (0, 0): 'empty',
       (0, 1): 'wall',
       (1, 0): 'player'
   }
   ```

4. **Unpacking/Multiple assignment**
   ```python
   name, age, city = ("Alice", 25, "NYC")
   x, y = (10, 20)
   ```

5. **Performance matters** (tuples are faster)
   ```python
   # Large datasets where modification not needed
   coordinates = tuple(range(1000000))
   ```

### Use LISTS when:
1. **Data needs to change**
   ```python
   scores = [85, 90, 78]
   scores.append(92)            # Need to modify
   ```

2. **Need list methods**
   ```python
   items = ['a', 'b', 'c']
   items.insert(1, 'x')         # Need insert, append, remove, etc.
   ```

3. **Dynamic collection**
   ```python
   results = []
   for i in range(10):
       results.append(i * 2)    # Building collection over time
   ```

---

## TUPLE COMPREHENSIONS (Generator → Tuple)

**Note:** `(x for x in ...)` creates a GENERATOR, not a tuple. Use `tuple()` to convert.

```python
# WRONG - This is a generator, not tuple!
wrong = (x for x in range(5))    # <generator object>

# CORRECT - Convert generator to tuple
correct = tuple(x for x in range(5))  # → (0, 1, 2, 3, 4)

# Examples
squares = tuple(x**2 for x in range(10))  # → (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
evens = tuple(x for x in range(20) if x % 2 == 0)  # → (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
upper_words = tuple(w.upper() for w in ['hello', 'world'])  # → ('HELLO', 'WORLD')

# From existing sequence
numbers = [1, 2, 3, 4, 5]
doubled = tuple(n * 2 for n in numbers)  # → (2, 4, 6, 8, 10)

# Nested comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = tuple(item for row in matrix for item in row)  # → (1, 2, 3, 4, 5, 6)

# With conditional
grades = [85, 92, 78, 90, 65, 88]
passing = tuple(g for g in grades if g >= 70)  # → (85, 92, 78, 90, 88)
```

---

## COMMON PROJECT PATTERNS

### Pattern 1: Function Returns Multiple Values
```python
def analyze_text(text):
    """Return multiple statistics about text"""
    word_count = len(text.split())
    char_count = len(text)
    line_count = text.count('\n') + 1
    
    return word_count, char_count, line_count  # Returns tuple

# Unpack results
words, chars, lines = analyze_text("Hello\nWorld")
print(f"Words: {words}, Chars: {chars}, Lines: {lines}")
```

### Pattern 2: Coordinate Systems
```python
# Game coordinates
player_pos = (100, 200)
enemy_pos = (150, 180)

def distance(p1, p2):
    """Calculate distance between two points"""
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

dist = distance(player_pos, enemy_pos)

# Move player
def move_player(position, dx, dy):
    x, y = position
    return (x + dx, y + dy)

new_pos = move_player(player_pos, 10, -5)  # → (110, 195)
```

### Pattern 3: Database Records
```python
# Student records as tuples
students = [
    (101, 'Alice', 'Computer Science', 3.8),
    (102, 'Bob', 'Mathematics', 3.6),
    (103, 'Charlie', 'Physics', 3.9)
]

# Search by ID
def find_student(student_id, students):
    for student in students:
        if student[0] == student_id:
            return student
    return None

# Filter by major
def get_major_students(major, students):
    return [s for s in students if s[2] == major]

cs_students = get_major_students('Computer Science', students)

# Sort by GPA
sorted_students = sorted(students, key=lambda s: s[3], reverse=True)
```

### Pattern 4: Configuration Data
```python
# RGB colors as tuples
COLORS = {
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0)
}

def apply_color(color_tuple):
    r, g, b = color_tuple
    return f"rgb({r}, {g}, {b})"

# Window dimensions
WINDOW_SIZE = (800, 600)
width, height = WINDOW_SIZE

# Application settings (immutable)
APP_CONFIG = (
    'MyApp',          # name
    '1.0.0',          # version
    True,             # debug_mode
    (800, 600),       # window_size
    60                # framerate
)

name, version, debug, size, fps = APP_CONFIG
```

### Pattern 5: Menu Options
```python
# Menu system with tuples
MENU_OPTIONS = [
    (1, 'View Records'),
    (2, 'Add Record'),
    (3, 'Delete Record'),
    (4, 'Search Records'),
    (5, 'Exit')
]

def display_menu():
    print("\n=== MAIN MENU ===")
    for num, option in MENU_OPTIONS:
        print(f"{num}. {option}")

def get_menu_choice():
    display_menu()
    while True:
        try:
            choice = int(input("\nEnter choice: "))
            if 1 <= choice <= len(MENU_OPTIONS):
                return choice
            print("Invalid choice!")
        except ValueError:
            print("Enter a number!")
```

### Pattern 6: Data Validation
```python
# Valid range as tuple
VALID_AGE_RANGE = (0, 120)
VALID_GRADE_RANGE = (0.0, 4.0)
VALID_SCORE_RANGE = (0, 100)

def validate_value(value, valid_range):
    min_val, max_val = valid_range
    return min_val <= value <= max_val

age = 25
if validate_value(age, VALID_AGE_RANGE):
    print("Valid age")

# Validation tuples with error messages
VALIDATIONS = [
    ('age', VALID_AGE_RANGE, 'Age must be between 0-120'),
    ('gpa', VALID_GRADE_RANGE, 'GPA must be between 0.0-4.0'),
    ('score', VALID_SCORE_RANGE, 'Score must be between 0-100')
]

def validate_data(data):
    for field, (min_val, max_val), error_msg in VALIDATIONS:
        if field in data:
            if not (min_val <= data[field] <= max_val):
                return False, error_msg
    return True, "Valid"
```

---

## SUMMARY - KEY TAKEAWAYS

1. **Tuples are IMMUTABLE** - cannot be changed after creation
2. **Only 2 methods**: `count()` and `index()`
3. **Tuple unpacking** is extremely powerful for clean code
4. **Use tuples for**:
   - Fixed data (coordinates, RGB colors, configs)
   - Function returns (multiple values)
   - Dictionary keys (hashable)
   - Performance (faster than lists)
5. **Named tuples** add readability with field names
6. **Tuple comprehensions** don't exist - use `tuple(generator)`
7. **Single-element tuples** require comma: `(1,)` not `(1)`
8. **Tuples can be concatenated** (+) and repeated (*) to create new tuples

