# LOOPS

## Core Definition
**Loops** are control structures that enable repeated execution of code blocks based on specified conditions or iteration patterns. Python provides `for` loops for definite iteration over sequences and `while` loops for indefinite iteration based on conditions. Essential for processing collections, automating tasks, and implementing algorithms.

**Tags**: #loops #iteration #for #while #break #continue #range #enumerate #nested-loops

---

## COMPLETE LOOP SYNTAX QUICK REFERENCE

### LOOP OPERATIONS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# FOR LOOP - DEFINITE ITERATION
# ═══════════════════════════════════════════════════════════════════════════
for item in iterable:           # Iterable | Iterate over items | Executes block for each item
for i in range(n):              # Range | Iterate n times | Executes block 0 to n-1
for i in range(start, stop):    # Range | Iterate from start to stop-1 | Executes block in range
for i in range(start, stop, step): # Range + step | Iterate with step | Executes every step
for i, item in enumerate(list): # List | Get index and item | Returns (index, item) pairs
for k, v in dict.items():       # Dict | Iterate key-value pairs | Returns (key, value) pairs
for item in reversed(iterable): # Iterable | Iterate in reverse | Executes in reverse order
for item in sorted(iterable):   # Iterable | Iterate sorted | Executes in sorted order
for x in iterable if condition: # ERROR: No inline if | Use comprehension or if inside loop

# ═══════════════════════════════════════════════════════════════════════════
# WHILE LOOP - INDEFINITE ITERATION
# ═══════════════════════════════════════════════════════════════════════════
while condition:                # Condition | Loop while True | Executes until condition False
while True:                     # Infinite | Infinite loop | Executes forever (use break)
while condition and flag:       # Multiple conditions | Loop with AND | Executes if all True
while condition or flag:        # Multiple conditions | Loop with OR | Executes if any True

# ═══════════════════════════════════════════════════════════════════════════
# LOOP CONTROL STATEMENTS
# ═══════════════════════════════════════════════════════════════════════════
break                           # No args | Exit loop immediately | Terminates loop
continue                        # No args | Skip to next iteration | Jumps to loop start
pass                            # No args | Do nothing (placeholder) | No operation
else: (after loop)              # No condition | Execute if no break | Runs after normal completion

# ═══════════════════════════════════════════════════════════════════════════
# LOOP HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
range(stop)                     # Stop value | Generate 0 to stop-1 | Returns range object
range(start, stop)              # Start, stop | Generate start to stop-1 | Returns range object
range(start, stop, step)        # Start, stop, step | Generate with step | Returns range object
enumerate(iterable)             # Iterable | Add index counter | Returns (index, item) pairs
enumerate(iterable, start=n)    # Iterable + start | Custom starting index | Returns (index, item) from n
zip(iter1, iter2)               # Multiple iterables | Combine iterables | Returns tuples of paired items
reversed(iterable)              # Iterable | Reverse order | Returns reversed iterator
sorted(iterable)                # Iterable | Sort items | Returns sorted list

# ═══════════════════════════════════════════════════════════════════════════
# NESTED LOOPS
# ═══════════════════════════════════════════════════════════════════════════
for i in outer:                 # Outer loop | First level iteration | Executes outer loop
    for j in inner:             # Inner loop | Second level iteration | Executes inner for each outer
        operation               # Code block | Process nested items | Executes for all combinations
```

---

## DETAILED EXAMPLES

### 1. Basic For Loop with Lists

```python
# Iterate over list items
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
date
```

---

### 2. For Loop with range()

```python
# range(stop) - from 0 to stop-1
for i in range(5):
    print(i)

print()

# range(start, stop) - from start to stop-1
for i in range(2, 7):
    print(i)

print()

# range(start, stop, step) - with step increment
for i in range(0, 10, 2):
    print(i)
```

**Output:**
```
0
1
2
3
4

2
3
4
5
6

0
2
4
6
8
```

---

### 3. For Loop with enumerate()

```python
# Get index and value simultaneously
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

print()

# Start enumerate from custom number
for index, color in enumerate(colors, start=1):
    print(f"#{index}: {color}")
```

**Output:**
```
Index 0: red
Index 1: green
Index 2: blue

#1: red
#2: green
#3: blue
```

---

### 4. Iterating Over Dictionaries

```python
# Iterate over dictionary
student_grades = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 96
}

# Iterate keys only
for name in student_grades:
    print(name)

print()

# Iterate key-value pairs
for name, grade in student_grades.items():
    print(f"{name}: {grade}")

print()

# Iterate values only
for grade in student_grades.values():
    print(grade)
```

**Output:**
```
Alice
Bob
Charlie
Diana

Alice: 92
Bob: 85
Charlie: 78
Diana: 96

92
85
78
96
```

---

### 5. While Loop - Basic Usage

```python
# Simple while loop with counter
count = 0

while count < 5:
    print(f"Count: {count}")
    count += 1

print("Done!")
```

**Output:**
```
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
Done!
```

---

### 6. While Loop - Input Validation

```python
# Input validation with while loop
while True:
    age = input("Enter your age (18-100): ")
    
    if not age.isdigit():
        print("Please enter a number!")
        continue
    
    age = int(age)
    
    if age < 18 or age > 100:
        print("Age must be between 18 and 100")
        continue
    
    print(f"Valid age: {age}")
    break
```

**Output (example interaction):**
```
Enter your age (18-100): abc
Please enter a number!
Enter your age (18-100): 15
Age must be between 18 and 100
Enter your age (18-100): 25
Valid age: 25
```

---

### 7. Loop Control - break Statement

```python
# Using break to exit loop early
numbers = [1, 3, 5, 7, 8, 10, 12]

for num in numbers:
    print(num)
    if num == 7:
        print("Found 7, stopping!")
        break
```

**Output:**
```
1
3
5
7
Found 7, stopping!
```

---

### 8. Loop Control - continue Statement

```python
# Using continue to skip iterations
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```

**Output:**
```
1
3
5
7
9
```

---

### 9. Loop with else Clause

```python
# else executes if loop completes without break
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
else:
    print("No even numbers found!")

print()

# Example with break
numbers2 = [1, 3, 5, 8, 9]

for num in numbers2:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
else:
    print("No even numbers found!")
```

**Output:**
```
No even numbers found!

Found even number: 8
```

---

### 10. Nested Loops

```python
# Simple nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
    print()

# Multiplication table
print("Multiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{product:3d}", end=" ")
    print()
```

**Output:**
```
i=1, j=1
i=1, j=2
i=1, j=3

i=2, j=1
i=2, j=2
i=2, j=3

i=3, j=1
i=3, j=2
i=3, j=3

Multiplication Table:
  1   2   3   4   5 
  2   4   6   8  10 
  3   6   9  12  15 
  4   8  12  16  20 
  5  10  15  20  25 
```

---

## COMMON USE CASES

### 1. Accumulator Pattern

```python
# Sum all numbers in list
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Total: {total}")

# Count specific items
fruits = ["apple", "banana", "apple", "cherry", "apple"]
apple_count = 0

for fruit in fruits:
    if fruit == "apple":
        apple_count += 1

print(f"Apples: {apple_count}")
```

**Output:**
```
Total: 150
Apples: 3
```

---

### 2. Finding Min/Max

```python
# Find minimum and maximum
numbers = [45, 12, 67, 23, 89, 34]

# Initialize with first element
minimum = numbers[0]
maximum = numbers[0]

for num in numbers[1:]:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print(f"Min: {minimum}, Max: {maximum}")

# Or use built-in functions
print(f"Min: {min(numbers)}, Max: {max(numbers)}")
```

**Output:**
```
Min: 12, Max: 89
Min: 12, Max: 89
```

---

### 3. Building New Lists

```python
# Create new list from existing list
numbers = [1, 2, 3, 4, 5]
squared = []

for num in numbers:
    squared.append(num ** 2)

print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Filter list
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"Evens: {evens}")
```

**Output:**
```
Original: [1, 2, 3, 4, 5]
Squared: [1, 4, 9, 16, 25]
Evens: [2, 4]
```

---

### 4. String Processing

```python
# Iterate over characters in string
text = "Python"

for char in text:
    print(char)

print()

# Count vowels
vowel_count = 0
for char in text.lower():
    if char in "aeiou":
        vowel_count += 1

print(f"Vowels in '{text}': {vowel_count}")
```

**Output:**
```
P
y
t
h
o
n

Vowels in 'Python': 1
```

---

### 5. Menu Systems

```python
def menu_system():
    """Interactive menu using while loop"""
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Option A")
        print("2. Option B")
        print("3. Option C")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == "1":
            print("You selected Option A")
        elif choice == "2":
            print("You selected Option B")
        elif choice == "3":
            print("You selected Option C")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# menu_system()  # Uncomment to run
```

---

### 6. Pattern Generation

```python
# Right triangle
for i in range(1, 6):
    print("*" * i)

print()

# Pyramid
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

print()

# Number patterns
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

**Output:**
```
*
**
***
****
*****

    *
   ***
  *****
 *******
*********

1
12
123
1234
12345
```

---

### 7. Data Processing with zip()

```python
# Combine multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Los Angeles", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

print()

# Calculate parallel list operations
prices = [10.99, 25.50, 15.75]
quantities = [2, 1, 3]

total = 0
for price, qty in zip(prices, quantities):
    subtotal = price * qty
    total += subtotal
    print(f"${price} x {qty} = ${subtotal:.2f}")

print(f"Total: ${total:.2f}")
```

**Output:**
```
Alice, 25, from New York
Bob, 30, from Los Angeles
Charlie, 35, from Chicago

$10.99 x 2 = $21.98
$25.5 x 1 = $25.50
$15.75 x 3 = $47.25
Total: $94.73
```

---

### 8. File Processing Simulation

```python
# Process lines from data (simulating file reading)
data_lines = [
    "Alice,92",
    "Bob,85",
    "Charlie,78",
    "Diana,96"
]

students = []
for line in data_lines:
    name, grade = line.split(",")
    students.append({"name": name, "grade": int(grade)})

# Calculate statistics
total_grade = 0
for student in students:
    print(f"{student['name']}: {student['grade']}")
    total_grade += student['grade']

average = total_grade / len(students)
print(f"\nAverage grade: {average:.2f}")
```

**Output:**
```
Alice: 92
Bob: 85
Charlie: 78
Diana: 96

Average grade: 87.75
```

---

### 9. List Comprehension Alternative

```python
# Traditional loop
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)

print(f"Loop result: {squares}")

# List comprehension (more Pythonic)
squares_comp = [num ** 2 for num in numbers]
print(f"Comprehension result: {squares_comp}")

# Filtered list comprehension
evens = [num for num in numbers if num % 2 == 0]
print(f"Evens: {evens}")
```

**Output:**
```
Loop result: [1, 4, 9, 16, 25]
Comprehension result: [1, 4, 9, 16, 25]
Evens: [2, 4]
```

---

### 10. Searching in Loops

```python
# Linear search
numbers = [45, 23, 67, 12, 89, 34]
target = 67

found = False
for i, num in enumerate(numbers):
    if num == target:
        print(f"Found {target} at index {i}")
        found = True
        break

if not found:
    print(f"{target} not found")

# Search with condition
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 78}
]

for student in students:
    if student["grade"] >= 90:
        print(f"{student['name']} has an A!")
```

**Output:**
```
Found 67 at index 2
Alice has an A!
```

---

## ADVANCED PATTERNS

### 1. Loop with Multiple Conditions

```python
# Complex while loop conditions
count = 0
max_count = 10
found = False

while count < max_count and not found:
    count += 1
    print(f"Checking {count}...")
    
    if count == 7:
        print("Found lucky number!")
        found = True

print(f"Stopped at count: {count}")
```

**Output:**
```
Checking 1...
Checking 2...
Checking 3...
Checking 4...
Checking 5...
Checking 6...
Checking 7...
Found lucky number!
Stopped at count: 7
```

---

### 2. Sentinel-Controlled Loop

```python
# Loop until sentinel value
print("Enter numbers (type 'done' to finish):")

total = 0
count = 0

# Simulate input
inputs = ["10", "20", "30", "done"]

for value in inputs:
    print(f"Input: {value}")
    
    if value.lower() == "done":
        break
    
    try:
        number = float(value)
        total += number
        count += 1
    except ValueError:
        print("Invalid number, skipping...")

if count > 0:
    average = total / count
    print(f"\nAverage: {average:.2f}")
else:
    print("No numbers entered")
```

**Output:**
```
Input: 10
Input: 20
Input: 30
Input: done

Average: 20.00
```

---

### 3. Nested Loop with Break

```python
# Breaking out of nested loops
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False

for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == target:
            print(f"Found {target} at position ({i}, {j})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{target} not found in matrix")
```

**Output:**
```
Found 5 at position (1, 1)
```

---

### 4. Parallel Iteration

```python
# Iterate multiple lists with different lengths
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']

# zip stops at shortest list
print("Using zip (stops at shortest):")
for num, letter in zip(list1, list2):
    print(f"{num} - {letter}")

print()

# Manual parallel iteration
print("Manual iteration (handle different lengths):")
max_len = max(len(list1), len(list2))
for i in range(max_len):
    num = list1[i] if i < len(list1) else None
    letter = list2[i] if i < len(list2) else None
    print(f"{num} - {letter}")
```

**Output:**
```
Using zip (stops at shortest):
1 - a
2 - b
3 - c

Manual iteration (handle different lengths):
1 - a
2 - b
3 - c
None - d
```

---

### 5. Generator Expression in Loop

```python
# Generator for memory-efficient iteration
def large_range_simulation():
    """Simulate processing large dataset"""
    # Generator expression (lazy evaluation)
    squares_gen = (x ** 2 for x in range(10))
    
    print("Processing with generator:")
    for i, square in enumerate(squares_gen, 1):
        print(f"Item {i}: {square}")
        if i >= 5:  # Process only first 5
            print("Stopping early...")
            break

large_range_simulation()
```

**Output:**
```
Processing with generator:
Item 1: 0
Item 2: 1
Item 3: 4
Item 4: 9
Item 5: 16
Stopping early...
```

---

## BEST PRACTICES

### 1. Choose the Right Loop Type

```python
# ✓ GOOD: Use for loop for definite iteration
for i in range(10):
    print(i)

# ✓ GOOD: Use while loop for indefinite iteration
while condition:
    # Process until condition is False
    pass

# ✗ BAD: Using while for definite iteration
i = 0
while i < 10:
    print(i)
    i += 1  # Easy to forget, risk of infinite loop
```

---

### 2. Avoid Infinite Loops

```python
# ✓ GOOD: Clear termination condition
count = 0
while count < 10:
    print(count)
    count += 1  # Always increment

# ✗ BAD: No termination (infinite loop)
# while True:
#     print("Forever!")  # Missing break statement

# ✓ GOOD: Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
```

---

### 3. Use Descriptive Variable Names

```python
# ✓ GOOD: Descriptive names
for student_name in student_list:
    print(student_name)

for index, grade in enumerate(grades):
    print(f"Student {index + 1}: {grade}")

# ✗ BAD: Single letter variables (except simple counters)
for x in y:
    print(x)
```

---

### 4. Don't Modify List While Iterating

```python
# ✗ BAD: Modifying list during iteration
numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # Can cause issues

# ✓ GOOD: Create new list or use list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)

# ✓ GOOD: Iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # Iterate over copy
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)
```

**Output:**
```
[1, 3, 5]
[1, 3, 5]
```

---

### 5. Use enumerate() Instead of range(len())

```python
items = ["apple", "banana", "cherry"]

# ✗ BAD: Using range(len())
for i in range(len(items)):
    print(f"{i}: {items[i]}")

print()

# ✓ GOOD: Using enumerate()
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

**Output:**
```
0: apple
1: banana
2: cherry

0: apple
1: banana
2: cherry
```

---

## PERFORMANCE TIPS

### 1. List Comprehension vs Loop

```python
import time

# Traditional loop
start = time.time()
squares = []
for i in range(100000):
    squares.append(i ** 2)
loop_time = time.time() - start

# List comprehension (faster)
start = time.time()
squares_comp = [i ** 2 for i in range(100000)]
comp_time = time.time() - start

print(f"Loop time: {loop_time:.4f}s")
print(f"Comprehension time: {comp_time:.4f}s")
print(f"Speedup: {loop_time / comp_time:.2f}x")
```

---

### 2. Minimize Function Calls in Loops

```python
# ✗ SLOWER: Function call in every iteration
data = list(range(1000))
result = []
for item in data:
    result.append(str(item))  # str() called 1000 times

# ✓ FASTER: Store function reference
data = list(range(1000))
result = []
str_func = str  # Store reference
for item in data:
    result.append(str_func(item))

# ✓ FASTEST: Use list comprehension or map
result = [str(item) for item in data]
# or
result = list(map(str, data))
```

---

## SUMMARY TABLE

| Loop Type | Use Case | Example |
|-----------|----------|---------|
| **for** | Definite iteration | `for item in list:` |
| **while** | Indefinite iteration | `while condition:` |
| **break** | Exit loop early | `if found: break` |
| **continue** | Skip iteration | `if invalid: continue` |
| **else** | After normal completion | `for...else:` |
| **enumerate()** | Index + value | `for i, val in enumerate(list):` |
| **zip()** | Parallel iteration | `for a, b in zip(l1, l2):` |
| **range()** | Number sequence | `for i in range(10):` |
| **Nested** | Multi-dimensional | `for i... for j...` |

---

## KEY TAKEAWAYS

1. **For Loop**: Use for definite iteration over sequences and ranges
2. **While Loop**: Use for indefinite iteration based on conditions
3. **break**: Exit loop immediately, skipping else clause
4. **continue**: Skip current iteration, proceed to next
5. **else**: Executes only if loop completes without break
6. **enumerate()**: Get index and value simultaneously
7. **zip()**: Iterate multiple sequences in parallel
8. **range()**: Generate number sequences efficiently
9. **Nested Loops**: Use for multi-dimensional processing (limit depth)
10. **Optimization**: Prefer list comprehensions for simple transformations

---

## COMMON PITFALLS

### 1. Infinite Loops
```python
# Always ensure loop variables are modified
# Always have a clear exit condition
# Use break statements in while True loops
```

### 2. Off-by-One Errors
```python
# range(n) goes from 0 to n-1, not n
# Remember Python uses 0-based indexing
```

### 3. Modifying Collections During Iteration
```python
# Create a copy or new list instead
# Use list comprehensions for filtering
```

### 4. Nested Loop Complexity
```python
# Limit nesting to 2-3 levels
# Consider alternative approaches for deep nesting
```

---

## EXTERNAL RESOURCES

- **Official Docs**: https://docs.python.org/3/tutorial/controlflow.html
- **W3Schools**: https://www.w3schools.com/python/python_for_loops.asp
- **Real Python**: https://realpython.com/python-for-loop/
- **Python Wiki**: https://wiki.python.org/moin/ForLoop

---

**Last Updated**: December 2025  
**Python Version**: 3.7+  
**Concept Level**: Fundamental control structure
