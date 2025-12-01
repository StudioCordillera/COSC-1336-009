# STRING_METHODS

## Core Definition
**Strings** are immutable sequences of Unicode characters. Support extensive methods for manipulation, formatting, validation, and searching.

**Tags**: #string #immutable #text-processing #formatting #validation

---

## COMPLETE STRING METHODS QUICK REFERENCE

### STRING METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# CASE CONVERSION METHODS
# ═══════════════════════════════════════════════════════════════════════════
str.upper()                  # String | Convert to uppercase | Returns new uppercase string
str.lower()                  # String | Convert to lowercase | Returns new lowercase string
str.capitalize()             # String | First char upper, rest lower | Returns new capitalized string
str.title()                  # String | Title case (each word capitalized) | Returns new title-cased string
str.swapcase()               # String | Swap case of all chars | Returns new string with inverted case
str.casefold()               # String | Aggressive lowercase for comparison | Returns new casefolded string

# ═══════════════════════════════════════════════════════════════════════════
# WHITESPACE METHODS
# ═══════════════════════════════════════════════════════════════════════════
str.strip()                  # String | Remove leading/trailing whitespace | Returns new stripped string
str.strip(chars)             # String | Remove specified chars from ends | Returns new stripped string
str.lstrip()                 # String | Remove leading whitespace | Returns new left-stripped string
str.lstrip(chars)            # String | Remove specified chars from left | Returns new left-stripped string
str.rstrip()                 # String | Remove trailing whitespace | Returns new right-stripped string
str.rstrip(chars)            # String | Remove specified chars from right | Returns new right-stripped string
str.removeprefix(prefix)     # String (3.9+) | Remove prefix if exists | Returns string without prefix
str.removesuffix(suffix)     # String (3.9+) | Remove suffix if exists | Returns string without suffix

# ═══════════════════════════════════════════════════════════════════════════
# SPLITTING & JOINING METHODS
# ═══════════════════════════════════════════════════════════════════════════
str.split()                  # String | Split on whitespace | Returns list of substrings
str.split(sep)               # String | Split on separator | Returns list of substrings
str.split(sep, maxsplit)     # String | Split with max splits | Returns list with max parts
str.rsplit()                 # String | Split from right on whitespace | Returns list of substrings
str.rsplit(sep, maxsplit)    # String | Split from right with max | Returns list with max parts
str.splitlines()             # String | Split on line breaks | Returns list of lines
str.splitlines(keepends=True) # String | Split keeping line breaks | Returns list with newlines
str.partition(sep)           # String | Split on first separator | Returns (before, sep, after) tuple
str.rpartition(sep)          # String | Split on last separator | Returns (before, sep, after) tuple
sep.join(iterable)           # Iterable | Join items with separator | Returns joined string

# ═══════════════════════════════════════════════════════════════════════════
# SEARCH & REPLACE METHODS
# ═══════════════════════════════════════════════════════════════════════════
str.find(sub)                # String | Find first occurrence | Returns index or -1 if not found
str.find(sub, start)         # String | Find from start position | Returns index or -1
str.find(sub, start, end)    # String | Find in range | Returns index or -1
str.rfind(sub)               # String | Find last occurrence | Returns index or -1
str.rfind(sub, start, end)   # String | Find last in range | Returns index or -1
str.index(sub)               # String | Find first occurrence | Returns index or ValueError
str.index(sub, start, end)   # String | Find in range | Returns index or ValueError
str.rindex(sub)              # String | Find last occurrence | Returns index or ValueError
str.count(sub)               # String | Count occurrences | Returns int count
str.count(sub, start, end)   # String | Count in range | Returns int count
str.replace(old, new)        # String | Replace all occurrences | Returns new string with replacements
str.replace(old, new, count) # String | Replace first count occurrences | Returns new string with replacements

# ═══════════════════════════════════════════════════════════════════════════
# VALIDATION/CHECK METHODS (Boolean Returns)
# ═══════════════════════════════════════════════════════════════════════════
str.startswith(prefix)       # String | Check if starts with | Returns True/False
str.startswith(tuple)        # String | Check multiple prefixes | Returns True/False
str.startswith(prefix, start, end) # String | Check in range | Returns True/False
str.endswith(suffix)         # String | Check if ends with | Returns True/False
str.endswith(tuple)          # String | Check multiple suffixes | Returns True/False
str.endswith(suffix, start, end) # String | Check in range | Returns True/False
str.isalpha()                # String | Check all alphabetic | Returns True/False
str.isdigit()                # String | Check all digits | Returns True/False
str.isalnum()                # String | Check alphanumeric | Returns True/False
str.isspace()                # String | Check all whitespace | Returns True/False
str.isupper()                # String | Check all uppercase | Returns True/False
str.islower()                # String | Check all lowercase | Returns True/False
str.istitle()                # String | Check title case | Returns True/False
str.isdecimal()              # String | Check decimal digits | Returns True/False
str.isnumeric()              # String | Check numeric chars | Returns True/False
str.isidentifier()           # String | Check valid Python identifier | Returns True/False
str.isprintable()            # String | Check all printable | Returns True/False
str.isascii()                # String (3.7+) | Check all ASCII | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# ALIGNMENT & PADDING METHODS
# ═══════════════════════════════════════════════════════════════════════════
str.center(width)            # String | Center in width | Returns centered string with spaces
str.center(width, fillchar)  # String | Center with fill char | Returns centered string with fillchar
str.ljust(width)             # String | Left-justify in width | Returns left-aligned string
str.ljust(width, fillchar)   # String | Left-justify with fill | Returns left-aligned string
str.rjust(width)             # String | Right-justify in width | Returns right-aligned string
str.rjust(width, fillchar)   # String | Right-justify with fill | Returns right-aligned string
str.zfill(width)             # String | Pad with zeros on left | Returns zero-padded string
str.expandtabs()             # String | Expand tabs to spaces | Returns string with spaces
str.expandtabs(tabsize)      # String | Expand tabs custom size | Returns string with custom spacing

# ═══════════════════════════════════════════════════════════════════════════
# FORMATTING METHODS
# ═══════════════════════════════════════════════════════════════════════════
str.format(*args, **kwargs)  # String | Format with placeholders | Returns formatted string
str.format_map(mapping)      # String | Format with dict | Returns formatted string
f"{var}"                     # F-string | Inline variable interpolation | Returns formatted string
f"{var:format_spec}"         # F-string | Formatted interpolation | Returns formatted string
f"{expr=}"                   # F-string (3.8+) | Debug format | Returns "expr=value"
"%s %d" % (str, int)         # %-formatting | Old-style format | Returns formatted string
"{}".format(val)             # String | Positional format | Returns formatted string
"{0} {1}".format(a, b)       # String | Indexed format | Returns formatted string
"{name}".format(name=val)    # String | Named format | Returns formatted string

# ═══════════════════════════════════════════════════════════════════════════
# ENCODING & TRANSLATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
str.encode()                 # String | Encode to bytes (UTF-8) | Returns bytes object
str.encode(encoding)         # String | Encode with encoding | Returns bytes object
str.encode(encoding, errors) # String | Encode with error handling | Returns bytes object
str.translate(table)         # String | Translate using table | Returns translated string
str.maketrans(x, y)          # Static | Create translation table | Returns translation table
str.maketrans(dict)          # Static | Create table from dict | Returns translation table

# ═══════════════════════════════════════════════════════════════════════════
# ACCESS & UTILITY METHODS
# ═══════════════════════════════════════════════════════════════════════════
str[index]                   # String | Access char by position | Returns char or IndexError
str[start:end]               # String | Slice substring | Returns new substring
str[start:end:step]          # String | Slice with step | Returns new substring with step
str[-1]                      # String | Access last char | Returns last char
len(str)                     # String | Get length | Returns int count of chars
str in other                 # String | Check substring membership | Returns True/False
str not in other             # String | Check substring absence | Returns True/False
min(str)                     # String | Find minimum char | Returns char with lowest value
max(str)                     # String | Find maximum char | Returns char with highest value
ord(char)                    # Single char | Get Unicode code point | Returns int code point
chr(int)                     # Integer | Get char from code point | Returns character string
str(obj)                     # Any object | Convert to string | Returns string representation
repr(str)                    # String | Get repr string | Returns quoted/escaped string
ascii(str)                   # String | Get ASCII repr | Returns ASCII-only repr string

# ═══════════════════════════════════════════════════════════════════════════
# ITERATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
for char in str:             # String | Iterate characters | Yields each character
enumerate(str)               # String | Index + iterate | Yields (index, char) tuples
enumerate(str, start=1)      # String | Index from start + iterate | Yields (index, char) from start
zip(str1, str2)              # Multiple strings | Pair chars together | Yields tuples of paired chars
reversed(str)                # String | Reverse iteration | Yields chars in reverse order
iter(str)                    # String | Create iterator | Returns iterator over chars
next(iter(str))              # String iterator | Get next char | Returns next char or StopIteration
filter(func, str)            # String + function | Filter chars | Returns iterator of matches
map(func, str)               # String + function | Apply to all chars | Returns iterator of results

# ═══════════════════════════════════════════════════════════════════════════
# STRING CREATION & OPERATORS
# ═══════════════════════════════════════════════════════════════════════════
''                           # Literal | Empty string | Returns empty string
'text'                       # Literal | Single quotes | Returns string
"text"                       # Literal | Double quotes | Returns string
'''text'''                   # Literal | Triple single quotes | Returns multiline string
"""text"""                   # Literal | Triple double quotes | Returns multiline string
r'text'                      # Raw string | No escape processing | Returns raw string
b'text'                      # Bytes literal | Byte string | Returns bytes object
f'text {var}'                # F-string | Formatted string | Returns formatted string
str1 + str2                  # Concatenation | Join strings | Returns combined string
str * n                      # Repetition | Repeat string n times | Returns repeated string
str[:]                       # Slicing | Full copy | Returns new string copy

# ═══════════════════════════════════════════════════════════════════════════
# COMPARISON OPERATORS
# ═══════════════════════════════════════════════════════════════════════════
str1 == str2                 # Two strings | Check equality | Returns True/False
str1 != str2                 # Two strings | Check inequality | Returns True/False
str1 < str2                  # Two strings | Lexicographic less than | Returns True/False
str1 > str2                  # Two strings | Lexicographic greater than | Returns True/False
str1 <= str2                 # Two strings | Less than or equal | Returns True/False
str1 >= str2                 # Two strings | Greater than or equal | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# ESCAPE SEQUENCES
# ═══════════════════════════════════════════════════════════════════════════
\n                           # Escape | Newline | Inserts line break
\t                           # Escape | Tab | Inserts horizontal tab
\r                           # Escape | Carriage return | Returns to line start
\\                           # Escape | Backslash | Inserts literal backslash
\'                           # Escape | Single quote | Inserts single quote
\"                           # Escape | Double quote | Inserts double quote
\b                           # Escape | Backspace | Moves cursor back one
\f                           # Escape | Form feed | Page break
\v                           # Escape | Vertical tab | Vertical spacing
\0                           # Escape | Null character | Null byte
\xhh                         # Escape | Hex value | Char from hex code
\ooo                         # Escape | Octal value | Char from octal code
\uxxxx                       # Escape | Unicode 16-bit | Unicode character
\Uxxxxxxxx                   # Escape | Unicode 32-bit | Unicode character
```

### COMMON OPERATION EXAMPLES

```python
# Example string
text = "Hello World"

# Case conversion
text.upper()                 # → "HELLO WORLD"
text.lower()                 # → "hello world"
text.title()                 # → "Hello World"

# Stripping
"  hello  ".strip()          # → "hello"
"###hello###".strip('#')     # → "hello"

# Splitting/Joining
text.split()                 # → ['Hello', 'World']
"-".join(['a', 'b', 'c'])    # → "a-b-c"

# Searching
text.find('World')           # → 6
text.count('l')              # → 3
text.startswith('Hello')     # → True

# Replacing
text.replace('World', 'Python')  # → "Hello Python"

# Validation
"123".isdigit()              # → True
"abc".isalpha()              # → True
"abc123".isalnum()           # → True

# Formatting
name = "John"
f"Hello {name}"              # → "Hello John"
"Hello {}".format(name)      # → "Hello John"
"Hello %s" % name            # → "Hello John"

# Alignment
"Hi".center(10)              # → "   Hi    "
"Hi".ljust(10)               # → "Hi        "
"Hi".rjust(10)               # → "        Hi"
"42".zfill(5)                # → "00042"
```

---

## DETAILED STRING OPERATIONS

### 1. SLICING PATTERNS

```python
text = "Python Programming"

# Basic slicing
text[0:6]                    # → "Python" (start to 6)
text[7:]                     # → "Programming" (7 to end)
text[:6]                     # → "Python" (start to 6)
text[:]                      # → "Python Programming" (full copy)

# Negative indexing
text[-11:]                   # → "Programming" (last 11 chars)
text[:-12]                   # → "Python" (everything except last 12)
text[-11:-5]                 # → "Progra" (slice from negative indices)

# Step slicing
text[::2]                    # → "Pto rgamn" (every 2nd char)
text[1::2]                   # → "yhnPoarmi" (every 2nd starting at 1)
text[::-1]                   # → "gnimmargorP nohtyP" (reverse)
text[6:0:-1]                 # → "nohtyP" (reverse slice)

# Substring check
"Python" in text             # → True
"Java" not in text           # → True
```

### 2. FORMAT STRING PATTERNS

```python
# F-strings (Python 3.6+)
name = "Alice"
age = 30
f"Name: {name}, Age: {age}"                    # → "Name: Alice, Age: 30"
f"Age next year: {age + 1}"                    # → "Age next year: 31"

# Formatting specifiers
pi = 3.14159
f"{pi:.2f}"                                    # → "3.14" (2 decimals)
f"{pi:10.2f}"                                  # → "      3.14" (width 10)
f"{pi:010.2f}"                                 # → "0000003.14" (zero-pad)

num = 42
f"{num:b}"                                     # → "101010" (binary)
f"{num:o}"                                     # → "52" (octal)
f"{num:x}"                                     # → "2a" (hex lowercase)
f"{num:X}"                                     # → "2A" (hex uppercase)

# Alignment in f-strings
f"{name:<10}"                                  # → "Alice     " (left)
f"{name:>10}"                                  # → "     Alice" (right)
f"{name:^10}"                                  # → "  Alice   " (center)
f"{name:*^10}"                                 # → "**Alice***" (center with *)

# Debug format (Python 3.8+)
x = 42
f"{x=}"                                        # → "x=42"
f"{x + 10=}"                                   # → "x + 10=52"

# .format() method
"Hello {0} {1}".format("Alice", "Bob")         # → "Hello Alice Bob"
"Hello {1} {0}".format("Alice", "Bob")         # → "Hello Bob Alice"
"Name: {name}, Age: {age}".format(name="Alice", age=30)  # → "Name: Alice, Age: 30"
"{:10}".format("Hi")                           # → "Hi        " (width 10)
"{:>10}".format("Hi")                          # → "        Hi" (right align)

# %-formatting (old style)
"Name: %s, Age: %d" % ("Alice", 30)            # → "Name: Alice, Age: 30"
"Pi: %.2f" % 3.14159                           # → "Pi: 3.14"
"Hex: %x" % 255                                # → "Hex: ff"
"Percent: %d%%" % 50                           # → "Percent: 50%"

# Template strings (from string module)
from string import Template
t = Template("Hello $name, you are $age years old")
t.substitute(name="Alice", age=30)             # → "Hello Alice, you are 30 years old"
```

### 3. SPLITTING & JOINING ADVANCED

```python
text = "apple,banana,cherry"

# Basic split
text.split(',')                                # → ['apple', 'banana', 'cherry']

# Maxsplit
text.split(',', 1)                             # → ['apple', 'banana,cherry']

# Right split
text.rsplit(',', 1)                            # → ['apple,banana', 'cherry']

# Split on whitespace (default)
"hello   world  test".split()                  # → ['hello', 'world', 'test']

# Splitlines
multiline = "Line 1\nLine 2\nLine 3"
multiline.splitlines()                         # → ['Line 1', 'Line 2', 'Line 3']
multiline.splitlines(keepends=True)            # → ['Line 1\n', 'Line 2\n', 'Line 3']

# Partition (splits into 3-tuple)
"hello:world".partition(':')                   # → ('hello', ':', 'world')
"hello:world".partition('@')                   # → ('hello:world', '', '')  # Not found
"hello:world:test".rpartition(':')             # → ('hello:world', ':', 'test')

# Join
words = ['apple', 'banana', 'cherry']
', '.join(words)                               # → "apple, banana, cherry"
''.join(words)                                 # → "applebananacherry"
'\n'.join(words)                               # → "apple\nbanana\ncherry"

# Join with non-strings (must convert)
nums = [1, 2, 3]
', '.join(map(str, nums))                      # → "1, 2, 3"
```

### 4. SEARCHING PATTERNS

```python
text = "hello world hello python"

# Find (returns -1 if not found)
text.find('hello')                             # → 0
text.find('hello', 5)                          # → 12 (start search at index 5)
text.find('hello', 5, 15)                      # → 12 (search in range)
text.find('java')                              # → -1 (not found)

# Rfind (find from right)
text.rfind('hello')                            # → 12 (last occurrence)

# Index (raises ValueError if not found)
text.index('hello')                            # → 0
# text.index('java')                           # → ValueError

# Count
text.count('hello')                            # → 2
text.count('l')                                # → 5
text.count('ll')                               # → 2

# Startswith/Endswith
text.startswith('hello')                       # → True
text.startswith(('hello', 'hi'))               # → True (tuple of options)
text.endswith('python')                        # → True
text.endswith(('.py', '.txt'))                 # → False

# Replace
text.replace('hello', 'goodbye')               # → "goodbye world goodbye python"
text.replace('hello', 'hi', 1)                 # → "hi world hello python" (max 1)
```

### 5. VALIDATION METHODS (is* family)

```python
# Character type checks
"abc".isalpha()              # → True
"123".isdigit()              # → True
"abc123".isalnum()           # → True
"   ".isspace()              # → True

# Case checks
"HELLO".isupper()            # → True
"hello".islower()            # → True
"Hello World".istitle()      # → True

# Number checks
"123".isdecimal()            # → True (0-9 only)
"123".isnumeric()            # → True (includes fractions, superscripts)
"½".isnumeric()              # → True
"½".isdecimal()              # → False

# Identifier check
"variable_name".isidentifier()  # → True
"123abc".isidentifier()         # → False (can't start with digit)

# ASCII check (Python 3.7+)
"hello".isascii()            # → True
"hello🎉".isascii()          # → False

# Printable check
"hello".isprintable()        # → True
"hello\n".isprintable()      # → False (contains non-printable \n)
```

### 6. ENCODING & TRANSLATION

```python
# Encoding
text = "Hello"
text.encode()                # → b'Hello' (default UTF-8)
text.encode('ascii')         # → b'Hello'

# Unicode
text = "Héllo"
text.encode('utf-8')         # → b'H\xc3\xa9llo'
text.encode('ascii', errors='ignore')  # → b'Hllo' (skip non-ASCII)
text.encode('ascii', errors='replace') # → b'H?llo' (replace with ?)

# Decoding (bytes to string)
b'Hello'.decode()            # → "Hello"

# Translation
# Remove vowels
remove_vowels = str.maketrans('', '', 'aeiouAEIOU')
"Hello World".translate(remove_vowels)  # → "Hll Wrld"

# Character mapping
swap = str.maketrans('aeiou', '12345')
"hello".translate(swap)      # → "h2ll4"

# Dictionary mapping
mapping = {'a': '1', 'e': '2', 'i': '3'}
trans = str.maketrans(mapping)
"aeiou".translate(trans)     # → "12345"
```

### 7. MULTILINE STRING PATTERNS

```python
# Triple quotes
multiline = """
Line 1
Line 2
Line 3
"""

# Preserve formatting
poem = """\
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""

# Escape newlines
text = "Line 1\n\
Line 2\n\
Line 3"

# Raw strings (no escape processing)
path = r"C:\Users\name\file.txt"               # → "C:\Users\name\file.txt"
regex = r"\d+\.\d+"                            # → "\d+\.\d+" (not "\d+.d+")

# Combining raw and f-strings (Python 3.6+)
name = "Alice"
fr"Hello {name}\n"                             # → "Hello Alice\\n" (raw f-string)
```

### 8. ITERATION PATTERNS

```python
text = "Python"

# Basic iteration
for char in text:
    print(char)              # P, y, t, h, o, n

# Enumerate (index + char)
for i, char in enumerate(text):
    print(f"{i}: {char}")    # 0: P, 1: y, 2: t, 3: h, 4: o, 5: n

# Enumerate with custom start
for i, char in enumerate(text, start=1):
    print(f"{i}: {char}")    # 1: P, 2: y, 3: t, 4: h, 5: o, 6: n

# Zip multiple strings
for c1, c2 in zip("ABC", "123"):
    print(f"{c1}-{c2}")      # A-1, B-2, C-3

# Reversed iteration
for char in reversed(text):
    print(char)              # n, o, h, t, y, P

# Manual iterator
it = iter(text)
next(it)                     # → 'P'
next(it)                     # → 'y'
list(it)                     # → ['t', 'h', 'o', 'n']

# Filter characters
vowels = filter(lambda c: c in 'aeiouAEIOU', text)
list(vowels)                 # → ['o']

# Map over characters
upper_chars = map(str.upper, text)
list(upper_chars)            # → ['P', 'Y', 'T', 'H', 'O', 'N']
```

### 9. COMPREHENSION PATTERNS

```python
text = "Hello World"

# List comprehension
[c for c in text]                              # → ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
[c.upper() for c in text]                      # → ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
[c for c in text if c.isalpha()]               # → ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']

# Create new string from comprehension
''.join([c.upper() for c in text])             # → "HELLO WORLD"
''.join([c for c in text if c != ' '])         # → "HelloWorld"

# Dict comprehension
{i: c for i, c in enumerate(text)}             # → {0: 'H', 1: 'e', ...}
{c: text.count(c) for c in set(text)}          # → {'H': 1, 'e': 1, 'l': 3, ...}

# Set comprehension
{c.lower() for c in text}                      # → {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
```

### 10. ADVANCED FORMATTING

```python
# Number formatting
value = 1234567.89
f"{value:,.2f}"                                # → "1,234,567.89" (thousand separator)
f"{value:_.2f}"                                # → "1_234_567.89" (underscore separator, 3.6+)

# Percentage
ratio = 0.875
f"{ratio:.2%}"                                 # → "87.50%"

# Scientific notation
big = 1234567890
f"{big:e}"                                     # → "1.234568e+09"
f"{big:.2e}"                                   # → "1.23e+09"

# Binary/Octal/Hex with prefix
num = 255
f"{num:#b}"                                    # → "0b11111111"
f"{num:#o}"                                    # → "0o377"
f"{num:#x}"                                    # → "0xff"

# Sign formatting
pos = 42
neg = -42
f"{pos:+d}"                                    # → "+42" (force sign)
f"{neg:+d}"                                    # → "-42"
f"{pos: d}"                                    # → " 42" (space for positive)

# Date formatting (with datetime)
from datetime import datetime
now = datetime.now()
f"{now:%Y-%m-%d}"                              # → "2025-01-15"
f"{now:%B %d, %Y}"                             # → "January 15, 2025"
f"{now:%I:%M %p}"                              # → "03:45 PM"

# Custom object formatting
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __format__(self, spec):
        if spec == 'short':
            return f"{self.name}"
        elif spec == 'long':
            return f"{self.name} ({self.age})"
        return str(self)

p = Person("Alice", 30)
f"{p:short}"                                   # → "Alice"
f"{p:long}"                                    # → "Alice (30)"
```

---

## PRACTICAL PROJECT PATTERNS

### Pattern 1: Input Validation
```python
def validate_ssn(ssn):
    """Validate SSN format (XXX-XX-XXXX)"""
    # Remove spaces
    ssn = ssn.strip()
    
    # Check format
    if len(ssn) != 11:
        return False
    if ssn[3] != '-' or ssn[6] != '-':
        return False
    
    # Check digits
    parts = ssn.split('-')
    return all(part.isdigit() for part in parts)

def validate_email(email):
    """Basic email validation"""
    email = email.strip().lower()
    if '@' not in email or '.' not in email:
        return False
    if email.count('@') != 1:
        return False
    return True
```

### Pattern 2: Text Processing
```python
def clean_text(text):
    """Clean and normalize text input"""
    # Strip whitespace
    text = text.strip()
    
    # Remove extra spaces
    text = ' '.join(text.split())
    
    # Title case
    text = text.title()
    
    return text

def parse_csv_line(line):
    """Parse CSV line manually"""
    # Strip and split
    fields = [field.strip() for field in line.split(',')]
    return fields
```

### Pattern 3: String Building
```python
def format_student_record(name, id, gpa):
    """Format student record for display"""
    # Build formatted string
    record = f"""
Student Information:
{'='*40}
Name: {name:<30}
ID:   {id:>10}
GPA:  {gpa:5.2f}
{'='*40}
"""
    return record.strip()

def build_table(headers, rows):
    """Build ASCII table"""
    # Calculate column widths
    widths = [max(len(str(row[i])) for row in [headers] + rows) 
              for i in range(len(headers))]
    
    # Build header
    header = ' | '.join(h.ljust(w) for h, w in zip(headers, widths))
    separator = '-+-'.join('-' * w for w in widths)
    
    # Build rows
    body = '\n'.join(' | '.join(str(cell).ljust(w) 
                      for cell, w in zip(row, widths)) 
                     for row in rows)
    
    return f"{header}\n{separator}\n{body}"
```

### Pattern 4: Parsing & Extraction
```python
def extract_numbers(text):
    """Extract all numbers from text"""
    return [int(s) for s in text.split() if s.isdigit()]

def parse_key_value(line):
    """Parse 'key: value' format"""
    if ':' not in line:
        return None, None
    
    key, value = line.split(':', 1)
    return key.strip().lower(), value.strip()

def extract_extension(filename):
    """Extract file extension"""
    if '.' not in filename:
        return ''
    return filename.rsplit('.', 1)[-1].lower()
```

### Pattern 5: Menu Display
```python
def display_menu():
    """Display formatted menu"""
    menu = """
╔════════════════════════════════╗
║        STUDENT SYSTEM          ║
╠════════════════════════════════╣
║  1. Add Student                ║
║  2. Search Student             ║
║  3. Display All                ║
║  4. Exit                       ║
╚════════════════════════════════╝
"""
    print(menu)

def get_menu_choice():
    """Get and validate menu choice"""
    while True:
        choice = input("Enter choice: ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice. Try again.")
```

### Pattern 6: File Path Handling
```python
def normalize_path(path):
    """Normalize file path (cross-platform)"""
    # Replace backslashes with forward slashes
    path = path.replace('\\', '/')
    
    # Remove trailing slash
    path = path.rstrip('/')
    
    return path

def get_filename(path):
    """Extract filename from path"""
    # Works with both / and \
    return path.replace('\\', '/').split('/')[-1]
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: Index Out of Range
```python
# WRONG
text = "Hi"
char = text[5]               # IndexError

# RIGHT
if len(text) > 5:
    char = text[5]

# OR use slicing (never fails)
char = text[5:6]             # Returns '' if out of range
```

### Error 2: Type Mismatch in Join
```python
# WRONG
nums = [1, 2, 3]
result = ', '.join(nums)     # TypeError

# RIGHT
result = ', '.join(map(str, nums))
result = ', '.join(str(n) for n in nums)
```

### Error 3: Mutating String (Impossible)
```python
# WRONG
text = "hello"
text[0] = 'H'                # TypeError (strings immutable)

# RIGHT
text = 'H' + text[1:]        # Create new string
text = text.capitalize()     # Use method
```

### Error 4: Find vs Index Confusion
```python
# WRONG
text = "hello"
pos = text.index('x')        # ValueError if not found

# RIGHT - use find for "not found" handling
pos = text.find('x')
if pos != -1:
    print(f"Found at {pos}")
else:
    print("Not found")

# OR - use index with try/except
try:
    pos = text.index('x')
except ValueError:
    print("Not found")
```

---

## PERFORMANCE TIPS

1. **Use join() instead of += for building strings**
   ```python
   # SLOW
   result = ''
   for s in strings:
       result += s
   
   # FAST
   result = ''.join(strings)
   ```

2. **Use f-strings for formatting (fastest)**
   ```python
   # SLOW
   s = "Hello %s" % name
   
   # FASTER
   s = "Hello {}".format(name)
   
   # FASTEST
   s = f"Hello {name}"
   ```

3. **Use in for membership, not find()**
   ```python
   # SLOWER
   if text.find('substring') != -1:
       pass
   
   # FASTER
   if 'substring' in text:
       pass
   ```

4. **Use string methods instead of regex for simple operations**
   ```python
   # SLOWER
   import re
   result = re.sub('old', 'new', text)
   
   # FASTER
   result = text.replace('old', 'new')
   ```
