import functools


# 1. IIFE (Immediately Invoked Function Expression)
# Definition and execution in one step.
print("1. IIFE (Immediately Invoked):")
x = 5
result = (lambda x: x * 5)(x)
print(f"   (lambda x: x * 5)(5) -> {result}")




# 2. map() - Transformation
# Apply a function to every item in an iterable.
print("\n2. With map() (Transform List):")
nums = [1, 2, 3, 4]
squared = list(map(lambda n: n**2, nums))
print(f"   Original: {nums} -> Squared: {squared}")




# 3. filter() - Selection
# Keep items that satisfy a condition.
print("\n3. With filter() (Filter List):")
evens = list(filter(lambda n: n % 2 == 0, nums))
print(f"   Original: {nums} -> Evens: {evens}")




# 4. reduce() - Accumulation
# Combine all items into a single value (requires functools).
print("\n4. With reduce() (Accumulate):")
product = functools.reduce(lambda a, b: a * b, nums)
print(f"   Product of {nums}: {product}")




# 5. sorted() - Custom Sorting Key
# Sort complex objects by a specific attribute.
print("\n5. With sorted() (Custom Sort Key):")
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda p: p[1]) # Sort by the string (2nd element)
print(f"   Pairs: {pairs}")
print(f"   Sorted by name: {sorted_pairs}")




# 6. max() / min() - Custom Comparison Key
# Find max/min based on a specific attribute.
print("\n6. With max() (Custom Key):")
words = ["apple", "banana", "pear"]
longest = max(words, key=lambda w: len(w))
print(f"   Words: {words}")
print(f"   Longest word: {longest}")




# 7. Function Factory (Closure)
# Create functions dynamically.
print("\n7. Function Factory (Closure):")
def power_factory(n):
    return lambda x: x ** n

square = power_factory(2) # Returns a lambda that squares
cube = power_factory(3)   # Returns a lambda that cubes
print(f"   Square of 4: {square(4)}")
print(f"   Cube of 4: {cube(4)}")

# 8. Dictionary Dispatch (Switch/Case replacement)
# Select and execute functions based on a key.
print("\n8. Dictionary Dispatch Table:")
operations = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b
}
op = 'mul'
val1, val2 = 5, 3
result_op = operations[op](val1, val2)
print(f"   Operation '{op}' on {val1}, {val2} -> {result_op}")
