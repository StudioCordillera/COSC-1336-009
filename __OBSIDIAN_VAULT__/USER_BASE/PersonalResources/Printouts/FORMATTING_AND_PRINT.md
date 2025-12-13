# FORMATTING AND PRINT

## Core Definition
**String formatting** provides methods to embed values into strings with precise control over appearance. **print()** outputs formatted text to console with control over separators, endings, and output streams.

**Tags**: #formatting #print #f-strings #format-method #string-interpolation #output

---

## COMPLETE FORMATTING QUICK REFERENCE

### FORMATTING METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# F-STRINGS (Python 3.6+) - RECOMMENDED
# ═══════════════════════════════════════════════════════════════════════════
f"{variable}"                      # Variable | Insert value | Returns formatted string
f"{expression}"                    # Expression | Evaluate and insert | Returns formatted string
f"{value:format_spec}"             # Value + spec | Formatted insertion | Returns formatted string
f"{value!r}"                       # Value | repr() representation | Returns repr string
f"{value!s}"                       # Value | str() representation | Returns str string
f"{value!a}"                       # Value | ascii() representation | Returns ASCII string
f"{value=}"                        # Variable (3.8+) | Debug format | Returns "value=result"
f"{{literal_braces}}"              # Literal | Escape braces | Returns "{literal_braces}"

# ═══════════════════════════════════════════════════════════════════════════
# STR.FORMAT() METHOD - VERSATILE
# ═══════════════════════════════════════════════════════════════════════════
"{}".format(value)                 # Value | Positional insert | Returns formatted string
"{0}".format(value)                # Value | Indexed insert | Returns formatted string
"{name}".format(name=value)        # Keyword | Named insert | Returns formatted string
"{0:format_spec}".format(value)    # Value + spec | Formatted insert | Returns formatted string
"{{literal}}".format()             # Literal | Escape braces | Returns "{literal}"
"{!r}".format(value)               # Value | repr() representation | Returns repr string
"{.attribute}".format(obj)         # Object | Access attribute | Returns attribute value
"{[key]}".format(dict)             # Dict | Access key | Returns dict value

# ═══════════════════════════════════════════════════════════════════════════
# %-FORMATTING (OLD STYLE) - LEGACY
# ═══════════════════════════════════════════════════════════════════════════
"%s" % value                       # String | Insert as string | Returns formatted string
"%d" % value                       # Integer | Insert as decimal | Returns formatted string
"%f" % value                       # Float | Insert as float | Returns formatted string
"%x" % value                       # Integer | Hex lowercase | Returns hex string
"%X" % value                       # Integer | Hex uppercase | Returns hex string
"%o" % value                       # Integer | Octal | Returns octal string
"%e" % value                       # Float | Scientific notation | Returns scientific string
"%%" % ()                          # Literal | Escape percent | Returns "%"
"%(name)s" % {'name': value}       # Dict | Named insert | Returns formatted string

# ═══════════════════════════════════════════════════════════════════════════
# FORMAT SPECIFICATION MINI-LANGUAGE
# ═══════════════════════════════════════════════════════════════════════════
# Syntax: [[fill]align][sign][#][0][width][grouping][.precision][type]

"{:width}"                         # Value | Fixed width | Returns padded string
"{:<width}"                        # Value | Left align | Returns left-aligned string
"{:>width}"                        # Value | Right align | Returns right-aligned string
"{:^width}"                        # Value | Center align | Returns centered string
"{:fillchar^width}"                # Value | Center with fill | Returns centered with char
"{:+}"                             # Number | Force sign | Returns signed string
"{:-}"                             # Number | Negative only (default) | Returns string
"{: }"                             # Number | Space for positive | Returns signed string
"{:#x}"                            # Integer | Hex with prefix | Returns "0x..." string
"{:#o}"                            # Integer | Octal with prefix | Returns "0o..." string
"{:#b}"                            # Integer | Binary with prefix | Returns "0b..." string
"{:0width}"                        # Number | Zero padding | Returns zero-padded string
"{:,}"                             # Number | Thousand separator | Returns formatted number
"{:_}"                             # Number (3.6+) | Underscore separator | Returns formatted number
"{:.precision}"                    # Number | Decimal precision | Returns rounded string
"{:.precisions}"                   # String | Max length | Returns truncated string
"{:type}"                          # Value | Type specifier | Returns typed string

# Type Specifiers:
# 's' - String (default)
# 'd' - Decimal integer
# 'f' - Fixed-point float
# 'e' - Scientific notation (lowercase)
# 'E' - Scientific notation (uppercase)
# 'g' - General format (auto)
# 'G' - General format (auto, uppercase)
# '%' - Percentage
# 'b' - Binary
# 'o' - Octal
# 'x' - Hex lowercase
# 'X' - Hex uppercase
# 'c' - Character (Unicode)

# ═══════════════════════════════════════════════════════════════════════════
# PRINT FUNCTION PARAMETERS
# ═══════════════════════════════════════════════════════════════════════════
print(*objects)                    # Values | Print all | Outputs to stdout
print(*objects, sep=' ')           # Values + separator | Custom separator | Outputs with separator
print(*objects, end='\n')          # Values + ending | Custom ending | Outputs with ending
print(*objects, file=sys.stdout)   # Values + file | Output to file | Writes to file object
print(*objects, flush=False)       # Values + flush | Control buffering | Outputs with flush control
print()                            # None | Print blank line | Outputs newline

# ═══════════════════════════════════════════════════════════════════════════
# ADVANCED PRINT PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
print(f"{var}", end='')            # No newline | Continue on same line | Outputs without newline
print(f"{var}", flush=True)        # Immediate | Force output immediately | Outputs without buffering
print(*items, sep=', ')            # Multiple items | Custom separator | Outputs "item1, item2, item3"
print(f"{val}", file=file_obj)     # To file | Write to file | Writes to file object
sys.stdout.write(f"{val}")         # Direct write | No newline default | Writes to stdout
```

### COMMON FORMATTING EXAMPLES

```python
# Basic f-string
name = "Alice"
age = 30
f"Name: {name}, Age: {age}"                    # → "Name: Alice, Age: 30"

# Format specification
pi = 3.14159
f"{pi:.2f}"                                    # → "3.14" (2 decimals)
f"{pi:10.2f}"                                  # → "      3.14" (width 10)

# Alignment
text = "Hi"
f"{text:<10}"                                  # → "Hi        " (left)
f"{text:>10}"                                  # → "        Hi" (right)
f"{text:^10}"                                  # → "    Hi    " (center)
f"{text:*^10}"                                 # → "****Hi****" (center with *)

# Number formatting
num = 1234567
f"{num:,}"                                     # → "1,234,567" (thousand separator)
f"{num:_}"                                     # → "1_234_567" (underscore separator)
f"{num:b}"                                     # → "100101101011010000111" (binary)
f"{num:#x}"                                    # → "0x12d687" (hex with prefix)

# Percentage
ratio = 0.875
f"{ratio:.2%}"                                 # → "87.50%"

# Print with custom separator
print("A", "B", "C", sep=" | ")                # → "A | B | C"

# Print without newline
print("Loading", end="...")                     # → "Loading..." (no newline)
print(" Done!")                                # → " Done!" (same line)
```

---

## F-STRINGS - MODERN PYTHON FORMATTING (3.6+)

F-strings (formatted string literals) are the **recommended** way to format strings in modern Python.

### Basic F-String Syntax:
```python
# Simple variable insertion
name = "Alice"
age = 30
message = f"Hello, {name}. You are {age} years old."
# → "Hello, Alice. You are 30 years old."

# Expression evaluation
x = 10
y = 20
result = f"The sum of {x} and {y} is {x + y}"
# → "The sum of 10 and 20 is 30"

# Method calls
text = "hello"
formatted = f"Uppercase: {text.upper()}"
# → "Uppercase: HELLO"

# Dictionary access
person = {'name': 'Bob', 'age': 25}
info = f"Name: {person['name']}, Age: {person['age']}"
# → "Name: Bob, Age: 25"

# List indexing
items = ['apple', 'banana', 'cherry']
first = f"First item: {items[0]}"
# → "First item: apple"

# Object attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Charlie", 35)
details = f"Person: {p.name}, {p.age}"
# → "Person: Charlie, 35"
```

### F-String with Format Specifications:
```python
# Width and alignment
name = "Alice"
f"{name:10}"                       # → "Alice     " (width 10, left default)
f"{name:<10}"                      # → "Alice     " (left aligned)
f"{name:>10}"                      # → "     Alice" (right aligned)
f"{name:^10}"                      # → "  Alice   " (center aligned)

# Custom fill character
f"{name:*<10}"                     # → "Alice*****" (left, fill with *)
f"{name:*>10}"                     # → "*****Alice" (right, fill with *)
f"{name:*^10}"                     # → "**Alice***" (center, fill with *)

# Numbers with width
num = 42
f"{num:5}"                         # → "   42" (width 5, right aligned)
f"{num:05}"                        # → "00042" (zero padding)

# Float precision
pi = 3.14159265359
f"{pi:.2f}"                        # → "3.14" (2 decimal places)
f"{pi:.4f}"                        # → "3.1416" (4 decimal places)
f"{pi:.0f}"                        # → "3" (no decimal places)

# Float with width and precision
f"{pi:10.2f}"                      # → "      3.14" (width 10, 2 decimals)
f"{pi:010.2f}"                     # → "0000003.14" (zero pad)

# String precision (truncate)
text = "Hello World"
f"{text:.5}"                       # → "Hello" (first 5 chars)
```

### Number Formatting:
```python
num = 42

# Binary
f"{num:b}"                         # → "101010" (binary)
f"{num:#b}"                        # → "0b101010" (binary with prefix)
f"{num:08b}"                       # → "00101010" (8 digits, zero padded)

# Octal
f"{num:o}"                         # → "52" (octal)
f"{num:#o}"                        # → "0o52" (octal with prefix)

# Hexadecimal
f"{num:x}"                         # → "2a" (hex lowercase)
f"{num:X}"                         # → "2A" (hex uppercase)
f"{num:#x}"                        # → "0x2a" (hex with prefix)
f"{num:#X}"                        # → "0X2A" (hex uppercase with prefix)

# Decimal
f"{num:d}"                         # → "42" (decimal)
f"{num:5d}"                        # → "   42" (width 5)
f"{num:05d}"                       # → "00042" (zero padded)

# Thousand separators
big_num = 1234567890
f"{big_num:,}"                     # → "1,234,567,890" (comma separator)
f"{big_num:_}"                     # → "1_234_567_890" (underscore separator)
f"{big_num:,.2f}"                  # → "1,234,567,890.00" (with decimals)

# Float variations
value = 1234.56789
f"{value:f}"                       # → "1234.567890" (default 6 decimals)
f"{value:.2f}"                     # → "1234.57" (2 decimals)
f"{value:,.2f}"                    # → "1,234.57" (with separator)
f"{value:012.2f}"                  # → "00001234.57" (zero padded)
```

### Sign Control:
```python
positive = 42
negative = -42
zero = 0

# Default (- only for negative)
f"{positive}"                      # → "42"
f"{negative}"                      # → "-42"

# Force sign (+ for positive, - for negative)
f"{positive:+}"                    # → "+42"
f"{negative:+}"                    # → "-42"
f"{zero:+}"                        # → "+0"

# Space for positive (space for positive, - for negative)
f"{positive: }"                    # → " 42" (space before)
f"{negative: }"                    # → "-42"

# Sign with width
f"{positive:+5}"                   # → "  +42"
f"{negative:+5}"                   # → "  -42"
```

### Percentage Formatting:
```python
ratio = 0.875
decimal = 0.3333

# Basic percentage
f"{ratio:%}"                       # → "87.500000%" (default precision)
f"{ratio:.0%}"                     # → "88%" (0 decimals, rounded)
f"{ratio:.1%}"                     # → "87.5%" (1 decimal)
f"{ratio:.2%}"                     # → "87.50%" (2 decimals)

# With width
f"{ratio:10.2%}"                   # → "    87.50%" (width 10)

# Multiple values
score = 85
total = 100
percentage = score / total
f"Score: {score}/{total} ({percentage:.1%})"
# → "Score: 85/100 (85.0%)"
```

### Scientific Notation:
```python
large = 1234567890
small = 0.00000123

# Lowercase 'e'
f"{large:e}"                       # → "1.234568e+09"
f"{small:e}"                       # → "1.230000e-06"
f"{large:.2e}"                     # → "1.23e+09" (2 decimals)

# Uppercase 'E'
f"{large:E}"                       # → "1.234568E+09"
f"{small:.3E}"                     # → "1.230E-06" (3 decimals)

# General format (auto-chooses f or e)
f"{large:g}"                       # → "1.23457e+09"
f"{small:g}"                       # → "1.23e-06"
f"{42.5:g}"                        # → "42.5" (uses f for small numbers)
```

### Conversion Flags (!r, !s, !a):
```python
text = "Hello\nWorld"
number = 42

# !s - str() conversion (default)
f"{text!s}"                        # → "Hello\nWorld"
f"{number!s}"                      # → "42"

# !r - repr() conversion (shows quotes and escapes)
f"{text!r}"                        # → "'Hello\\nWorld'" (shows escape)
f"{number!r}"                      # → "42"

# !a - ascii() conversion (escapes non-ASCII)
unicode_text = "Héllo"
f"{unicode_text!a}"                # → "'H\\xe9llo'" (escapes é)

# Practical use case
def debug(var_name, value):
    print(f"{var_name} = {value!r}")

debug("text", "hello\nworld")      # text = 'hello\nworld'
debug("num", 42)                   # num = 42
```

### Debug F-Strings (Python 3.8+):
```python
# Self-documenting expressions (3.8+)
x = 42
y = 10

# Regular f-string
f"x = {x}, y = {y}"                # → "x = 42, y = 10"

# Debug f-string (shows expression and value)
f"{x=}"                            # → "x=42"
f"{y=}"                            # → "y=10"
f"{x + y=}"                        # → "x + y=52"

# With format specification
pi = 3.14159
f"{pi=:.2f}"                       # → "pi=3.14"

# Multiple variables
name = "Alice"
age = 30
f"{name=}, {age=}"                 # → "name='Alice', age=30"

# Complex expressions
items = [1, 2, 3, 4, 5]
f"{sum(items)=}"                   # → "sum(items)=15"
f"{len(items)=}"                   # → "len(items)=5"

# Practical debugging
def calculate(a, b):
    result = a * b + 10
    print(f"{a=}, {b=}, {result=}")
    return result

calculate(5, 3)
# Output: a=5, b=3, result=25
```

### Nested F-Strings:
```python
# F-strings within f-strings
width = 10
precision = 2
value = 3.14159

# Dynamic format specification
f"{value:{width}.{precision}f}"    # → "      3.14" (width 10, precision 2)

# Conditional formatting
is_important = True
text = "ALERT"
f"{text:{'*^20' if is_important else '<20'}}"
# → "********ALERT*******" (centered with * if important)

# Table with dynamic width
name = "Alice"
col_width = 15
f"{name:<{col_width}}"             # → "Alice          " (dynamic width)

# Precision based on variable
decimal_places = 3
pi = 3.14159
f"{pi:.{decimal_places}f}"         # → "3.142"
```

### Multiline F-Strings:
```python
name = "Alice"
age = 30
city = "NYC"

# Multiline f-string
message = f"""
Name: {name}
Age:  {age}
City: {city}
"""

# With formatting
score = 85.5
info = f"""
Student Report
{'='*40}
Name:  {name:<20}
Score: {score:>10.2f}
{'='*40}
"""

# Triple quotes with expressions
data = [1, 2, 3, 4, 5]
report = f"""
Data Summary:
  Count: {len(data)}
  Sum:   {sum(data)}
  Avg:   {sum(data)/len(data):.2f}
"""
```

### Escaping Braces:
```python
# Double braces for literal braces
f"{{This is in braces}}"           # → "{This is in braces}"

# Mix literal and variables
name = "Alice"
f"{{name}} = {name}"               # → "{name} = Alice"

# JSON-like output
key = "id"
value = 42
f'{{"{key}": {value}}}'            # → '{"id": 42}'
```

---

## STR.FORMAT() METHOD - VERSATILE FORMATTING

The `.format()` method provides powerful formatting with positional and keyword arguments.

### Basic Format Syntax:
```python
# Positional arguments
"Hello {}".format("World")                     # → "Hello World"
"{} + {} = {}".format(5, 3, 8)                 # → "5 + 3 = 8"

# Indexed arguments
"{0} {1}".format("Hello", "World")             # → "Hello World"
"{1} {0}".format("Hello", "World")             # → "World Hello"
"{0} {0} {1}".format("A", "B")                 # → "A A B" (reuse)

# Named arguments
"Hello {name}".format(name="Alice")            # → "Hello Alice"
"{name} is {age} years old".format(name="Bob", age=25)
# → "Bob is 25 years old"

# Mix positional and named
"{0} is {age} years old".format("Charlie", age=30)
# → "Charlie is 30 years old"
```

### Format Specifications:
```python
# Width and alignment
"'{:<10}'".format("Hi")                        # → "'Hi        '" (left)
"'{:>10}'".format("Hi")                        # → "'        Hi'" (right)
"'{:^10}'".format("Hi")                        # → "'    Hi    '" (center)

# Custom fill character
"'{:*<10}'".format("Hi")                       # → "'Hi********'" (left)
"'{:*>10}'".format("Hi")                       # → "'********Hi'" (right)
"'{:*^10}'".format("Hi")                       # → "'****Hi****'" (center)

# Number formatting
"{:d}".format(42)                              # → "42" (decimal)
"{:5d}".format(42)                             # → "   42" (width 5)
"{:05d}".format(42)                            # → "00042" (zero pad)

# Float precision
"{:.2f}".format(3.14159)                       # → "3.14"
"{:10.2f}".format(3.14159)                     # → "      3.14" (width + precision)

# Percentage
"{:.2%}".format(0.875)                         # → "87.50%"

# Thousand separators
"{:,}".format(1234567)                         # → "1,234,567"
"{:_.2f}".format(1234567.89)                   # → "1_234_567.89"
```

### Accessing Attributes and Items:
```python
# Access object attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
"{0.name} is {0.age} years old".format(person)
# → "Alice is 30 years old"

# Access dictionary items
data = {'name': 'Bob', 'age': 25}
"{0[name]} is {0[age]} years old".format(data)
# → "Bob is 25 years old"

# Access list items
items = ['apple', 'banana', 'cherry']
"First: {0[0]}, Second: {0[1]}".format(items)
# → "First: apple, Second: banana"

# Named access
"Name: {p[name]}, Age: {p[age]}".format(p=data)
# → "Name: Bob, Age: 25"
```

### Format with Unpacking:
```python
# Unpack list
values = [5, 3]
"{} + {} = {}".format(*values, sum(values))
# → "5 + 3 = 8"

# Unpack dictionary
person = {'name': 'Alice', 'age': 30}
"{name} is {age}".format(**person)
# → "Alice is 30"

# Combined
data = {'name': 'Bob'}
"{0} {name}".format("Hello", **data)
# → "Hello Bob"
```

### Advanced Number Formatting:
```python
# Binary, octal, hex
num = 42
"{0:b} {0:o} {0:x}".format(num)                # → "101010 52 2a"
"{:#b} {:#o} {:#x}".format(num)                # → "0b101010 0o52 0x2a"

# Sign control
"{:+d} {:+d}".format(42, -42)                  # → "+42 -42"
"{: d} {: d}".format(42, -42)                  # → " 42 -42"

# Scientific notation
"{:e}".format(1234567)                         # → "1.234567e+06"
"{:.2e}".format(1234567)                       # → "1.23e+06"
"{:E}".format(1234567)                         # → "1.234567E+06"

# General format
"{:g}".format(1234567)                         # → "1.23457e+06"
"{:g}".format(123.456)                         # → "123.456"
```

### Nested Format Specifications:
```python
# Dynamic width
width = 10
"'{:{}}'".format("Hi", width)                  # → "'Hi        '"

# Dynamic precision
precision = 2
"{:.{}f}".format(3.14159, precision)           # → "3.14"

# Dynamic width and precision
width, precision = 10, 2
"{:{}.{}f}".format(3.14159, width, precision)  # → "      3.14"
```

### Custom Format for Classes:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __format__(self, format_spec):
        if format_spec == 'polar':
            import math
            r = math.sqrt(self.x**2 + self.y**2)
            theta = math.atan2(self.y, self.x)
            return f"(r={r:.2f}, θ={theta:.2f})"
        # Default cartesian
        return f"({self.x}, {self.y})"

p = Point(3, 4)
"{:}".format(p)                                # → "(3, 4)"
"{:polar}".format(p)                           # → "(r=5.00, θ=0.93)"
```

### Format with Format_Map:
```python
# Using format_map with dictionary
data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
template = "Name: {name}, Age: {age}, City: {city}"
template.format_map(data)
# → "Name: Alice, Age: 30, City: NYC"

# Advantage: can use dict subclasses
class DefaultDict(dict):
    def __missing__(self, key):
        return f"<{key}>"

data = DefaultDict(name='Bob')
"Name: {name}, Age: {age}".format_map(data)
# → "Name: Bob, Age: <age>"
```

---

## %-FORMATTING - OLD STYLE (LEGACY)

The `%` operator provides C-style formatting (legacy, but still used).

### Basic %-Formatting:
```python
# String
"Hello %s" % "World"                           # → "Hello World"

# Integer
"Number: %d" % 42                              # → "Number: 42"

# Float
"Pi: %f" % 3.14159                             # → "Pi: 3.141590"

# Multiple values (tuple)
"%s is %d years old" % ("Alice", 30)
# → "Alice is 30 years old"
```

### Format Specifiers:
```python
# %s - String
"%s" % "text"                                  # → "text"

# %d - Decimal integer
"%d" % 42                                      # → "42"
"%5d" % 42                                     # → "   42" (width 5)
"%05d" % 42                                    # → "00042" (zero pad)

# %f - Float
"%f" % 3.14                                    # → "3.140000" (default 6 decimals)
"%.2f" % 3.14159                               # → "3.14" (2 decimals)
"%10.2f" % 3.14                                # → "      3.14" (width + precision)

# %e - Scientific notation
"%e" % 1234567                                 # → "1.234567e+06"
"%.2e" % 1234567                               # → "1.23e+06"

# %x - Hexadecimal
"%x" % 255                                     # → "ff"
"%X" % 255                                     # → "FF"
"%#x" % 255                                    # → "0xff" (with prefix)

# %o - Octal
"%o" % 64                                      # → "100"
"%#o" % 64                                     # → "0o100"

# %% - Literal percent
"100%%" % ()                                   # → "100%"
```

### Named Placeholders:
```python
# Dictionary-based formatting
"%(name)s is %(age)d" % {'name': 'Alice', 'age': 30}
# → "Alice is 30"

# Practical use
data = {'name': 'Bob', 'score': 95, 'grade': 'A'}
"Student: %(name)s, Score: %(score)d, Grade: %(grade)s" % data
# → "Student: Bob, Score: 95, Grade: A"
```

### Width and Precision:
```python
# Width
"%10s" % "Hi"                                  # → "        Hi"
"%-10s" % "Hi"                                 # → "Hi        " (left aligned)

# Integer width
"%5d" % 42                                     # → "   42"
"%05d" % 42                                    # → "00042"

# Float width and precision
"%10.2f" % 3.14                                # → "      3.14"
"%010.2f" % 3.14                               # → "0000003.14"
```

### Sign Control:
```python
# Plus sign for positive
"%+d" % 42                                     # → "+42"
"%+d" % -42                                    # → "-42"

# Space for positive
"% d" % 42                                     # → " 42"
"% d" % -42                                    # → "-42"
```

---

## PRINT FUNCTION - COMPREHENSIVE GUIDE

The `print()` function outputs text with control over formatting, separators, and destinations.

### Basic Print:
```python
# Simple print
print("Hello, World!")                         # → Hello, World!

# Multiple arguments
print("Hello", "World")                        # → Hello World

# Variables
name = "Alice"
age = 30
print("Name:", name, "Age:", age)              # → Name: Alice Age: 30

# Print newline
print()                                        # → (blank line)
```

### Custom Separator (sep):
```python
# Default separator is space
print("A", "B", "C")                           # → A B C

# Custom separator
print("A", "B", "C", sep=", ")                 # → A, B, C
print("A", "B", "C", sep=" | ")                # → A | B | C
print("A", "B", "C", sep="-")                  # → A-B-C
print("A", "B", "C", sep="")                   # → ABC (no separator)

# Multiple lines with separator
print("Line 1", "Line 2", "Line 3", sep="\n")
# → Line 1
#   Line 2
#   Line 3

# Tab separator
print("Name", "Age", "City", sep="\t")         # → Name    Age    City
```

### Custom Ending (end):
```python
# Default ending is newline '\n'
print("Hello")
print("World")
# → Hello
#   World

# Custom ending
print("Hello", end=" ")
print("World")                                 # → Hello World (same line)

# No ending
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" Done!")                                # → Loading... Done!

# Custom ending character
print("Item 1", end=" | ")
print("Item 2", end=" | ")
print("Item 3")                                # → Item 1 | Item 2 | Item 3

# Empty ending
for i in range(5):
    print(i, end="")                           # → 01234
print()  # Add newline at end
```

### Print to File:
```python
# Print to file
with open('output.txt', 'w') as f:
    print("Hello, World!", file=f)

# Multiple prints to file
with open('output.txt', 'w') as f:
    print("Line 1", file=f)
    print("Line 2", file=f)
    print("Line 3", file=f)

# Print to stderr
import sys
print("Error message", file=sys.stderr)

# Redirect output
original_stdout = sys.stdout
with open('log.txt', 'w') as f:
    sys.stdout = f
    print("This goes to file")
    sys.stdout = original_stdout
print("This goes to console")
```

### Flush Output:
```python
import time

# Without flush (buffered)
for i in range(5):
    print(i, end=" ")
    time.sleep(1)
# Output appears all at once after 5 seconds

# With flush (immediate)
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)
# Each number appears immediately

# Progress indicator
import sys
for i in range(100):
    print(f"\rProgress: {i+1}%", end="", flush=True)
    time.sleep(0.05)
print()  # Newline at end
```

### Print with Unpacking:
```python
# Unpack list
items = ["apple", "banana", "cherry"]
print(*items)                                  # → apple banana cherry
print(*items, sep=", ")                        # → apple, banana, cherry

# Unpack range
print(*range(5))                               # → 0 1 2 3 4
print(*range(1, 6), sep=" + ")                 # → 1 + 2 + 3 + 4 + 5

# Unpack string
print(*"HELLO")                                # → H E L L O
print(*"HELLO", sep="-")                       # → H-E-L-L-O
```

### Combined Parameters:
```python
# sep + end
print("A", "B", sep="-", end=" | ")
print("C", "D", sep="-")                       # → A-B | C-D

# sep + end + file
with open('output.txt', 'w') as f:
    print("Line 1", "data1", sep=": ", end="\n---\n", file=f)
    print("Line 2", "data2", sep=": ", end="\n---\n", file=f)

# sep + end + flush
for i in range(3):
    print(f"Step {i+1}", end="...", flush=True, sep="")
    time.sleep(1)
print("Done!")
```

### Pretty Printing:
```python
# Print dictionary (basic)
data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
print(data)
# → {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Print dictionary (formatted)
for key, value in data.items():
    print(f"{key:10} : {value}")
# → name       : Alice
#   age        : 30
#   city       : NYC

# Print list (one per line)
items = ['apple', 'banana', 'cherry']
print(*items, sep="\n")
# → apple
#   banana
#   cherry

# Using pprint module
from pprint import pprint
complex_data = {
    'users': [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ],
    'settings': {'theme': 'dark', 'lang': 'en'}
}
pprint(complex_data, indent=2)
```

### Table Printing:
```python
# Simple table
print(f"{'Name':<10} {'Age':>5} {'City':<10}")
print("-" * 27)
print(f"{'Alice':<10} {30:>5} {'NYC':<10}")
print(f"{'Bob':<10} {25:>5} {'LA':<10}")
# → Name       Age City      
#   ---------------------------
#   Alice       30 NYC       
#   Bob         25 LA        

# Dynamic table
data = [
    ['Alice', 30, 'NYC'],
    ['Bob', 25, 'LA'],
    ['Charlie', 35, 'Chicago']
]

# Header
print(f"{'Name':<10} {'Age':>5} {'City':<10}")
print("=" * 27)

# Rows
for name, age, city in data:
    print(f"{name:<10} {age:>5} {city:<10}")
```

### Progress Bars:
```python
import time

# Simple progress bar
def progress_bar(total):
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = '█' * int(percent / 2)
        print(f"\r[{bar:<50}] {percent:.0f}%", end="", flush=True)
        time.sleep(0.1)
    print()  # Newline at end

progress_bar(50)

# Spinner
def spinner(duration):
    chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\rLoading {chars[i % 4]}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print("\rLoading complete!")

spinner(3)
```

### Colored Output (ANSI):
```python
# ANSI color codes
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
BOLD = "\033[1m"

# Colored text
print(f"{RED}Error message{RESET}")
print(f"{GREEN}Success message{RESET}")
print(f"{YELLOW}Warning message{RESET}")
print(f"{BLUE}Info message{RESET}")

# Bold text
print(f"{BOLD}Bold text{RESET}")

# Combined
print(f"{BOLD}{RED}Bold Red Error{RESET}")

# Background colors
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
print(f"{BG_RED}Red background{RESET}")
print(f"{BG_GREEN}Green background{RESET}")
```

---

## ADVANCED FORMATTING PATTERNS

### Pattern 1: Currency Formatting
```python
# US Dollar
price = 1234.56
f"${price:,.2f}"                               # → "$1,234.56"
f"${price:>10,.2f}"                            # → " $1,234.56" (right aligned)

# Multiple currencies
prices = {'USD': 1234.56, 'EUR': 1050.00, 'GBP': 950.75}
for currency, amount in prices.items():
    print(f"{currency}: {amount:>10,.2f}")
# → USD:   1,234.56
#   EUR:   1,050.00
#   GBP:     950.75

# With currency symbols
symbols = {'USD': '$', 'EUR': '€', 'GBP': '£'}
for currency, amount in prices.items():
    symbol = symbols[currency]
    print(f"{currency}: {symbol}{amount:>9,.2f}")
```

### Pattern 2: Date and Time Formatting
```python
from datetime import datetime, date, time

now = datetime.now()

# Using f-strings with strftime
f"{now:%Y-%m-%d}"                              # → "2025-12-12"
f"{now:%B %d, %Y}"                             # → "December 12, 2025"
f"{now:%I:%M %p}"                              # → "03:45 PM"
f"{now:%A, %B %d, %Y at %I:%M %p}"             # → "Thursday, December 12, 2025 at 03:45 PM"

# ISO format
f"{now:%Y-%m-%d %H:%M:%S}"                     # → "2025-12-12 15:45:30"

# Custom formats
f"{now:%d/%m/%Y}"                              # → "12/12/2025" (DD/MM/YYYY)
f"{now:%m/%d/%Y}"                              # → "12/12/2025" (MM/DD/YYYY)

# Time only
f"{now:%H:%M:%S}"                              # → "15:45:30" (24-hour)
f"{now:%I:%M:%S %p}"                           # → "03:45:30 PM" (12-hour)

# Combining with other formatting
birthday = date(1990, 5, 15)
name = "Alice"
age = 35
f"{name} was born on {birthday:%B %d, %Y} (age {age})"
# → "Alice was born on May 15, 1990 (age 35)"
```

### Pattern 3: File Size Formatting
```python
def format_bytes(bytes_value):
    """Format bytes in human-readable form"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:3.1f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f} PB"

# Usage
print(format_bytes(1024))                      # → "1.0 KB"
print(format_bytes(1234567))                   # → "1.2 MB"
print(format_bytes(1234567890))                # → "1.1 GB"

# With formatting
sizes = [512, 1024, 1048576, 1073741824]
for size in sizes:
    print(f"{size:>12} bytes = {format_bytes(size):>10}")
# →         512 bytes =      512 B
#        1024 bytes =      1.0 KB
#     1048576 bytes =      1.0 MB
#  1073741824 bytes =      1.0 GB
```

### Pattern 4: ASCII Art and Boxes
```python
# Simple box
def box(text, width=None):
    if width is None:
        width = len(text) + 4
    print("┌" + "─" * (width - 2) + "┐")
    print(f"│ {text:^{width-4}} │")
    print("└" + "─" * (width - 2) + "┘")

box("Hello, World!")
# → ┌─────────────────┐
#   │ Hello, World!   │
#   └─────────────────┘

# Menu
def print_menu(title, options):
    width = max(len(title), max(len(opt) for opt in options)) + 6
    print("╔" + "═" * (width - 2) + "╗")
    print(f"║ {title:^{width-4}} ║")
    print("╠" + "═" * (width - 2) + "╣")
    for i, option in enumerate(options, 1):
        print(f"║ {i}. {option:<{width-7}}║")
    print("╚" + "═" * (width - 2) + "╝")

print_menu("Main Menu", ["Start Game", "Options", "Exit"])
```

### Pattern 5: Alignment and Columns
```python
# Multi-column data
data = [
    ("Alice", 30, "NYC", 85000),
    ("Bob", 25, "LA", 75000),
    ("Charlie", 35, "Chicago", 95000)
]

# Header
print(f"{'Name':<12} {'Age':>4} {'City':<10} {'Salary':>10}")
print("─" * 40)

# Data rows
for name, age, city, salary in data:
    print(f"{name:<12} {age:>4} {city:<10} ${salary:>9,}")
# → Name         Age City       Salary
#   ────────────────────────────────────────
#   Alice         30 NYC        $  85,000
#   Bob           25 LA         $  75,000
#   Charlie       35 Chicago    $  95,000

# Dynamic column widths
names = ["Alice", "Bob", "Christopher"]
name_width = max(len(n) for n in names)
for name in names:
    print(f"{name:<{name_width}} | Info")
```

### Pattern 6: Number Padding and Formatting
```python
# Invoice numbers
for i in range(1, 11):
    print(f"INV-{i:04d}")                      # → INV-0001, INV-0002, ...

# IP addresses
octets = [192, 168, 1, 1]
ip = ".".join(f"{octet:3d}" for octet in octets)
print(ip)                                      # → "192.168.  1.  1"

# Better IP
ip = ".".join(str(octet) for octet in octets)
print(ip)                                      # → "192.168.1.1"

# Version numbers
major, minor, patch = 1, 2, 3
f"v{major}.{minor}.{patch}"                    # → "v1.2.3"

# Phone numbers
phone = 5551234567
f"({phone:010d})"                              # → "(5551234567)"
# Better format
f"({phone//10000000:03d}) {phone//10000%1000:03d}-{phone%10000:04d}"
# → "(555) 123-4567"
```

### Pattern 7: Binary, Hex, Octal Display
```python
num = 42

# All formats
print(f"Decimal: {num:d}")                     # → Decimal: 42
print(f"Binary:  {num:#010b}")                 # → Binary:  0b00101010
print(f"Octal:   {num:#05o}")                  # → Octal:   0o52
print(f"Hex:     {num:#04x}")                  # → Hex:     0x2a

# Table of representations
for n in [8, 16, 32, 64, 128]:
    print(f"{n:3d} = {n:#010b} = {n:#05o} = {n:#04x}")
# →   8 = 0b00001000 = 0o010 = 0x08
#   16 = 0b00010000 = 0o020 = 0x10
#   32 = 0b00100000 = 0o040 = 0x20
#   64 = 0b01000000 = 0o100 = 0x40
#  128 = 0b10000000 = 0o200 = 0x80
```

### Pattern 8: Scientific Data Display
```python
# Scientific notation with proper formatting
data = [1.23e-10, 4.56e-5, 7.89e0, 1.23e5, 4.56e10]

print(f"{'Value':>15} {'Scientific':>15} {'Fixed':>15}")
print("─" * 47)
for val in data:
    print(f"{val:>15.2e} {val:>15.6e} {val:>15.2f}")

# Chemistry/Physics formatting
avogadro = 6.02214076e23
planck = 6.62607015e-34

print(f"Avogadro's number: {avogadro:.2e} mol⁻¹")
print(f"Planck constant:   {planck:.5e} J⋅s")
```

### Pattern 9: Conditional Formatting
```python
# Color code based on value
def format_grade(score):
    if score >= 90:
        return f"{score:3d} (A) ✓"
    elif score >= 80:
        return f"{score:3d} (B) ✓"
    elif score >= 70:
        return f"{score:3d} (C) ○"
    else:
        return f"{score:3d} (F) ✗"

scores = [95, 85, 72, 65]
for i, score in enumerate(scores, 1):
    print(f"Student {i}: {format_grade(score)}")

# Status indicators
def format_status(value, threshold):
    symbol = "●" if value > threshold else "○"
    color = "HIGH" if value > threshold else "LOW"
    return f"{value:6.2f} {symbol} [{color}]"

values = [75.5, 45.2, 80.1, 30.0]
for val in values:
    print(format_status(val, 50))
```

### Pattern 10: Template Strings
```python
from string import Template

# Basic template
template = Template("Hello, $name! You are $age years old.")
result = template.substitute(name="Alice", age=30)
print(result)
# → "Hello, Alice! You are 30 years old."

# Safe substitute (doesn't raise error for missing keys)
template = Template("$greeting, $name!")
result = template.safe_substitute(greeting="Hello")
print(result)
# → "Hello, $name!" (missing name not replaced)

# Template for reports
report_template = Template("""
╔═══════════════════════════════════╗
║        MONTHLY REPORT             ║
╠═══════════════════════════════════╣
║ Month: $month                     ║
║ Sales: $$$sales                   ║
║ Goal:  $$$goal                    ║
║ Status: $status                   ║
╚═══════════════════════════════════╝
""")

print(report_template.substitute(
    month="December",
    sales="125,000",
    goal="100,000",
    status="EXCEEDED ✓"
))
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: Missing Format Specifier Colon
```python
# ❌ WRONG
# f"{value.2f}"                              # SyntaxError

# ✅ CORRECT
f"{value:.2f}"                               # Need colon before format spec
```

### Error 2: Mixing Positional and Named Without Index
```python
# ❌ WRONG (in format())
# "{} {name}".format("Hello", name="World")  # Error in Python 3.1+

# ✅ CORRECT
"{0} {name}".format("Hello", name="World")   # Use index for positional
```

### Error 3: Forgetting to Convert to String
```python
# ❌ WRONG (in %-formatting)
# "%s %s" % (42, 3.14)                       # Works but not type-safe

# ✅ CORRECT (explicit types)
"%d %.2f" % (42, 3.14)                       # Use correct type specifiers
```

### Error 4: Unmatched Braces in F-Strings
```python
# ❌ WRONG
# f"{{value}"                                # Unmatched brace

# ✅ CORRECT
f"{{value}}"                                 # → "{value}"
f"{{{value}}}"                               # → "{42}" (if value=42)
```

### Error 5: Print Separator/End Type Error
```python
# ❌ WRONG
# print("A", "B", sep=123)                   # TypeError: sep must be str

# ✅ CORRECT
print("A", "B", sep=str(123))                # Convert to string
print("A", "B", sep="123")                   # Use string literal
```

---

## PERFORMANCE TIPS

1. **F-strings are fastest** (Python 3.6+)
   ```python
   # FASTEST
   name = "Alice"
   f"Hello, {name}"
   
   # SLOWER
   "Hello, {}".format(name)
   
   # SLOWEST
   "Hello, " + name
   ```

2. **Avoid repeated formatting in loops**
   ```python
   # SLOW
   for i in range(1000):
       print(f"{i:05d}")
   
   # FASTER
   formatted = [f"{i:05d}" for i in range(1000)]
   print("\n".join(formatted))
   ```

3. **Use join() for multiple strings**
   ```python
   # SLOW
   result = ""
   for item in items:
       result += str(item) + ", "
   
   # FAST
   result = ", ".join(str(item) for item in items)
   ```

4. **Format once, reuse**
   ```python
   # SLOW (if used multiple times)
   for _ in range(100):
       header = f"{'Name':<10} {'Age':>5}"
   
   # FAST
   header = f"{'Name':<10} {'Age':>5}"
   for _ in range(100):
       print(header)
   ```

5. **Use sys.stdout.write for performance-critical output**
   ```python
   import sys
   
   # print() has overhead
   for i in range(10000):
       print(i)
   
   # Faster for many small writes
   for i in range(10000):
       sys.stdout.write(f"{i}\n")
   ```

---

## SUMMARY - KEY TAKEAWAYS

**Formatting Methods**:
1. **F-strings (f"{}")**: Modern, fast, readable - **RECOMMENDED**
2. **str.format()**: Versatile, supports templates
3. **%-formatting**: Legacy, C-style - use only for compatibility

**Format Specifications**:
- **Alignment**: `<` (left), `>` (right), `^` (center)
- **Width**: `{:10}` (minimum 10 characters)
- **Precision**: `{:.2f}` (2 decimal places)
- **Type**: `d` (int), `f` (float), `s` (string), `x` (hex), etc.
- **Sign**: `+` (force), `-` (default), ` ` (space for positive)
- **Padding**: `{:0>10}` (zero pad), `{:*^10}` (fill with *)
- **Grouping**: `{:,}` (comma), `{:_}` (underscore)

**Print Function**:
- **sep**: Custom separator between arguments
- **end**: Custom line ending
- **file**: Redirect output to file
- **flush**: Force immediate output

**Best Practices**:
1. Use f-strings for modern Python (3.6+)
2. Use `.format()` for templates and dynamic formatting
3. Avoid %-formatting unless required for compatibility
4. Use `print(sep=...)` instead of manual string concatenation
5. Use `flush=True` for real-time output (progress bars, etc.)
6. Format numbers with appropriate precision
7. Align columns for readable tables
8. Use debug f-strings `{var=}` for quick debugging
