# Domain: String

## Overview
Strings in Python are sequences of characters used to store and manipulate text. They are immutable (cannot be changed after creation) and can be enclosed in single quotes (''), double quotes (""), or triple quotes (''' or """) for multi-line strings.

---

## Methods List

### capitalize()
**What it does**: Converts the first character to uppercase and all others to lowercase.

**Requirements**:
- No parameters needed
- Works on any string

**Data Types**:
- Input: string (the string object itself)
- Output: string (new string with first char uppercase)

**Use Case Examples**:
```python
# Example 1: Basic usage
text = "hello world"
result = text.capitalize()
print(result)  # "Hello world"

# Example 2: Already capitalized
text = "HELLO WORLD"
result = text.capitalize()
print(result)  # "Hello world"

# Example 3: Starting with number
text = "123 hello"
result = text.capitalize()
print(result)  # "123 hello" (numbers don't change)

# When to use: Formatting names, titles, or sentences
name = "john doe"
formatted = name.capitalize()
print(formatted)  # "John doe"
```

---

### casefold()
**What it does**: Converts string to lowercase, more aggressive than lower(). Used for caseless matching.

**Requirements**:
- No parameters needed
- Better for comparisons across languages

**Data Types**:
- Input: string
- Output: string (all lowercase, even special characters)

**Use Case Examples**:
```python
# Example 1: Basic usage
text = "HELLO World"
result = text.casefold()
print(result)  # "hello world"

# Example 2: German sharp s
text = "Straße"  # German word for "street"
print(text.lower())     # "straße"
print(text.casefold())  # "strasse" (converts ß to ss)

# Example 3: Case-insensitive comparison
user_input = "PYTHON"
if user_input.casefold() == "python":
    print("Match!")  # This will print

# When to use: Comparing user input, internationalization
```

---

### center(width, fillchar=' ')
**What it does**: Centers the string within a given width, padding with specified character.

**Requirements**:
- `width` (required): Total width of resulting string
- `fillchar` (optional): Character to pad with (default is space)

**Data Types**:
- Input: `width` (integer), `fillchar` (single character string)
- Output: string (centered with padding)

**Use Case Examples**:
```python
# Example 1: Basic centering with spaces
text = "Python"
result = text.center(20)
print(result)  # "       Python       "
print(len(result))  # 20

# Example 2: Custom fill character
text = "TITLE"
result = text.center(20, '*')
print(result)  # "*******TITLE********"

# Example 3: Smaller width than text (no change)
text = "Hello World"
result = text.center(5)
print(result)  # "Hello World" (unchanged)

# When to use: Creating headers, formatting reports, ASCII art
header = "REPORT".center(50, '=')
print(header)  # "======================REPORT======================"
```

---

### count(substring, start=0, end=len)
**What it does**: Returns how many times a substring appears in the string.

**Requirements**:
- `substring` (required): What to count
- `start` (optional): Where to start searching (index)
- `end` (optional): Where to stop searching (index)

**Data Types**:
- Input: `substring` (string), `start` (int), `end` (int)
- Output: integer (count of occurrences)

**Use Case Examples**:
```python
# Example 1: Count all occurrences
text = "hello hello world hello"
count = text.count("hello")
print(count)  # 3

# Example 2: Count with start position
text = "hello hello world hello"
count = text.count("hello", 10)  # Start from index 10
print(count)  # 1 (only last "hello")

# Example 3: Count in a range
text = "aaabbbaaabbb"
count = text.count("a", 0, 6)  # First 6 characters
print(count)  # 3

# When to use: Analyzing text, validating passwords, data analysis
password = "MyP@ssw0rd"
special_count = password.count("@") + password.count("#")
print(f"Special characters: {special_count}")
```

---

### encode(encoding='utf-8', errors='strict')
**What it does**: Converts string to bytes using specified encoding.

**Requirements**:
- `encoding` (optional): Encoding scheme (default: 'utf-8')
- `errors` (optional): How to handle errors ('strict', 'ignore', 'replace')

**Data Types**:
- Input: `encoding` (string), `errors` (string)
- Output: bytes object

**Use Case Examples**:
```python
# Example 1: Basic UTF-8 encoding
text = "Hello"
encoded = text.encode()
print(encoded)  # b'Hello'
print(type(encoded))  # <class 'bytes'>

# Example 2: Different encoding
text = "Café"
encoded_utf8 = text.encode('utf-8')
encoded_ascii = text.encode('ascii', errors='ignore')
print(encoded_utf8)   # b'Caf\xc3\xa9'
print(encoded_ascii)  # b'Caf' (é removed)

# Example 3: Error handling
text = "Hello 世界"
safe = text.encode('ascii', errors='replace')
print(safe)  # b'Hello ??'

# When to use: Saving files, network transmission, API calls
```

---

### endswith(suffix, start=0, end=len)
**What it does**: Checks if string ends with specified suffix.

**Requirements**:
- `suffix` (required): String or tuple of strings to check
- `start` (optional): Start position for checking
- `end` (optional): End position for checking

**Data Types**:
- Input: `suffix` (string or tuple), `start` (int), `end` (int)
- Output: boolean (True/False)

**Use Case Examples**:
```python
# Example 1: Simple check
filename = "document.pdf"
if filename.endswith('.pdf'):
    print("PDF file")  # This prints

# Example 2: Multiple suffixes
filename = "image.jpg"
if filename.endswith(('.jpg', '.jpeg', '.png')):
    print("Image file")  # This prints

# Example 3: Check within range
text = "hello world"
result = text.endswith("world", 0, 11)
print(result)  # True

# When to use: File validation, URL checking, data filtering
def is_valid_image(filename):
    return filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))

print(is_valid_image("photo.png"))  # True
```

---

### expandtabs(tabsize=8)
**What it does**: Replaces tab characters (\t) with spaces.

**Requirements**:
- `tabsize` (optional): Number of spaces per tab (default: 8)

**Data Types**:
- Input: `tabsize` (integer)
- Output: string (with tabs expanded to spaces)

**Use Case Examples**:
```python
# Example 1: Default tab size
text = "Name\tAge\tCity"
result = text.expandtabs()
print(result)  # "Name    Age     City"

# Example 2: Custom tab size
text = "Col1\tCol2\tCol3"
result = text.expandtabs(4)
print(result)  # "Col1    Col2    Col3"

# Example 3: Formatting table data
data = "Python\t3.9\t2020\nJava\t17\t2021"
formatted = data.expandtabs(15)
print(formatted)
# Python         3.9            2020
# Java           17             2021

# When to use: Formatting output, cleaning data, text alignment
```

---

### find(substring, start=0, end=len)
**What it does**: Returns the lowest index where substring is found. Returns -1 if not found.

**Requirements**:
- `substring` (required): What to search for
- `start` (optional): Start position
- `end` (optional): End position

**Data Types**:
- Input: `substring` (string), `start` (int), `end` (int)
- Output: integer (index or -1)

**Use Case Examples**:
```python
# Example 1: Basic search
text = "Hello World"
index = text.find("World")
print(index)  # 6

# Example 2: Not found
text = "Hello World"
index = text.find("Python")
print(index)  # -1

# Example 3: Find with range
text = "hello hello hello"
first = text.find("hello")
second = text.find("hello", first + 1)
print(f"First: {first}, Second: {second}")  # First: 0, Second: 6

# When to use: Parsing text, extracting data, validating format
email = "user@example.com"
at_position = email.find("@")
if at_position > 0:
    username = email[:at_position]
    print(f"Username: {username}")  # Username: user
```

---

### format(*args, **kwargs)
**What it does**: Formats string by replacing placeholders with values.

**Requirements**:
- Placeholders: `{}`, `{0}`, `{name}`, etc.
- Arguments: Positional (*args) or keyword (**kwargs)

**Data Types**:
- Input: any data types as arguments
- Output: formatted string

**Use Case Examples**:
```python
# Example 1: Basic positional
template = "Hello, {}!"
result = template.format("Alice")
print(result)  # "Hello, Alice!"

# Example 2: Multiple with indexes
template = "{0} + {1} = {2}"
result = template.format(5, 3, 8)
print(result)  # "5 + 3 = 8"

# Example 3: Named placeholders
template = "Name: {name}, Age: {age}"
result = template.format(name="Bob", age=30)
print(result)  # "Name: Bob, Age: 30"

# Example 4: Number formatting
template = "Price: ${:.2f}"
result = template.format(19.99999)
print(result)  # "Price: $19.99"

# When to use: Building messages, reports, dynamic content
def generate_report(name, score, total):
    return "Student: {}, Score: {}/{} ({:.1f}%)".format(
        name, score, total, (score/total)*100
    )

print(generate_report("Alice", 45, 50))
# "Student: Alice, Score: 45/50 (90.0%)"
```

---

### format_map(mapping)
**What it does**: Similar to format() but takes a dictionary/mapping.

**Requirements**:
- `mapping` (required): Dictionary with values for placeholders

**Data Types**:
- Input: dictionary/mapping
- Output: formatted string

**Use Case Examples**:
```python
# Example 1: Basic usage
template = "{name} is {age} years old"
data = {'name': 'Alice', 'age': 25}
result = template.format_map(data)
print(result)  # "Alice is 25 years old"

# Example 2: From object attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Bob", 30)
template = "{name} is {age}"
result = template.format_map(vars(person))
print(result)  # "Bob is 30"

# When to use: Template processing, config-driven formatting
```

---

### index(substring, start=0, end=len)
**What it does**: Like find() but raises ValueError if not found.

**Requirements**:
- `substring` (required): What to search for
- `start` (optional): Start position
- `end` (optional): End position

**Data Types**:
- Input: `substring` (string), `start` (int), `end` (int)
- Output: integer (index) or raises ValueError

**Use Case Examples**:
```python
# Example 1: Found
text = "Hello World"
try:
    index = text.index("World")
    print(f"Found at: {index}")  # Found at: 6
except ValueError:
    print("Not found")

# Example 2: Not found (raises error)
text = "Hello World"
try:
    index = text.index("Python")
except ValueError:
    print("'Python' not found")  # This prints

# When to use: When substring MUST exist (error if not)
```

---

### isalnum()
**What it does**: Returns True if all characters are alphanumeric (letters/numbers).

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Valid alphanumeric
text = "Hello123"
print(text.isalnum())  # True

# Example 2: With spaces (False)
text = "Hello 123"
print(text.isalnum())  # False

# Example 3: Only numbers
text = "12345"
print(text.isalnum())  # True

# When to use: Username validation, password checking
def is_valid_username(username):
    return username.isalnum() and 3 <= len(username) <= 20

print(is_valid_username("User123"))  # True
print(is_valid_username("User 123"))  # False
```

---

### isalpha()
**What it does**: Returns True if all characters are letters (a-z, A-Z).

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Only letters
text = "Hello"
print(text.isalpha())  # True

# Example 2: With numbers
text = "Hello123"
print(text.isalpha())  # False

# When to use: Name validation
def is_valid_name(name):
    return name.isalpha() or ' ' in name

print(is_valid_name("John"))  # True
```

---

### isascii()
**What it does**: Returns True if all characters are ASCII (0-127).

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Pure ASCII
text = "Hello123!@#"
print(text.isascii())  # True

# Example 2: Non-ASCII
text = "Café"
print(text.isascii())  # False

# When to use: Checking if text can be safely encoded
```

---

### isdecimal()
**What it does**: Returns True if all characters are decimal digits (0-9).

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Decimal digits
text = "12345"
print(text.isdecimal())  # True

# Example 2: Not decimal
text = "12.345"
print(text.isdecimal())  # False (has period)

# When to use: Strict numeric validation
def is_integer_string(text):
    return text.isdecimal() or (text[0] == '-' and text[1:].isdecimal())
```

---

### isdigit()
**What it does**: Returns True if all characters are digits (includes superscripts).

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Regular digits
text = "12345"
print(text.isdigit())  # True

# Example 2: Superscript
text = "²"  # Superscript 2
print(text.isdigit())  # True
print(text.isdecimal())  # False

# When to use: Number validation with special formats
```

---

### isidentifier()
**What it does**: Returns True if string is a valid Python identifier.

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Valid identifier
text = "my_variable"
print(text.isidentifier())  # True

# Example 2: Invalid (starts with number)
text = "2variable"
print(text.isidentifier())  # False

# Example 3: Keyword check
import keyword
name = "class"
if name.isidentifier() and not keyword.iskeyword(name):
    print("Valid variable name")
else:
    print("Cannot use as variable")  # This prints

# When to use: Dynamic code generation, validation
```

---

### islower()
**What it does**: Returns True if all cased characters are lowercase.

**Requirements**: No parameters (ignores non-letter characters)

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: All lowercase
text = "hello"
print(text.islower())  # True

# Example 2: Mixed case
text = "Hello"
print(text.islower())  # False

# Example 3: With numbers
text = "hello123"
print(text.islower())  # True (numbers ignored)

# When to use: Case validation
```

---

### isnumeric()
**What it does**: Returns True if all characters are numeric (broadest check).

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Regular numbers
text = "12345"
print(text.isnumeric())  # True

# Example 2: Fractions
text = "½"
print(text.isnumeric())  # True

# When to use: Broad numeric validation
```

---

### isprintable()
**What it does**: Returns True if all characters are printable.

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Printable
text = "Hello World!"
print(text.isprintable())  # True

# Example 2: With newline
text = "Hello\nWorld"
print(text.isprintable())  # False

# When to use: Cleaning display text
```

---

### isspace()
**What it does**: Returns True if all characters are whitespace.

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Only spaces
text = "   "
print(text.isspace())  # True

# Example 2: Empty string
text = ""
print(text.isspace())  # False

# When to use: Input validation
def is_empty_or_whitespace(text):
    return not text or text.isspace()
```

---

### istitle()
**What it does**: Returns True if string is titlecased (each word starts with uppercase).

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Proper title case
text = "Hello World"
print(text.istitle())  # True

# Example 2: Not title case
text = "Hello world"
print(text.istitle())  # False

# When to use: Title validation
```

---

### isupper()
**What it does**: Returns True if all cased characters are uppercase.

**Requirements**: No parameters

**Data Types**:
- Output: boolean

**Use Case Examples**:
```python
# Example 1: All uppercase
text = "HELLO"
print(text.isupper())  # True

# Example 2: Mixed case
text = "Hello"
print(text.isupper())  # False

# When to use: Constant name validation
```

---

### join(iterable)
**What it does**: Joins elements of iterable into a single string using the string as separator.

**Requirements**:
- `iterable` (required): List, tuple, or any iterable of strings

**Data Types**:
- Input: iterable of strings
- Output: single string

**Use Case Examples**:
```python
# Example 1: Join list with space
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)  # "Hello World Python"

# Example 2: Join with comma
items = ["apple", "banana", "cherry"]
result = ", ".join(items)
print(result)  # "apple, banana, cherry"

# Example 3: Join with newline
lines = ["First line", "Second line", "Third line"]
result = "\n".join(lines)
print(result)
# First line
# Second line
# Third line

# Example 4: Create CSV
data = ["John", "30", "Engineer"]
csv_line = ",".join(data)
print(csv_line)  # "John,30,Engineer"

# When to use: Building strings from lists, creating formatted output
```

---

### ljust(width, fillchar=' ')
**What it does**: Left-justifies string in a field of given width.

**Requirements**:
- `width` (required): Total width
- `fillchar` (optional): Fill character (default: space)

**Data Types**:
- Input: `width` (int), `fillchar` (single char string)
- Output: string

**Use Case Examples**:
```python
# Example 1: Left justify with spaces
text = "Python"
result = text.ljust(20)
print(result + "|")  # "Python              |"

# Example 2: Custom fill character
text = "Item"
result = text.ljust(20, '-')
print(result)  # "Item----------------"

# When to use: Creating aligned columns
print("Name".ljust(20) + "Age")
print("Alice".ljust(20) + "25")
print("Bob".ljust(20) + "30")
```

---

### lower()
**What it does**: Converts all characters to lowercase.

**Requirements**: No parameters

**Data Types**:
- Output: string (lowercase)

**Use Case Examples**:
```python
# Example 1: Basic conversion
text = "HELLO WORLD"
result = text.lower()
print(result)  # "hello world"

# Example 2: Case-insensitive comparison
user_input = "YES"
if user_input.lower() == "yes":
    print("Confirmed")  # This prints

# When to use: Normalizing input, comparisons
```

---

### lstrip(chars=None)
**What it does**: Removes leading characters (left side).

**Requirements**:
- `chars` (optional): Characters to remove (default: whitespace)

**Data Types**:
- Input: `chars` (string of characters)
- Output: string

**Use Case Examples**:
```python
# Example 1: Remove leading spaces
text = "   Hello"
result = text.lstrip()
print(result)  # "Hello"

# Example 2: Remove specific characters
text = "###Hello###"
result = text.lstrip('#')
print(result)  # "Hello###"

# When to use: Cleaning user input
```

---

### partition(sep)
**What it does**: Splits string at first occurrence of separator into 3-tuple.

**Requirements**:
- `sep` (required): Separator string

**Data Types**:
- Input: `sep` (string)
- Output: tuple of 3 strings (before, separator, after)

**Use Case Examples**:
```python
# Example 1: Basic partition
text = "user@example.com"
before, sep, after = text.partition("@")
print(f"User: {before}, Domain: {after}")
# User: user, Domain: example.com

# Example 2: Not found
text = "no separator here"
result = text.partition("@")
print(result)  # ('no separator here', '', '')

# When to use: Parsing structured text
```

---

### replace(old, new, count=-1)
**What it does**: Replaces occurrences of old substring with new.

**Requirements**:
- `old` (required): Substring to replace
- `new` (required): Replacement string
- `count` (optional): Max replacements (default: all)

**Data Types**:
- Input: `old` (string), `new` (string), `count` (int)
- Output: string

**Use Case Examples**:
```python
# Example 1: Replace all
text = "Hello World, Hello Python"
result = text.replace("Hello", "Hi")
print(result)  # "Hi World, Hi Python"

# Example 2: Limit replacements
text = "Hello Hello Hello"
result = text.replace("Hello", "Hi", 2)
print(result)  # "Hi Hi Hello"

# Example 3: Remove substring
text = "Hello World!!!"
result = text.replace("!", "")
print(result)  # "Hello World"

# When to use: Text cleaning, censoring, templating
def censor_email(email):
    parts = email.split("@")
    if len(parts) == 2:
        censored = parts[0][:2] + "***"
        return censored + "@" + parts[1]
    return email

print(censor_email("john@example.com"))  # "jo***@example.com"
```

---

### rfind(substring, start=0, end=len)
**What it does**: Like find() but searches from right (returns last occurrence).

**Requirements**:
- `substring` (required): What to search for
- `start`, `end` (optional): Range to search

**Data Types**:
- Input: `substring` (string), `start` (int), `end` (int)
- Output: integer (index or -1)

**Use Case Examples**:
```python
# Example 1: Find last occurrence
text = "hello hello hello"
index = text.rfind("hello")
print(index)  # 12

# Example 2: Get file extension
filename = "document.backup.txt"
last_dot = filename.rfind(".")
if last_dot != -1:
    extension = filename[last_dot+1:]
    print(extension)  # "txt"

# When to use: Finding last occurrence
```

---

### rindex(substring, start=0, end=len)
**What it does**: Like rfind() but raises ValueError if not found.

**Requirements**:
- `substring` (required): What to search for
- `start`, `end` (optional): Range

**Data Types**:
- Input: `substring` (string), `start` (int), `end` (int)
- Output: integer or raises ValueError

**Use Case Examples**:
```python
# Example: Must exist
text = "hello hello"
try:
    index = text.rindex("hello")
    print(f"Last at: {index}")  # Last at: 6
except ValueError:
    print("Not found")

# When to use: When last occurrence MUST exist
```

---

### rjust(width, fillchar=' ')
**What it does**: Right-justifies string in field of given width.

**Requirements**:
- `width` (required): Total width
- `fillchar` (optional): Fill character

**Data Types**:
- Input: `width` (int), `fillchar` (string)
- Output: string

**Use Case Examples**:
```python
# Example 1: Right align numbers
numbers = ["1", "25", "300"]
for num in numbers:
    print(num.rjust(10))
#          1
#         25
#        300

# Example 2: Custom fill
text = "Total"
result = text.rjust(20, '-')
print(result)  # "---------------Total"

# When to use: Aligning numbers, creating tables
```

---

### rpartition(sep)
**What it does**: Like partition() but splits at last occurrence.

**Requirements**:
- `sep` (required): Separator

**Data Types**:
- Input: `sep` (string)
- Output: tuple of 3 strings

**Use Case Examples**:
```python
# Example: Split from right
path = "C:\\Users\\Documents\\file.txt"
before, sep, filename = path.rpartition("\\")
print(f"Directory: {before}")  # C:\Users\Documents
print(f"File: {filename}")     # file.txt

# When to use: Path parsing, getting last segment
```

---

### rsplit(sep=None, maxsplit=-1)
**What it does**: Splits from right with optional maximum splits.

**Requirements**:
- `sep` (optional): Separator (default: whitespace)
- `maxsplit` (optional): Max splits (default: all)

**Data Types**:
- Input: `sep` (string), `maxsplit` (int)
- Output: list of strings

**Use Case Examples**:
```python
# Example: Split from right
text = "a,b,c,d,e"
result = text.rsplit(",", 2)
print(result)  # ['a,b,c', 'd', 'e']

# When to use: Getting last N parts
```

---

### rstrip(chars=None)
**What it does**: Removes trailing characters (right side).

**Requirements**:
- `chars` (optional): Characters to remove

**Data Types**:
- Input: `chars` (string)
- Output: string

**Use Case Examples**:
```python
# Example 1: Remove trailing spaces
text = "Hello   "
result = text.rstrip()
print(result + "|")  # "Hello|"

# Example 2: Remove specific chars
text = "###Hello###"
result = text.rstrip('#')
print(result)  # "###Hello"

# Example 3: Remove newlines
text = "Line of text\n\n"
result = text.rstrip('\n')
print(result)  # "Line of text"

# When to use: Cleaning file input
```

---

### split(sep=None, maxsplit=-1)
**What it does**: Splits string into list.

**Requirements**:
- `sep` (optional): Separator (default: any whitespace)
- `maxsplit` (optional): Maximum splits

**Data Types**:
- Input: `sep` (string), `maxsplit` (int)
- Output: list of strings

**Use Case Examples**:
```python
# Example 1: Split on spaces
text = "Hello World Python"
words = text.split()
print(words)  # ['Hello', 'World', 'Python']

# Example 2: Split with delimiter
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# Example 3: Limit splits
text = "a:b:c:d"
parts = text.split(":", 2)
print(parts)  # ['a', 'b', 'c:d']

# Example 4: Parse CSV line
line = "John,30,Engineer,New York"
name, age, job, city = line.split(",")
print(f"{name} is a {age}-year-old {job}")

# When to use: Parsing text, processing input
```

---

### splitlines(keepends=False)
**What it does**: Splits string at line breaks.

**Requirements**:
- `keepends` (optional): Keep line break characters (default: False)

**Data Types**:
- Input: `keepends` (boolean)
- Output: list of strings

**Use Case Examples**:
```python
# Example 1: Basic split
text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# Example 2: Keep line endings
text = "Line 1\nLine 2\n"
lines = text.splitlines(keepends=True)
print(lines)  # ['Line 1\n', 'Line 2\n']

# Example 3: Process file content
content = """Name: John
Age: 30
City: NYC"""
for line in content.splitlines():
    print(line.strip())

# When to use: Processing multi-line text, files
```

---

### startswith(prefix, start=0, end=len)
**What it does**: Checks if string starts with prefix.

**Requirements**:
- `prefix` (required): String or tuple to check
- `start`, `end` (optional): Range

**Data Types**:
- Input: `prefix` (string/tuple), `start` (int), `end` (int)
- Output: boolean

**Use Case Examples**:
```python
# Example 1: Simple check
text = "Hello World"
if text.startswith("Hello"):
    print("Starts with Hello")  # This prints

# Example 2: Multiple prefixes
url = "https://example.com"
if url.startswith(('http://', 'https://')):
    print("Valid URL")  # This prints

# Example 3: Check command
command = "/help user"
if command.startswith("/"):
    cmd = command[1:].split()[0]
    print(f"Command: {cmd}")  # Command: help

# When to use: Command parsing, protocol checking
```

---

### strip(chars=None)
**What it does**: Removes leading AND trailing characters.

**Requirements**:
- `chars` (optional): Characters to remove (default: whitespace)

**Data Types**:
- Input: `chars` (string)
- Output: string

**Use Case Examples**:
```python
# Example 1: Remove whitespace
text = "   Hello World   "
result = text.strip()
print(result)  # "Hello World"

# Example 2: Remove specific characters
text = "###Hello###"
result = text.strip('#')
print(result)  # "Hello"

# Example 3: Clean user input
user_input = "  yes  \n"
cleaned = user_input.strip().lower()
if cleaned == "yes":
    print("Confirmed")  # This prints

# When to use: Cleaning ALL user input
```

---

### swapcase()
**What it does**: Swaps case of all characters.

**Requirements**: No parameters

**Data Types**:
- Output: string

**Use Case Examples**:
```python
# Example 1: Basic swap
text = "Hello World"
result = text.swapcase()
print(result)  # "hELLO wORLD"

# Example 2: Toggle case
text = "PyThOn"
result = text.swapcase()
print(result)  # "pYtHoN"

# When to use: Text effects, encoding
```

---

### title()
**What it does**: Converts to title case (first letter of each word capitalized).

**Requirements**: No parameters

**Data Types**:
- Output: string

**Use Case Examples**:
```python
# Example 1: Basic title case
text = "hello world python"
result = text.title()
print(result)  # "Hello World Python"

# Example 2: From various cases
text = "HELLO world PyThOn"
result = text.title()
print(result)  # "Hello World Python"

# Example 3: Formatting names
names = ["john doe", "jane smith", "bob jones"]
formatted = [name.title() for name in names]
print(formatted)  # ['John Doe', 'Jane Smith', 'Bob Jones']

# When to use: Formatting titles, names, headings
```

---

### translate(table)
**What it does**: Translates string using translation table.

**Requirements**:
- `table` (required): Translation mapping (from str.maketrans())

**Data Types**:
- Input: translation table (dict)
- Output: string

**Use Case Examples**:
```python
# Example 1: Replace multiple characters
table = str.maketrans("aeiou", "12345")
text = "hello world"
result = text.translate(table)
print(result)  # "h2ll4 w4rld"

# Example 2: Remove characters
table = str.maketrans("", "", "aeiou")  # Remove vowels
text = "hello world"
result = text.translate(table)
print(result)  # "hll wrld"

# Example 3: Cipher
table = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                     "nopqrstuvwxyzabcdefghijklm")  # ROT13
text = "hello"
encrypted = text.translate(table)
print(encrypted)  # "uryyb"

# When to use: Bulk character replacement, encoding
```

---

### upper()
**What it does**: Converts all characters to uppercase.

**Requirements**: No parameters

**Data Types**:
- Output: string

**Use Case Examples**:
```python
# Example 1: Basic conversion
text = "hello world"
result = text.upper()
print(result)  # "HELLO WORLD"

# Example 2: Case-insensitive comparison
password = "SecretPass"
if password.upper() == "SECRETPASS":
    print("Match")  # This prints

# Example 3: Creating constants
module_name = "database_manager"
constant = module_name.upper()
print(constant)  # "DATABASE_MANAGER"

# When to use: Constants, normalization
```

---

### zfill(width)
**What it does**: Pads string with zeros on the left.

**Requirements**:
- `width` (required): Total width

**Data Types**:
- Input: `width` (int)
- Output: string

**Use Case Examples**:
```python
# Example 1: Pad numbers
number = "42"
result = number.zfill(5)
print(result)  # "00042"

# Example 2: Handle signs
number = "-42"
result = number.zfill(5)
print(result)  # "-0042"

# Example 3: Create IDs
id_num = 7
id_string = str(id_num).zfill(6)
print(f"ID: {id_string}")  # "ID: 000007"

# Example 4: Format invoice numbers
invoices = [1, 45, 237]
for inv in invoices:
    print(f"INV-{str(inv).zfill(4)}")
# INV-0001
# INV-0045
# INV-0237

# When to use: IDs, invoice numbers, sorting
```

---

## Concepts

### Slicing
**What it is**: Extracting parts of a string using index notation `[start:stop:step]`.

**Syntax**: `string[start:stop:step]`
- `start`: Starting index (inclusive, default: 0)
- `stop`: Ending index (exclusive, default: len(string))
- `step`: Skip pattern (default: 1)

**Examples**:
```python
text = "Hello World"

# Basic slicing
print(text[0:5])    # "Hello" (index 0-4)
print(text[6:11])   # "World" (index 6-10)

# Omit start (from beginning)
print(text[:5])     # "Hello"

# Omit stop (to end)
print(text[6:])     # "World"

# Negative indices (from end)
print(text[-5:])    # "World" (last 5 chars)
print(text[:-6])    # "Hello" (all but last 6)

# Step (skip pattern)
print(text[::2])    # "HloWrd" (every 2nd char)
print(text[1::2])   # "el ol" (every 2nd starting from 1)

# Reverse string
print(text[::-1])   # "dlroW olleH"

# Get first and last
print(text[0])      # "H"
print(text[-1])     # "d"

# Middle portion
print(text[2:9])    # "llo Wor"

# Real-world examples
email = "user@example.com"
username = email[:email.index("@")]  # "user"
domain = email[email.index("@")+1:]  # "example.com"

# Extract date parts
date = "2025-11-29"
year = date[:4]    # "2025"
month = date[5:7]  # "11"
day = date[8:]     # "29"

# Skip every 3rd character
text = "abcdefghijklmnop"
result = text[::3]  # "adgjm"
```

**Common Patterns**:
```python
text = "Python Programming"

# First N characters
first_5 = text[:5]  # "Pytho"

# Last N characters
last_5 = text[-5:]  # "mming"

# Remove first/last character
no_first = text[1:]      # "ython Programming"
no_last = text[:-1]      # "Python Programmin"

# Get every other character
alternating = text[::2]  # "Pto rgamn"

# Reverse
reversed_text = text[::-1]  # "gnimmargorP nohtyP"

# Middle section
middle = text[3:-3]  # "hon Program"
```

---

### Modify
**What it is**: Strings are immutable, so "modifying" creates new strings.

**Common Modification Operations**:

```python
text = "Hello World"

# 1. Change case
uppercase = text.upper()        # "HELLO WORLD"
lowercase = text.lower()        # "hello world"
titlecase = text.title()        # "Hello World"
swapped = text.swapcase()       # "hELLO wORLD"
capitalized = text.capitalize() # "Hello world"

# 2. Replace content
replaced = text.replace("World", "Python")  # "Hello Python"
replaced_all = text.replace("l", "L")       # "HeLLo WorLd"
replaced_limited = text.replace("l", "L", 2) # "HeLLo World"

# 3. Strip/trim
spaced = "  Hello  "
stripped = spaced.strip()   # "Hello"
lstripped = spaced.lstrip() # "Hello  "
rstripped = spaced.rstrip() # "  Hello"

# 4. Add/remove characters
text = "Hello"
added = text + " World"           # "Hello World"
repeated = text * 3               # "HelloHelloHello"
joined = "-".join(text)           # "H-e-l-l-o"

# 5. Character translation
text = "hello world"
vowel_map = str.maketrans("aeiou", "12345")
translated = text.translate(vowel_map)  # "h2ll4 w4rld"

# 6. Using list conversion for complex modifications
text = "Hello World"
chars = list(text)
chars[6] = 'P'  # Change 'W' to 'P'
modified = ''.join(chars)  # "Hello Porld"

# 7. Insert at position
def insert_at(string, index, substring):
    return string[:index] + substring + string[index:]

text = "Hello World"
modified = insert_at(text, 6, "Beautiful ")
print(modified)  # "Hello Beautiful World"

# 8. Remove at position
def remove_at(string, start, end):
    return string[:start] + string[end:]

text = "Hello World"
modified = remove_at(text, 6, 12)
print(modified)  # "Hello "

# 9. Reverse
text = "Hello"
reversed_text = text[::-1]  # "olleH"

# 10. Remove duplicates
text = "hello"
unique = ''.join(sorted(set(text), key=text.index))
print(unique)  # "helo"
```

**Best Practices**:
```python
# Build strings efficiently
# BAD (slow for many concatenations)
result = ""
for i in range(1000):
    result += str(i)

# GOOD (fast)
result = ''.join(str(i) for i in range(1000))

# Or use list
parts = []
for i in range(1000):
    parts.append(str(i))
result = ''.join(parts)
```

---

### Concat (Concatenation)
**What it is**: Joining multiple strings together.

**Methods**:

```python
# 1. Plus operator (+)
first = "Hello"
last = "World"
full = first + " " + last  # "Hello World"

# 2. Multiple concatenations
greeting = "Hello" + " " + "beautiful" + " " + "world"
# "Hello beautiful world"

# 3. join() method (most efficient)
words = ["Hello", "World", "Python"]
sentence = " ".join(words)  # "Hello World Python"

# Different separators
csv = ",".join(words)       # "Hello,World,Python"
newlines = "\n".join(words) # "Hello\nWorld\nPython"

# 4. f-strings (Python 3.6+)
name = "Alice"
age = 25
info = f"{name} is {age} years old"  # "Alice is 25 years old"

# 5. format() method
info = "{} is {} years old".format(name, age)
# "Alice is 25 years old"

# 6. % formatting (old style)
info = "%s is %d years old" % (name, age)
# "Alice is 25 years old"

# 7. Multiplication (repeat)
dash_line = "-" * 50  # 50 dashes
repeated = "Ha" * 3   # "HaHaHa"

# 8. String building with StringIO (for many operations)
from io import StringIO
buffer = StringIO()
buffer.write("Hello")
buffer.write(" ")
buffer.write("World")
result = buffer.getvalue()  # "Hello World"

# Real-world examples

# Build path
parts = ["home", "user", "documents", "file.txt"]
path = "/".join(parts)  # "home/user/documents/file.txt"

# Create table row
columns = ["Name", "Age", "City"]
row = " | ".join(columns)  # "Name | Age | City"

# Build query string
params = {"name": "John", "age": "30", "city": "NYC"}
query = "&".join(f"{k}={v}" for k, v in params.items())
# "name=John&age=30&city=NYC"

# Concatenate with condition
prefix = "Mr. "
suffix = ", PhD"
name = "Smith"
title = prefix + name + suffix  # "Mr. Smith, PhD"

# Build multi-line string
lines = [
    "Line 1",
    "Line 2",
    "Line 3"
]
text = "\n".join(lines)

# Efficient concatenation in loops
# BAD
result = ""
for i in range(1000):
    result += str(i) + ","

# GOOD
parts = [str(i) for i in range(1000)]
result = ",".join(parts)
```

**Performance Comparison**:
```python
import timeit

# Method 1: Plus operator (slow for many ops)
def concat_plus():
    result = ""
    for i in range(100):
        result = result + str(i)
    return result

# Method 2: join() (fast)
def concat_join():
    return ''.join(str(i) for i in range(100))

# join() is typically 2-3x faster
```

---

### Format
**What it is**: Creating strings with embedded variables/expressions.

**Methods**:

```python
# 1. f-strings (Python 3.6+) - RECOMMENDED
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
# "Name: Alice, Age: 25"

# With expressions
print(f"Next year: {age + 1}")
# "Next year: 26"

# Format specifiers
price = 19.99
print(f"Price: ${price:.2f}")  # "Price: $19.99"

# Alignment
print(f"{'Left':<10}|")    # "Left      |"
print(f"{'Center':^10}|")  # "  Center  |"
print(f"{'Right':>10}|")   # "     Right|"

# 2. str.format() method
template = "Name: {}, Age: {}"
print(template.format("Bob", 30))
# "Name: Bob, Age: 30"

# With index
template = "{0} is {1} years old. {0} is a programmer."
print(template.format("Alice", 25))
# "Alice is 25 years old. Alice is a programmer."

# With names
template = "{name} is {age} years old"
print(template.format(name="Charlie", age=35))
# "Charlie is 35 years old"

# 3. % formatting (old style, avoid in new code)
print("Name: %s, Age: %d" % ("David", 40))
# "Name: David, Age: 40"

# 4. Template strings (from string module)
from string import Template
t = Template("$name is $age years old")
print(t.substitute(name="Eve", age=28))
# "Eve is 28 years old"
```

**Format Specifications**:

```python
# Numbers
num = 42
print(f"{num:d}")      # "42" (decimal)
print(f"{num:05d}")    # "00042" (pad with zeros)
print(f"{num:,}")      # "42" (with thousands separator)

large = 1000000
print(f"{large:,}")    # "1,000,000"

# Floats
pi = 3.14159265359
print(f"{pi:.2f}")     # "3.14" (2 decimal places)
print(f"{pi:.4f}")     # "3.1416" (4 decimal places)
print(f"{pi:10.2f}")   # "      3.14" (width 10)

# Percentage
ratio = 0.75
print(f"{ratio:.1%}")  # "75.0%"

# Scientific notation
big = 12345678
print(f"{big:e}")      # "1.234568e+07"
print(f"{big:.2e}")    # "1.23e+07"

# Binary, Octal, Hex
num = 255
print(f"{num:b}")      # "11111111" (binary)
print(f"{num:o}")      # "377" (octal)
print(f"{num:x}")      # "ff" (hex lowercase)
print(f"{num:X}")      # "FF" (hex uppercase)

# Alignment and padding
text = "Python"
print(f"{text:>10}")   # "    Python" (right align, width 10)
print(f"{text:<10}")   # "Python    " (left align)
print(f"{text:^10}")   # "  Python  " (center)
print(f"{text:*^10}")  # "**Python**" (center with *)

# Dates
from datetime import datetime
now = datetime.now()
print(f"{now:%Y-%m-%d}")         # "2025-11-29"
print(f"{now:%H:%M:%S}")         # "14:30:45"
print(f"{now:%B %d, %Y}")        # "November 29, 2025"

# Nested formatting
width = 10
precision = 2
value = 3.14159
print(f"{value:{width}.{precision}f}")  # "      3.14"
```

**Real-World Examples**:

```python
# 1. Creating reports
def generate_report(name, sales, target):
    percentage = (sales / target) * 100
    return f"""
    Sales Report
    ============
    Employee: {name}
    Sales:    ${sales:,.2f}
    Target:   ${target:,.2f}
    Progress: {percentage:.1f}%
    Status:   {'✓ Met' if sales >= target else '✗ Not Met'}
    """

print(generate_report("Alice", 125000, 100000))

# 2. Table formatting
def format_table(data):
    print(f"{'Name':<15} {'Age':>5} {'City':<10}")
    print("-" * 32)
    for row in data:
        print(f"{row['name']:<15} {row['age']:>5} {row['city']:<10}")

data = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"},
]
format_table(data)

# 3. Progress bar
def progress_bar(current, total, width=50):
    percent = current / total
    filled = int(width * percent)
    bar = '█' * filled + '░' * (width - filled)
    return f"|{bar}| {percent:.1%}"

print(progress_bar(75, 100))
# |█████████████████████████████████████░░░░░░░░░░░░░░░| 75.0%

# 4. Logging format
import datetime
def log(level, message):
    timestamp = datetime.datetime.now()
    return f"[{timestamp:%Y-%m-%d %H:%M:%S}] {level:8} - {message}"

print(log("INFO", "Application started"))
print(log("ERROR", "Connection failed"))
```

---

### Escape
**What it is**: Using special character sequences that represent non-printable or special characters.

**Common Escape Sequences**:

```python
# \n - Newline
print("Line 1\nLine 2")
# Line 1
# Line 2

# \t - Tab
print("Name:\tAlice\nAge:\t25")
# Name:	Alice
# Age:	25

# \\ - Backslash
print("Path: C:\\Users\\Documents")
# Path: C:\Users\Documents

# \' - Single quote
print('It\'s a beautiful day')
# It's a beautiful day

# \" - Double quote
print("He said \"Hello\"")
# He said "Hello"

# \r - Carriage return
print("Loading\rDone")  # Overwrites "Loading"
# Done

# \b - Backspace
print("Hello\b\b\b\bGood")
# Good (backspaces remove "llo")

# \a - Bell/alert (system beep)
print("Alert!\a")

# \0 - Null character
print("Null:\0character")

# \xhh - Character with hex value
print("\x48\x65\x6C\x6C\x6F")  # "Hello"

# \uhhhh - Unicode character (16-bit)
print("\u0048\u0065\u006C\u006C\u006F")  # "Hello"
print("\u2665")  # ♥ (heart symbol)

# \Uhhhhhhhh - Unicode character (32-bit)
print("\U0001F600")  # 😀 (emoji)

# \N{name} - Unicode character by name
print("\N{BLACK HEART SUIT}")  # ♥
print("\N{SNOWMAN}")  # ☃
```

**Raw Strings** (prefix with `r`):
```python
# Without raw string (escape sequences processed)
path = "C:\new\folder\test"
print(path)  # Escape sequences interpreted
# C:
# ew\folder	est

# With raw string (escape sequences NOT processed)
path = r"C:\new\folder\test"
print(path)  # Literal backslashes
# C:\new\folder\test

# Common use cases
regex = r"\d+\.\d+"  # Regex pattern
print(regex)  # \d+\.\d+

windows_path = r"C:\Users\Documents\file.txt"
print(windows_path)  # C:\Users\Documents\file.txt

# Raw f-strings (Python 3.12+)
name = "Alice"
text = rf"C:\Users\{name}\Documents"
print(text)  # C:\Users\Alice\Documents
```

**Triple-Quoted Strings** (preserve formatting):
```python
# Multi-line strings
text = """Line 1
Line 2
Line 3"""
print(text)

# With escape sequences
formatted = """Name:\t\tJohn
Age:\t\t30
City:\t\tNYC"""
print(formatted)

# Docstrings
def example():
    """
    This is a docstring.
    It can span multiple lines.
    Escape sequences work: \n, \t, etc.
    """
    pass
```

**Escaping Special Characters in Different Contexts**:

```python
# 1. In regular expressions
import re
text = "Price: $19.99"
# Need to escape $ (special in regex)
pattern = r"\$\d+\.\d+"
match = re.search(pattern, text)
print(match.group())  # "$19.99"

# 2. In URLs
url = "https://example.com/search?q=hello world"
# Space needs encoding
import urllib.parse
encoded = urllib.parse.quote("hello world")
print(encoded)  # "hello%20world"

# 3. In SQL queries (avoid SQL injection)
# BAD - vulnerable to injection
name = "'; DROP TABLE users; --"
query = f"SELECT * FROM users WHERE name = '{name}'"

# GOOD - use parameterized queries
# (depends on your database library)

# 4. In HTML
html_text = "<p>Use &lt; and &gt; for brackets</p>"
print(html_text)  # <p>Use &lt; and &gt; for brackets</p>

# 5. In JSON
import json
data = {"message": "Line 1\nLine 2"}
json_str = json.dumps(data)
print(json_str)  # {"message": "Line 1\nLine 2"}
```

**Working with Escape Sequences**:

```python
# Check for escape sequences
text = "Hello\nWorld"
print(repr(text))  # 'Hello\nWorld' (shows escape sequences)
print(text)        # Hello
                   # World

# Remove escape sequences
text = "Hello\\nWorld"
decoded = text.encode().decode('unicode_escape')
print(decoded)  # Hello
                # World

# Add escape sequences
text = "Hello\tWorld"
encoded = repr(text)
print(encoded)  # 'Hello\tWorld'

# Escape for printing literal
def show_escapes(text):
    return repr(text)[1:-1]  # Remove quotes

print(show_escapes("Hello\nWorld"))  # Hello\nWorld
```

**Common Patterns**:

```python
# 1. File paths (Windows)
# Use raw strings or double backslashes
path1 = r"C:\Users\Documents\file.txt"
path2 = "C:\\Users\\Documents\\file.txt"

# Or use forward slashes (works on Windows too)
path3 = "C:/Users/Documents/file.txt"

# 2. Multi-line text with proper indentation
message = """
Dear {name},

Thank you for your order #{order_id}.

Best regards,
Customer Service
""".format(name="Alice", order_id="12345")

# 3. Creating formatted output
def print_box(text):
    border = "+" + "-" * (len(text) + 2) + "+"
    content = f"| {text} |"
    return f"{border}\n{content}\n{border}"

print(print_box("Hello World"))
# +--------------+
# | Hello World |
# +--------------+

# 4. Escape for specific output
def create_c_string(text):
    """Convert Python string to C-style escaped string."""
    escaped = text.replace('\\', '\\\\')
    escaped = escaped.replace('"', '\\"')
    escaped = escaped.replace('\n', '\\n')
    escaped = escaped.replace('\t', '\\t')
    return f'"{escaped}"'

print(create_c_string("Hello\nWorld"))  # "Hello\nWorld"
```

---

## Quick Reference

### String Creation
```python
single = 'Hello'
double = "Hello"
triple = '''Multi
line'''
raw = r"C:\path"
formatted = f"Value: {x}"
```

### Common Operations
```python
# Case
s.upper(), s.lower(), s.title()

# Search
s.find("x"), s.index("x"), s.count("x")

# Check
s.startswith("x"), s.endswith("x")

# Clean
s.strip(), s.lstrip(), s.rstrip()

# Transform
s.replace("old", "new"), s.split(",")

# Build
" ".join(list), f"{var}"
```

### String Checks
```python
s.isalpha()     # Only letters
s.isdigit()     # Only digits
s.isalnum()     # Letters or digits
s.isspace()     # Only whitespace
s.isupper()     # All uppercase
s.islower()     # All lowercase
```

