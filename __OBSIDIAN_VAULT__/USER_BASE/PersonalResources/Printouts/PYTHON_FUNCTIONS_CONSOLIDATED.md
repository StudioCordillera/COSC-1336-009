## STRING METHODS

**CASE CONVERSION:**
```python
str.upper()                  # "hello" → "HELLO"
str.lower()                  # "HELLO" → "hello"  
str.capitalize()             # "hello world" → "Hello world"
str.title()                  # "hello world" → "Hello World"
str.swapcase()               # "Hello" → "hELLO"
str.casefold()               # "ß" → "ss" (aggressive lowercase)
```

**WHITESPACE:**
```python
str.strip()                  # "  hello  " → "hello"
str.strip(chars)             # "---hello---" → "hello" with .strip('-')
str.lstrip()                 # "  hello" → "hello"
str.rstrip()                 # "hello  " → "hello"
str.removeprefix(prefix)     # "TestString" → "String"
str.removesuffix(suffix)     # "hello.txt" → "hello"
```

**SPLITTING & JOINING:**
```python
str.split()                  # "a b c" → ['a', 'b', 'c']
str.split(sep)               # "a,b,c" → ['a', 'b', 'c']
str.split(sep, maxsplit)     # "a,b,c,d" → ['a', 'b', 'c,d']
str.rsplit()                 # Split from right
str.rsplit(sep, maxsplit)    # "a,b,c,d" → ['a,b,c', 'd']
str.splitlines()             # "line1\nline2" → ['line1', 'line2']
str.splitlines(keepends)     # Keep line breaks
str.partition(sep)           # "a-b-c" → ('a', '-', 'b-c')
str.rpartition(sep)          # "a-b-c" → ('a-b', '-', 'c')
sep.join(iterable)           # ','.join(['a','b']) → "a,b"
```

**SEARCH & REPLACE:**
```python
str.find(sub)                # "hello".find('l') → 2
str.find(sub, start)         # Search from position
str.find(sub, start, end)    # Search in range
str.rfind(sub)               # Find from right
str.index(sub)               # Like find() but raises ValueError
str.rindex(sub)              # Index from right
str.count(sub)               # "hello".count('l') → 2
str.count(sub, start, end)   # Count in range
str.replace(old, new)        # "hello".replace('l', 'L') → "heLLo"
str.replace(old, new, count) # Replace first n occurrences
```

**VALIDATION/CHECKS:**
```python
str.startswith(prefix)       # "hello.txt".startswith("hello") → True
str.startswith(tuple)        # Check multiple prefixes
str.endswith(suffix)         # "hello.txt".endswith(".txt") → True
str.endswith(tuple)          # Check multiple suffixes
str.isalpha()                # "abc".isalpha() → True
str.isdigit()                # "123".isdigit() → True
str.isalnum()                # "abc123".isalnum() → True
str.isspace()                # "   ".isspace() → True
str.isupper()                # "HELLO".isupper() → True
str.islower()                # "hello".islower() → True
str.istitle()                # "Hello World".istitle() → True
str.isdecimal()              # "123".isdecimal() → True
str.isnumeric()              # "①②③".isnumeric() → True
str.isidentifier()           # "var_name".isidentifier() → True
str.isprintable()            # Check all chars printable
str.isascii()                # Check all chars ASCII
```

**ALIGNMENT & PADDING:**
```python
str.center(width)            # "hi".center(10) → "    hi    "
str.center(width, fillchar)  # "hi".center(10, '*') → "****hi****"
str.ljust(width)             # "hi".ljust(10) → "hi        "
str.ljust(width, fillchar)   # "hi".ljust(10, '-') → "hi--------"
str.rjust(width)             # "hi".rjust(10) → "        hi"
str.rjust(width, fillchar)   # "hi".rjust(10, '-') → "--------hi"
str.zfill(width)             # "42".zfill(5) → "00042"
str.expandtabs()             # "\t" → "        " (8 spaces)
str.expandtabs(tabsize)      # "\t".expandtabs(4) → "    "
```

**FORMATTING:**
```python
str.format(*args, **kwargs)  # "Hello {}".format("World")
str.format_map(mapping)      # "{name}".format_map({'name': 'Alice'})
f"{var}"                     # f"Hello {name}"
f"{var:format_spec}"         # f"{value:.2f}"
f"{expr=}"                   # f"{x=}" → "x=5"
"%s %d" % (str, int)         # "Hello %s" % "World"
```

**ENCODING & TRANSLATION:**
```python
str.encode()                 # "hello".encode() → b'hello'
str.encode(encoding)         # "hello".encode('utf-8')
str.encode(encoding, errors) # Handle errors: 'ignore', 'replace'
str.translate(table)         # Translate using table
str.maketrans(x, y)          # str.maketrans("abc", "123")
str.maketrans(dict)          # str.maketrans({'a': '1', 'b': '2'})
```

**SLICING & ACCESS:**
```python
str[index]                   # "hello"[0] → 'h'
str[start:end]               # "hello"[1:4] → "ell"
str[start:end:step]          # "hello"[::2] → "hlo"
str[-1]                      # "hello"[-1] → 'o'
len(str)                     # len("hello") → 5
str in other                 # 'lo' in "hello" → True
str not in other             # 'x' not in "hello" → True
```

---

## LIST METHODS

**ADDING ELEMENTS:**
```python
list.append(item)            # nums.append(4) adds to end
list.extend(iterable)        # nums.extend([4, 5, 6]) adds multiple
list.insert(index, item)     # nums.insert(0, 99) inserts at position
```

**REMOVING ELEMENTS:**
```python
list.remove(item)            # nums.remove(2) removes first occurrence
list.pop()                   # nums.pop() removes & returns last item
list.pop(index)              # nums.pop(0) removes & returns at index
list.clear()                 # nums.clear() empties list
```

**SORTING & REVERSING:**
```python
list.sort()                  # nums.sort() sorts in-place
list.sort(reverse=True)      # Sort descending
list.sort(key=function)      # Sort by custom key
list.reverse()               # nums.reverse() reverses in-place
```

**SEARCHING:**
```python
list.index(item)             # nums.index(5) returns first index
list.index(item, start)      # Search from start position
list.index(item, start, end) # Search in range
list.count(item)             # nums.count(2) counts occurrences
```

**COPYING:**
```python
list.copy()                  # nums.copy() creates shallow copy
list[:]                      # nums[:] also creates copy
```

**SLICING:**
```python
list[start:end]              # nums[1:4] gets slice
list[start:end:step]         # nums[::2] every other item
list[::-1]                   # nums[::-1] reversed copy
```

---

## DICTIONARY METHODS

**ACCESSING:**
```python
dict[key]                    # person['name'] gets value or KeyError
dict.get(key)                # person.get('name') returns None if missing
dict.get(key, default)       # person.get('age', 0) returns default
dict.keys()                  # person.keys() returns view of keys
dict.values()                # person.values() returns view of values  
dict.items()                 # person.items() returns (key, value) pairs
```

**MODIFYING:**
```python
dict[key] = value            # person['name'] = 'Alice' adds/updates
dict.update(other)           # person.update({'age': 25})
dict.update(**kwargs)        # person.update(age=25, city='NYC')
dict.setdefault(key)         # Get or set with default value
dict.setdefault(key, default)  # person.setdefault('age', 0)
```

**REMOVING:**
```python
dict.pop(key)                # person.pop('age') removes & returns value
dict.pop(key, default)       # Returns default if key not found
dict.popitem()               # person.popitem() removes & returns last pair
dict.clear()                 # person.clear() empties dictionary
del dict[key]                # del person['age'] removes key
```

**CHECKING:**
```python
key in dict                  # 'name' in person → True/False
key not in dict              # 'email' not in person → True/False
```

**COPYING:**
```python
dict.copy()                  # person.copy() shallow copy
dict.fromkeys(seq)           # dict.fromkeys(['a','b'], 0)
dict.fromkeys(seq, value)    # Initialize with value
```

---

## TUPLE METHODS

**Note: Only 2 methods - tuples are immutable!**

**SEARCHING:**
```python
tuple.count(item)            # coords.count(5) counts occurrences
tuple.index(item)            # coords.index(5) returns first index
tuple.index(item, start)     # Search from start position
tuple.index(item, start, end)  # Search in range
```

**ACCESSING:**
```python
tuple[index]                 # coords[0] gets element
tuple[start:end]             # coords[1:3] gets slice
len(tuple)                   # len(coords) gets length
```

**UNPACKING:**
```python
a, b = tuple                 # x, y = (1, 2)
a, *rest = tuple             # first, *others = (1, 2, 3, 4)
*start, last = tuple         # *firsts, last = (1, 2, 3, 4)
```

---

## SET METHODS

**ADDING:**
```python
set.add(item)                # nums.add(5) adds element
set.update(iterable)         # nums.update([5, 6, 7]) adds multiple
```

**REMOVING:**
```python
set.remove(item)             # nums.remove(5) removes or raises KeyError
set.discard(item)            # nums.discard(5) removes, no error if missing
set.pop()                    # nums.pop() removes & returns arbitrary element
set.clear()                  # nums.clear() empties set
```

**SET OPERATIONS:**
```python
set.union(other)             # a.union(b) or a | b
set.intersection(other)      # a.intersection(b) or a & b
set.difference(other)        # a.difference(b) or a - b
set.symmetric_difference(other)  # a.symmetric_difference(b) or a ^ b
```

**SET OPERATIONS (IN-PLACE):**
```python
set.update(other)            # a.update(b) or a |= b
set.intersection_update(other)  # a.intersection_update(b) or a &= b
set.difference_update(other)  # a.difference_update(b) or a -= b
set.symmetric_difference_update(other)  # a ^= b
```

**CHECKING:**
```python
set.issubset(other)          # a.issubset(b) or a <= b
set.issuperset(other)        # a.issuperset(b) or a >= b
set.isdisjoint(other)        # a.isdisjoint(b) checks no common elements
```

**COPYING:**
```python
set.copy()                   # nums.copy() creates shallow copy
```

---

## FILE OPERATIONS

**OPENING & CLOSING:**
```python
open(file, mode)             # f = open("file.txt", "r")
open(file, mode, encoding)   # f = open("file.txt", "r", encoding="utf-8")
file.close()                 # f.close() closes file
with open(file) as f:        # Context manager (auto-closes)
```

**MODES:**
```python
'r'                          # Read (default)
'w'                          # Write (overwrites)
'a'                          # Append
'r+'                         # Read and write
'w+'                         # Write and read (overwrites)
'rb'                         # Read binary
'wb'                         # Write binary
```

**READING:**
```python
file.read()                  # f.read() reads entire file
file.read(size)              # f.read(100) reads 100 bytes
file.readline()              # f.readline() reads one line
file.readlines()             # f.readlines() reads all lines into list
for line in file:            # Iterate lines efficiently
```

**WRITING:**
```python
file.write(string)           # f.write("Hello") writes string
file.writelines(list)        # f.writelines(['a\n', 'b\n']) writes list
```

**FILE POSITION:**
```python
file.tell()                  # f.tell() returns current position
file.seek(offset)            # f.seek(0) moves to position
file.seek(offset, whence)    # whence: 0=start, 1=current, 2=end
```

**FILE INFO:**
```python
file.name                    # f.name returns filename
file.mode                    # f.mode returns mode
file.closed                  # f.closed checks if closed
```

---

## INPUT/OUTPUT FUNCTIONS

**INPUT:**
```python
input()                      # name = input() reads line
input(prompt)                # name = input("Enter name: ")
```

**OUTPUT:**
```python
print(*objects)              # print("Hello", "World")
print(*objects, sep)         # print("a", "b", "c", sep=", ")
print(*objects, end)         # print("text", end=" ") no newline
print(*objects, file)        # print("text", file=f) write to file
print(*objects, flush)       # print("text", flush=True) force output
```

---

## BUILT-IN FUNCTIONS

**TYPE CONVERSION:**
```python
int(x)                       # int("42") → 42
int(x, base)                 # int("10", 16) → 16
float(x)                     # float("3.14") → 3.14
str(x)                       # str(42) → "42"
bool(x)                      # bool(0) → False
list(x)                      # list("abc") → ['a', 'b', 'c']
tuple(x)                     # tuple([1,2,3]) → (1, 2, 3)
set(x)                       # set([1,2,2,3]) → {1, 2, 3}
dict(x)                      # dict([('a',1), ('b',2)])
```

**MATH:**
```python
abs(x)                       # abs(-5) → 5
round(x)                     # round(3.7) → 4
round(x, n)                  # round(3.14159, 2) → 3.14
pow(x, y)                    # pow(2, 3) → 8
divmod(x, y)                 # divmod(10, 3) → (3, 1)
min(iterable)                # min([1,2,3]) → 1
min(*args)                   # min(1, 2, 3) → 1
max(iterable)                # max([1,2,3]) → 3
max(*args)                   # max(1, 2, 3) → 3
sum(iterable)                # sum([1,2,3]) → 6
sum(iterable, start)         # sum([1,2,3], 10) → 16
```

**SEQUENCES:**
```python
len(x)                       # len([1,2,3]) → 3
range(stop)                  # range(5) → 0,1,2,3,4
range(start, stop)           # range(2, 5) → 2,3,4
range(start, stop, step)     # range(0, 10, 2) → 0,2,4,6,8
sorted(iterable)             # sorted([3,1,2]) → [1,2,3]
sorted(iterable, reverse)    # sorted([3,1,2], reverse=True) → [3,2,1]
sorted(iterable, key)        # sorted(words, key=len)
reversed(iterable)           # reversed([1,2,3]) → iterator
enumerate(iterable)          # enumerate(['a','b']) → (0,'a'), (1,'b')
enumerate(iterable, start)   # enumerate(['a','b'], 1) → (1,'a'), (2,'b')
zip(*iterables)              # zip([1,2], ['a','b']) → (1,'a'), (2,'b')
```

**FUNCTIONAL:**
```python
map(function, iterable)      # map(str, [1,2,3]) → ['1','2','3']
filter(function, iterable)   # filter(None, [0,1,2,False]) → [1,2]
all(iterable)                # all([True, True, False]) → False
any(iterable)                # any([True, False, False]) → True
```

**TYPE CHECKING:**
```python
type(x)                      # type(5) → <class 'int'>
isinstance(x, type)          # isinstance(5, int) → True
isinstance(x, tuple)         # isinstance(5, (int, float)) → True
```

**OTHER:**
```python
chr(x)                       # chr(65) → 'A'
ord(x)                       # ord('A') → 65
hex(x)                       # hex(255) → '0xff'
oct(x)                       # oct(8) → '0o10'
bin(x)                       # bin(5) → '0b101'
id(x)                        # id(obj) returns memory address
hash(x)                      # hash("hello") returns hash value
repr(x)                      # repr("hi") → "'hi'"
ascii(x)                     # ascii("ü") → "'\\xfc'"
eval(expression)             # eval("2 + 2") → 4
exec(code)                   # exec("x = 5")
compile(source, filename, mode)  # Compile source code
```

---

## LOOPS & CONTROL

**FOR LOOPS:**
```python
for var in iterable:         # for x in [1,2,3]:
for i in range(n):           # for i in range(5):
for i in range(start, stop): # for i in range(2, 7):
for i in range(start, stop, step): # for i in range(0, 10, 2):
for i, val in enumerate(list):  # for i, x in enumerate(nums):
for i, val in enumerate(list, start): # for i, x in enumerate(nums, 1):
for k, v in dict.items():    # for key, val in person.items():
for a, b in zip(list1, list2):  # for x, y in zip(xs, ys):
for item in reversed(iterable): # for x in reversed([1,2,3]):
for item in sorted(iterable): # for x in sorted([3,1,2]):
```

**WHILE LOOPS:**
```python
while condition:             # while x < 10:
while True:                  # Infinite loop
while condition and flag:    # while x < 10 and running:
while condition or flag:     # while x < 10 or retry:
```

**CONTROL:**
```python
break                        # Exit loop immediately
continue                     # Skip to next iteration
pass                         # Do nothing (placeholder)
else: (after loop)           # else: print("No break")
```

**CONDITIONALS:**
```python
if condition:                # if x > 0:
elif condition:              # elif x == 0:
else:                        # else:
```

**COMPREHENSIONS:**
```python
[expr for var in iterable]   # [x*2 for x in range(5)]
[expr for var in iterable if cond]  # [x for x in range(10) if x % 2 == 0]
{expr for var in iterable}   # {x*2 for x in range(5)} set comprehension
{k:v for var in iterable}    # {x: x*2 for x in range(5)} dict comprehension
(expr for var in iterable)   # (x*2 for x in range(5)) generator expression
```1, p2):            # Multiple parameters
def func(param=default):     # With default value
def func(*args):             # Variable positional args
def func(**kwargs):          # Variable keyword args
def func(*args, **kwargs):   # Both
return value                 # Return value
return value1, value2        # Return multiple values (tuple)
return                       # Return None
return expr if cond else alt # Conditional return
```

**FUNCTION CALLS:**
```python
function_name()              # Call without arguments
function_name(arg)           # Positional argument
function_name(arg1, arg2)    # Multiple arguments
function_name(param=value)   # Keyword argument
function_name(*list)         # Unpack list as arguments
function_name(**dict)        # Unpack dict as keyword arguments
```

**LAMBDA:**
```python
lambda x: expression         # lambda x: x * 2
lambda x, y: expression      # lambda x, y: x + y
lambda: expression           # lambda: 42 (no parameters)
map(lambda x: expr, iterable) # map(lambda x: x*2, [1,2,3])
filter(lambda x: cond, iter) # filter(lambda x: x>0, nums)
sorted(iter, key=lambda x: x.attr) # sorted(people, key=lambda p: p.age)
```

**SCOPE:**
```python
global var                   # Declare global variable
nonlocal var                 # Access enclosing function variable
locals()                     # Get local namespace dict
globals()                    # Get global namespace dict
```

**DECORATORS:**
```python
@decorator                   # Basic decorator
@decorator(args)             # Decorator with arguments
@staticmethod                # Static method
@classmethod                 # Class method
@property                    # Property getter
```

**RECURSION:**
```python
def func(n):                 # Recursive function
    if base_case:            # Base case check
        return value         # Stop recursion
    return func(n-1)         # Recursive call
```

**TYPE HINTS:**
```python
def func(x: int) -> int:     # Type hints
def func(x: str) -> None:    # Returns nothing
def func(x: List[int]) -> Dict[str, int]: # Complex types
def func(x: Optional[str]) -> str: # Optional type
**DECORATORS:**
```python
@decorator                   # @staticmethod
def func():                  # @property
```

**TYPE HINTS:**
```python
def func(x: int) -> int:     # Type hints
def func(x: str) -> None:    # Returns nothing
```

---

## OS MODULE

**DIRECTORY:**
```python
os.getcwd()                  # Get current directory
os.chdir(path)               # Change directory
os.listdir(path)             # List directory contents
os.mkdir(path)               # Create directory
os.makedirs(path)            # Create directory tree
os.rmdir(path)               # Remove empty directory
os.removedirs(path)          # Remove empty directory tree
```

**FILES:**
```python
os.remove(path)              # Delete file
os.rename(old, new)          # Rename file/directory
os.replace(old, new)         # Rename (overwrites destination)
```

**PATH OPERATIONS:**
```python
os.path.exists(path)         # Check if exists
os.path.isfile(path)         # Check if file
os.path.isdir(path)          # Check if directory
os.path.join(path, *paths)   # Join paths
os.path.split(path)          # Split into (dir, file)
os.path.splitext(path)       # Split into (name, extension)
os.path.basename(path)       # Get filename
os.path.dirname(path)        # Get directory name
os.path.abspath(path)        # Get absolute path
os.path.getsize(path)        # Get file size
```

**ENVIRONMENT:**
```python
os.environ                   # Environment variables dict
os.environ.get(key)          # Get environment variable
os.getenv(key)               # Get environment variable
os.getenv(key, default)      # Get with default
```

**PROCESS:**
```python
os.system(command)           # Execute command
os.getpid()                  # Get process ID
```

---

## OPERATORS

**ARITHMETIC:**
```python
+                            # Addition: 5 + 3 → 8
-                            # Subtraction: 5 - 3 → 2
*                            # Multiplication: 5 * 3 → 15
/                            # Division: 5 / 2 → 2.5
//                           # Floor division: 5 // 2 → 2
%                            # Modulus: 5 % 2 → 1
**                           # Exponentiation: 2 ** 3 → 8
```

**COMPARISON:**
```python
==                           # Equal: 5 == 5 → True
!=                           # Not equal: 5 != 3 → True
<                            # Less than: 3 < 5 → True
>                            # Greater than: 5 > 3 → True
<=                           # Less or equal: 5 <= 5 → True
>=                           # Greater or equal: 5 >= 3 → True
```

**LOGICAL:**
```python
and                          # True and False → False
or                           # True or False → True
not                          # not True → False
```

**BITWISE:**
```python
&                            # AND: 5 & 3 → 1
|                            # OR: 5 | 3 → 7
^                            # XOR: 5 ^ 3 → 6
~                            # NOT: ~5 → -6
<<                           # Left shift: 5 << 1 → 10
>>                           # Right shift: 5 >> 1 → 2
```

**ASSIGNMENT:**
```python
=                            # Assign: x = 5
+=                           # Add and assign: x += 3
-=                           # Subtract and assign: x -= 3
*=                           # Multiply and assign: x *= 3
/=                           # Divide and assign: x /= 3
//=                          # Floor divide and assign: x //= 3
%=                           # Modulus and assign: x %= 3
**=                          # Exponent and assign: x **= 3
&=                           # Bitwise AND and assign
|=                           # Bitwise OR and assign
^=                           # Bitwise XOR and assign
<<=                          # Left shift and assign
>>=                          # Right shift and assign
```

**MEMBERSHIP:**
```python
in                           # 'a' in "abc" → True
not in                       # 'x' not in "abc" → True
```

**IDENTITY:**
```python
is                           # x is y (same object)
is not                       # x is not y (different objects)
```

---

## TEXT FORMATTING

**F-STRINGS:**
```python
f"{var}"                     # Basic interpolation
f"{expr}"                    # Expression evaluation
f"{var!r}"                   # repr() representation
f"{var!s}"                   # str() representation
f"{var!a}"                   # ascii() representation
f"{var=}"                    # Debug format (3.8+)
f"{var:spec}"                # Format specification
f"{var:width}"               # Minimum width
f"{var:<width}"              # Left align
f"{var:>width}"              # Right align
f"{var:^width}"              # Center align
f"{var:0width}"              # Zero padding
f"{num:.2f}"                 # 2 decimal places
f"{num:,}"                   # Thousand separator
f"{num:_}"                   # Underscore separator
f"{num:b}"                   # Binary format
f"{num:o}"                   # Octal format
f"{num:x}"                   # Hex lowercase
f"{num:X}"                   # Hex uppercase
f"{num:e}"                   # Scientific notation
f"{num:%}"                   # Percentage
```

**FORMAT METHOD:**
```python
"{}".format(val)             # Positional
"{} {}".format(a, b)         # Multiple positional
"{0} {1}".format(a, b)       # Indexed
"{1} {0}".format(a, b)       # Reversed
"{name}".format(name=val)    # Named
"{0.attr}".format(obj)       # Attribute access
"{0[key]}".format(dict)      # Item access
```

**%-FORMATTING:**
```python
"%s" % val                   # String
"%d" % val                   # Integer
"%f" % val                   # Float
"%.2f" % val                 # Float with precision
"%x" % val                   # Hex
"%(name)s" % dict            # Named substitution
```

**STRING ALIGNMENT:**
```python
str.center(width)            # Center in width
str.center(width, fill)      # Center with fill char
str.ljust(width)             # Left justify
str.ljust(width, fill)       # Left justify with fill
str.rjust(width)             # Right justify
str.rjust(width, fill)       # Right justify with fill
str.zfill(width)             # Zero-pad left
```

**ESCAPE SEQUENCES:**
```python
\n                           # Newline
\t                           # Tab
\r                           # Carriage return
\\                           # Backslash
\'                           # Single quote
\"                           # Double quote
\b                           # Backspace
\f                           # Form feed
\v                           # Vertical tab
\0                           # Null character
\xhh                         # Hex value
\uhhhh                       # Unicode 16-bit
\Uhhhhhhhh                   # Unicode 32-bit
```

---

## ADDITIONAL STRING METHODS (COMPREHENSIVE)

```python
# Translation and character operations
str.translate(table)         # Translate using table
str.maketrans(x, y)          # Create translation table
str.maketrans(dict)          # Create table from dict

# Encoding operations
str.encode()                 # Encode to bytes (UTF-8)
str.encode(encoding)         # Encode with encoding
str.encode(encoding, errors) # Encode with error handling
bytes.decode()               # Decode bytes to string
bytes.decode(encoding)       # Decode with encoding
bytes.decode(encoding, errors) # Decode with error handling

# Advanced checks
str.isprintable()            # Check all printable
str.isascii()                # Check all ASCII (3.7+)
str.isidentifier()           # Check valid identifier
str.isdecimal()              # Check decimal digits
str.isnumeric()              # Check numeric chars

# Unicode operations
ord(char)                    # Get Unicode code point
chr(int)                     # Get char from code point
ascii(str)                   # Get ASCII repr
```

---

## COMPREHENSIVE LIST OPERATIONS

```python
# All modification methods
list.append(item)            # Add to end
list.extend(iterable)        # Add multiple items
list.insert(index, item)     # Insert at position
list.remove(item)            # Remove first occurrence
list.pop()                   # Remove last item
list.pop(index)              # Remove at index
list.clear()                 # Remove all items
list.reverse()               # Reverse in place
list.sort()                  # Sort in place
list.sort(reverse=True)      # Sort descending
list.sort(key=func)          # Sort by custom key
list.copy()                  # Shallow copy

# Slicing operations
list[start:end]              # Basic slice
list[start:end:step]         # Slice with step
list[::-1]                   # Reverse copy
list[::2]                    # Every other item
list[1::2]                   # Odd indices
list[-n:]                    # Last n items
list[:-n]                    # All but last n

# Unpacking
a, b, c = list               # Unpack to variables
first, *rest = list          # First + rest
*start, last = list          # Start + last
first, *mid, last = list     # First, middle, last

# Operations
list1 + list2                # Concatenate
list * n                     # Repeat
item in list                 # Membership
item not in list             # Non-membership
len(list)                    # Length
min(list)                    # Minimum
max(list)                    # Maximum
sum(list)                    # Sum (numbers)
all(list)                    # All truthy
any(list)                    # Any truthy
sorted(list)                 # Sorted copy
reversed(list)               # Reverse iterator
```

---

## COMPREHENSIVE DICTIONARY OPERATIONS

```python
# All access methods
dict[key]                    # Direct access (KeyError if missing)
dict.get(key)                # Safe access (None if missing)
dict.get(key, default)       # Safe access with default
dict.setdefault(key, default)# Get or set default
dict.keys()                  # Get keys view
dict.values()                # Get values view
dict.items()                 # Get items view

# All modification methods
dict[key] = value            # Add/update
dict.update(other)           # Merge dictionaries
dict.update(key=value)       # Update with kwargs
dict.update([(k,v), ...])    # Update from pairs
dict.pop(key)                # Remove and return
dict.pop(key, default)       # Remove with default
dict.popitem()               # Remove last item (LIFO)
dict.clear()                 # Remove all items
del dict[key]                # Delete key

# Creation methods
dict()                       # Empty dict
dict(a=1, b=2)              # From kwargs
dict([('a',1), ('b',2)])    # From pairs
dict.fromkeys(keys)          # From keys (None values)
dict.fromkeys(keys, value)   # From keys with value
{k: v for k, v in items}     # Dict comprehension
{**dict1, **dict2}           # Merge with unpacking (3.5+)
dict1 | dict2                # Union operator (3.9+)

# Comparison operations
dict1 == dict2               # Check equality
dict1 != dict2               # Check inequality

# View operations (on .keys())
dict.keys() & other.keys()   # Intersection
dict.keys() | other.keys()   # Union
dict.keys() - other.keys()   # Difference
dict.keys() ^ other.keys()   # Symmetric difference

# Iteration
for key in dict:             # Iterate keys
for value in dict.values():  # Iterate values
for k, v in dict.items():    # Iterate pairs
enumerate(dict)              # Index + keys
enumerate(dict.items())      # Index + pairs
reversed(dict)               # Reverse (3.8+)

# Utility functions
len(dict)                    # Count items
key in dict                  # Check membership
sorted(dict)                 # Sort keys
sorted(dict.items())         # Sort by keys
sorted(dict, key=dict.get)   # Sort keys by values
min(dict)                    # Min key
max(dict)                    # Max key
sum(dict.values())           # Sum values
list(dict)                   # Keys to list
tuple(dict)                  # Keys to tuple
set(dict)                    # Keys to set
```

---

## COMPREHENSIVE SET OPERATIONS

```python
# Creation
{1, 2, 3}                    # Set literal
set()                        # Empty set
set(iterable)                # From iterable
{x for x in iterable}        # Set comprehension

# Modification
set.add(item)                # Add element
set.remove(item)             # Remove (KeyError if missing)
set.discard(item)            # Remove (no error)
set.pop()                    # Remove arbitrary element
set.clear()                  # Remove all elements
set.update(iterable)         # Add multiple

# Set operations (return new set)
set.union(other)             # All elements from both
set.intersection(other)      # Common elements
set.difference(other)        # In first but not second
set.symmetric_difference(other) # In either but not both

# Set operators
set1 | set2                  # Union
set1 & set2                  # Intersection
set1 - set2                  # Difference
set1 ^ set2                  # Symmetric difference

# In-place operations
set1 |= set2                 # Union update
set1 &= set2                 # Intersection update
set1 -= set2                 # Difference update
set1 ^= set2                 # Symmetric difference update

# Comparisons
set.issubset(other)          # Check if subset
set <= other                 # Subset operator
set < other                  # Proper subset
set.issuperset(other)        # Check if superset
set >= other                 # Superset operator
set > other                  # Proper superset
set.isdisjoint(other)        # No common elements

# Utilities
len(set)                     # Count elements
item in set                  # Membership
min(set)                     # Minimum
max(set)                     # Maximum
sum(set)                     # Sum
sorted(set)                  # Sorted list
```

---

## COMPREHENSIVE TUPLE OPERATIONS

```python
# Creation
()                           # Empty tuple
(item,)                      # Single item (comma required!)
(1, 2, 3)                    # Multiple items
tuple()                      # Empty tuple
tuple(iterable)              # From iterable
1, 2, 3                      # Tuple packing

# Only 2 methods (immutable!)
tuple.count(item)            # Count occurrences
tuple.index(item)            # Find first index
tuple.index(item, start)     # Search from start
tuple.index(item, start, end) # Search in range

# Access and slicing
tuple[index]                 # Access element
tuple[-1]                    # Last element
tuple[start:end]             # Slice
tuple[start:end:step]        # Slice with step
tuple[::-1]                  # Reverse

# Unpacking
a, b = tuple                 # Basic unpacking
a, *rest = tuple             # First + rest
*start, last = tuple         # Start + last
first, *mid, last = tuple    # First, middle, last

# Operations
tuple1 + tuple2              # Concatenate
tuple * n                    # Repeat
item in tuple                # Membership
len(tuple)                   # Length
min(tuple)                   # Minimum
max(tuple)                   # Maximum
sum(tuple)                   # Sum
sorted(tuple)                # Sorted list (not tuple!)

# Utilities
tuple(sorted(t))             # Get sorted tuple
type(t)                      # Check type
bool(t)                      # Check if empty
```

---

## COMPREHENSIVE FILE OPERATIONS

```python
# Opening modes
open(file, 'r')              # Read (default)
open(file, 'w')              # Write (overwrites)
open(file, 'a')              # Append
open(file, 'x')              # Exclusive create
open(file, 'r+')             # Read and write
open(file, 'w+')             # Write and read
open(file, 'a+')             # Append and read
open(file, 'rb')             # Read binary
open(file, 'wb')             # Write binary
open(file, encoding='utf-8') # With encoding

# Context manager (best practice)
with open(file, mode) as f:  # Auto-closing

# Reading methods
file.read()                  # Read entire file
file.read(size)              # Read size bytes
file.readline()              # Read one line
file.readlines()             # Read all lines
for line in file:            # Iterate lines
next(file)                   # Read next line

# Writing methods
file.write(string)           # Write string
file.writelines(list)        # Write list of strings
file.flush()                 # Force write buffer

# Position methods
file.tell()                  # Get position
file.seek(offset)            # Move to position
file.seek(offset, whence)    # Relative move (0=start, 1=current, 2=end)

# Info attributes
file.name                    # Filename
file.mode                    # Mode
file.closed                  # Check if closed
file.readable()              # Check if readable
file.writable()              # Check if writable
file.seekable()              # Check if seekable

# Closing
file.close()                 # Close file
```

---

## COMPREHENSIVE OS MODULE

```python
# Directory operations
os.getcwd()                  # Get current directory
os.chdir(path)               # Change directory
os.mkdir(path)               # Create directory
os.mkdir(path, mode)         # Create with permissions
os.makedirs(path)            # Create nested directories
os.makedirs(path, exist_ok=True) # Don't error if exists
os.rmdir(path)               # Remove empty directory
os.removedirs(path)          # Remove empty nested dirs
os.listdir(path)             # List contents
os.scandir(path)             # Iterator of DirEntry objects
os.walk(top)                 # Walk directory tree
os.walk(top, topdown=False)  # Walk bottom-up

# File operations
os.remove(path)              # Delete file
os.unlink(path)              # Delete file (alias)
os.rename(src, dst)          # Rename/move
os.replace(src, dst)         # Rename (overwrites)
os.stat(path)                # Get file info
os.chmod(path, mode)         # Change permissions
os.chown(path, uid, gid)     # Change owner (Unix)

# Path checking
os.path.exists(path)         # Check if exists
os.path.isfile(path)         # Check if file
os.path.isdir(path)          # Check if directory
os.path.islink(path)         # Check if symlink
os.path.isabs(path)          # Check if absolute
os.path.ismount(path)        # Check if mount point

# Path manipulation
os.path.join(path, *paths)   # Join paths
os.path.split(path)          # Split into (dir, file)
os.path.splitext(path)       # Split into (name, ext)
os.path.splitdrive(path)     # Split drive letter
os.path.dirname(path)        # Get directory
os.path.basename(path)       # Get filename
os.path.abspath(path)        # Get absolute path
os.path.relpath(path, start) # Get relative path
os.path.realpath(path)       # Resolve symlinks
os.path.normpath(path)       # Normalize path
os.path.normcase(path)       # Normalize case
os.path.expanduser(path)     # Expand ~ to home
os.path.expandvars(path)     # Expand env variables
os.path.commonpath(paths)    # Find common base
os.path.commonprefix(paths)  # Find common prefix

# Path info
os.path.getsize(path)        # Get file size
os.path.getmtime(path)       # Get modification time
os.path.getatime(path)       # Get access time
os.path.getctime(path)       # Get creation time
os.access(path, mode)        # Check permissions

# Environment variables
os.environ                   # All env vars (dict-like)
os.environ['VAR']            # Get env var
os.environ.get('VAR')        # Safe get
os.environ.get('VAR', default) # Get with default
os.getenv('VAR')             # Get env var
os.getenv('VAR', default)    # Get with default
os.environ['VAR'] = 'value'  # Set env var
os.putenv('VAR', 'value')    # Set env var (legacy)
os.unsetenv('VAR')           # Remove env var

# Process operations
os.system(command)           # Execute command
os.getpid()                  # Get process ID
os.getppid()                 # Get parent process ID
os.kill(pid, signal)         # Send signal
os._exit(n)                  # Exit immediately
os.abort()                   # Generate abort signal

# System info
os.name                      # OS name ('posix', 'nt')
os.uname()                   # System info (Unix)
os.cpu_count()               # CPU count
os.getlogin()                # Login name
os.sep                       # Path separator
os.pathsep                   # PATH separator
os.linesep                   # Line separator
os.devnull                   # Null device path
os.curdir                    # Current dir symbol ('.')
os.pardir                    # Parent dir symbol ('..')

# Terminal operations
os.get_terminal_size()       # Get terminal dimensions
os.isatty(fd)                # Check if terminal
os.ttyname(fd)               # Get terminal name (Unix)

# Permission constants
os.F_OK                      # Check existence
os.R_OK                      # Check read permission
os.W_OK                      # Check write permission
os.X_OK                      # Check execute permission

# File descriptor operations
os.open(path, flags)         # Open file (low level)
os.close(fd)                 # Close file descriptor
os.read(fd, n)               # Read n bytes
os.write(fd, data)           # Write bytes
os.lseek(fd, pos, how)       # Seek in file
os.dup(fd)                   # Duplicate FD
os.dup2(fd, fd2)             # Duplicate to specific FD
os.pipe()                    # Create pipe
os.fsync(fd)                 # Force write to disk

# Stat result attributes
stat_result.st_mode          # File mode/permissions
stat_result.st_ino           # Inode number
stat_result.st_dev           # Device ID
stat_result.st_nlink         # Number of hard links
stat_result.st_uid           # User ID
stat_result.st_gid           # Group ID
stat_result.st_size          # File size
stat_result.st_atime         # Last access time
stat_result.st_mtime         # Last modification time
stat_result.st_ctime         # Creation/change time
```

---

## CSV & JSON OPERATIONS

```python
# CSV operations (import csv)
csv.reader(file)             # Read CSV as lists
csv.writer(file)             # Write lists to CSV
csv.DictReader(file)         # Read CSV as dicts
csv.DictWriter(file, fields) # Write dicts to CSV
writer.writerow(row)         # Write single row
writer.writerows(rows)       # Write multiple rows
writer.writeheader()         # Write header row

# JSON operations (import json)
json.load(file)              # Read JSON from file
json.loads(string)           # Parse JSON string
json.dump(obj, file)         # Write object to JSON
json.dump(obj, file, indent=2) # Write formatted JSON
json.dumps(obj)              # Convert to JSON string
json.dumps(obj, indent=2)    # Format JSON string
```

---

## ADVANCED BUILT-IN FUNCTIONS

```python
# Iterator functions
iter(iterable)               # Create iterator
next(iterator)               # Get next item
next(iterator, default)      # Get next with default
enumerate(iter)              # Index + iterate
enumerate(iter, start)       # Custom start index
zip(*iterables)              # Pair items together
zip(*lists)                  # Unzip/transpose
filter(func, iter)           # Filter by condition
map(func, iter)              # Apply function to all
reversed(iterable)           # Reverse iteration

# Comprehension generators
[expr for x in iter]         # List comprehension
{expr for x in iter}         # Set comprehension
{k: v for x in iter}         # Dict comprehension
(expr for x in iter)         # Generator expression

# Object inspection
type(obj)                    # Get type
isinstance(obj, type)        # Check type
issubclass(class, classinfo) # Check subclass
hasattr(obj, name)           # Check attribute
getattr(obj, name)           # Get attribute
getattr(obj, name, default)  # Get with default
setattr(obj, name, value)    # Set attribute
delattr(obj, name)           # Delete attribute
dir(obj)                     # List attributes
vars(obj)                    # Get __dict__
callable(obj)                # Check if callable

# Numeric functions
abs(x)                       # Absolute value
round(x)                     # Round to nearest
round(x, n)                  # Round to n decimals
pow(x, y)                    # x ** y
pow(x, y, z)                 # (x ** y) % z
divmod(x, y)                 # (x // y, x % y)
complex(real, imag)          # Create complex number

# Sequence functions
all(iterable)                # All truthy
any(iterable)                # Any truthy
min(iterable)                # Minimum
min(*args)                   # Minimum of args
min(iter, key=func)          # Min by key
max(iterable)                # Maximum
max(*args)                   # Maximum of args
max(iter, key=func)          # Max by key
sum(iterable)                # Sum
sum(iterable, start)         # Sum with start value

# String functions
chr(int)                     # Int to character
ord(char)                    # Character to int
bin(x)                       # To binary string
oct(x)                       # To octal string
hex(x)                       # To hex string
format(value, spec)          # Apply format spec

# Memory and identity
id(obj)                      # Memory address
hash(obj)                    # Hash value

# Code execution
eval(expression)             # Evaluate expression
exec(code)                   # Execute code
compile(source, file, mode)  # Compile source

# I/O functions
print(*objects, sep=' ', end='\n', file=None, flush=False)
input()                      # Read line
input(prompt)                # Read with prompt

# Utility functions
help(obj)                    # Get help
len(obj)                     # Get length
slice(stop)                  # Create slice object
slice(start, stop)           # Create slice
slice(start, stop, step)     # Create slice with step
```

---

## TEXTWRAP MODULE (import textwrap)

```python
textwrap.wrap(text, width)   # Wrap to width
textwrap.fill(text, width)   # Wrap and join
textwrap.shorten(text, width) # Shorten to fit
textwrap.dedent(text)        # Remove indentation
textwrap.indent(text, prefix) # Add prefix to lines
TextWrapper(width)           # Create wrapper object
```

---

## PPRINT MODULE (import pprint)

```python
pprint.pprint(obj)           # Pretty print
pprint.pprint(obj, indent=n) # With indentation
pprint.pprint(obj, width=n)  # Max width
pprint.pprint(obj, depth=n)  # Max depth
pprint.pformat(obj)          # Format as string
pprint.pp(obj)               # Shorthand (3.8+)
```

---

## DATETIME FORMATTING

```python
# Datetime format codes
f"{dt:%Y}"                   # Year 4-digit
f"{dt:%y}"                   # Year 2-digit
f"{dt:%m}"                   # Month 2-digit
f"{dt:%B}"                   # Month full name
f"{dt:%b}"                   # Month abbreviation
f"{dt:%d}"                   # Day of month
f"{dt:%A}"                   # Weekday full
f"{dt:%a}"                   # Weekday abbreviation
f"{dt:%H}"                   # Hour 24-hour
f"{dt:%I}"                   # Hour 12-hour
f"{dt:%M}"                   # Minute
f"{dt:%S}"                   # Second
f"{dt:%p}"                   # AM/PM
f"{dt:%Y-%m-%d}"             # ISO date
dt.strftime("%Y-%m-%d")      # Format method
```

---

## ANSI ESCAPE CODES (Terminal Colors)

```python
"\033[0m"                    # Reset all
"\033[1m"                    # Bold
"\033[2m"                    # Dim
"\033[3m"                    # Italic
"\033[4m"                    # Underline
"\033[7m"                    # Reverse

# Foreground colors
"\033[30m"                   # Black
"\033[31m"                   # Red
"\033[32m"                   # Green
"\033[33m"                   # Yellow
"\033[34m"                   # Blue
"\033[35m"                   # Magenta
"\033[36m"                   # Cyan
"\033[37m"                   # White
"\033[90m"                   # Bright black (gray)
"\033[91m"                   # Bright red
"\033[92m"                   # Bright green
"\033[93m"                   # Bright yellow
"\033[94m"                   # Bright blue
"\033[95m"                   # Bright magenta
"\033[96m"                   # Bright cyan
"\033[97m"                   # Bright white

# Background colors
"\033[40m"                   # Black background
"\033[41m"                   # Red background
"\033[42m"                   # Green background
"\033[43m"                   # Yellow background
"\033[44m"                   # Blue background
"\033[45m"                   # Magenta background
"\033[46m"                   # Cyan background
"\033[47m"                   # White background
```

---

## LOCALE MODULE (import locale)

```python
locale.setlocale(category, locale) # Set locale
locale.format_string(fmt, val)  # Format with locale
locale.currency(val)         # Format as currency
locale.str(float)            # Locale-aware string
locale.atof(string)          # Parse locale float
locale.atoi(string)          # Parse locale int
```

---

## BYTES OPERATIONS

```python
b"text"                      # Bytes literal
bytes(string, encoding)      # Encode string
bytes(iterable)              # From ints
bytes(size)                  # Zero-filled
bytearray(source)            # Mutable bytes
bytes.decode()               # Decode to string
bytes.decode(encoding)       # Decode with encoding
bytes.hex()                  # To hex string
bytes.fromhex(string)        # From hex string
```

---

## UNICODE OPERATIONS (import unicodedata)

```python
unicodedata.normalize(form, str) # Normalize Unicode
unicodedata.name(char)       # Get character name
unicodedata.lookup(name)     # Get char by name
unicodedata.category(char)   # Get category
unicodedata.decimal(char)    # Get decimal value
unicodedata.digit(char)      # Get digit value
unicodedata.numeric(char)    # Get numeric value
```

---

## NAMEDTUPLE (from collections import namedtuple)

```python
namedtuple(name, fields)     # Create named tuple class
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)              # Create instance
p.x, p.y                     # Access by name
p[0], p[1]                   # Access by index
p._asdict()                  # Convert to dict
p._replace(x=10)             # Create modified copy
p._fields                    # Get field names
```

---

## FROZENSET OPERATIONS

```python
frozenset()                  # Empty frozenset
frozenset(iterable)          # Create immutable set
# Supports all query/mathematical operations
# NO modification methods (immutable)
# Hashable - can be dict key or set element
```


---

```python
f"{var}"                     # f"{name}" → value of name
f"{var:width}"               # f"{name:10}" → padded to 10 chars
f"{var:<width}"              # f"{name:<10}" → left-align
f"{var:>width}"              # f"{name:>10}" → right-align
f"{var:^width}"              # f"{name:^10}" → center-align
f"{var:0width}"              # f"{num:05}" → zero-padded
f"{num:.2f}"                 # f"{3.14159:.2f}" → "3.14"
f"{num:,.2f}"                # f"{1000:.2f}" → "1,000.00"
f"{num:e}"                   # f"{1000:e}" → "1.000000e+03"
f"{num:%}"                   # f"{0.25:%}" → "25.000000%"
f"{num:b}"                   # f"{10:b}" → "1010" (binary)
f"{num:x}"                   # f"{255:x}" → "ff" (hex)
f"{num:o}"                   # f"{8:o}" → "10" (octal)
```

**.format() METHOD:**
```python
"{}".format(val)             # "Hello {}".format("World")
"{0} {1}".format(a, b)       # "{0} {1}".format("Hello", "World")
"{name}".format(name=val)    # "{name} is {age}".format(name="Alice", age=25)
"{:10}".format(val)          # Width
"{:<10}".format(val)         # Left-align
"{:>10}".format(val)         # Right-align
"{:^10}".format(val)         # Center-align
"{:.2f}".format(num)         # 2 decimal places
```

**%-FORMATTING:**
```python
"%s" % val                   # "Hello %s" % "World"
"%d" % num                   # "%d items" % 5
"%f" % num                   # "%f" % 3.14159
"%.2f" % num                 # "%.2f" % 3.14159 → "3.14"
"%s %d" % (str, num)         # "Hello %s, you have %d items" % ("Alice", 5)
```
