# FUNCTOOLS_MODULE

## Core Definition
**functools** is a module for higher-order functions that act on or return other functions. Provides tools for function manipulation, caching, composition, and functional programming patterns.

**Tags**: #functools #decorators #caching #functional-programming #higher-order-functions

---

## COMPLETE FUNCTOOLS QUICK REFERENCE

### FUNCTOOLS METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# CACHING DECORATORS
# ═══════════════════════════════════════════════════════════════════════════
@functools.lru_cache(maxsize=128)           # Function | Cache results (LRU) | Returns cached decorator
@functools.lru_cache(maxsize=None)          # Function | Unbounded cache | Returns cached decorator
@functools.cache                             # Function (3.9+) | Unbounded cache (alias) | Returns cached decorator
func.cache_info()                            # Cached function | Get cache statistics | Returns CacheInfo(hits, misses, maxsize, currsize)
func.cache_clear()                           # Cached function | Clear cache | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# FUNCTION COMPARISON & ORDERING
# ═══════════════════════════════════════════════════════════════════════════
@functools.total_ordering                    # Class | Generate comparison methods | Returns class with all comparisons
functools.cmp_to_key(func)                   # Comparison function | Convert to key function | Returns key function for sorted/min/max

# ═══════════════════════════════════════════════════════════════════════════
# PARTIAL APPLICATION
# ═══════════════════════════════════════════════════════════════════════════
functools.partial(func, *args, **kwargs)    # Function + args | Create partial function | Returns new callable with frozen args
functools.partialmethod(func, *args, **kwargs) # Method + args | Create partial method | Returns descriptor for class methods

# ═══════════════════════════════════════════════════════════════════════════
# FUNCTION COMPOSITION & REDUCTION
# ═══════════════════════════════════════════════════════════════════════════
functools.reduce(func, iterable)            # Binary function + iterable | Reduce to single value | Returns accumulated result
functools.reduce(func, iterable, initializer) # Binary function + iterable + init | Reduce with initial | Returns accumulated result

# ═══════════════════════════════════════════════════════════════════════════
# FUNCTION METADATA PRESERVATION
# ═══════════════════════════════════════════════════════════════════════════
@functools.wraps(wrapped)                   # Function decorator | Copy metadata from wrapped | Returns decorator preserving metadata
functools.update_wrapper(wrapper, wrapped)  # Two functions | Copy metadata manually | Returns wrapper with updated metadata
functools.WRAPPER_ASSIGNMENTS                # Constant | Tuple of copied attributes | ('__module__', '__name__', '__qualname__', '__annotations__', '__doc__')
functools.WRAPPER_UPDATES                    # Constant | Tuple of updated attributes | ('__dict__',)

# ═══════════════════════════════════════════════════════════════════════════
# SINGLE DISPATCH GENERIC FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
@functools.singledispatch                   # Function | Create generic function | Returns generic function dispatcher
@func.register(type)                        # Generic function | Register type handler | Returns decorator for type-specific impl
func.register(type, impl)                   # Generic function | Register impl directly | Returns implementation function
func.dispatch(type)                         # Generic function | Get handler for type | Returns registered implementation
func.registry                               # Generic function | View all handlers | Returns mapping of types to implementations

# ═══════════════════════════════════════════════════════════════════════════
# SINGLE DISPATCH METHOD (3.8+)
# ═══════════════════════════════════════════════════════════════════════════
@functools.singledispatchmethod            # Method | Create generic method | Returns generic method dispatcher
@method.register                            # Generic method | Register type handler | Returns decorator for type-specific impl

# ═══════════════════════════════════════════════════════════════════════════
# CACHED PROPERTIES (3.8+)
# ═══════════════════════════════════════════════════════════════════════════
@functools.cached_property                  # Method | Cache property value | Returns cached property descriptor

# ═══════════════════════════════════════════════════════════════════════════
# TOPLEVEL (3.10+)
# ═══════════════════════════════════════════════════════════════════════════
@functools.cache                            # Function (3.9+) | Simple unbounded cache | Returns cached function
```

### COMMON OPERATION EXAMPLES

```python
from functools import lru_cache, partial, reduce, wraps, total_ordering

# Caching expensive computations
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(100)              # Fast due to caching
fibonacci.cache_info()      # CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)

# Partial application
multiply = lambda x, y: x * y
double = partial(multiply, 2)
double(5)                   # → 10

# Reduce
numbers = [1, 2, 3, 4, 5]
reduce(lambda x, y: x + y, numbers)        # → 15
reduce(lambda x, y: x * y, numbers)        # → 120

# Preserving function metadata
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello"""
    return f"Hello {name}"

greet.__name__              # → "greet" (not "wrapper")
greet.__doc__               # → "Say hello"

# Total ordering
@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
    # __le__, __gt__, __ge__ automatically generated

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)
s1 > s2                     # → True (auto-generated)
```

---

## DETAILED FUNCTOOLS OPERATIONS

### 1. CACHING WITH LRU_CACHE

```python
from functools import lru_cache

# Basic caching
@lru_cache(maxsize=128)
def expensive_operation(n):
    """Simulate expensive computation"""
    print(f"Computing for {n}")
    return n * n

expensive_operation(5)      # Prints "Computing for 5" → 25
expensive_operation(5)      # Uses cache → 25 (no print)
expensive_operation(6)      # Prints "Computing for 6" → 36

# Cache statistics
expensive_operation.cache_info()
# CacheInfo(hits=1, misses=2, maxsize=128, currsize=2)

# Clear cache
expensive_operation.cache_clear()

# Unbounded cache (stores everything)
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Python 3.9+ simple cache decorator
@cache
def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

# LRU Cache with typed arguments (separate cache for different types)
@lru_cache(maxsize=128, typed=True)
def compute(x):
    return x * 2

compute(5)                  # → 10 (cached)
compute(5.0)                # → 10.0 (separate cache entry due to typed=True)

# Practical example: memoized recursive function
@lru_cache(maxsize=None)
def count_ways(n, coins):
    """Count ways to make change"""
    coins = tuple(sorted(coins))  # Make hashable
    if n == 0:
        return 1
    if n < 0 or not coins:
        return 0
    return count_ways(n - coins[0], coins) + count_ways(n, coins[1:])

count_ways(100, (1, 5, 10, 25))  # Fast with caching

# Monitoring cache performance
def report_cache_stats(func):
    """Decorator to report cache stats"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Cache stats: {func.cache_info()}")
        return result
    return wrapper

@report_cache_stats
@lru_cache(maxsize=100)
def cached_func(x):
    return x ** 2
```

### 2. PARTIAL FUNCTION APPLICATION

```python
from functools import partial

# Basic partial application
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

square(5)                   # → 25
cube(5)                     # → 125

# Partial with positional args
def greet(greeting, name):
    return f"{greeting}, {name}!"

say_hello = partial(greet, "Hello")
say_goodbye = partial(greet, "Goodbye")

say_hello("Alice")          # → "Hello, Alice!"
say_goodbye("Bob")          # → "Goodbye, Bob!"

# Practical: creating specialized functions
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
triple = partial(multiply, 3)

list(map(double, [1, 2, 3, 4]))     # → [2, 4, 6, 8]
list(map(triple, [1, 2, 3, 4]))     # → [3, 6, 9, 12]

# Partial with methods
class Logger:
    def log(self, level, message):
        print(f"[{level}] {message}")

logger = Logger()
error = partial(logger.log, "ERROR")
warning = partial(logger.log, "WARNING")

error("Something went wrong")       # [ERROR] Something went wrong
warning("Be careful")               # [WARNING] Be careful

# PartialMethod for class definitions
from functools import partialmethod

class Cell:
    def __init__(self):
        self._alive = False
    
    def set_state(self, state):
        self._alive = state
    
    # Create convenience methods
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

cell = Cell()
cell.set_alive()            # Same as cell.set_state(True)

# Practical: int conversion with different bases
int_base2 = partial(int, base=2)
int_base16 = partial(int, base=16)

int_base2("1010")           # → 10
int_base16("FF")            # → 255

# Callback functions with fixed parameters
import tkinter as tk

def button_click(button_id, event=None):
    print(f"Button {button_id} clicked")

root = tk.Tk()
for i in range(5):
    btn = tk.Button(root, text=f"Button {i}", 
                    command=partial(button_click, i))
    btn.pack()
```

### 3. REDUCE FOR ACCUMULATION

```python
from functools import reduce

# Basic reduction
numbers = [1, 2, 3, 4, 5]

# Sum
reduce(lambda x, y: x + y, numbers)         # → 15
reduce(lambda x, y: x + y, numbers, 0)      # → 15 (with initializer)

# Product
reduce(lambda x, y: x * y, numbers)         # → 120

# Maximum
reduce(lambda x, y: x if x > y else y, numbers)  # → 5

# Minimum
reduce(lambda x, y: x if x < y else y, numbers)  # → 1

# String concatenation
words = ["Hello", " ", "World"]
reduce(lambda x, y: x + y, words)           # → "Hello World"

# Complex accumulation: count occurrences
items = ['a', 'b', 'a', 'c', 'b', 'a']
counts = reduce(
    lambda acc, item: {**acc, item: acc.get(item, 0) + 1},
    items,
    {}
)
# → {'a': 3, 'b': 2, 'c': 1}

# Flatten nested lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda x, y: x + y, nested)   # → [1, 2, 3, 4, 5, 6]

# Build dictionary from pairs
pairs = [('a', 1), ('b', 2), ('c', 3)]
dict_result = reduce(
    lambda d, pair: {**d, pair[0]: pair[1]},
    pairs,
    {}
)
# → {'a': 1, 'b': 2, 'c': 3}

# Compose functions
def compose(*functions):
    """Compose multiple functions right-to-left"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

add_one = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

# Compose: square(double(add_one(x)))
composed = compose(square, double, add_one)
composed(5)                 # → ((5+1)*2)^2 = 144

# Practical: calculate compound interest
def compound_interest(principal, rate, years):
    """Calculate compound interest using reduce"""
    return reduce(
        lambda amount, _: amount * (1 + rate),
        range(years),
        principal
    )

compound_interest(1000, 0.05, 10)  # → 1628.89

# Chain operations
operations = [
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x - 5
]
result = reduce(lambda val, func: func(val), operations, 5)
# 5 → 15 → 30 → 25

# Validate all conditions
conditions = [
    lambda x: x > 0,
    lambda x: x < 100,
    lambda x: x % 2 == 0
]
value = 42
is_valid = reduce(lambda acc, func: acc and func(value), conditions, True)
# → True
```

### 4. WRAPS FOR DECORATOR METADATA

```python
from functools import wraps
import time

# Without wraps (BAD)
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def greet(name):
    """Greet someone"""
    return f"Hello {name}"

greet.__name__              # → "wrapper" (WRONG!)
greet.__doc__               # → None (LOST!)

# With wraps (GOOD)
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timing_decorator
def calculate(n):
    """Calculate sum of squares"""
    return sum(i**2 for i in range(n))

calculate.__name__          # → "calculate" (CORRECT!)
calculate.__doc__           # → "Calculate sum of squares" (PRESERVED!)

# Decorator with arguments
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    """Print hello"""
    print("Hello")

say_hello.__name__          # → "say_hello"

# Preserving additional attributes
def advanced_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    
    wrapper.call_count = 0
    return wrapper

@advanced_decorator
def my_func():
    """My function"""
    pass

my_func()
my_func()
my_func.call_count          # → 2

# Class-based decorator with wraps
class CountCalls:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.call_count = 0
    
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)

@CountCalls
def process_data(data):
    """Process the data"""
    return data * 2

process_data.__name__       # → "process_data"
process_data.call_count     # → 0

# Manual update_wrapper usage
def manual_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    # Manually copy metadata
    from functools import update_wrapper
    update_wrapper(wrapper, func)
    return wrapper
```

### 5. TOTAL_ORDERING FOR COMPARISON

```python
from functools import total_ordering

# Define only __eq__ and __lt__, get rest free
@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
    
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

alice = Student("Alice", 90)
bob = Student("Bob", 85)
charlie = Student("Charlie", 90)

# All comparison operators work
alice > bob                 # → True (auto-generated from __lt__)
alice >= bob                # → True (auto-generated)
alice <= charlie            # → True (auto-generated)
alice == charlie            # → True (uses __eq__)
alice != bob                # → True (from __eq__)

# Can sort lists
students = [bob, alice, charlie]
sorted(students)            # Works automatically

# Practical: Version comparison
@total_ordering
class Version:
    def __init__(self, version_string):
        self.parts = tuple(map(int, version_string.split('.')))
    
    def __eq__(self, other):
        return self.parts == other.parts
    
    def __lt__(self, other):
        return self.parts < other.parts
    
    def __repr__(self):
        return f"Version({'.'.join(map(str, self.parts))})"

v1 = Version("1.2.3")
v2 = Version("1.2.4")
v3 = Version("2.0.0")

v1 < v2                     # → True
v2 >= v1                    # → True
v3 > v2                     # → True
sorted([v3, v1, v2])        # → [Version(1.2.3), Version(1.2.4), Version(2.0.0)]

# Custom ordering: reverse alphabetical
@total_ordering
class ReverseStr:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value > other.value  # Reversed!
    
    def __repr__(self):
        return f"ReverseStr({self.value})"

words = [ReverseStr("apple"), ReverseStr("zebra"), ReverseStr("banana")]
sorted(words)               # → [ReverseStr(zebra), ReverseStr(banana), ReverseStr(apple)]

# Priority queue item
@total_ordering
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    
    def __eq__(self, other):
        return self.priority == other.priority
    
    def __lt__(self, other):
        return self.priority > other.priority  # Higher priority = "less than"
    
    def __repr__(self):
        return f"Task({self.priority}, {self.name})"

tasks = [Task(1, "Low"), Task(3, "High"), Task(2, "Medium")]
sorted(tasks)               # → [Task(3, High), Task(2, Medium), Task(1, Low)]
```

### 6. CMP_TO_KEY FOR SORTING

```python
from functools import cmp_to_key

# Convert old-style comparison function to key function
def compare_length(s1, s2):
    """Compare strings by length"""
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    return 0

words = ["apple", "pie", "banana", "a"]
sorted(words, key=cmp_to_key(compare_length))
# → ['a', 'pie', 'apple', 'banana']

# Complex comparison: sort by multiple criteria
def compare_students(s1, s2):
    """Compare by grade (desc), then name (asc)"""
    if s1['grade'] != s2['grade']:
        return s2['grade'] - s1['grade']  # Descending
    return -1 if s1['name'] < s2['name'] else 1  # Ascending

students = [
    {'name': 'Alice', 'grade': 90},
    {'name': 'Bob', 'grade': 85},
    {'name': 'Charlie', 'grade': 90}
]

sorted(students, key=cmp_to_key(compare_students))
# → [{'name': 'Alice', 'grade': 90}, 
#    {'name': 'Charlie', 'grade': 90}, 
#    {'name': 'Bob', 'grade': 85}]

# Custom ordering: sort by specific order
def compare_by_priority(x, y):
    """Sort by custom priority order"""
    priority = {'high': 3, 'medium': 2, 'low': 1}
    return priority.get(x, 0) - priority.get(y, 0)

tasks = ['low', 'high', 'medium', 'high', 'low']
sorted(tasks, key=cmp_to_key(compare_by_priority))
# → ['low', 'low', 'medium', 'high', 'high']

# Reverse comparison
def reverse_compare(x, y):
    """Reverse standard comparison"""
    return -1 if x > y else (1 if x < y else 0)

numbers = [3, 1, 4, 1, 5, 9]
sorted(numbers, key=cmp_to_key(reverse_compare))
# → [9, 5, 4, 3, 1, 1]

# Locale-aware string comparison
import locale

def locale_compare(s1, s2):
    """Compare strings according to locale"""
    return locale.strcoll(s1, s2)

# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
names = ['Zoë', 'Alice', 'Émile', 'Bob']
sorted(names, key=cmp_to_key(locale_compare))
```

### 7. SINGLEDISPATCH FOR POLYMORPHISM

```python
from functools import singledispatch
from decimal import Decimal

# Generic function with type-based dispatch
@singledispatch
def process(arg):
    """Default implementation"""
    print(f"Processing generic: {arg}")
    return arg

@process.register(int)
def _(arg):
    print(f"Processing integer: {arg}")
    return arg * 2

@process.register(str)
def _(arg):
    print(f"Processing string: {arg}")
    return arg.upper()

@process.register(list)
def _(arg):
    print(f"Processing list: {arg}")
    return sorted(arg)

process(5)                  # Processing integer: 5 → 10
process("hello")            # Processing string: hello → "HELLO"
process([3, 1, 2])          # Processing list: [3, 1, 2] → [1, 2, 3]
process(3.14)               # Processing generic: 3.14 → 3.14

# Register multiple types
@process.register(tuple)
@process.register(set)
def _(arg):
    print(f"Processing collection: {arg}")
    return list(arg)

process((1, 2, 3))          # Processing collection: (1, 2, 3) → [1, 2, 3]

# Direct registration
def process_dict(arg):
    print(f"Processing dict: {arg}")
    return list(arg.keys())

process.register(dict, process_dict)
process({'a': 1, 'b': 2})   # Processing dict: {'a': 1, 'b': 2} → ['a', 'b']

# View registry
process.registry            # MappingProxyType({<class 'object'>: <function>, ...})

# Get specific implementation
int_processor = process.dispatch(int)
int_processor(5)            # → 10

# Practical: HTML formatting
@singledispatch
def to_html(data):
    """Convert data to HTML"""
    return f"<span>{data}</span>"

@to_html.register(int)
@to_html.register(float)
def _(data):
    return f"<span class='number'>{data}</span>"

@to_html.register(str)
def _(data):
    return f"<span class='text'>{data}</span>"

@to_html.register(list)
def _(data):
    items = ''.join(f"<li>{to_html(item)}</li>" for item in data)
    return f"<ul>{items}</ul>"

@to_html.register(dict)
def _(data):
    items = ''.join(f"<tr><td>{k}</td><td>{to_html(v)}</td></tr>" 
                    for k, v in data.items())
    return f"<table>{items}</table>"

to_html(42)                 # <span class='number'>42</span>
to_html("hello")            # <span class='text'>hello</span>
to_html([1, 2, 3])          # <ul><li>...</li>...</ul>

# Singledispatchmethod (Python 3.8+)
from functools import singledispatchmethod

class DataProcessor:
    @singledispatchmethod
    def process(self, data):
        """Default processor"""
        return str(data)
    
    @process.register
    def _(self, data: int):
        return data * 2
    
    @process.register
    def _(self, data: str):
        return data.upper()
    
    @process.register
    def _(self, data: list):
        return sorted(data)

processor = DataProcessor()
processor.process(5)        # → 10
processor.process("hello")  # → "HELLO"
processor.process([3, 1, 2]) # → [1, 2, 3]
```

### 8. CACHED_PROPERTY (Python 3.8+)

```python
from functools import cached_property
import time

class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    @cached_property
    def mean(self):
        """Calculate mean (cached after first call)"""
        print("Computing mean...")
        time.sleep(1)  # Simulate expensive computation
        return sum(self.data) / len(self.data)
    
    @cached_property
    def variance(self):
        """Calculate variance (cached)"""
        print("Computing variance...")
        time.sleep(1)
        mean = self.mean
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)

analyzer = DataAnalyzer([1, 2, 3, 4, 5])
analyzer.mean               # Prints "Computing mean..." → 3.0 (1 second)
analyzer.mean               # → 3.0 (instant, cached)
analyzer.variance           # Prints "Computing variance..." → 2.0 (1 second)

# Clear cache by deleting attribute
del analyzer.mean
analyzer.mean               # Prints "Computing mean..." again

# Practical: expensive computations
class Employee:
    def __init__(self, name, salary, bonus_percent):
        self.name = name
        self.salary = salary
        self.bonus_percent = bonus_percent
    
    @cached_property
    def total_compensation(self):
        """Calculate total compensation (expensive)"""
        print(f"Calculating compensation for {self.name}")
        bonus = self.salary * (self.bonus_percent / 100)
        taxes = (self.salary + bonus) * 0.3
        return self.salary + bonus - taxes

emp = Employee("Alice", 100000, 10)
emp.total_compensation      # Calculates once
emp.total_compensation      # Returns cached value

# Difference from @property
class WithProperty:
    @property
    def value(self):
        print("Computing...")
        return 42

class WithCachedProperty:
    @cached_property
    def value(self):
        print("Computing...")
        return 42

obj1 = WithProperty()
obj1.value                  # Prints "Computing..."
obj1.value                  # Prints "Computing..." again (no cache)

obj2 = WithCachedProperty()
obj2.value                  # Prints "Computing..."
obj2.value                  # No print (cached)

# Database query caching
class UserRepository:
    def __init__(self, user_id):
        self.user_id = user_id
    
    @cached_property
    def user_data(self):
        """Fetch user data from database (cached)"""
        print(f"Querying database for user {self.user_id}")
        # Simulate database query
        return {'id': self.user_id, 'name': 'Alice', 'email': 'alice@example.com'}
    
    @cached_property
    def user_posts(self):
        """Fetch user posts (cached)"""
        print(f"Querying posts for user {self.user_id}")
        return ['Post 1', 'Post 2', 'Post 3']

repo = UserRepository(123)
repo.user_data              # Query once
repo.user_data              # Cached
repo.user_posts             # Query once
```

### 9. PRACTICAL PATTERNS & RECIPES

```python
# Pattern 1: Memoization for dynamic programming
@lru_cache(maxsize=None)
def knapsack(capacity, weights, values, n):
    """0/1 knapsack problem"""
    weights = tuple(weights)
    values = tuple(values)
    
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n-1] > capacity:
        return knapsack(capacity, weights, values, n-1)
    
    include = values[n-1] + knapsack(capacity - weights[n-1], weights, values, n-1)
    exclude = knapsack(capacity, weights, values, n-1)
    
    return max(include, exclude)

# Pattern 2: Function composition pipeline
def pipe(*functions):
    """Create a pipeline of functions (left-to-right)"""
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

# Usage
add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2
square = lambda x: x ** 2

pipeline = pipe(add_one, multiply_by_two, square)
pipeline(5)                 # ((5 + 1) * 2) ** 2 = 144

# Pattern 3: Retry decorator with exponential backoff
from functools import wraps
import time

def retry(max_attempts=3, delay=1, backoff=2):
    """Retry decorator with exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1, backoff=2)
def unreliable_api_call():
    """Simulated API call that might fail"""
    import random
    if random.random() < 0.7:
        raise ConnectionError("API unavailable")
    return "Success"

# Pattern 4: Singleton using cached_property
class Singleton:
    _instance = None
    
    @classmethod
    @lru_cache(maxsize=1)
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# Pattern 5: Rate limiting decorator
from time import time

def rate_limit(calls_per_second):
    """Limit function calls per second"""
    min_interval = 1.0 / calls_per_second
    
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time() - last_called[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            result = func(*args, **kwargs)
            last_called[0] = time()
            return result
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)
def api_call(endpoint):
    print(f"Calling {endpoint}")
    return f"Response from {endpoint}"

# Pattern 6: Method chaining with partial
class QueryBuilder:
    def __init__(self):
        self.filters = []
    
    def where(self, field, operator, value):
        self.filters.append((field, operator, value))
        return self
    
    def equals(self, field, value):
        return partial(self.where, operator='=')(field, value)
    
    def greater_than(self, field, value):
        return partial(self.where, operator='>')(field, value)
    
    def build(self):
        return ' AND '.join(f"{f} {op} {v}" for f, op, v in self.filters)

# Pattern 7: Type-based validation with singledispatch
@singledispatch
def validate(value, rules):
    """Generic validation"""
    raise TypeError(f"Unsupported type: {type(value)}")

@validate.register(int)
def _(value, rules):
    if 'min' in rules and value < rules['min']:
        raise ValueError(f"Value must be >= {rules['min']}")
    if 'max' in rules and value > rules['max']:
        raise ValueError(f"Value must be <= {rules['max']}")
    return True

@validate.register(str)
def _(value, rules):
    if 'min_length' in rules and len(value) < rules['min_length']:
        raise ValueError(f"String too short")
    if 'max_length' in rules and len(value) > rules['max_length']:
        raise ValueError(f"String too long")
    if 'pattern' in rules:
        import re
        if not re.match(rules['pattern'], value):
            raise ValueError(f"Pattern mismatch")
    return True

validate(42, {'min': 0, 'max': 100})        # True
validate("hello", {'min_length': 3})        # True

# Pattern 8: Aggregate reduction operations
from operator import add, mul

def sum_all(iterable):
    return reduce(add, iterable, 0)

def product_all(iterable):
    return reduce(mul, iterable, 1)

def concat_all(iterable):
    return reduce(add, iterable, "")

sum_all([1, 2, 3, 4])       # → 10
product_all([1, 2, 3, 4])   # → 24
concat_all(['a', 'b', 'c']) # → "abc"
```

---

## PRACTICAL PROJECT PATTERNS

### Pattern 1: Cached Configuration Loader
```python
from functools import lru_cache
import json

@lru_cache(maxsize=1)
def load_config(config_file='config.json'):
    """Load and cache configuration"""
    print(f"Loading config from {config_file}")
    with open(config_file) as f:
        return json.load(f)

# Config loaded once, cached thereafter
config = load_config()
config2 = load_config()  # Same object, no file I/O
```

### Pattern 2: Database Connection Pool
```python
from functools import lru_cache

@lru_cache(maxsize=10)
def get_db_connection(database):
    """Get or create cached database connection"""
    print(f"Creating connection to {database}")
    # return actual database connection
    return f"Connection to {database}"

conn1 = get_db_connection('users')
conn2 = get_db_connection('users')  # Same connection
```

### Pattern 3: Event Handler Registry
```python
from functools import singledispatch

@singledispatch
def handle_event(event):
    """Default event handler"""
    print(f"Unhandled event: {event}")

@handle_event.register(dict)
def _(event):
    if event.get('type') == 'click':
        print(f"Click at ({event['x']}, {event['y']})")
    elif event.get('type') == 'keypress':
        print(f"Key pressed: {event['key']}")

@handle_event.register(str)
def _(event):
    print(f"String event: {event}")
```

### Pattern 4: API Request Builder
```python
from functools import partial

def make_request(method, url, headers=None, data=None):
    """Generic HTTP request"""
    print(f"{method} {url}")
    if headers:
        print(f"Headers: {headers}")
    if data:
        print(f"Data: {data}")
    return f"Response from {url}"

# Create specialized request functions
get = partial(make_request, 'GET')
post = partial(make_request, 'POST')
put = partial(make_request, 'PUT')
delete = partial(make_request, 'DELETE')

# API client with auth header
api_get = partial(get, headers={'Authorization': 'Bearer token123'})

# Usage
api_get('/users')
post('/users', data={'name': 'Alice'})
```

### Pattern 5: Validation Pipeline
```python
from functools import reduce

def validate_not_empty(value):
    if not value:
        raise ValueError("Value cannot be empty")
    return value

def validate_min_length(min_len):
    def validator(value):
        if len(value) < min_len:
            raise ValueError(f"Minimum length is {min_len}")
        return value
    return validator

def validate_max_length(max_len):
    def validator(value):
        if len(value) > max_len:
            raise ValueError(f"Maximum length is {max_len}")
        return value
    return validator

def validate_pattern(pattern):
    import re
    def validator(value):
        if not re.match(pattern, value):
            raise ValueError(f"Must match pattern {pattern}")
        return value
    return validator

# Create validation pipeline
validators = [
    validate_not_empty,
    validate_min_length(3),
    validate_max_length(20),
    validate_pattern(r'^[a-zA-Z0-9_]+$')
]

def validate_username(username):
    """Run all validators"""
    return reduce(lambda val, validator: validator(val), validators, username)

try:
    validate_username("alice_123")  # Valid
    validate_username("ab")         # Raises ValueError (too short)
except ValueError as e:
    print(e)
```

### Pattern 6: Calculation Pipeline
```python
from functools import reduce

# Define calculation steps
def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

def apply_tax(price, tax_percent):
    return price * (1 + tax_percent / 100)

def apply_shipping(price, shipping_cost):
    return price + shipping_cost

# Build calculation pipeline
def calculate_final_price(base_price, discount=10, tax=8.5, shipping=5.99):
    """Calculate final price with discount, tax, and shipping"""
    operations = [
        lambda p: apply_discount(p, discount),
        lambda p: apply_tax(p, tax),
        lambda p: apply_shipping(p, shipping)
    ]
    return reduce(lambda price, op: op(price), operations, base_price)

final = calculate_final_price(100.00)
print(f"Final price: ${final:.2f}")
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: Unhashable Arguments to lru_cache
```python
# WRONG
@lru_cache
def process_list(items):
    return sum(items)

# process_list([1, 2, 3])  # TypeError: unhashable type: 'list'

# RIGHT - Convert to tuple
@lru_cache
def process_list(items):
    items = tuple(items)  # Make hashable
    return sum(items)

process_list((1, 2, 3))  # Works with tuple

# OR - Accept tuple parameter
@lru_cache
def process_tuple(items: tuple):
    return sum(items)

process_tuple((1, 2, 3))
```

### Error 2: Forgetting @wraps in Decorators
```python
# WRONG
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello"""
    pass

# greet.__name__ → "wrapper" (LOST!)

# RIGHT
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello"""
    pass

# greet.__name__ → "greet" (PRESERVED!)
```

### Error 3: Missing __eq__ with @total_ordering
```python
# WRONG
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, age):
        self.age = age
    
    def __lt__(self, other):
        return self.age < other.age
    # Missing __eq__!

# RIGHT
@total_ordering
class Person:
    def __init__(self, age):
        self.age = age
    
    def __eq__(self, other):  # Required!
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
```

### Error 4: Partial with Incorrect Argument Order
```python
from functools import partial

def divide(a, b):
    return a / b

# WRONG - confusing order
half = partial(divide, 2)
half(10)                # → 2 / 10 = 0.2 (NOT 10 / 2)

# RIGHT - use keyword arguments
half = partial(divide, b=2)
half(10)                # → 10 / 2 = 5.0

# OR - define better function signature
def divide(numerator, denominator):
    return numerator / denominator

half = partial(divide, denominator=2)
half(10)                # → 10 / 2 = 5.0
```

### Error 5: Mutating Cached Objects
```python
# WRONG
@lru_cache
def get_list():
    return [1, 2, 3]

lst1 = get_list()
lst1.append(4)          # Mutates cached object!
lst2 = get_list()       # → [1, 2, 3, 4] (UNEXPECTED!)

# RIGHT - Return copies
@lru_cache
def get_list():
    return [1, 2, 3]

def get_list_copy():
    return get_list().copy()

lst1 = get_list_copy()
lst1.append(4)
lst2 = get_list_copy()  # → [1, 2, 3] (CORRECT!)

# OR - Cache immutable data
@lru_cache
def get_tuple():
    return (1, 2, 3)
```

---

## PERFORMANCE TIPS

1. **Use lru_cache for recursive functions**
   ```python
   # SLOW - exponential time
   def fibonacci(n):
       if n < 2:
           return n
       return fibonacci(n-1) + fibonacci(n-2)
   
   # FAST - linear time with caching
   @lru_cache(maxsize=None)
   def fibonacci(n):
       if n < 2:
           return n
       return fibonacci(n-1) + fibonacci(n-2)
   ```

2. **Use appropriate maxsize for lru_cache**
   ```python
   # For small input space
   @lru_cache(maxsize=128)
   def small_func(x):
       return x * 2
   
   # For unlimited caching
   @lru_cache(maxsize=None)
   def unlimited_cache(x):
       return expensive_operation(x)
   
   # Python 3.9+
   @cache  # Equivalent to lru_cache(maxsize=None)
   def simple_cache(x):
       return expensive_operation(x)
   ```

3. **Use partial to avoid lambda overhead**
   ```python
   # SLOWER - lambda creates new function each time
   buttons = [Button(callback=lambda i=i: click(i)) for i in range(100)]
   
   # FASTER - partial reuses function
   from functools import partial
   buttons = [Button(callback=partial(click, i)) for i in range(100)]
   ```

4. **Use reduce for large accumulations**
   ```python
   # SLOWER - intermediate list creation
   result = sum([func(x) for x in large_list])
   
   # FASTER - no intermediate list
   from functools import reduce
   from operator import add
   result = reduce(add, (func(x) for x in large_list))
   ```

5. **Use cached_property for expensive attribute access**
   ```python
   # SLOW - recomputes every time
   class DataSet:
       @property
       def statistics(self):
           return expensive_calculation(self.data)
   
   # FAST - computes once
   class DataSet:
       @cached_property
       def statistics(self):
           return expensive_calculation(self.data)
   ```

6. **Clear cache when memory is a concern**
   ```python
   @lru_cache(maxsize=1000)
   def cached_func(x):
       return expensive_operation(x)
   
   # Check cache size
   info = cached_func.cache_info()
   if info.currsize > 800:
       cached_func.cache_clear()  # Clear when getting full
   ```

7. **Use singledispatch to avoid isinstance chains**
   ```python
   # SLOW - many isinstance checks
   def process(data):
       if isinstance(data, int):
           return data * 2
       elif isinstance(data, str):
           return data.upper()
       elif isinstance(data, list):
           return sorted(data)
   
   # FASTER - direct dispatch
   @singledispatch
   def process(data):
       return data
   
   @process.register(int)
   def _(data):
       return data * 2
   
   @process.register(str)
   def _(data):
       return data.upper()
   
   @process.register(list)
   def _(data):
       return sorted(data)
   ```

---

## RELATED MODULES & ADVANCED TOPICS

### Related Standard Library Modules
- **itertools**: Functional iterator tools (chain, combinations, etc.)
- **operator**: Function equivalents of operators (add, mul, etc.)
- **collections**: Specialized container datatypes (Counter, defaultdict)

### Advanced Patterns
```python
# Compose with reduce
from functools import reduce

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

# Currying with partial
def curry2(func):
    """Convert 2-arg function to curried form"""
    return lambda x: partial(func, x)

# Memoization decorator
def memoize(func):
    """Custom memoization decorator"""
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

---

## SUMMARY

**functools** provides essential tools for:
- **Caching**: `lru_cache`, `cache`, `cached_property`
- **Function manipulation**: `partial`, `wraps`, `update_wrapper`
- **Comparison**: `total_ordering`, `cmp_to_key`
- **Reduction**: `reduce`
- **Polymorphism**: `singledispatch`, `singledispatchmethod`

**Best practices**:
1. Always use `@wraps` when creating decorators
2. Use `lru_cache` for expensive recursive functions
3. Make arguments hashable for caching (use tuples, not lists)
4. Choose appropriate `maxsize` for `lru_cache`
5. Use `@total_ordering` to reduce boilerplate in comparison classes
6. Prefer `singledispatch` over chains of `isinstance` checks
7. Use `cached_property` for expensive computed attributes
8. Clear caches when memory is constrained

**Common use cases**:
- Memoizing expensive function calls
- Creating specialized functions via partial application
- Implementing polymorphic functions
- Preserving function metadata in decorators
- Reducing sequences to single values
- Generating comparison methods automatically
