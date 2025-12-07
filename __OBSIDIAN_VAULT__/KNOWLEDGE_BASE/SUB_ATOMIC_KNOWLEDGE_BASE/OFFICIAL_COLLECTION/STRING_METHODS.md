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

---

## UI COMPONENT CONSTRUCTION GUIDE
### String Methods for Atomic-to-App Level UI Assembly

This section maps string operations to UI component construction patterns, following atomic design principles from basic elements to complete applications.

**Tags**: #ui-construction #atomic-design #component-assembly #dpg #dearpygui

---

### UI CONSTRUCTION HIERARCHY

```
LEVEL 1: ATOMIC      → Individual UI elements (button, label, input)
LEVEL 2: MOLECULAR   → Combined elements (form field, menu item, list entry)
LEVEL 3: ORGANISM    → Complex components (form, table, navigation bar)
LEVEL 4: TEMPLATE    → Layout structures (dashboard, settings page, dialog)
LEVEL 5: APP         → Full application (multi-page, navigation, state)
```

---

## LEVEL 1: ATOMIC UI ELEMENTS
### Building Individual UI Components with Strings

### 1.1 Label Construction

```python
# Basic label formatting
def create_label(text, width=20):
    """Create formatted label text"""
    return f"{text:<{width}}"

# Status labels with indicators
def status_label(status, message):
    """Create status label with symbol"""
    symbols = {
        'success': '✓',
        'error': '✗',
        'warning': '⚠',
        'info': 'ℹ'
    }
    symbol = symbols.get(status, '•')
    return f"{symbol} {message}"

# Dynamic width labels
def create_header_label(text, total_width=50):
    """Create centered header label"""
    padding = (total_width - len(text)) // 2
    return f"{' ' * padding}{text}{' ' * padding}".ljust(total_width)

# Examples
print(create_label("Username:", 15))           # → "Username:      "
print(status_label('success', 'Connected'))    # → "✓ Connected"
print(create_header_label("Settings", 40))     # → "              Settings              "
```

### 1.2 Button Text Formatting

```python
# Button label with icon
def button_label(text, icon=''):
    """Format button with optional icon"""
    if icon:
        return f"{icon} {text}"
    return text

# Button with state
def state_button(base_text, is_active=False):
    """Create button text with state indicator"""
    if is_active:
        return f"[✓] {base_text}"
    return f"[ ] {base_text}"

# Action button with hotkey
def action_button(text, hotkey=''):
    """Format button with hotkey hint"""
    if hotkey:
        return f"{text:<20} ({hotkey})"
    return text

# Examples
print(button_label("Save", "💾"))              # → "💾 Save"
print(state_button("Dark Mode", True))         # → "[✓] Dark Mode"
print(action_button("New File", "Ctrl+N"))     # → "New File            (Ctrl+N)"
```

### 1.3 Input Field Placeholders

```python
# Placeholder text
def create_placeholder(field_name, example=''):
    """Generate placeholder text for input"""
    if example:
        return f"Enter {field_name.lower()} (e.g., {example})"
    return f"Enter {field_name.lower()}..."

# Validation hint
def input_hint(field_name, format_spec):
    """Create input format hint"""
    return f"{field_name}: {format_spec}"

# Character counter
def char_counter(current, max_chars):
    """Format character count display"""
    remaining = max_chars - current
    if remaining < 0:
        return f"⚠ {abs(remaining)} over limit"
    return f"{current}/{max_chars}"

# Examples
print(create_placeholder("Email", "user@example.com"))  # → "Enter email (e.g., user@example.com)"
print(input_hint("Phone", "XXX-XXX-XXXX"))             # → "Phone: XXX-XXX-XXXX"
print(char_counter(45, 50))                            # → "45/50"
```

### 1.4 ID and Tag Generation

```python
# Generate unique IDs
def generate_id(component_type, label):
    """Create component ID from type and label"""
    # Clean label: lowercase, replace spaces with underscores
    clean_label = label.lower().replace(' ', '_')
    clean_label = ''.join(c for c in clean_label if c.isalnum() or c == '_')
    return f"{component_type}_{clean_label}"

# Tag formatting
def create_tag(category, name):
    """Format tag string"""
    return f"{category}::{name}"

# Class name generation
def generate_class_name(*parts):
    """Generate CSS-like class name"""
    return '-'.join(part.lower() for part in parts)

# Examples
print(generate_id("btn", "Save File"))         # → "btn_save_file"
print(create_tag("user", "settings"))          # → "user::settings"
print(generate_class_name("Primary", "Button", "Large"))  # → "primary-button-large"
```

---

## LEVEL 2: MOLECULAR UI COMPONENTS
### Combining Atomic Elements into Functional Units

### 2.1 Form Field Assembly

```python
# Complete form field with label and input
def form_field(label, value='', width=30, required=False):
    """Assemble form field with label and value"""
    req_marker = '*' if required else ' '
    label_part = f"{label:<20}{req_marker}"
    value_part = f"[{value:<{width}}]"
    return f"{label_part} {value_part}"

# Field with validation message
def field_with_validation(label, value, error_msg=''):
    """Form field with validation feedback"""
    field = form_field(label, value)
    if error_msg:
        return f"{field}\n{'':>22}⚠ {error_msg}"
    return field

# Field group
def field_group(fields_dict):
    """Create multiple related fields"""
    lines = []
    max_label_len = max(len(label) for label in fields_dict.keys())
    
    for label, value in fields_dict.items():
        padded_label = f"{label}:".ljust(max_label_len + 2)
        lines.append(f"{padded_label} {value}")
    
    return '\n'.join(lines)

# Examples
print(form_field("Username", "john_doe", required=True))
# → "Username            * [john_doe                      ]"

print(field_with_validation("Email", "invalid", "Invalid email format"))
# → "Email                [invalid                       ]"
# → "                      ⚠ Invalid email format"

fields = {"First Name": "John", "Last Name": "Doe", "Age": "30"}
print(field_group(fields))
# → "First Name:  John"
# → "Last Name:   Doe"
# → "Age:         30"
```

### 2.2 Menu Item Construction

```python
# Menu item with icon and shortcut
def menu_item(label, shortcut='', icon='', enabled=True):
    """Create formatted menu item"""
    # Build components
    icon_part = f"{icon} " if icon else ""
    label_part = f"{icon_part}{label:<25}"
    shortcut_part = f"{shortcut:>10}" if shortcut else ""
    
    # Dim if disabled
    if not enabled:
        label_part = f"({label_part.strip()})"
    
    return f"{label_part}{shortcut_part}"

# Submenu indicator
def submenu_item(label, has_children=True):
    """Menu item that opens submenu"""
    arrow = " ▶" if has_children else ""
    return f"{label:<30}{arrow}"

# Menu separator
def menu_separator(width=40, char='─'):
    """Create menu separator line"""
    return char * width

# Examples
print(menu_item("New File", "Ctrl+N", "📄"))   # → "📄 New File                Ctrl+N"
print(menu_item("Save", "Ctrl+S", "💾", False))# → "(💾 Save)                  Ctrl+S"
print(submenu_item("Recent Files"))            # → "Recent Files                      ▶"
print(menu_separator())                        # → "────────────────────────────────────────"
```

### 2.3 List Item Formatting

```python
# List item with bullet
def list_item(text, bullet='•', indent=0):
    """Format list item with bullet and indentation"""
    indent_str = '  ' * indent
    return f"{indent_str}{bullet} {text}"

# Numbered list item
def numbered_item(index, text, total=None):
    """Format numbered list item"""
    if total:
        width = len(str(total))
        number = f"{index:>{width}}"
    else:
        number = str(index)
    return f"{number}. {text}"

# Checklist item
def checklist_item(text, checked=False):
    """Format checklist item"""
    checkbox = "[✓]" if checked else "[ ]"
    return f"{checkbox} {text}"

# Expandable item
def expandable_item(text, is_expanded=False):
    """Format expandable/collapsible item"""
    indicator = "▼" if is_expanded else "▶"
    return f"{indicator} {text}"

# Examples
print(list_item("First item"))                 # → "• First item"
print(list_item("Nested item", indent=1))      # → "  • Nested item"
print(numbered_item(1, "Step one", 10))        # → " 1. Step one"
print(checklist_item("Complete task", True))   # → "[✓] Complete task"
print(expandable_item("Folder", True))         # → "▼ Folder"
```

### 2.4 Key-Value Pair Display

```python
# Property display
def property_display(key, value, width=20):
    """Display key-value pair"""
    return f"{key}:".ljust(width) + str(value)

# Multi-column property
def property_columns(*pairs, col_width=25):
    """Display properties in columns"""
    columns = []
    for key, value in pairs:
        col = f"{key}: {value}".ljust(col_width)
        columns.append(col)
    return ''.join(columns)

# Property group with separator
def property_group(title, properties_dict):
    """Group related properties with title"""
    lines = [title, '─' * len(title)]
    for key, value in properties_dict.items():
        lines.append(property_display(key, value))
    return '\n'.join(lines)

# Examples
print(property_display("Name", "John Doe"))    # → "Name:               John Doe"
print(property_columns(("ID", "123"), ("Status", "Active")))
# → "ID: 123                  Status: Active           "

props = {"Created": "2024-01-01", "Modified": "2024-12-06", "Size": "1.2 MB"}
print(property_group("File Properties", props))
# → "File Properties"
# → "───────────────"
# → "Created:            2024-01-01"
# → "Modified:           2024-12-06"
# → "Size:               1.2 MB"
```

---

## LEVEL 3: ORGANISM UI ASSEMBLIES
### Building Complex Multi-Component Interfaces

### 3.1 Complete Form Construction

```python
# Full form with header, fields, and buttons
def build_form(title, fields, buttons):
    """Construct complete form interface"""
    # Header
    header_width = 50
    header = f"""
╔{'═' * (header_width - 2)}╗
║{title.center(header_width - 2)}║
╚{'═' * (header_width - 2)}╝
"""
    
    # Fields section
    field_lines = []
    for label, value, required in fields:
        field_lines.append(form_field(label, value, required=required))
    
    # Buttons section
    button_line = '  '.join(f"[{btn}]" for btn in buttons)
    button_center = button_line.center(header_width)
    
    # Assemble
    form = header + '\n'.join(field_lines) + '\n\n' + button_center
    return form

# Examples
form_data = [
    ("Username", "jdoe", True),
    ("Email", "jdoe@example.com", True),
    ("Phone", "", False)
]
print(build_form("User Registration", form_data, ["Submit", "Cancel"]))
```

### 3.2 Data Table Construction

```python
# Build ASCII table with headers and data
def build_table(headers, rows, col_widths=None):
    """Construct formatted data table"""
    # Auto-calculate widths if not provided
    if col_widths is None:
        col_widths = []
        for i in range(len(headers)):
            max_width = len(headers[i])
            for row in rows:
                max_width = max(max_width, len(str(row[i])))
            col_widths.append(max_width + 2)
    
    # Build separator
    separator = '─┼─'.join('─' * w for w in col_widths)
    top_border = '┌─' + separator.replace('┼', '┬') + '─┐'
    mid_border = '├─' + separator + '─┤'
    bottom_border = '└─' + separator.replace('┼', '┴') + '─┘'
    
    # Build header row
    header_cells = []
    for header, width in zip(headers, col_widths):
        header_cells.append(header.center(width))
    header_row = '│ ' + ' │ '.join(header_cells) + ' │'
    
    # Build data rows
    data_rows = []
    for row in rows:
        cells = []
        for cell, width in zip(row, col_widths):
            cells.append(str(cell).ljust(width))
        data_rows.append('│ ' + ' │ '.join(cells) + ' │')
    
    # Assemble table
    table = [top_border, header_row, mid_border]
    table.extend(data_rows)
    table.append(bottom_border)
    
    return '\n'.join(table)

# Example
headers = ["ID", "Name", "Status"]
data = [
    ["001", "Alice", "Active"],
    ["002", "Bob", "Inactive"],
    ["003", "Charlie", "Active"]
]
print(build_table(headers, data))
```

### 3.3 Navigation Menu Assembly

```python
# Multi-level navigation menu
def build_navigation(menu_structure, current_path=''):
    """Build hierarchical navigation menu"""
    lines = []
    
    def render_level(items, level=0):
        for item in items:
            if isinstance(item, dict):
                label = item['label']
                path = item.get('path', '')
                children = item.get('children', [])
                
                # Mark current
                is_current = (path == current_path)
                marker = '▶' if is_current else ' '
                
                # Indent based on level
                indent = '  ' * level
                lines.append(f"{indent}{marker} {label}")
                
                # Render children
                if children:
                    render_level(children, level + 1)
    
    render_level(menu_structure)
    return '\n'.join(lines)

# Example
nav_menu = [
    {'label': 'Dashboard', 'path': '/dashboard'},
    {'label': 'Users', 'path': '/users', 'children': [
        {'label': 'All Users', 'path': '/users/all'},
        {'label': 'Add User', 'path': '/users/add'}
    ]},
    {'label': 'Settings', 'path': '/settings'}
]
print(build_navigation(nav_menu, current_path='/users/all'))
```

### 3.4 Card Component

```python
# Information card with title, content, footer
def build_card(title, content_lines, footer='', width=50):
    """Construct card-style component"""
    # Card borders
    top = f"┌{'─' * (width - 2)}┐"
    bottom = f"└{'─' * (width - 2)}┘"
    separator = f"├{'─' * (width - 2)}┤"
    
    # Title
    title_line = f"│ {title.ljust(width - 4)} │"
    
    # Content
    content = []
    for line in content_lines:
        # Wrap if necessary
        if len(line) > width - 4:
            wrapped = [line[i:i+(width-4)] for i in range(0, len(line), width-4)]
            for wrap_line in wrapped:
                content.append(f"│ {wrap_line.ljust(width - 4)} │")
        else:
            content.append(f"│ {line.ljust(width - 4)} │")
    
    # Footer
    footer_section = []
    if footer:
        footer_section = [separator, f"│ {footer.ljust(width - 4)} │"]
    
    # Assemble
    card_parts = [top, title_line, separator] + content + footer_section + [bottom]
    return '\n'.join(card_parts)

# Example
print(build_card(
    "User Profile",
    ["Name: John Doe", "Email: john@example.com", "Status: Active"],
    "Last login: 2024-12-06"
))
```

### 3.5 Progress Indicator

```python
# Progress bar
def progress_bar(current, total, width=30, fill='█', empty='░'):
    """Create text-based progress bar"""
    percentage = current / total if total > 0 else 0
    filled = int(width * percentage)
    bar = fill * filled + empty * (width - filled)
    percent_text = f"{percentage * 100:.1f}%"
    return f"[{bar}] {percent_text}"

# Multi-step progress
def step_progress(steps, current_step):
    """Display multi-step progress"""
    step_displays = []
    for i, step_name in enumerate(steps, 1):
        if i < current_step:
            marker = '✓'
        elif i == current_step:
            marker = '●'
        else:
            marker = '○'
        step_displays.append(f"{marker} {step_name}")
    
    return '\n'.join(step_displays)

# Examples
print(progress_bar(75, 100))
# → "[██████████████████████░░░░░░░] 75.0%"

steps = ["Login", "Enter Details", "Confirm", "Complete"]
print(step_progress(steps, 2))
# → "✓ Login"
# → "● Enter Details"
# → "○ Confirm"
# → "○ Complete"
```

---

## LEVEL 4: TEMPLATE-LEVEL PATTERNS
### Constructing Full Screen Layouts and Containers

### 4.1 Dashboard Layout

```python
# Complete dashboard template
def build_dashboard(title, stats, recent_items, quick_actions):
    """Construct dashboard layout"""
    width = 80
    
    # Header
    header = f"""
╔{'═' * (width - 2)}╗
║{title.center(width - 2)}║
╠{'═' * (width - 2)}╣
"""
    
    # Stats section (3 columns)
    stat_width = (width - 6) // 3
    stat_boxes = []
    for label, value in stats:
        box = f"{value}\n{label}".center(stat_width)
        stat_boxes.append(box)
    
    stats_lines = []
    box_lines = [box.split('\n') for box in stat_boxes]
    for i in range(len(box_lines[0])):
        line = ' │ '.join(box[i] for box in box_lines)
        stats_lines.append(f"║ {line} ║")
    
    # Recent items section
    recent_section = [f"╠{'═' * (width - 2)}╣", "║ Recent Activity:".ljust(width - 1) + "║"]
    for item in recent_items[:5]:  # Limit to 5
        recent_section.append(f"║   • {item}".ljust(width - 1) + "║")
    
    # Quick actions
    actions_section = [f"╠{'═' * (width - 2)}╣", "║ Quick Actions:".ljust(width - 1) + "║"]
    action_buttons = '   '.join(f"[{action}]" for action in quick_actions)
    actions_section.append(f"║ {action_buttons}".ljust(width - 1) + "║")
    
    # Footer
    footer = f"╚{'═' * (width - 2)}╝"
    
    # Assemble all sections
    dashboard = (header + '\n'.join(stats_lines) + '\n' + 
                 '\n'.join(recent_section) + '\n' + 
                 '\n'.join(actions_section) + '\n' + footer)
    
    return dashboard

# Example
stats = [("Total Users", "1,234"), ("Active", "987"), ("New Today", "45")]
recent = ["User john_doe logged in", "New registration: alice", "File uploaded: report.pdf"]
actions = ["New User", "Export Data", "Settings"]
print(build_dashboard("Admin Dashboard", stats, recent, actions))
```

### 4.2 Settings Page Layout

```python
# Settings page with sections
def build_settings_page(sections_dict):
    """Construct multi-section settings page"""
    lines = []
    width = 60
    
    # Page title
    lines.append("╔" + "═" * (width - 2) + "╗")
    lines.append("║" + "SETTINGS".center(width - 2) + "║")
    lines.append("╠" + "═" * (width - 2) + "╣")
    
    # Each section
    for section_title, settings in sections_dict.items():
        # Section header
        lines.append("║")
        lines.append("║ " + section_title)
        lines.append("║ " + "─" * (width - 4))
        
        # Settings in section
        for setting_name, setting_value in settings.items():
            line = f"║   {setting_name}: {setting_value}"
            lines.append(line.ljust(width - 1) + "║")
    
    # Footer
    lines.append("║")
    lines.append("╠" + "═" * (width - 2) + "╣")
    lines.append("║ " + "[Save]  [Cancel]  [Reset]".center(width - 2) + "║")
    lines.append("╚" + "═" * (width - 2) + "╝")
    
    return '\n'.join(lines)

# Example
settings_data = {
    "Appearance": {
        "Theme": "Dark",
        "Font Size": "12pt",
        "Show Icons": "Yes"
    },
    "Notifications": {
        "Email": "Enabled",
        "Desktop": "Enabled",
        "Sound": "Disabled"
    }
}
print(build_settings_page(settings_data))
```

### 4.3 Dialog Box Templates

```python
# Confirmation dialog
def confirmation_dialog(title, message, buttons=None):
    """Create confirmation dialog"""
    if buttons is None:
        buttons = ["Yes", "No"]
    
    width = max(40, len(message) + 10, len(title) + 10)
    
    lines = []
    lines.append("┌" + "─" * (width - 2) + "┐")
    lines.append("│ " + title.ljust(width - 4) + " │")
    lines.append("├" + "─" * (width - 2) + "┤")
    lines.append("│")
    lines.append("│ " + message.center(width - 4) + " │")
    lines.append("│")
    lines.append("├" + "─" * (width - 2) + "┤")
    
    button_text = "  ".join(f"[{btn}]" for btn in buttons)
    lines.append("│ " + button_text.center(width - 4) + " │")
    lines.append("└" + "─" * (width - 2) + "┘")
    
    return '\n'.join(lines)

# Input dialog
def input_dialog(title, prompt, default_value=''):
    """Create input dialog"""
    width = 50
    
    lines = []
    lines.append("┌" + "─" * (width - 2) + "┐")
    lines.append("│ " + title.center(width - 4) + " │")
    lines.append("├" + "─" * (width - 2) + "┤")
    lines.append("│")
    lines.append("│ " + prompt.ljust(width - 4) + " │")
    lines.append("│ " + f"[{default_value}]".center(width - 4) + " │")
    lines.append("│")
    lines.append("├" + "─" * (width - 2) + "┤")
    lines.append("│ " + "[OK]  [Cancel]".center(width - 4) + " │")
    lines.append("└" + "─" * (width - 2) + "┘")
    
    return '\n'.join(lines)

# Examples
print(confirmation_dialog("Delete File", "Are you sure you want to delete this file?"))
print(input_dialog("Rename", "Enter new name:", "document.txt"))
```

---

## LEVEL 5: APP-LEVEL INTEGRATION
### Full Application Assembly with State and Navigation

### 5.1 Application Shell

```python
# Complete application framework
class AppShell:
    """Application shell with navigation and content areas"""
    
    def __init__(self, app_name):
        self.app_name = app_name
        self.current_page = 'home'
        self.user_name = 'Guest'
        self.notifications = []
    
    def render(self, content):
        """Render full application shell"""
        width = 100
        
        # Top bar
        top_bar = self._render_top_bar(width)
        
        # Navigation
        nav = self._render_navigation()
        
        # Content area
        content_lines = content.split('\n')
        content_area = self._render_content_area(content_lines, width)
        
        # Status bar
        status_bar = self._render_status_bar(width)
        
        # Combine all parts
        return f"{top_bar}\n{nav}\n{content_area}\n{status_bar}"
    
    def _render_top_bar(self, width):
        """Render application top bar"""
        left = f"  {self.app_name}"
        right = f"{self.user_name}  "
        
        if self.notifications:
            notif_count = f"🔔 {len(self.notifications)}"
            right = f"{notif_count}  │  {right}"
        
        middle_space = width - len(left) - len(right)
        return f"{'═' * width}\n{left}{' ' * middle_space}{right}\n{'═' * width}"
    
    def _render_navigation(self):
        """Render navigation menu"""
        pages = ['home', 'users', 'reports', 'settings']
        nav_items = []
        
        for page in pages:
            if page == self.current_page:
                nav_items.append(f"[{page.upper()}]")
            else:
                nav_items.append(f" {page.title()} ")
        
        return "  ".join(nav_items) + "\n" + "─" * 100
    
    def _render_content_area(self, content_lines, width):
        """Render main content area"""
        padded_lines = [f"│ {line.ljust(width - 4)} │" for line in content_lines]
        return '\n'.join(padded_lines)
    
    def _render_status_bar(self, width):
        """Render bottom status bar"""
        left_status = f"  Page: {self.current_page.title()}"
        right_status = f"Ready  "
        middle = width - len(left_status) - len(right_status)
        
        return f"{'─' * width}\n{left_status}{' ' * middle}{right_status}"

# Example usage
app = AppShell("My Application")
app.current_page = 'users'
app.user_name = 'John Doe'
app.notifications = ['New message', 'Update available']

content = """
User Management

Total Users: 150
Active Users: 120
Inactive Users: 30

[Add New User]  [Export List]  [Search]
"""

print(app.render(content.strip()))
```

### 5.2 Dynamic Content Generation

```python
# Generate dynamic UI based on data
def generate_user_list_ui(users_data):
    """Generate complete user list interface"""
    
    # Header
    header = build_header("User Directory", 80)
    
    # Search bar
    search = """
┌──────────────────────────────────────────────────────────────────────────────┐
│ 🔍 [Search users...]                                          [Filter ▼]      │
└──────────────────────────────────────────────────────────────────────────────┘
"""
    
    # User cards
    user_cards = []
    for user in users_data:
        card = f"""
  ┌────────────────────────────────────────┐
  │ {user['name']:<38} │
  │ ───────────────────────────────────── │
  │ Email: {user['email']:<28} │
  │ Role:  {user['role']:<28} │
  │ Status: {user['status']:<27} │
  │                                        │
  │ [View Profile]  [Edit]  [Delete]       │
  └────────────────────────────────────────┘
"""
        user_cards.append(card.strip())
    
    # Footer with pagination
    total = len(users_data)
    footer = f"""
{'─' * 80}
Showing {total} users                                      [< Prev]  [Next >]
"""
    
    return header + search + '\n' + '\n\n'.join(user_cards) + footer

def build_header(title, width):
    """Build consistent header"""
    return f"""
╔{'═' * (width - 2)}╗
║{title.center(width - 2)}║
╚{'═' * (width - 2)}╝
"""

# Example
users = [
    {"name": "Alice Johnson", "email": "alice@example.com", "role": "Admin", "status": "Active"},
    {"name": "Bob Smith", "email": "bob@example.com", "role": "User", "status": "Active"},
]
print(generate_user_list_ui(users))
```

### 5.3 State-Driven UI Updates

```python
# UI that changes based on application state
class StatefulUI:
    """UI component that updates based on state"""
    
    def __init__(self):
        self.state = {
            'loading': False,
            'error': None,
            'data': None,
            'user_logged_in': False
        }
    
    def render(self):
        """Render UI based on current state"""
        if self.state['loading']:
            return self._render_loading()
        
        if self.state['error']:
            return self._render_error(self.state['error'])
        
        if not self.state['user_logged_in']:
            return self._render_login()
        
        if self.state['data']:
            return self._render_content(self.state['data'])
        
        return self._render_empty()
    
    def _render_loading(self):
        return """
    ┌──────────────────────┐
    │                      │
    │   Loading...  ⟳     │
    │                      │
    └──────────────────────┘
"""
    
    def _render_error(self, error_msg):
        return f"""
    ┌──────────────────────────────┐
    │  ⚠ Error                    │
    │  ─────────────────────────  │
    │  {error_msg:<26} │
    │                              │
    │  [Retry]  [Cancel]           │
    └──────────────────────────────┘
"""
    
    def _render_login(self):
        return """
    ┌──────────────────────────────┐
    │  Please Login                │
    │  ─────────────────────────  │
    │                              │
    │  Username: [____________]    │
    │  Password: [____________]    │
    │                              │
    │  [Login]                     │
    └──────────────────────────────┘
"""
    
    def _render_content(self, data):
        return f"""
    ┌──────────────────────────────┐
    │  Dashboard                   │
    │  ─────────────────────────  │
    │                              │
    │  Welcome back!               │
    │  Data: {str(data):<19} │
    │                              │
    └──────────────────────────────┘
"""
    
    def _render_empty(self):
        return """
    ┌──────────────────────────────┐
    │  No data available           │
    │                              │
    │  [Load Data]                 │
    └──────────────────────────────┘
"""

# Example usage
ui = StatefulUI()
print("Loading state:")
ui.state['loading'] = True
print(ui.render())

print("\nError state:")
ui.state['loading'] = False
ui.state['error'] = "Connection timeout"
print(ui.render())

print("\nLogin required:")
ui.state['error'] = None
print(ui.render())

print("\nLogged in with data:")
ui.state['user_logged_in'] = True
ui.state['data'] = "12,345 records"
print(ui.render())
```

---

## DEARPYGUI SPECIFIC PATTERNS
### String Operations for DearPyGUI UI Construction

### DPG ID Management

```python
# Generate unique DPG tags
def dpg_tag(component_type, identifier, parent=''):
    """Generate DearPyGUI tag string"""
    parts = [component_type, identifier]
    if parent:
        parts.insert(0, parent)
    return '_'.join(parts).lower().replace(' ', '_')

# Create hierarchical tags
def dpg_child_tag(parent_tag, child_type, child_name):
    """Create child component tag"""
    return f"{parent_tag}_{child_type}_{child_name}"

# Examples
window_tag = dpg_tag('window', 'Main Settings')
# → "window_main_settings"

button_tag = dpg_child_tag(window_tag, 'button', 'Save')
# → "window_main_settings_button_save"
```

### DPG Label Formatting

```python
# Format labels for DPG widgets
def dpg_label(text, show_colon=True, width=None):
    """Format label for DPG input widgets"""
    label = f"{text}:" if show_colon else text
    if width:
        return label.ljust(width)
    return label

# Format with value display
def dpg_value_label(label, value, units=''):
    """Create label showing current value"""
    value_str = f"{value} {units}".strip()
    return f"{label}: {value_str}"

# Create tooltip text
def dpg_tooltip(description, hotkey=''):
    """Format tooltip text"""
    if hotkey:
        return f"{description}\n\nShortcut: {hotkey}"
    return description

# Examples
print(dpg_label("Username", width=15))
# → "Username:      "

print(dpg_value_label("Volume", 75, "%"))
# → "Volume: 75 %"

print(dpg_tooltip("Save current file", "Ctrl+S"))
# → "Save current file\n\nShortcut: Ctrl+S"
```

### DPG Menu Construction

```python
# Build menu structure for DPG
def dpg_menu_structure(menu_dict):
    """Convert dict to DPG menu string representation"""
    lines = []
    
    def process_item(label, value, level=0):
        indent = '  ' * level
        
        if isinstance(value, dict):
            # Submenu
            lines.append(f"{indent}{label} ▶")
            for sub_label, sub_value in value.items():
                process_item(sub_label, sub_value, level + 1)
        elif isinstance(value, tuple):
            # Menu item with callback and shortcut
            callback, shortcut = value
            shortcut_str = f"  ({shortcut})" if shortcut else ""
            lines.append(f"{indent}{label}{shortcut_str}")
        else:
            # Simple menu item
            lines.append(f"{indent}{label}")
    
    for key, val in menu_dict.items():
        process_item(key, val)
    
    return '\n'.join(lines)

# Example
menu = {
    "File": {
        "New": ("new_file_callback", "Ctrl+N"),
        "Open": ("open_file_callback", "Ctrl+O"),
        "Recent": {
            "file1.txt": ("open_recent", ""),
            "file2.txt": ("open_recent", "")
        },
        "Save": ("save_file", "Ctrl+S")
    },
    "Edit": {
        "Cut": ("cut", "Ctrl+X"),
        "Copy": ("copy", "Ctrl+C"),
        "Paste": ("paste", "Ctrl+V")
    }
}

print(dpg_menu_structure(menu))
```

### DPG Table Data Formatting

```python
# Format data for DPG tables
def dpg_table_rows(data_list, columns):
    """Format data rows for DPG table"""
    formatted_rows = []
    
    for row_data in data_list:
        row_values = []
        for col in columns:
            value = row_data.get(col, '')
            row_values.append(str(value))
        formatted_rows.append(row_values)
    
    return formatted_rows

# Create table header labels
def dpg_table_headers(column_names, column_widths=None):
    """Format table headers"""
    if column_widths:
        return [name.ljust(width) for name, width in zip(column_names, column_widths)]
    return column_names

# Example
data = [
    {"id": 1, "name": "Alice", "score": 95},
    {"id": 2, "name": "Bob", "score": 87},
    {"id": 3, "name": "Charlie", "score": 92}
]

columns = ["id", "name", "score"]
rows = dpg_table_rows(data, columns)
headers = dpg_table_headers(["ID", "Name", "Score"], [5, 15, 8])

print("Headers:", headers)
print("Rows:", rows)
```

### DPG Form Builder

```python
# Build form field configuration for DPG
def dpg_form_config(form_fields):
    """Generate form configuration for DPG"""
    config = []
    
    for field in form_fields:
        field_config = {
            'tag': dpg_tag('input', field['name']),
            'label': dpg_label(field['label']),
            'default': field.get('default', ''),
            'hint': field.get('hint', ''),
            'required': field.get('required', False)
        }
        
        if field_config['required']:
            field_config['label'] += ' *'
        
        config.append(field_config)
    
    return config

# Example
fields = [
    {'name': 'username', 'label': 'Username', 'required': True, 'hint': 'alphanumeric only'},
    {'name': 'email', 'label': 'Email Address', 'required': True},
    {'name': 'phone', 'label': 'Phone Number', 'default': '', 'hint': 'optional'}
]

form_config = dpg_form_config(fields)
for field in form_config:
    print(f"Tag: {field['tag']}")
    print(f"Label: {field['label']}")
    print(f"Hint: {field['hint']}")
    print()
```

---

## STRING MUTATION PATTERNS FOR UI UPDATES

### Dynamic Text Transformation

```python
# Transform UI text based on state
def transform_button_text(base_text, state):
    """Transform button text based on state"""
    state_prefixes = {
        'loading': '⟳ ',
        'success': '✓ ',
        'error': '✗ ',
        'disabled': '◯ '
    }
    
    prefix = state_prefixes.get(state, '')
    
    if state == 'disabled':
        return f"({prefix}{base_text})"
    
    return f"{prefix}{base_text}"

# Examples
print(transform_button_text("Submit", "loading"))   # → "⟳ Submit"
print(transform_button_text("Submit", "success"))   # → "✓ Submit"
print(transform_button_text("Submit", "disabled"))  # → "(◯ Submit)"
```

### String Interpolation for Data Binding

```python
# Template with data binding
class UITemplate:
    """UI template with variable interpolation"""
    
    def __init__(self, template):
        self.template = template
    
    def render(self, **kwargs):
        """Render template with data"""
        result = self.template
        
        # Replace all {{variable}} with values
        for key, value in kwargs.items():
            placeholder = f"{{{{{key}}}}}"
            result = result.replace(placeholder, str(value))
        
        return result

# Example
card_template = UITemplate("""
┌─────────────────────────────┐
│ {{title}}                   
│ ───────────────────────────
│ Name: {{name}}              
│ Email: {{email}}            
│ Status: {{status}}          
└─────────────────────────────┘
""")

print(card_template.render(
    title="User Profile",
    name="John Doe",
    email="john@example.com",
    status="Active"
))
```

### Component Composition

```python
# Compose UI components using string building
def compose_components(*components, separator='\n'):
    """Combine multiple UI components"""
    return separator.join(str(c) for c in components)

# Wrap component with container
def wrap_in_container(component, title='', width=50):
    """Wrap component in bordered container"""
    border_top = f"┌{'─' * (width - 2)}┐"
    border_bottom = f"└{'─' * (width - 2)}┘"
    
    lines = [border_top]
    
    if title:
        lines.append(f"│ {title.ljust(width - 4)} │")
        lines.append(f"├{'─' * (width - 2)}┤")
    
    for line in component.split('\n'):
        lines.append(f"│ {line.ljust(width - 4)} │")
    
    lines.append(border_bottom)
    
    return '\n'.join(lines)

# Example
button1 = "[Save]"
button2 = "[Cancel]"
button_group = compose_components(button1, button2, separator='  ')

print(wrap_in_container(button_group, "Actions", 30))
```

---

## PRACTICAL UI CONSTRUCTION WORKFLOW

### Complete Example: Building a Login Screen

```python
def build_login_screen(app_name, error_message=''):
    """Complete login screen with all levels"""
    
    # ATOMIC: Individual elements
    title = app_name.center(40)
    username_label = "Username:".ljust(15)
    password_label = "Password:".ljust(15)
    username_input = "[" + "".ljust(20) + "]"
    password_input = "[" + "".ljust(20) + "]"
    
    # MOLECULAR: Combined elements
    username_field = f"{username_label} {username_input}"
    password_field = f"{password_label} {password_input}"
    
    error_display = ''
    if error_message:
        error_display = f"\n⚠ {error_message}\n"
    
    # ORGANISM: Form assembly
    form = f"""
{username_field}
{password_field}
{error_display}
[Login]  [Register]  [Forgot Password?]
"""
    
    # TEMPLATE: Full screen layout
    width = 50
    screen = f"""
╔{'═' * (width - 2)}╗
║{title}║
╠{'═' * (width - 2)}╣
║{'':^{width-2}}║
{chr(10).join('║ ' + line.ljust(width-4) + ' ║' for line in form.split(chr(10)) if line)}
║{'':^{width-2}}║
╚{'═' * (width - 2)}╝

Version 1.0.0                              [Help]
"""
    
    return screen

# Usage
print(build_login_screen("My Application"))
print("\n" + "="*50 + "\n")
print(build_login_screen("My Application", "Invalid username or password"))
```

### Example: Building a Data Dashboard

```python
def build_data_dashboard(metrics, chart_data, alerts):
    """Complete data dashboard assembly"""
    
    # ATOMIC: Metric cards
    metric_cards = []
    for label, value, change in metrics:
        change_indicator = f"↑ {change}" if change >= 0 else f"↓ {abs(change)}"
        card = f"""
  ╭─────────────────╮
  │ {label:<15} │
  │ {str(value):<15} │
  │ {change_indicator:<15} │
  ╰─────────────────╯"""
        metric_cards.append(card)
    
    # MOLECULAR: Metrics row
    metrics_row = '\n\n'.join(metric_cards)
    
    # ORGANISM: Chart visualization
    chart = build_chart(chart_data)
    
    # ORGANISM: Alerts panel
    alerts_panel = build_alerts_panel(alerts)
    
    # TEMPLATE: Dashboard layout
    dashboard = f"""
╔════════════════════════════════════════════════════════════════╗
║                      DATA DASHBOARD                            ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  METRICS                                                       ║
{chr(10).join('║  ' + line.ljust(60) + '║' for line in metrics_row.split(chr(10)))}
║                                                                ║
╠────────────────────────────────────────────────────────────────╣
║  TREND CHART                                                   ║
{chr(10).join('║  ' + line.ljust(60) + '║' for line in chart.split(chr(10)))}
║                                                                ║
╠────────────────────────────────────────────────────────────────╣
║  ALERTS                                                        ║
{chr(10).join('║  ' + line.ljust(60) + '║' for line in alerts_panel.split(chr(10)))}
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""
    return dashboard

def build_chart(data_points):
    """Simple ASCII chart"""
    max_val = max(data_points)
    height = 10
    chart_lines = []
    
    for row in range(height, 0, -1):
        threshold = (max_val / height) * row
        line = ''
        for val in data_points:
            line += '█' if val >= threshold else ' '
        chart_lines.append(line)
    
    return '\n'.join(chart_lines)

def build_alerts_panel(alerts):
    """Build alerts list"""
    if not alerts:
        return "No active alerts"
    
    lines = []
    for severity, message in alerts[:3]:  # Show top 3
        icon = '🔴' if severity == 'high' else '🟡' if severity == 'medium' else '🟢'
        lines.append(f"{icon} {message}")
    
    return '\n'.join(lines)

# Example usage
metrics = [
    ("Total Sales", "$45,230", 12),
    ("Active Users", "1,234", -5),
    ("Conversion", "3.2%", 0.5)
]

chart = [3, 5, 4, 7, 6, 8, 9, 7, 10, 9]

alerts = [
    ("high", "Server CPU at 95%"),
    ("medium", "Low disk space"),
    ("low", "Update available")
]

print(build_data_dashboard(metrics, chart, alerts))
```

---

## BEST PRACTICES FOR UI STRING CONSTRUCTION

### 1. Maintain Consistent Widths
```python
# Define standard widths
LABEL_WIDTH = 20
INPUT_WIDTH = 30
BUTTON_WIDTH = 12
SCREEN_WIDTH = 80

# Use consistently
def format_field(label, value):
    return f"{label.ljust(LABEL_WIDTH)} {value.ljust(INPUT_WIDTH)}"
```

### 2. Use String Constants for Repeated Elements
```python
# Define once, use everywhere
HORIZONTAL_LINE = '─' * 80
DOUBLE_LINE = '═' * 80
BULLET = '•'
CHECKBOX_CHECKED = '[✓]'
CHECKBOX_UNCHECKED = '[ ]'
```

### 3. Create Reusable Template Functions
```python
# Template function library
def bordered_box(content, width=50):
    """Reusable bordered box"""
    top = f"┌{'─' * (width - 2)}┐"
    bottom = f"└{'─' * (width - 2)}┘"
    lines = [top]
    for line in content.split('\n'):
        lines.append(f"│ {line.ljust(width - 4)} │")
    lines.append(bottom)
    return '\n'.join(lines)
```

### 4. Separate Data from Presentation
```python
# Good: Data separate from formatting
user_data = {"name": "John", "email": "john@example.com"}

def format_user_card(data):
    return f"""
Name:  {data['name']}
Email: {data['email']}
"""

# Use
print(format_user_card(user_data))
```

### 5. Use String Builder Pattern for Complex UIs
```python
class UIBuilder:
    """Build complex UIs step by step"""
    
    def __init__(self):
        self.parts = []
    
    def add_header(self, text):
        self.parts.append(f"\n{'═' * 50}")
        self.parts.append(text.center(50))
        self.parts.append('═' * 50)
        return self
    
    def add_section(self, title, content):
        self.parts.append(f"\n{title}")
        self.parts.append('─' * 50)
        self.parts.append(content)
        return self
    
    def add_footer(self, text):
        self.parts.append(f"\n{text.center(50)}")
        return self
    
    def build(self):
        return '\n'.join(self.parts)

# Usage
ui = (UIBuilder()
      .add_header("Application")
      .add_section("Section 1", "Content here")
      .add_section("Section 2", "More content")
      .add_footer("© 2024")
      .build())

print(ui)
```
