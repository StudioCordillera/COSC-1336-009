# FUNCTIONS

## Core Definition
**Functions** are reusable blocks of code that perform specific tasks. Accept input through parameters, execute statements, and optionally return values. Enable modular programming by breaking complex problems into smaller, manageable components that can be called multiple times.

**Tags**: #functions #code-organization #parameters #return-values #scope #modular-programming #lambda #recursion

---

## COMPLETE FUNCTION SYNTAX QUICK REFERENCE

### FUNCTION OPERATIONS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# BASIC FUNCTION DEFINITION
# ═══════════════════════════════════════════════════════════════════════════
def function_name():            # No params | Define simple function | Returns None by default
def function_name(param):       # Single param | Define with parameter | Returns None by default
def function_name(p1, p2):      # Multiple params | Define multi-parameter | Returns None by default
def function_name(param=value): # Default param | Define with default | Returns None by default
def function_name(*args):       # Variable args | Accept any number of args | Returns None by default
def function_name(**kwargs):    # Keyword args | Accept any keyword args | Returns None by default
def function_name() -> type:    # Type hint | Define with return type hint | Returns specified type

# ═══════════════════════════════════════════════════════════════════════════
# RETURN STATEMENTS
# ═══════════════════════════════════════════════════════════════════════════
return value                    # Value | Return single value | Returns value to caller
return value1, value2           # Multiple values | Return tuple | Returns tuple to caller
return                          # No value | Exit function early | Returns None
return expression if cond else alt # Conditional | Return based on condition | Returns conditional value

# ═══════════════════════════════════════════════════════════════════════════
# FUNCTION CALLS
# ═══════════════════════════════════════════════════════════════════════════
function_name()                 # No args | Call without arguments | Executes function
function_name(arg)              # Positional | Call with argument | Executes with argument
function_name(arg1, arg2)       # Multiple args | Call with multiple | Executes with arguments
function_name(param=value)      # Keyword arg | Call with named param | Executes with keyword arg
function_name(*list)            # Unpack list | Call with unpacked list | Executes with unpacked args
function_name(**dict)           # Unpack dict | Call with unpacked dict | Executes with unpacked kwargs

# ═══════════════════════════════════════════════════════════════════════════
# LAMBDA FUNCTIONS (ANONYMOUS)
# ═══════════════════════════════════════════════════════════════════════════
lambda x: expression            # Single param | Create anonymous function | Returns function object
lambda x, y: expression         # Multiple params | Create multi-param lambda | Returns function object
lambda: expression              # No params | Create parameterless lambda | Returns function object
map(lambda x: expr, iterable)   # Map operation | Apply lambda to iterable | Returns map object
filter(lambda x: cond, iter)    # Filter operation | Filter with lambda | Returns filter object
sorted(iter, key=lambda x: x.attr) # Sort operation | Sort with lambda key | Returns sorted list

# ═══════════════════════════════════════════════════════════════════════════
# SCOPE OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
global variable_name            # Global keyword | Access global variable | Modifies global scope
nonlocal variable_name          # Nonlocal keyword | Access enclosing scope | Modifies enclosing scope
locals()                        # No params | Get local namespace | Returns dict of local variables
globals()                       # No params | Get global namespace | Returns dict of global variables

# ═══════════════════════════════════════════════════════════════════════════
# DECORATORS
# ═══════════════════════════════════════════════════════════════════════════
@decorator                      # Decorator | Wrap function with decorator | Returns modified function
@decorator(args)                # Parameterized | Decorator with arguments | Returns modified function
@staticmethod                   # Static method | Define static method | Returns static method
@classmethod                    # Class method | Define class method | Returns class method
@property                       # Property | Define property getter | Returns property object

# ═══════════════════════════════════════════════════════════════════════════
# RECURSION
# ═══════════════════════════════════════════════════════════════════════════
def func(): return func()       # Self-call | Recursive function call | Returns recursive result
```

---

## DETAILED EXAMPLES

### 1. Basic Function Definition and Calling

```python
# Simple function with no parameters
def greet():
    print("Hello, World!")

greet()  # Call the function
```

**Output:**
```
Hello, World!
```

---

### 2. Functions with Parameters and Return Values

```python
def calculate_area(length, width):
    """Calculate rectangle area"""
    area = length * width
    return area

def calculate_volume(length, width, height):
    """Calculate box volume"""
    volume = length * width * height
    return volume

# Function calls
rectangle_area = calculate_area(10, 5)
box_volume = calculate_volume(10, 5, 3)

print(f"Rectangle area: {rectangle_area}")
print(f"Box volume: {box_volume}")
```

**Output:**
```
Rectangle area: 50
Box volume: 150
```

---

### 3. Default Parameters and Keyword Arguments

```python
def create_profile(name, age, city="Unknown", country="USA"):
    """Create user profile with default values"""
    return f"{name}, {age} years old, from {city}, {country}"

# Different ways to call
profile1 = create_profile("Alice", 25)
profile2 = create_profile("Bob", 30, "New York")
profile3 = create_profile("Charlie", 35, city="Los Angeles", country="USA")
profile4 = create_profile(name="David", age=40, country="Canada", city="Toronto")

print(profile1)
print(profile2)
print(profile3)
print(profile4)
```

**Output:**
```
Alice, 25 years old, from Unknown, USA
Bob, 30 years old, from New York, USA
Charlie, 35 years old, from Los Angeles, USA
David, 40 years old, from Toronto, Canada
```

---

### 4. Multiple Return Values (Tuple Unpacking)

```python
def get_statistics(numbers):
    """Calculate min, max, and average"""
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

# Unpack multiple return values
data = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = get_statistics(data)

print(f"Min: {min_val}, Max: {max_val}, Avg: {avg_val}")
```

**Output:**
```
Min: 10, Max: 50, Avg: 30.0
```

---

### 5. Variable Arguments (*args and **kwargs)

```python
def sum_all(*args):
    """Sum any number of arguments"""
    return sum(args)

def print_info(**kwargs):
    """Print keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Variable positional arguments
print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40, 50))

# Variable keyword arguments
print_info(name="Alice", age=25, city="Boston")
```

**Output:**
```
6
150
name: Alice
age: 25
city: Boston
```

---

### 6. Lambda Functions (Anonymous Functions)

```python
# Simple lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print(square(5))
print(add(3, 4))
print(is_even(10))

# Lambda with map, filter, sorted
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Squared: {squared}")
print(f"Evens: {evens}")

# Lambda as sorting key
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
sorted_people = sorted(people, key=lambda p: p["age"])
print(sorted_people)
```

**Output:**
```
25
7
True
Squared: [1, 4, 9, 16, 25]
Evens: [2, 4]
[{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]
```

---

### 7. Scope: Local, Global, and Nonlocal

```python
# Global variable
counter = 0

def local_scope_demo():
    """Local variables are only accessible within function"""
    local_var = 10
    print(f"Local variable: {local_var}")

def global_scope_demo():
    """Access global variable"""
    global counter
    counter += 1
    print(f"Global counter: {counter}")

def nonlocal_scope_demo():
    """Nonlocal for nested functions"""
    outer_var = 5
    
    def inner_function():
        nonlocal outer_var
        outer_var += 1
        print(f"Outer variable modified: {outer_var}")
    
    inner_function()
    print(f"After inner function: {outer_var}")

# Test scope
local_scope_demo()
global_scope_demo()
global_scope_demo()
nonlocal_scope_demo()
```

**Output:**
```
Local variable: 10
Global counter: 1
Global counter: 2
Outer variable modified: 6
After inner function: 6
```

---

### 8. Recursion

```python
def factorial(n):
    """Calculate factorial recursively"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate nth Fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def countdown(n):
    """Countdown using recursion"""
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

# Test recursive functions
print(f"5! = {factorial(5)}")
print(f"Fibonacci(7) = {fibonacci(7)}")
countdown(5)
```

**Output:**
```
5! = 120
Fibonacci(7) = 13
5
4
3
2
1
Blastoff!
```

---

### 9. Docstrings and Function Documentation

```python
def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.
    
    Args:
        principal (float): Initial amount
        rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time (int): Number of years
        n (int, optional): Times interest compounds per year. Defaults to 1.
    
    Returns:
        tuple: (final_amount, interest_earned)
    
    Raises:
        ValueError: If principal, rate, or time are negative
    
    Example:
        >>> final, interest = calculate_compound_interest(1000, 0.05, 3)
        >>> print(f"Final: ${final:.2f}")
        Final: $1157.63
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Values must be non-negative")
    
    final_amount = principal * (1 + rate / n) ** (n * time)
    interest_earned = final_amount - principal
    
    return final_amount, interest_earned

# Use the function
final, interest = calculate_compound_interest(1000, 0.05, 3)
print(f"Final amount: ${final:.2f}")
print(f"Interest earned: ${interest:.2f}")

# Access docstring
print(calculate_compound_interest.__doc__)
```

**Output:**
```
Final amount: $1157.63
Interest earned: $157.63
[Docstring content displayed]
```

---

### 10. Type Hints and Annotations

```python
from typing import List, Dict, Tuple, Optional

def process_numbers(numbers: List[int]) -> Dict[str, float]:
    """
    Process list of numbers and return statistics
    
    Args:
        numbers: List of integers
    
    Returns:
        Dictionary with min, max, and average
    """
    return {
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers)
    }

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """
    Find user by ID
    
    Returns:
        User dict or None if not found
    """
    users = {1: {"name": "Alice", "email": "alice@example.com"}}
    return users.get(user_id)

# Test type-hinted functions
stats = process_numbers([1, 2, 3, 4, 5])
user = find_user(1)

print(f"Stats: {stats}")
print(f"User: {user}")
```

**Output:**
```
Stats: {'min': 1, 'max': 5, 'average': 3.0}
User: {'name': 'Alice', 'email': 'alice@example.com'}
```

---

## COMMON USE CASES

### 1. Input Validation Function

```python
def get_positive_integer(prompt):
    """Get positive integer from user with validation"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Usage
# age = get_positive_integer("Enter your age: ")
```

---

### 2. Data Processing Pipeline

```python
def clean_data(data):
    """Remove None values and convert to lowercase"""
    return [item.lower() for item in data if item is not None]

def filter_data(data, min_length):
    """Filter items by minimum length"""
    return [item for item in data if len(item) >= min_length]

def transform_data(data):
    """Add prefix to each item"""
    return [f"Item: {item}" for item in data]

# Pipeline usage
raw_data = ["Apple", None, "Banana", "Cherry", "a", "Grape"]
cleaned = clean_data(raw_data)
filtered = filter_data(cleaned, 5)
transformed = transform_data(filtered)

print(transformed)
```

**Output:**
```
['Item: apple', 'Item: banana', 'Item: cherry', 'Item: grape']
```

---

### 3. Decorator Functions

```python
def timer_decorator(func):
    """Measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    
    return wrapper

@timer_decorator
def slow_function():
    """Function that takes time"""
    import time
    time.sleep(0.1)
    return "Done"

# Test decorator
result = slow_function()
```

**Output:**
```
slow_function took 0.1001 seconds
```

---

### 4. Closure Functions

```python
def create_multiplier(factor):
    """Create a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

# Create specific multipliers
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

**Output:**
```
10
15
```

---

## FUNCTION DESIGN PRINCIPLES

### 1. Single Responsibility
```python
# ✓ GOOD: Each function has one clear purpose
def calculate_tax(amount, rate):
    return amount * rate

def calculate_total(amount, tax):
    return amount + tax

# ✗ BAD: Function does too many things
def process_order(amount, tax_rate, discount, shipping):
    # Too many responsibilities in one function
    pass
```

---

### 2. Descriptive Naming
```python
# ✓ GOOD: Clear, descriptive names
def calculate_monthly_payment(principal, rate, months):
    pass

def validate_email_address(email):
    pass

# ✗ BAD: Unclear names
def calc(p, r, m):
    pass

def check(e):
    pass
```

---

### 3. Appropriate Parameters
```python
# ✓ GOOD: Reasonable number of parameters
def create_user(name, email, age):
    pass

# ✗ BAD: Too many parameters
def create_user(name, email, age, address, city, state, zip, country, phone):
    # Consider using a dictionary or object instead
    pass
```

---

## COMMON PATTERNS AND IDIOMS

### Early Return Pattern
```python
def process_data(data):
    """Process data with early returns for edge cases"""
    if not data:
        return None
    
    if len(data) < 3:
        return data
    
    # Main processing logic
    return [item * 2 for item in data]
```

---

### Guard Clauses
```python
def divide_numbers(a, b):
    """Divide with guard clauses"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    
    return a / b
```

---

### Factory Functions
```python
def create_calculator(operation):
    """Factory function for calculators"""
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else None
    }
    
    return operations.get(operation)

# Usage
add_func = create_calculator("add")
print(add_func(5, 3))  # 8
```

---

## BEST PRACTICES

### 1. Always Include Docstrings
```python
def good_function(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    """
    pass
```

---

### 2. Use Type Hints When Appropriate
```python
def calculate_average(numbers: List[float]) -> float:
    """Calculate average with type hints"""
    return sum(numbers) / len(numbers)
```

---

### 3. Handle Errors Gracefully
```python
def safe_divide(a, b):
    """Division with error handling"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid types")
        return None
```

---

## SUMMARY TABLE

| Feature | Description | Use Case |
|---------|-------------|----------|
| **def** | Define function | Standard function creation |
| **Parameters** | Function inputs | Pass data to functions |
| **return** | Send value back | Output function results |
| **Default params** | Optional arguments | Flexible function calls |
| ***args** | Variable positional args | Unknown number of arguments |
| ****kwargs** | Variable keyword args | Unknown keyword arguments |
| **lambda** | Anonymous function | Short, inline functions |
| **global** | Access global scope | Modify global variables |
| **nonlocal** | Access enclosing scope | Nested function variables |
| **Recursion** | Self-calling function | Divide-and-conquer problems |
| **Decorators** | Wrap functions | Add functionality |
| **Type hints** | Specify types | Code documentation/checking |

---

## KEY TAKEAWAYS

1. **Modularity**: Functions break code into reusable, testable components
2. **Parameters**: Accept input through positional, keyword, default, *args, **kwargs
3. **Return Values**: Functions can return single values, tuples, or None
4. **Scope**: Understand local, global, and nonlocal variable access
5. **Lambda**: Use for short, inline anonymous functions
6. **Recursion**: Functions can call themselves for iterative problems
7. **Documentation**: Always include docstrings for clarity
8. **Type Hints**: Optional but helpful for code clarity and IDE support
9. **Single Responsibility**: Each function should have one clear purpose
10. **Error Handling**: Use try/except and validation for robust functions

---

## EXTERNAL RESOURCES

- **Official Docs**: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- **W3Schools**: https://www.w3schools.com/python/python_functions.asp
- **Real Python**: https://realpython.com/defining-your-own-python-function/
- **PEP 257**: Docstring Conventions
- **PEP 484**: Type Hints

---

**Last Updated**: December 2025  
**Python Version**: 3.7+  
**Concept Level**: Fundamental programming structure
```python
def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    """
    Calculate compound interest using the compound interest formula.
    
    Args:
        principal (float): Initial amount of money
        rate (float): Annual interest rate as decimal (e.g., 0.05 for 5%)
        time (int): Number of years
        compound_frequency (int, optional): Times interest compounds per year. Defaults to 1.
    
    Returns:
        tuple: (final_amount, interest_earned)
        
    Raises:
        ValueError: If principal, rate, or time are negative
        
    Example:
        >>> principal = 1000
        >>> rate = 0.05
        >>> time = 3
        >>> final, interest = calculate_compound_interest(principal, rate, time)
        >>> print(f"Final amount: ${final:.2f}")
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative")
        
    final_amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    interest_earned = final_amount - principal
    
    return final_amount, interest_earned
```

### Lambda Functions (Anonymous Functions)
```python
# W3Schools Lambda Integration
# Simple lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple parameters  
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# Lambda in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

### Recursive Functions
```python
def factorial(n):
    """
    Calculate factorial using recursion
    
    Parameters:
    n (int): Non-negative integer
    
    Returns:
    int: Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
```

## Quality Assessment

### Function Testing Strategy
```python
def test_function():
    """
    Comprehensive testing approach for functions
    """
    # Test with normal values
    assert calculate_area(5, 4) == 20
    
    # Test with edge cases
    assert calculate_area(0, 5) == 0
    
    # Test with decimal values
    assert calculate_area(2.5, 3.0) == 7.5
    
    print("All function tests passed!")

test_function()
```

### Common Function Errors and Debugging
- **Indentation Errors**: Function body must be properly indented
- **Parameter Mismatches**: Ensure correct number and type of arguments
- **Scope Issues**: Distinguish between local and global variable access
- **Return Statement Placement**: Return should be inside function, proper indentation
- **Function Call Errors**: Verify function name spelling and argument order

### Function Design Principles
1. **Single Responsibility**: Each function should have one clear purpose
2. **Clear Naming**: Function names should describe their action or purpose
3. **Appropriate Parameters**: Include necessary inputs, avoid excessive parameters
4. **Consistent Return Types**: Functions should return consistent data types
5. **Documentation**: All functions require clear docstrings and comments

## Backlink Reference System

### Incoming Links (Concepts that reference Functions)
- [[VARIABLES]] → Functions create and manipulate variables with local/global scope
- [[CONTROL_STRUCTURES]] → Functions contain and organize control flow logic
- [[INPUT_OUTPUT_OPERATIONS]] → Functions often encapsulate I/O operations for reusability
- Program Design → Functions enable modular, organized program architecture
- Code Testing → Functions create testable, isolated units of code
- Problem Decomposition → Functions break complex problems into manageable components

### Outgoing Links (Concepts Functions reference)
- [[PSEUDOCODE]] ← Functions designed first in pseudocode before implementation
- [[VARIABLES]] ← Functions declare local variables and access global variables
- [[CONTROL_STRUCTURES]] ← Functions implement loops, conditionals, and decision logic
- Parameter Passing ← Functions use various parameter passing techniques
- Return Values ← Functions send processed data back to calling code
- Scope Management ← Functions manage variable accessibility and lifetime

### Cross-Reference Networks
- **Programming Paradigms**: Procedural programming relies heavily on function organization
- **Software Engineering**: Functions enable code reusability, maintainability, and testing
- **Problem Solving**: Functions support divide-and-conquer problem-solving methodology
- **Code Quality**: Functions improve code organization, readability, and debugging capabilities

## Integration Points

### Course Integration
- **Project Applications**: All course projects require custom function implementation
- **Exam Preparation**: Functions appear in coding problems, scope questions, and program design
- **Lab Exercises**: Function writing, calling, and debugging practiced weekly
- **Problem Solving**: Functions essential for breaking complex assignments into manageable tasks

### Professional Development Connections
- **Software Engineering**: Functions form foundation of modular software design
- **Code Review Practices**: Function quality, documentation, and design patterns
- **Team Development**: Functions enable collaborative programming through clear interfaces
- **Industry Standards**: Professional coding standards emphasize function best practices

### Advanced Programming Pathways  
- **Object-Oriented Programming**: Functions evolve into methods within classes
- **Functional Programming**: Functions become first-class objects with advanced techniques
- **Algorithm Design**: Functions implement and encapsulate algorithmic solutions
- **Software Architecture**: Functions scale into modules, packages, and system components

---
*Last Updated: Current Session - Sub-Atomic Node with W3Schools Primary Source Integration*
*Node Family: Programming Structures → Code Organization → Function Systems*
*Cross-Reference Capacity: 15+ interconnected concepts with comprehensive backlinking*