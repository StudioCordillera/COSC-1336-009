# SET OPERATIONS - COMPREHENSIVE REFERENCE

## QUICK REFERENCE - SET OPERATIONS

```python
# ═══════════════════════════════════════════════════════════════════════════
# SET CREATION
# ═══════════════════════════════════════════════════════════════════════════
{1, 2, 3}                    # Literals | Create set | Returns {1, 2, 3}
set()                        # Empty | Create empty set | Returns set()
set(iterable)                # Iterable | Convert to set | Returns set (removes duplicates)
{x for x in iterable}        # Comprehension | Create set from expression | Returns set

# ═══════════════════════════════════════════════════════════════════════════
# SET MODIFICATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
s.add(item)                  # Set + item | Add element | Returns None (modifies set)
s.remove(item)               # Set + item | Remove element (error if not found) | Returns None
s.discard(item)              # Set + item | Remove element (no error) | Returns None
s.pop()                      # Set | Remove arbitrary element | Returns removed element
s.clear()                    # Set | Remove all elements | Returns None (set becomes empty)
s.update(iterable)           # Set + iterable | Add multiple elements | Returns None
s |= other                   # Set + set | Union update (in-place) | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# SET MATHEMATICAL OPERATIONS (Return New Set)
# ═══════════════════════════════════════════════════════════════════════════
s.union(other)               # Two sets | Combine all elements | Returns new set
s | other                    # Two sets | Union operator | Returns new set
s.intersection(other)        # Two sets | Common elements only | Returns new set
s & other                    # Two sets | Intersection operator | Returns new set
s.difference(other)          # Two sets | Elements in s but not other | Returns new set
s - other                    # Two sets | Difference operator | Returns new set
s.symmetric_difference(other) # Two sets | Elements in either but not both | Returns new set
s ^ other                    # Two sets | Symmetric difference operator | Returns new set

# ═══════════════════════════════════════════════════════════════════════════
# SET COMPARISON METHODS
# ═══════════════════════════════════════════════════════════════════════════
s.issubset(other)            # Two sets | Check if s ⊆ other | Returns bool
s <= other                   # Two sets | Subset operator | Returns bool
s < other                    # Two sets | Proper subset operator | Returns bool
s.issuperset(other)          # Two sets | Check if s ⊇ other | Returns bool
s >= other                   # Two sets | Superset operator | Returns bool
s > other                    # Two sets | Proper superset operator | Returns bool
s.isdisjoint(other)          # Two sets | Check if no common elements | Returns bool

# ═══════════════════════════════════════════════════════════════════════════
# SET OPERATIONS & QUERIES
# ═══════════════════════════════════════════════════════════════════════════
len(s)                       # Set | Count elements | Returns int
item in s                    # Item + set | Check membership | Returns bool
item not in s                # Item + set | Check non-membership | Returns bool
for item in s:               # Set | Iterate elements | Yields each element (unordered)
min(s)                       # Set | Get minimum | Returns min element
max(s)                       # Set | Get maximum | Returns max element
sum(s)                       # Set of numbers | Get sum | Returns sum
sorted(s)                    # Set | Get sorted list | Returns list (sorted)
list(s)                      # Set | Convert to list | Returns list (unordered)
tuple(s)                     # Set | Convert to tuple | Returns tuple (unordered)

# ═══════════════════════════════════════════════════════════════════════════
# FROZENSET (Immutable Set)
# ═══════════════════════════════════════════════════════════════════════════
frozenset()                  # Empty | Create empty frozenset | Returns frozenset()
frozenset(iterable)          # Iterable | Create immutable set | Returns frozenset
# Frozensets support all query/mathematical operations but NO modification methods
# Frozensets are hashable and can be dict keys or set elements

# ═══════════════════════════════════════════════════════════════════════════
# SET COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════════════════
{x for x in range(10)}       # Generator | Create set from range | Returns set
{x**2 for x in range(10)}    # Generator | Squared values | Returns set
{x for x in lst if x > 0}    # Filtered generator | Positive values only | Returns set
{x.lower() for x in words}   # Generator | Transform elements | Returns set (lowercase)
```

---

## SET BASICS - KEY CONCEPTS

### What is a Set?
- **Unordered collection** - no indexing, no slicing
- **Unique elements** - automatically removes duplicates
- **Mutable** - can add/remove elements
- **Fast membership testing** - O(1) lookup time
- **Elements must be hashable** - immutable types only (int, str, tuple, frozenset)

### Cannot Store in Sets:
```python
# ❌ These CANNOT be set elements (unhashable):
s = {[1, 2, 3]}              # ❌ TypeError: list is unhashable
s = {{1, 2, 3}}              # ❌ TypeError: set is unhashable
s = {{'key': 'value'}}       # ❌ TypeError: dict is unhashable

# ✅ These CAN be set elements (hashable):
s = {1, 2, 3}                # ✅ Integers
s = {'apple', 'banana'}      # ✅ Strings
s = {(1, 2), (3, 4)}         # ✅ Tuples
s = {frozenset([1, 2])}      # ✅ Frozensets
s = {1, 'hello', (1, 2)}     # ✅ Mixed hashable types
```

---

## SET CREATION

### Basic Creation:
```python
# Using curly braces (literal)
s = {1, 2, 3, 4, 5}
colors = {'red', 'green', 'blue'}
mixed = {1, 'hello', 3.14, (1, 2)}

# Empty set (MUST use set(), NOT {})
empty = set()                # ✅ Correct - empty set
wrong = {}                   # ❌ This is empty DICT, not set!

# From iterable (removes duplicates automatically)
from_list = set([1, 2, 2, 3, 3, 3])      # → {1, 2, 3}
from_string = set("hello")                # → {'h', 'e', 'l', 'o'}
from_tuple = set((1, 2, 3, 2, 1))        # → {1, 2, 3}
from_range = set(range(5))                # → {0, 1, 2, 3, 4}
```

### Removing Duplicates:
```python
# Primary use case: remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unique = set(numbers)                     # → {1, 2, 3, 4, 5}
unique_list = list(set(numbers))          # → [1, 2, 3, 4, 5] as list

# String characters (removes duplicates)
text = "mississippi"
unique_chars = set(text)                  # → {'m', 'i', 's', 'p'}
sorted_unique = sorted(set(text))         # → ['i', 'm', 'p', 's']

# Case-insensitive unique words
words = ['Hello', 'world', 'HELLO', 'World']
unique_words = {w.lower() for w in words} # → {'hello', 'world'}
```

---

## SET MODIFICATION METHODS

### add() - Add Single Element:
```python
s = {1, 2, 3}

s.add(4)                     # → {1, 2, 3, 4}
s.add(2)                     # No effect (2 already exists) → {1, 2, 3, 4}
s.add(10)                    # → {1, 2, 3, 4, 10}

# Building set dynamically
numbers = set()
for i in range(1, 6):
    numbers.add(i * i)       # → {1, 4, 9, 16, 25}

# Add to set conditionally
scores = set()
for score in [85, 90, 85, 78, 90]:
    if score >= 80:
        scores.add(score)    # → {85, 90}
```

### remove() - Remove Element (Error if Not Found):
```python
s = {1, 2, 3, 4, 5}

s.remove(3)                  # → {1, 2, 4, 5}
s.remove(5)                  # → {1, 2, 4}

# Raises KeyError if not found
try:
    s.remove(99)             # ❌ KeyError: 99
except KeyError:
    print("Element not found")

# Safe removal pattern
if 2 in s:
    s.remove(2)              # Only remove if exists
```

### discard() - Remove Element (No Error):
```python
s = {1, 2, 3, 4, 5}

s.discard(3)                 # → {1, 2, 4, 5}
s.discard(99)                # No error, no effect → {1, 2, 4, 5}

# Preferred for safe removal
s.discard(2)                 # Remove if exists, ignore if doesn't
s.discard(100)               # Safe - no KeyError

# Batch discard
to_remove = [1, 2, 99, 100]
for item in to_remove:
    s.discard(item)          # Safely removes existing items
```

### pop() - Remove Arbitrary Element:
```python
s = {1, 2, 3, 4, 5}

item = s.pop()               # Removes and returns random element
print(f"Removed: {item}")    # e.g., "Removed: 1"
print(s)                     # → {2, 3, 4, 5} (item removed)

# Remove all elements one by one
s = {10, 20, 30}
while s:
    item = s.pop()
    print(f"Processing {item}")
# Eventually s becomes empty set()

# Error on empty set
empty = set()
try:
    empty.pop()              # ❌ KeyError: 'pop from an empty set'
except KeyError:
    print("Cannot pop from empty set")
```

### clear() - Remove All Elements:
```python
s = {1, 2, 3, 4, 5}

s.clear()                    # → set() (empty)
print(len(s))                # → 0

# Reset set
data = {10, 20, 30}
data.clear()
data.add(100)                # → {100}
```

### update() - Add Multiple Elements:
```python
s = {1, 2, 3}

# Add from list
s.update([4, 5, 6])          # → {1, 2, 3, 4, 5, 6}

# Add from multiple iterables
s.update([7, 8], [9, 10])    # → {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Add from string
s = {'a', 'b'}
s.update('cde')              # → {'a', 'b', 'c', 'd', 'e'}

# Union update operator |=
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1 |= s2                     # Same as s1.update(s2) → {1, 2, 3, 4, 5}
```

---

## SET MATHEMATICAL OPERATIONS

### union() - Combine Sets (|):
```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Method form
result = s1.union(s2)        # → {1, 2, 3, 4, 5}

# Operator form
result = s1 | s2             # → {1, 2, 3, 4, 5}

# Multiple sets
s3 = {5, 6, 7}
all_together = s1 | s2 | s3  # → {1, 2, 3, 4, 5, 6, 7}

# Practical: Combine student lists
class_a = {'Alice', 'Bob', 'Charlie'}
class_b = {'Bob', 'Diana', 'Eve'}
all_students = class_a | class_b  # → {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'}
```

### intersection() - Common Elements (&):
```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Method form
result = s1.intersection(s2) # → {3, 4}

# Operator form
result = s1 & s2             # → {3, 4}

# Multiple sets
s3 = {2, 3, 4, 5}
common = s1 & s2 & s3        # → {3, 4}

# Practical: Find common interests
alice_hobbies = {'reading', 'gaming', 'cooking'}
bob_hobbies = {'gaming', 'sports', 'cooking'}
shared = alice_hobbies & bob_hobbies  # → {'gaming', 'cooking'}
```

### difference() - Elements in First but Not Second (-):
```python
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

# Method form
result = s1.difference(s2)   # → {1, 2} (in s1, not in s2)

# Operator form
result = s1 - s2             # → {1, 2}

# Opposite direction
result = s2 - s1             # → {6, 7} (in s2, not in s1)

# Practical: Find missing items
required = {'flour', 'eggs', 'milk', 'butter'}
have = {'flour', 'milk', 'sugar'}
need_to_buy = required - have  # → {'eggs', 'butter'}
```

### symmetric_difference() - In Either but Not Both (^):
```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Method form
result = s1.symmetric_difference(s2)  # → {1, 2, 5, 6}

# Operator form
result = s1 ^ s2             # → {1, 2, 5, 6}

# Practical: Find differences between versions
v1_features = {'login', 'search', 'profile', 'chat'}
v2_features = {'login', 'search', 'settings', 'notifications'}
changed = v1_features ^ v2_features  # → {'profile', 'chat', 'settings', 'notifications'}
```

---

## SET COMPARISON METHODS

### issubset() - Check if Subset (≤):
```python
s1 = {1, 2}
s2 = {1, 2, 3, 4}

# Method form
print(s1.issubset(s2))       # → True (s1 ⊆ s2)

# Operator form
print(s1 <= s2)              # → True

# Proper subset (strict)
print(s1 < s2)               # → True (s1 ⊂ s2, s1 ≠ s2)

# Equal sets
s3 = {1, 2, 3}
s4 = {1, 2, 3}
print(s3 <= s4)              # → True (equal sets are subsets)
print(s3 < s4)               # → False (not proper subset)

# Practical: Check permissions
user_permissions = {'read', 'write'}
required_permissions = {'read', 'write', 'execute'}
has_required = user_permissions <= required_permissions  # → True
```

### issuperset() - Check if Superset (≥):
```python
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3}

# Method form
print(s1.issuperset(s2))     # → True (s1 ⊇ s2)

# Operator form
print(s1 >= s2)              # → True

# Proper superset (strict)
print(s1 > s2)               # → True (s1 ⊃ s2, s1 ≠ s2)

# Practical: Check if has all requirements
available_tools = {'hammer', 'saw', 'drill', 'wrench'}
needed_tools = {'hammer', 'drill'}
have_all = available_tools >= needed_tools  # → True
```

### isdisjoint() - Check if No Common Elements:
```python
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = {3, 4, 5}

print(s1.isdisjoint(s2))     # → True (no common elements)
print(s1.isdisjoint(s3))     # → False (3 is common)

# Practical: Check schedule conflicts
meeting1_days = {'Monday', 'Wednesday'}
meeting2_days = {'Tuesday', 'Thursday'}
meeting3_days = {'Monday', 'Friday'}

no_conflict_1_2 = meeting1_days.isdisjoint(meeting2_days)  # → True
no_conflict_1_3 = meeting1_days.isdisjoint(meeting3_days)  # → False
```

---

## SET COMPREHENSIONS

```python
# Basic comprehension
squares = {x**2 for x in range(10)}  # → {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With condition
evens = {x for x in range(20) if x % 2 == 0}  # → {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# Transform strings
words = ['Hello', 'WORLD', 'Python']
lowercase = {w.lower() for w in words}  # → {'hello', 'world', 'python'}

# From nested structure
matrix = [[1, 2], [3, 4], [1, 2]]
unique_vals = {num for row in matrix for num in row}  # → {1, 2, 3, 4}

# Filter and transform
numbers = [1, -2, 3, -4, 5, -6]
positive_squares = {x**2 for x in numbers if x > 0}  # → {1, 9, 25}

# Extract unique first letters
names = ['Alice', 'Bob', 'Charlie', 'Anna']
initials = {name[0] for name in names}  # → {'A', 'B', 'C'}

# Unique word lengths
text = "the quick brown fox jumps over the lazy dog"
word_lengths = {len(word) for word in text.split()}  # → {3, 4, 5}
```

---

## FROZENSET - Immutable Sets

### Creation and Basic Operations:
```python
# Create frozenset
fs = frozenset([1, 2, 3, 4])
fs2 = frozenset({3, 4, 5, 6})
empty_fs = frozenset()

# Cannot modify (immutable)
# fs.add(5)          # ❌ AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1)       # ❌ AttributeError: 'frozenset' object has no attribute 'remove'

# Can do all query operations
print(len(fs))               # → 4
print(2 in fs)               # → True
print(min(fs))               # → 1

# Can do all mathematical operations
union = fs | fs2             # → frozenset({1, 2, 3, 4, 5, 6})
intersection = fs & fs2      # → frozenset({3, 4})
difference = fs - fs2        # → frozenset({1, 2})
```

### Use Cases for Frozenset:

#### 1. Dictionary Keys (Sets Can't Be Dict Keys):
```python
# ❌ Regular sets cannot be dict keys
# counts = {{1, 2}: 'first'}  # TypeError

# ✅ Frozensets can be dict keys
counts = {
    frozenset([1, 2]): 'first',
    frozenset([3, 4]): 'second',
    frozenset([5, 6]): 'third'
}

key = frozenset([1, 2])
print(counts[key])           # → 'first'

# Practical: Store graph edges
graph = {
    frozenset(['A', 'B']): 5,  # Edge A-B with weight 5
    frozenset(['B', 'C']): 3,  # Edge B-C with weight 3
    frozenset(['A', 'C']): 7   # Edge A-C with weight 7
}
```

#### 2. Set of Sets:
```python
# ❌ Cannot have set of sets
# groups = {{1, 2}, {3, 4}}  # TypeError

# ✅ Can have set of frozensets
groups = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}

# Practical: Store unique combinations
student_pairs = {
    frozenset(['Alice', 'Bob']),
    frozenset(['Charlie', 'Diana']),
    frozenset(['Alice', 'Charlie'])
}

# Check if pair exists
pair = frozenset(['Alice', 'Bob'])
if pair in student_pairs:
    print("Pair exists")
```

#### 3. Constant/Immutable Collections:
```python
# Configuration that shouldn't change
VALID_COMMANDS = frozenset(['start', 'stop', 'restart', 'status'])
ADMIN_USERS = frozenset(['alice', 'bob'])
ALLOWED_EXTENSIONS = frozenset(['.txt', '.csv', '.json'])

def validate_command(cmd):
    return cmd in VALID_COMMANDS

def is_admin(user):
    return user in ADMIN_USERS
```

---

## COMMON PROJECT PATTERNS

### Pattern 1: Remove Duplicates from Data
```python
def get_unique_values(data_list):
    """Remove duplicates while preserving data type"""
    return list(set(data_list))

# Student IDs
ids = [101, 102, 101, 103, 102, 104]
unique_ids = get_unique_values(ids)  # → [101, 102, 103, 104]

# Email addresses
emails = ['a@test.com', 'b@test.com', 'a@test.com']
unique_emails = list(set(emails))    # → ['a@test.com', 'b@test.com']
```

### Pattern 2: Fast Membership Testing
```python
# Instead of searching list (slow)
valid_ids_list = [101, 102, 103, 104, 105]  # O(n) lookup

# Use set (fast)
valid_ids_set = {101, 102, 103, 104, 105}    # O(1) lookup

def is_valid_id(student_id):
    return student_id in valid_ids_set  # Much faster!

# Practical: Validate large dataset
allowed_users = set(['alice', 'bob', 'charlie', 'diana'])

for user in login_attempts:
    if user in allowed_users:  # O(1) - instant lookup
        grant_access(user)
```

### Pattern 3: Find Common Elements
```python
# Find students in both classes
class_a = {'Alice', 'Bob', 'Charlie', 'Diana'}
class_b = {'Bob', 'Diana', 'Eve', 'Frank'}

both_classes = class_a & class_b  # → {'Bob', 'Diana'}

# Find students in either class
all_students = class_a | class_b

# Find students only in class_a
only_a = class_a - class_b        # → {'Alice', 'Charlie'}
```

### Pattern 4: Track Unique Events/Visits
```python
visited_pages = set()

def record_visit(page_id):
    visited_pages.add(page_id)
    return len(visited_pages)  # Count unique visits

# Usage
record_visit('home')      # 1 unique page
record_visit('about')     # 2 unique pages
record_visit('home')      # Still 2 (duplicate ignored)
record_visit('contact')   # 3 unique pages

# Unique visitors
visitors = set()
for log_entry in server_logs:
    visitors.add(log_entry['user_id'])
print(f"Unique visitors: {len(visitors)}")
```

### Pattern 5: Permission/Access Control
```python
# User permissions
user_permissions = {'read', 'write'}
admin_permissions = {'read', 'write', 'delete', 'admin'}

# Check if user has permission
def has_permission(user_perms, required_perm):
    return required_perm in user_perms

# Check if has all required permissions
def has_all_permissions(user_perms, required_perms):
    return required_perms <= user_perms  # Subset check

# Grant permission
def grant_permission(user_perms, new_perm):
    user_perms.add(new_perm)

# Revoke permission
def revoke_permission(user_perms, perm):
    user_perms.discard(perm)

# Upgrade to admin
def make_admin(user_perms):
    user_perms.update(admin_permissions)
```

### Pattern 6: Data Validation - Check for Duplicates
```python
def has_duplicates(items):
    """Check if list contains duplicates"""
    return len(items) != len(set(items))

# Validate student IDs
student_ids = [101, 102, 103, 102, 104]
if has_duplicates(student_ids):
    print("Error: Duplicate student IDs found!")

# Find duplicate values
def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

dups = find_duplicates([1, 2, 2, 3, 3, 4])  # → {2, 3}
```

### Pattern 7: Category/Tag System
```python
# Article tags
article_tags = {
    'article1': {'python', 'programming', 'tutorial'},
    'article2': {'python', 'data-science', 'pandas'},
    'article3': {'javascript', 'web', 'tutorial'}
}

# Find articles with specific tag
def find_by_tag(tag):
    return [article for article, tags in article_tags.items() 
            if tag in tags]

python_articles = find_by_tag('python')  # → ['article1', 'article2']

# Find articles with multiple tags (AND)
def find_with_all_tags(required_tags):
    return [article for article, tags in article_tags.items()
            if required_tags <= tags]  # Subset check

tutorials = find_with_all_tags({'python', 'tutorial'})  # → ['article1']

# Find articles with any tag (OR)
def find_with_any_tag(search_tags):
    return [article for article, tags in article_tags.items()
            if tags & search_tags]  # Intersection check
```

### Pattern 8: Set-Based Menu System
```python
MENU_OPTIONS = {
    '1': 'View Records',
    '2': 'Add Record',
    '3': 'Delete Record',
    '4': 'Search',
    '5': 'Exit'
}

ADMIN_OPTIONS = {'3', '6', '7'}  # Delete, Admin Panel, Settings
VALID_CHOICES = set(MENU_OPTIONS.keys())

def get_choice():
    while True:
        choice = input("Enter choice: ")
        if choice in VALID_CHOICES:
            return choice
        print("Invalid choice!")

def is_admin_option(choice):
    return choice in ADMIN_OPTIONS

# Permission-based menu
def show_menu(user_permissions):
    for option, description in MENU_OPTIONS.items():
        if option in ADMIN_OPTIONS:
            if 'admin' in user_permissions:
                print(f"{option}. {description}")
        else:
            print(f"{option}. {description}")
```

---

## PERFORMANCE COMPARISON

```python
# List vs Set membership testing
import time

# Large dataset
data_list = list(range(100000))
data_set = set(range(100000))

# Test lookup in list (slow - O(n))
start = time.time()
result = 99999 in data_list
list_time = time.time() - start
print(f"List lookup: {list_time:.6f} seconds")

# Test lookup in set (fast - O(1))
start = time.time()
result = 99999 in data_set
set_time = time.time() - start
print(f"Set lookup: {set_time:.6f} seconds")

# Set is 1000x+ faster!
```

**When to use SET vs LIST:**
- **Set**: Fast lookups, unique values, mathematical operations
- **List**: Need order, allow duplicates, need indexing

---

## SUMMARY - KEY TAKEAWAYS

1. **Sets are unordered and unique** - no duplicates, no indexing
2. **Fast membership testing** - O(1) lookup time
3. **Mathematical operations**: union (|), intersection (&), difference (-), symmetric difference (^)
4. **Elements must be hashable** - can't store lists, sets, or dicts
5. **Set comprehensions** create sets efficiently
6. **Frozensets are immutable** - can be dict keys or set elements
7. **Use sets for**:
   - Removing duplicates
   - Fast membership testing (item in set)
   - Mathematical operations
   - Unique value tracking
   - Permission/access control
8. **Common methods**: add(), remove(), discard(), pop(), clear(), update()
9. **Comparison methods**: issubset(), issuperset(), isdisjoint()
10. **No indexing or slicing** - convert to list if needed: `list(set)`

