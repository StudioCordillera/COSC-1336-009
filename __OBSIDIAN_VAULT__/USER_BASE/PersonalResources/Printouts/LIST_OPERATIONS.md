			# LIST_OPERATIONS

## Core Definition
**Lists** are mutable, ordered sequences that can contain any type of elements. Support indexing, slicing, and modification.

**Tags**: #list #sequence #mutable #indexing #slicing #iteration

---

## COMPLETE LIST METHODS QUICK REFERENCE

### LIST METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# ACCESS METHODS
# ═══════════════════════════════════════════════════════════════════════════
list[index]                  # List | Access item by position | Returns item or IndexError
list[start:end]              # List | Slice from start to end | Returns new list with subset
list[start:end:step]         # List | Slice with step | Returns new list with every nth item
list[start:]                 # List | Slice from start to end | Returns new list from start
list[:end]                   # List | Slice from beginning to end | Returns new list up to end
list[-1]                     # List | Access last item | Returns last item
list[-n]                     # List | Access nth from end | Returns nth item from end
list.index(item)             # List | Find first position of item | Returns index or ValueError
list.index(item, start)      # List | Find item from start pos | Returns index or ValueError
list.index(item, start, end) # List | Find item in range | Returns index or ValueError
list.count(item)             # List | Count occurrences | Returns int count

# ═══════════════════════════════════════════════════════════════════════════
# MODIFICATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
list.append(item)            # List | Add item to end | Modifies list, returns None
list.extend(iterable)        # List | Add all items from iterable | Modifies list, returns None
list.insert(index, item)     # List | Insert item at position | Modifies list, returns None
list.remove(item)            # List | Remove first occurrence | Modifies list or ValueError
list.pop()                   # List | Remove last item | Returns removed item
list.pop(index)              # List | Remove item at index | Returns removed item or IndexError
list.clear()                 # List | Remove all items | Empties list, returns None
list.reverse()               # List | Reverse items in place | Modifies list, returns None
list.sort()                  # List | Sort in place ascending | Modifies list, returns None
list.sort(reverse=True)      # List | Sort in place descending | Modifies list, returns None
list.sort(key=func)          # List | Sort by custom function | Modifies list, returns None
list.copy()                  # List | Shallow copy | Returns new list (same object refs)
del list[index]              # List | Delete item at index | Deletes item, no return
del list[start:end]          # List | Delete slice | Deletes slice, no return
list[index] = value          # List | Replace item at index | Modifies list, returns None
list[start:end] = iterable   # List | Replace slice | Modifies list, returns None
list += other_list           # List | Extend with + operator | Modifies list, returns None
list *= n                    # List | Repeat list n times | Modifies list, returns None

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY METHODS
# ═══════════════════════════════════════════════════════════════════════════
len(list)                    # List | Count items | Returns int count
item in list                 # List | Check membership | Returns True/False
item not in list             # List | Check absence | Returns True/False
min(list)                    # List | Find minimum | Returns smallest item
max(list)                    # List | Find maximum | Returns largest item
sum(list)                    # List of numbers | Sum all items | Returns total sum
all(list)                    # List | Check all truthy | Returns True if all items truthy
any(list)                    # List | Check any truthy | Returns True if any item truthy
sorted(list)                 # List | Sort copy ascending | Returns new sorted list
sorted(list, reverse=True)   # List | Sort copy descending | Returns new sorted list
sorted(list, key=func)       # List | Sort copy by function | Returns new sorted list
reversed(list)               # List | Reverse iterator | Returns reverse iterator
type(list)                   # Any object | Check object type | Returns <class 'list'>
bool(list)                   # List | Check if empty | Returns False if empty, else True
str(list)                    # List | Convert to string | Returns string representation
list(iterable)               # Iterable | Convert to list | Returns new list from iterable
tuple(list)                  # List | Convert to tuple | Returns tuple with same items
set(list)                    # List | Convert to set | Returns set (removes duplicates)

# ═══════════════════════════════════════════════════════════════════════════
# ITERATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
for item in list:            # List | Iterate items | Yields each item
enumerate(list)              # List | Index + iterate | Yields (index, item) tuples
enumerate(list, start=1)     # List | Index from start + iterate | Yields (index, item) from start
zip(list1, list2)            # Multiple lists | Pair items together | Yields tuples of paired items
zip(*lists)                  # List of lists | Unzip/transpose | Yields tuples unpacked
reversed(list)               # List | Reverse iteration | Yields items in reverse order
iter(list)                   # List | Create iterator | Returns iterator object
next(iter(list))             # List iterator | Get next item | Returns next item or StopIteration
filter(func, list)           # List + function | Filter by condition | Returns iterator of matches
map(func, list)              # List + function | Apply function to all | Returns iterator of results
range(len(list))             # List | Index range | Returns range object for indices

# ═══════════════════════════════════════════════════════════════════════════
# COMPREHENSION PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
[expr for item in list]      # List | Transform items | Returns new list with transformed items
[item for item in list if cond] # List + condition | Filter items | Returns new list with filtered items
[expr for item in list if cond] # List + condition | Transform filtered | Returns new transformed/filtered list
[item for sublist in list for item in sublist] # Nested list | Flatten | Returns flattened list
[[item for item in sublist] for sublist in list] # Nested list | Nested comprehension | Returns list of lists
[expr if cond else other for item in list] # List + ternary | Conditional transform | Returns list with conditional values

# ═══════════════════════════════════════════════════════════════════════════
# LIST CREATION
# ═══════════════════════════════════════════════════════════════════════════
[]                           # Literal | Create empty | Returns empty list
[1, 2, 3]                    # Literal | Create with items | Returns list with items
list()                       # Constructor | Create empty | Returns empty list
list(iterable)               # Constructor | Create from iterable | Returns list from iterable
list(range(n))               # Constructor + range | Create sequence | Returns list [0, 1, ..., n-1]
list('string')               # Constructor + string | Split into chars | Returns list of characters
[item] * n                   # Repetition | Repeat item n times | Returns list with item repeated
[0] * n                      # Repetition | Create n zeros | Returns list of n zeros
list1 + list2                # Concatenation | Combine lists | Returns new combined list
[*list1, *list2]             # Unpacking | Merge with unpacking | Returns new merged list

# ═══════════════════════════════════════════════════════════════════════════
# SLICING PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
list[:]                      # List | Full copy | Returns new list with all items
list[::-1]                   # List | Reverse copy | Returns new reversed list
list[::2]                    # List | Every other item | Returns new list with even indices
list[1::2]                   # List | Every other starting at 1 | Returns list with odd indices
list[:n]                     # List | First n items | Returns new list with first n items
list[-n:]                    # List | Last n items | Returns new list with last n items
list[n:-n]                   # List | Middle items | Returns list excluding first/last n

# ═══════════════════════════════════════════════════════════════════════════
# UNPACKING PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
a, b, c = list               # List with 3 items | Unpack to variables | Assigns items to variables
first, *rest = list          # List | Unpack first + rest | Assigns first item and remaining list
*start, last = list          # List | Unpack start + last | Assigns all but last and last item
first, *middle, last = list  # List | Unpack first, middle, last | Assigns first, middle list, last
_, b, _ = list               # List with 3 items | Unpack ignore some | Assigns only desired items

# ═══════════════════════════════════════════════════════════════════════════
# COMPARISON OPERATORS
# ═══════════════════════════════════════════════════════════════════════════
list1 == list2               # Two lists | Check equality | Returns True if same items in order
list1 != list2               # Two lists | Check inequality | Returns True if different
list1 < list2                # Two lists | Lexicographic less than | Returns True/False
list1 > list2                # Two lists | Lexicographic greater than | Returns True/False
list1 <= list2               # Two lists | Less than or equal | Returns True/False
list1 >= list2               # Two lists | Greater than or equal | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# NESTED LIST ACCESS
# ═══════════════════════════════════════════════════════════════════════════
list[i][j]                   # 2D list | Access nested item | Returns item at [i][j]
list[i][j][k]                # 3D list | Access deep nested | Returns item at [i][j][k]
```

### COMMON OPERATION EXAMPLES

```python
# Example list
numbers = [1, 2, 3, 4, 5]

# Access
numbers[0]                   # → 1
numbers[-1]                  # → 5
numbers[1:3]                 # → [2, 3]

# Modify
numbers.append(6)            # [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)         # [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)            # [0, 1, 2, 4, 5, 6]
numbers.pop()                # → 6, list is [0, 1, 2, 4, 5]

# Iterate
for n in numbers:            # Loop through items
    print(n)

for i, n in enumerate(numbers): # With index
    print(f"{i}: {n}")

# Comprehension
squares = [x**2 for x in numbers]  # → [0, 1, 4, 16, 25]
evens = [x for x in numbers if x % 2 == 0]  # → [0, 2, 4]

# Utility
len(numbers)                 # → 5
sum(numbers)                 # → 12
max(numbers)                 # → 5
```

---

## DETAILED SECTIONS

### SLICING IN DEPTH

```python
# Basic slicing syntax: list[start:end:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Standard slices
numbers[2:5]                 # [2, 3, 4] - items at index 2, 3, 4
numbers[:5]                  # [0, 1, 2, 3, 4] - first 5 items
numbers[5:]                  # [5, 6, 7, 8, 9] - from index 5 to end
numbers[:]                   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - full copy

# Step slicing
numbers[::2]                 # [0, 2, 4, 6, 8] - every 2nd item
numbers[1::2]                # [1, 3, 5, 7, 9] - every 2nd starting at 1
numbers[::3]                 # [0, 3, 6, 9] - every 3rd item

# Negative indices
numbers[-3:]                 # [7, 8, 9] - last 3 items
numbers[:-3]                 # [0, 1, 2, 3, 4, 5, 6] - all but last 3
numbers[-5:-2]               # [5, 6, 7] - slice using negative indices

# Reverse with slicing
numbers[::-1]                # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reversed
numbers[::-2]                # [9, 7, 5, 3, 1] - reverse every 2nd

# Slice assignment
numbers[2:5] = [20, 30, 40]  # Replace slice
numbers[2:5] = []            # Delete slice by assigning empty
numbers[2:2] = [99]          # Insert without replacing
```

### ITERATION PATTERNS

```python
fruits = ['apple', 'banana', 'cherry']

# Pattern 1: Simple iteration
for fruit in fruits:
    print(fruit)

# Pattern 2: Enumerate with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Pattern 3: Enumerate starting at 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry

# Pattern 4: Iterate with zip (parallel lists)
prices = [1.50, 0.75, 2.00]
for fruit, price in zip(fruits, prices):
    print(f"{fruit}: ${price}")
# apple: $1.50
# banana: $0.75
# cherry: $2.00

# Pattern 5: Iterate indices
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Pattern 6: Reversed iteration
for fruit in reversed(fruits):
    print(fruit)
# cherry
# banana
# apple

# Pattern 7: Filter with comprehension
long_fruits = [f for f in fruits if len(f) > 5]  # ['banana', 'cherry']

# Pattern 8: Map transformation
upper_fruits = [f.upper() for f in fruits]  # ['APPLE', 'BANANA', 'CHERRY']
```

### LIST COMPREHENSIONS IN DEPTH

```python
# Basic comprehension
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transform and filter
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# If-else in comprehension
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Nested comprehension (2D lists)
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]

# String operations in comprehension
words = ['hello', 'world']
upper_words = [w.upper() for w in words]
# ['HELLO', 'WORLD']

# Multiple conditions
filtered = [x for x in range(20) if x % 2 == 0 if x > 10]
# [12, 14, 16, 18]
```

### NESTED LISTS

```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access nested items
first_row = matrix[0]         # [1, 2, 3]
middle_item = matrix[1][1]    # 5
last_row_first = matrix[2][0] # 7

# Iterate 2D list
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()  # Newline after each row

# Enumerate 2D list
for i, row in enumerate(matrix):
    for j, item in enumerate(row):
        print(f"[{i}][{j}] = {item}")

# Comprehension on 2D list
all_items = [item for row in matrix for item in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create 2D list with comprehension
zeros = [[0 for _ in range(3)] for _ in range(3)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# List of dictionaries (common pattern)
students = [
    {'name': 'John', 'grade': 85},
    {'name': 'Alice', 'grade': 92},
    {'name': 'Bob', 'grade': 78}
]

for student in students:
    print(f"{student['name']}: {student['grade']}")

# Extract specific field
names = [s['name'] for s in students]
# ['John', 'Alice', 'Bob']
```

### UNPACKING PATTERNS

```python
# Basic unpacking
colors = ['red', 'green', 'blue']
r, g, b = colors  # r='red', g='green', b='blue'

# Extended unpacking with *
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers        # first=1, rest=[2,3,4,5]
*start, last = numbers        # start=[1,2,3,4], last=5
first, *middle, last = numbers  # first=1, middle=[2,3,4], last=5

# Ignore values with _
a, _, c = [1, 2, 3]           # a=1, c=3 (2 is ignored)
first, *_ = numbers           # first=1 (rest ignored)

# Unpacking in loops
pairs = [(1, 2), (3, 4), (5, 6)]
for a, b in pairs:
    print(f"{a} + {b} = {a + b}")

# Unpacking with enumerate
for i, (a, b) in enumerate(pairs):
    print(f"{i}: ({a}, {b})")
```

### SORTING AND ORDERING

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# In-place sort
numbers.sort()                # [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)    # [9, 6, 5, 4, 3, 2, 1, 1]

# Return new sorted list
original = [3, 1, 4]
sorted_copy = sorted(original)  # original unchanged
# sorted_copy = [1, 3, 4]

# Sort by key function
words = ['banana', 'pie', 'Washington', 'book']
words.sort(key=len)           # Sort by length
# ['pie', 'book', 'banana', 'Washington']

words.sort(key=str.lower)     # Case-insensitive sort
# ['banana', 'book', 'pie', 'Washington']

# Sort complex objects
students = [
    {'name': 'John', 'grade': 85},
    {'name': 'Alice', 'grade': 92},
    {'name': 'Bob', 'grade': 78}
]

students.sort(key=lambda s: s['grade'])  # Sort by grade
# [{'name': 'Bob', 'grade': 78}, {'name': 'John', 'grade': 85}, ...]

# Reverse list in place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()             # [5, 4, 3, 2, 1]

# Reverse with slicing (creates new list)
reversed_copy = numbers[::-1]
```

### COMMON PROJECT PATTERNS

```python
# Pattern 1: Collect multiple inputs
def get_student_list():
    """Collect list of student names"""
    students = []
    while True:
        name = input("Enter student name (or 'done'): ")
        if name.lower() == 'done':
            break
        students.append(name)
    return students

# Pattern 2: Menu validation
def get_menu_choice():
    """Get validated menu choice from list"""
    valid_choices = ['A', 'B', 'C', 'Q']
    while True:
        choice = input("Enter choice (A/B/C/Q): ").upper()
        if choice in valid_choices:
            return choice
        print("Invalid choice!")

# Pattern 3: Process list of numbers
def calculate_statistics(numbers):
    """Calculate stats from list of numbers"""
    if not numbers:
        return None
    
    stats = {
        'count': len(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }
    return stats

# Pattern 4: Read file into list
def read_file_to_list(filename):
    """Read file lines into list"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Remove newline characters
    lines = [line.strip() for line in lines]
    return lines

# Pattern 5: Filter and transform
def get_passing_students(grades):
    """Get list of students with grade >= 70"""
    passing = [
        {'name': s['name'], 'grade': s['grade']}
        for s in grades
        if s['grade'] >= 70
    ]
    return passing

# Pattern 6: Build frequency map
def count_occurrences(items):
    """Count how many times each item appears"""
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

# Pattern 7: Remove duplicates while preserving order
def remove_duplicates(items):
    """Remove duplicates keeping first occurrence"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### ERROR HANDLING

```python
# IndexError prevention
numbers = [1, 2, 3]

# WRONG: Can raise IndexError
try:
    value = numbers[10]  # IndexError!
except IndexError:
    value = None

# BETTER: Check length first
if 10 < len(numbers):
    value = numbers[10]
else:
    value = None

# ValueError with index()
# WRONG: Can raise ValueError
try:
    pos = numbers.index(5)  # ValueError if not found
except ValueError:
    pos = -1

# BETTER: Check membership first
if 5 in numbers:
    pos = numbers.index(5)
else:
    pos = -1

# Safe removal
# WRONG: Can raise ValueError
try:
    numbers.remove(5)  # ValueError if not in list
except ValueError:
    pass

# BETTER: Check before removing
if 5 in numbers:
    numbers.remove(5)

# Safe pop
# WRONG: Can raise IndexError
try:
    item = numbers.pop(10)  # IndexError if out of range
except IndexError:
    item = None

# BETTER: Use conditional
item = numbers.pop(10) if len(numbers) > 10 else None
```

### PERFORMANCE TIPS

```python
# Fast: List comprehension
squares = [x**2 for x in range(1000)]

# Slower: Loop with append
squares = []
for x in range(1000):
    squares.append(x**2)

# Fast: Check membership in set (O(1))
valid_set = set(['A', 'B', 'C'])
if choice in valid_set:  # Very fast
    pass

# Slower: Check membership in list (O(n))
valid_list = ['A', 'B', 'C']
if choice in valid_list:  # Slower for large lists
    pass

# Fast: Extend once
result = []
result.extend([1, 2, 3, 4, 5])

# Slower: Multiple appends
result = []
for i in [1, 2, 3, 4, 5]:
    result.append(i)

# Memory efficient: Generator for large data
# Instead of: [x**2 for x in range(1000000)]
# Use: (x**2 for x in range(1000000))
```

---

*Last Updated: November 30, 2025*
*Focus: Methods-first, iteration patterns, slicing, comprehensions, unpacking*