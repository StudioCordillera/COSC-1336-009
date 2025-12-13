# TEXTWRAP_MODULE

## Core Definition
**textwrap** is a module providing utilities for wrapping, filling, and formatting plain text by manipulating string line breaks. Designed for formatting text in fixed-width displays and terminals.

**Tags**: #textwrap #text-formatting #line-wrapping #text-processing #indentation

---

## COMPLETE TEXTWRAP METHODS QUICK REFERENCE

### TEXTWRAP FUNCTIONS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# CONVENIENCE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
textwrap.wrap(text, width=70, **kwargs)              # Text | Wrap to lines of max width | Returns list of lines
textwrap.fill(text, width=70, **kwargs)              # Text | Wrap and join with newlines | Returns single string
textwrap.shorten(text, width, **kwargs)              # Text | Truncate to fit width | Returns shortened string
textwrap.dedent(text)                                # Text | Remove common leading whitespace | Returns dedented string
textwrap.indent(text, prefix, predicate=None)        # Text | Add prefix to lines | Returns indented string

# ═══════════════════════════════════════════════════════════════════════════
# TEXTWRAPPER CLASS
# ═══════════════════════════════════════════════════════════════════════════
TextWrapper(**kwargs)                                # Constructor | Create wrapper instance | Returns TextWrapper object
TextWrapper.wrap(text)                               # Text | Wrap paragraph to lines | Returns list of lines
TextWrapper.fill(text)                               # Text | Wrap and join paragraph | Returns single string

# ═══════════════════════════════════════════════════════════════════════════
# TEXTWRAPPER ATTRIBUTES (Constructor kwargs)
# ═══════════════════════════════════════════════════════════════════════════
width                                                # Attribute | Maximum line length | Default: 70
expand_tabs                                          # Attribute | Expand tabs to spaces | Default: True
tabsize                                              # Attribute | Tab expansion size | Default: 8
replace_whitespace                                   # Attribute | Collapse whitespace | Default: True
drop_whitespace                                      # Attribute | Remove leading/trailing | Default: True
initial_indent                                       # Attribute | First line prefix | Default: ''
subsequent_indent                                    # Attribute | Other lines prefix | Default: ''
fix_sentence_endings                                 # Attribute | Two spaces after sentences | Default: False
break_long_words                                     # Attribute | Break words longer than width | Default: True
break_on_hyphens                                     # Attribute | Break on hyphens | Default: True
max_lines                                            # Attribute | Maximum output lines | Default: None
placeholder                                          # Attribute | Truncation indicator | Default: ' [...]'
```

---

## DETAILED FUNCTION OPERATIONS

### 1. WRAP FUNCTION

**Purpose**: Split text into lines with maximum width

```python
import textwrap

# Basic wrapping
text = "This is a very long line that needs to be wrapped to fit within a specific width."
lines = textwrap.wrap(text, width=40)
# → ['This is a very long line that needs',
#    'to be wrapped to fit within a',
#    'specific width.']

# With indentation
lines = textwrap.wrap(text, width=40, initial_indent="  ", subsequent_indent="    ")
# → ['  This is a very long line that',
#    '    needs to be wrapped to fit within',
#    '    a specific width.']

# Preserve specific formatting
code = "def function(): return True"
lines = textwrap.wrap(code, width=20, break_long_words=False)
# → ['def function():', 'return True']

# All parameters
textwrap.wrap(
    text,
    width=70,                    # Maximum line width
    initial_indent='',           # Prefix for first line
    subsequent_indent='',        # Prefix for subsequent lines
    expand_tabs=True,            # Convert tabs to spaces
    replace_whitespace=True,     # Collapse whitespace
    fix_sentence_endings=False,  # Two spaces after sentences
    break_long_words=True,       # Break words exceeding width
    drop_whitespace=True,        # Drop leading/trailing whitespace
    break_on_hyphens=True,       # Break on hyphen boundaries
    tabsize=8,                   # Tab width if expand_tabs=True
    max_lines=None,              # Limit output lines
    placeholder=' [...]'         # Truncation placeholder
)
```

### 2. FILL FUNCTION

**Purpose**: Wrap text and join with newlines (shorthand for `"\n".join(wrap(...))`)

```python
import textwrap

# Basic filling
text = "This is a very long line that needs to be wrapped to fit within a specific width."
result = textwrap.fill(text, width=40)
print(result)
# This is a very long line that needs
# to be wrapped to fit within a
# specific width.

# With hanging indent
result = textwrap.fill(
    "Error: File not found in the specified directory location",
    width=30,
    initial_indent="",
    subsequent_indent="       "
)
print(result)
# Error: File not found in the
#        specified directory
#        location

# Bullet list formatting
items = ["First item with a long description", 
         "Second item also long", 
         "Third item"]
for item in items:
    print(textwrap.fill(item, width=35, 
                       initial_indent="  • ",
                       subsequent_indent="    "))
# Output:
#   • First item with a long
#     description
#   • Second item also long
#   • Third item

# All parameters (same as wrap)
textwrap.fill(
    text,
    width=70,
    initial_indent='',
    subsequent_indent='',
    expand_tabs=True,
    replace_whitespace=True,
    fix_sentence_endings=False,
    break_long_words=True,
    drop_whitespace=True,
    break_on_hyphens=True,
    tabsize=8,
    max_lines=None,
    placeholder=' [...]'
)
```

### 3. SHORTEN FUNCTION

**Purpose**: Collapse and truncate text to fit width

```python
import textwrap

# Basic shortening
text = "Hello world! This is a very long message."
short = textwrap.shorten(text, width=20)
# → "Hello world! [...]"

# Custom placeholder
short = textwrap.shorten(text, width=20, placeholder="...")
# → "Hello world!..."

# Whitespace collapse
text = "Hello    world!    Multiple    spaces!"
short = textwrap.shorten(text, width=30)
# → "Hello world! Multiple [...]"

# Just fits (no truncation)
short = textwrap.shorten("Hello world!", width=12)
# → "Hello world!"

# Too short (truncates)
short = textwrap.shorten("Hello world!", width=11)
# → "Hello [...]"

# All parameters
textwrap.shorten(
    text,
    width,                       # Required: target width
    fix_sentence_endings=False,  # Two spaces after sentences
    break_long_words=True,       # Break words exceeding width
    break_on_hyphens=True,       # Break on hyphen boundaries
    placeholder=' [...]'         # Truncation indicator
)

# Note: tabsize, expand_tabs, drop_whitespace, replace_whitespace
# have no effect because whitespace is collapsed before processing
```

### 4. DEDENT FUNCTION

**Purpose**: Remove common leading whitespace from all lines

```python
import textwrap

# Remove indentation from triple-quoted string
def example():
    text = """\
    Hello
      World
        Python
    """
    print(repr(text))
    # '    Hello\n      World\n        Python\n    '
    
    print(repr(textwrap.dedent(text)))
    # 'Hello\n  World\n    Python\n'

# Practical use: clean docstrings
def get_help():
    return textwrap.dedent("""\
        Usage: program [options]
        
        Options:
            -h    Show this help
            -v    Verbose mode
        """)

print(get_help())
# Usage: program [options]
# 
# Options:
#     -h    Show this help
#     -v    Verbose mode

# Mixed indentation (tabs and spaces treated separately)
text1 = "  hello"        # 2 spaces
text2 = "\thello"        # 1 tab
combined = text1 + "\n" + text2
dedented = textwrap.dedent(combined)
# No common whitespace found (tab ≠ spaces)

# Empty/whitespace-only lines ignored
text = """
    Line 1
    
    Line 2
"""
result = textwrap.dedent(text)
# '\nLine 1\n\nLine 2\n'
```

### 5. INDENT FUNCTION

**Purpose**: Add prefix to selected lines

```python
import textwrap

# Basic indentation
text = "hello\nworld"
result = textwrap.indent(text, '  ')
# '  hello\n  world'

# Empty lines not indented by default
text = "hello\n\n \nworld"
result = textwrap.indent(text, '  ')
# '  hello\n\n \n  world'

# Indent all lines including empty (using predicate)
result = textwrap.indent(text, '  ', lambda line: True)
# '  hello\n  \n   \n  world'

# Comment out code
code = """def hello():
    print("world")"""
commented = textwrap.indent(code, '# ')
print(commented)
# # def hello():
# #     print("world")

# Quote text
quote = """To be or not to be,
that is the question."""
quoted = textwrap.indent(quote, '> ')
print(quoted)
# > To be or not to be,
# > that is the question.

# Custom predicate: indent only long lines
def long_lines(line):
    return len(line.strip()) > 10

text = "short\nthis is a longer line\nhi"
result = textwrap.indent(text, '>>> ', long_lines)
# 'short\n>>> this is a longer line\nhi'

# All parameters
textwrap.indent(
    text,                        # Text to indent
    prefix,                      # String to prepend
    predicate=None               # Function(line) -> bool (default: non-empty lines)
)
```

---

## TEXTWRAPPER CLASS

### Class Overview

**Purpose**: Reusable wrapper object for efficient batch text processing

```python
import textwrap

# Create wrapper with configuration
wrapper = textwrap.TextWrapper(
    width=40,
    initial_indent="  ",
    subsequent_indent="    "
)

# Reuse for multiple texts
text1 = "First paragraph to wrap."
text2 = "Second paragraph to wrap."

lines1 = wrapper.wrap(text1)
lines2 = wrapper.wrap(text2)

# Modify settings between uses
wrapper.width = 60
wrapper.initial_indent = ""
lines3 = wrapper.wrap("Third paragraph with new settings.")

# Why use TextWrapper:
# - More efficient for processing many texts
# - Can change settings without recreating
# - Direct attribute access for customization
```

### TextWrapper Attributes

#### WIDTH
```python
# (default: 70) Maximum line length
wrapper = textwrap.TextWrapper(width=50)
wrapper.width = 60  # Can modify directly
```

#### EXPAND_TABS
```python
# (default: True) Convert tabs to spaces
wrapper = textwrap.TextWrapper(expand_tabs=True, tabsize=4)
text = "hello\tworld"  # → "hello    world" (then wrapped)
```

#### TABSIZE
```python
# (default: 8) Tab expansion width
wrapper = textwrap.TextWrapper(expand_tabs=True, tabsize=4)
```

#### REPLACE_WHITESPACE
```python
# (default: True) Replace whitespace with single space
wrapper = textwrap.TextWrapper(replace_whitespace=True)
# "hello\n\nworld" → "hello world"
# "hello\tworld" → "hello world"
```

#### DROP_WHITESPACE
```python
# (default: True) Remove leading/trailing whitespace per line
wrapper = textwrap.TextWrapper(drop_whitespace=True)
```

#### INITIAL_INDENT
```python
# (default: '') Prefix for first line
wrapper = textwrap.TextWrapper(initial_indent="  • ")
```

#### SUBSEQUENT_INDENT
```python
# (default: '') Prefix for all lines except first
wrapper = textwrap.TextWrapper(
    initial_indent="Question: ",
    subsequent_indent="          "
)
```

#### FIX_SENTENCE_ENDINGS
```python
# (default: False) Ensure two spaces after sentence endings
wrapper = textwrap.TextWrapper(fix_sentence_endings=True)
# "Hello. World." → "Hello.  World." (two spaces)
# Only works for English: lowercase + [.!?] + optional quote + space
```

#### BREAK_LONG_WORDS
```python
# (default: True) Break words longer than width
wrapper = textwrap.TextWrapper(width=10, break_long_words=True)
# "supercalifragilisticexpialidocious" → breaks mid-word

wrapper = textwrap.TextWrapper(width=10, break_long_words=False)
# "supercalifragilisticexpialidocious" → line exceeds width
```

#### BREAK_ON_HYPHENS
```python
# (default: True) Break compound words at hyphens
wrapper = textwrap.TextWrapper(break_on_hyphens=True)
# "long-compound-word-here" → can break at any hyphen

wrapper = textwrap.TextWrapper(break_on_hyphens=False)
# "long-compound-word-here" → treated as single word
```

#### MAX_LINES
```python
# (default: None) Limit output lines
wrapper = textwrap.TextWrapper(width=20, max_lines=3, placeholder="...")
long_text = "Very long text that goes on and on and on"
# Result: exactly 3 lines with "..." at end
```

#### PLACEHOLDER
```python
# (default: ' [...]') Truncation indicator
wrapper = textwrap.TextWrapper(
    width=30,
    max_lines=2,
    placeholder="... (more)"
)
```

### TextWrapper Methods

#### WRAP METHOD
```python
wrapper = textwrap.TextWrapper(width=30)
text = "This is a sample paragraph for wrapping."
lines = wrapper.wrap(text)
# Returns: ['This is a sample paragraph', 'for wrapping.']
```

#### FILL METHOD
```python
wrapper = textwrap.TextWrapper(width=30)
text = "This is a sample paragraph for wrapping."
result = wrapper.fill(text)
# Returns: "This is a sample paragraph\nfor wrapping."
```

---

## COMMON PATTERNS & USE CASES

### Pattern 1: Format Help Text
```python
import textwrap

def print_help():
    help_text = """\
    Usage: myprogram [OPTIONS] FILE
    
    Process FILE with various options.
    
    Options:
      -h, --help      Show this help message
      -v, --verbose   Enable verbose output
      -o, --output    Specify output file
    """
    print(textwrap.dedent(help_text))

print_help()
```

### Pattern 2: Format Error Messages
```python
import textwrap

def format_error(error_msg, width=60):
    return textwrap.fill(
        f"ERROR: {error_msg}",
        width=width,
        initial_indent="",
        subsequent_indent="       "
    )

print(format_error("File not found in the specified directory location"))
# ERROR: File not found in the specified directory
#        location
```

### Pattern 3: Bullet Lists
```python
import textwrap

def format_list(items, width=50):
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent="  • ",
        subsequent_indent="    "
    )
    for item in items:
        print(wrapper.fill(item))

items = [
    "First item with a long description that needs wrapping",
    "Second item",
    "Third item also has a very long description"
]
format_list(items)
```

### Pattern 4: Comment Code Block
```python
import textwrap

def comment_out(code):
    return textwrap.indent(code, '# ')

code = """def hello():
    print("world")
    return True"""

print(comment_out(code))
# # def hello():
# #     print("world")
# #     return True
```

### Pattern 5: Format Console Output
```python
import textwrap

class ConsoleFormatter:
    def __init__(self, width=70):
        self.wrapper = textwrap.TextWrapper(width=width)
    
    def header(self, text):
        border = "=" * self.wrapper.width
        centered = text.center(self.wrapper.width)
        return f"{border}\n{centered}\n{border}"
    
    def paragraph(self, text):
        return self.wrapper.fill(text)
    
    def indent(self, text, level=1):
        prefix = "  " * level
        return textwrap.indent(text, prefix)

fmt = ConsoleFormatter(width=50)
print(fmt.header("Welcome"))
print(fmt.paragraph("This is a very long welcome message that needs to be wrapped properly."))
```

### Pattern 6: Truncate Long Messages
```python
import textwrap

def preview_text(text, max_length=50):
    return textwrap.shorten(text, width=max_length, placeholder="...")

notification = "You have received a new message from John about the project deadline"
print(preview_text(notification, 40))
# You have received a new message from...
```

### Pattern 7: Format Docstrings
```python
import textwrap

def clean_docstring(func):
    """Remove leading indentation from docstring"""
    if func.__doc__:
        func.__doc__ = textwrap.dedent(func.__doc__).strip()
    return func

@clean_docstring
def example():
    """
    This is a docstring
    with multiple lines
    and indentation
    """
    pass

print(example.__doc__)
# This is a docstring
# with multiple lines
# and indentation
```

### Pattern 8: Display Menu
```python
import textwrap

def display_menu(title, options, width=60):
    wrapper = textwrap.TextWrapper(
        width=width - 4,  # Account for borders
        initial_indent="  ",
        subsequent_indent="  "
    )
    
    border = "+" + "-" * (width - 2) + "+"
    title_line = f"| {title.center(width - 4)} |"
    
    print(border)
    print(title_line)
    print(border)
    
    for num, option in enumerate(options, 1):
        formatted = wrapper.fill(f"{num}. {option}")
        for line in formatted.split('\n'):
            print(f"| {line.ljust(width - 4)} |")
    
    print(border)

display_menu("Main Menu", [
    "Add new student record",
    "Search for existing student",
    "Display all students in the system",
    "Exit program"
])
```

### Pattern 9: Quote Text
```python
import textwrap

def quote_text(text, width=60):
    wrapper = textwrap.TextWrapper(
        width=width - 2,  # Account for prefix
        initial_indent="> ",
        subsequent_indent="> "
    )
    return wrapper.fill(text)

quote = "To be or not to be, that is the question whether tis nobler"
print(quote_text(quote, width=40))
# > To be or not to be, that is the
# > question whether tis nobler
```

### Pattern 10: Log Formatting
```python
import textwrap
from datetime import datetime

def format_log_entry(level, message, width=80):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prefix = f"[{timestamp}] {level}: "
    
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent=prefix,
        subsequent_indent=" " * len(prefix)
    )
    
    return wrapper.fill(message)

print(format_log_entry("ERROR", "Database connection failed after multiple retry attempts", width=60))
# [2025-12-09 14:30:45] ERROR: Database connection failed
#                                after multiple retry
#                                attempts
```

---

## PARAMETER COMBINATIONS

### Combination 1: Hanging Indent
```python
wrapper = textwrap.TextWrapper(
    width=50,
    initial_indent="",
    subsequent_indent="    "
)
# First line flush left, subsequent lines indented
```

### Combination 2: Block Quote
```python
wrapper = textwrap.TextWrapper(
    width=50,
    initial_indent="  | ",
    subsequent_indent="  | "
)
# All lines prefixed with quote marker
```

### Combination 3: Numbered List
```python
for i, item in enumerate(items, 1):
    wrapper = textwrap.TextWrapper(
        width=50,
        initial_indent=f"  {i}. ",
        subsequent_indent="     "
    )
    print(wrapper.fill(item))
```

### Combination 4: Preserve Long Words
```python
wrapper = textwrap.TextWrapper(
    width=30,
    break_long_words=False,
    break_on_hyphens=False
)
# URLs and technical terms stay intact
```

### Combination 5: Strict Truncation
```python
wrapper = textwrap.TextWrapper(
    width=50,
    max_lines=3,
    placeholder="... [Read More]"
)
# Exactly 3 lines with custom truncation indicator
```

---

## PRACTICAL SCENARIOS

### Scenario 1: Terminal Output Formatting
```python
import textwrap
import shutil

# Get terminal width
terminal_width = shutil.get_terminal_size().columns

wrapper = textwrap.TextWrapper(width=terminal_width - 5)

def print_wrapped(text):
    print(wrapper.fill(text))

print_wrapped("This text will automatically fit your terminal width.")
```

### Scenario 2: Email Formatting
```python
import textwrap

def format_email(subject, body, width=72):
    """Format email with proper line wrapping"""
    result = []
    result.append(f"Subject: {subject}")
    result.append("")
    
    wrapper = textwrap.TextWrapper(width=width)
    paragraphs = body.split('\n\n')
    
    for para in paragraphs:
        result.append(wrapper.fill(para))
        result.append("")
    
    return '\n'.join(result)

email = format_email(
    "Meeting Update",
    "The meeting has been rescheduled to next week.\n\nPlease confirm your attendance."
)
print(email)
```

### Scenario 3: Code Documentation
```python
import textwrap

def format_docstring(description, params, returns, width=70):
    doc = []
    
    # Description
    wrapper = textwrap.TextWrapper(width=width)
    doc.append(wrapper.fill(description))
    doc.append("")
    
    # Parameters
    if params:
        doc.append("Parameters:")
        param_wrapper = textwrap.TextWrapper(
            width=width,
            initial_indent="    ",
            subsequent_indent="        "
        )
        for name, desc in params.items():
            doc.append(param_wrapper.fill(f"{name}: {desc}"))
    
    # Returns
    if returns:
        doc.append("")
        doc.append("Returns:")
        return_wrapper = textwrap.TextWrapper(
            width=width,
            initial_indent="    ",
            subsequent_indent="    "
        )
        doc.append(return_wrapper.fill(returns))
    
    return '\n'.join(doc)

result = format_docstring(
    "Calculate the total price including tax and shipping",
    {"price": "Base price of item", "tax_rate": "Tax rate as decimal"},
    "Final total price as float"
)
print(result)
```

### Scenario 4: Config File Comments
```python
import textwrap

def add_config_comment(key, value, description, width=70):
    """Add commented description above config line"""
    comment_wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent="# ",
        subsequent_indent="# "
    )
    
    comment = comment_wrapper.fill(description)
    config_line = f"{key} = {value}"
    
    return f"{comment}\n{config_line}"

print(add_config_comment(
    "MAX_RETRIES",
    "3",
    "Maximum number of retry attempts before failing. Set to 0 to disable retries."
))
```

---

## EDGE CASES & GOTCHAS

### Edge Case 1: Empty String
```python
textwrap.wrap("")                    # → []
textwrap.fill("")                    # → ""
textwrap.shorten("", width=10)       # → ""
textwrap.dedent("")                  # → ""
textwrap.indent("", "  ")            # → ""
```

### Edge Case 2: Very Small Width
```python
# width < word length
textwrap.wrap("hello", width=3)      # → ['hel', 'lo']
textwrap.wrap("hello", width=3, break_long_words=False)  # → ['hello']

# width < placeholder
textwrap.shorten("hello", width=5, placeholder="...")     # → "..."
```

### Edge Case 3: Only Whitespace
```python
text = "   \n\n   "
textwrap.wrap(text)                  # → []
textwrap.fill(text)                  # → ""
textwrap.dedent(text)                # → "   \n\n   "
textwrap.indent(text, "> ")          # → "   \n\n   " (default predicate skips)
textwrap.indent(text, "> ", lambda l: True)  # → ">    \n> \n>    "
```

### Edge Case 4: Tabs vs Spaces in Dedent
```python
# dedent() treats tabs and spaces as different
mixed = "\thello\n  hello"
textwrap.dedent(mixed)               # → "\thello\n  hello" (no common whitespace)

same_type = "  hello\n  world"
textwrap.dedent(same_type)           # → "hello\nworld" (removes 2 spaces)
```

### Edge Case 5: Replace Whitespace Side Effects
```python
text = "hello\nworld"
wrapper = textwrap.TextWrapper(replace_whitespace=False, width=5)
# May produce strange output with newlines mid-line
```

### Edge Case 6: Fix Sentence Endings Limitations
```python
# Cannot detect abbreviations
text = "Dr. Smith went to the store. He bought milk."
wrapper = textwrap.TextWrapper(fix_sentence_endings=True, width=50)
# May incorrectly add two spaces after "Dr."
```

### Edge Case 7: Max Lines Behavior
```python
wrapper = textwrap.TextWrapper(width=20, max_lines=2, placeholder="...")
text = "word " * 20

result = wrapper.fill(text)
# Last line includes placeholder and fits within width
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: TypeError with Non-String Input
```python
# WRONG
textwrap.wrap(12345)                 # TypeError

# RIGHT
textwrap.wrap(str(12345))
textwrap.wrap("12345")
```

### Error 2: Forgetting to Import
```python
# WRONG
wrap("text", width=50)               # NameError

# RIGHT
import textwrap
textwrap.wrap("text", width=50)

# OR
from textwrap import wrap
wrap("text", width=50)
```

### Error 3: Mutating Original String
```python
# textwrap functions return NEW strings, don't modify originals
text = "hello world"
textwrap.wrap(text, width=5)
print(text)                          # → "hello world" (unchanged)

# Must capture return value
lines = textwrap.wrap(text, width=5)
```

### Error 4: Wrong Width Calculation
```python
# WRONG - forgetting prefix length
wrapper = textwrap.TextWrapper(
    width=50,
    initial_indent="  • "            # 4 chars, leaves 46 for text
)

# RIGHT - account for prefix if needed
prefix_len = len("  • ")
wrapper = textwrap.TextWrapper(
    width=50,
    initial_indent="  • "
)
# TextWrapper automatically accounts for indent in width
```

### Error 5: Mixing wrap() and fill()
```python
# WRONG - wrap() returns list, not string
print(textwrap.wrap("hello world", width=5))  # → ['hello', 'world']

# RIGHT - use fill() for string output
print(textwrap.fill("hello world", width=5))  # → "hello\nworld"

# OR - join wrap() result
print('\n'.join(textwrap.wrap("hello world", width=5)))
```

### Error 6: Shorten Width Too Small
```python
# WRONG - width smaller than placeholder
textwrap.shorten("hello", width=5, placeholder=" [...]")  # ValueError

# RIGHT - ensure width >= len(placeholder)
textwrap.shorten("hello", width=10, placeholder=" [...]")
textwrap.shorten("hello", width=5, placeholder="...")     # OK
```

---

## COMPARISON WITH STRING METHODS

```python
# textwrap.wrap() vs str.split()
text = "hello world this is a test"
str.split()                          # → ['hello', 'world', 'this', 'is', 'a', 'test']
textwrap.wrap(text, width=10)        # → ['hello', 'world this', 'is a test']
# wrap() respects width, split() only separates on whitespace

# textwrap.dedent() vs str.lstrip()
text = "    hello\n    world"
text.lstrip()                        # → "hello\n    world" (only first line)
textwrap.dedent(text)                # → "hello\nworld" (all lines)

# textwrap.indent() vs string concatenation
lines = "hello\nworld"
"  " + lines                         # → "  hello\nworld" (only first line)
textwrap.indent(lines, "  ")         # → "  hello\n  world" (all lines)

# textwrap.shorten() vs slicing
text = "hello world this is a test"
text[:15]                            # → "hello world thi" (cuts mid-word)
textwrap.shorten(text, width=15)     # → "hello [...]" (respects word boundaries)
```

---

## PERFORMANCE CONSIDERATIONS

```python
# For single text: use convenience functions
result = textwrap.fill(text, width=50)

# For many texts: use TextWrapper instance (more efficient)
wrapper = textwrap.TextWrapper(width=50)
results = [wrapper.fill(text) for text in many_texts]

# Avoid recreating wrapper in loops
# SLOW
for text in texts:
    result = textwrap.fill(text, width=50)  # Creates new wrapper each time

# FAST
wrapper = textwrap.TextWrapper(width=50)
for text in texts:
    result = wrapper.fill(text)              # Reuses wrapper
```

---

## REFERENCES & RELATED MODULES

- **Official Documentation**: https://docs.python.org/3/library/textwrap.html
- **Source Code**: Lib/textwrap.py
- **Related String Methods**: `str.split()`, `str.splitlines()`, `str.join()`, `str.strip()`
- **Related Modules**: 
  - `shutil.get_terminal_size()` - Get terminal dimensions
  - `string` - String constants and utilities
  - `re` - Regular expressions for advanced text processing

---

## VERSION HISTORY

- **Python 3.3**: Added `indent()` function and `tabsize` parameter
- **Python 3.4**: Added `shorten()` function, `max_lines` and `placeholder` parameters
- **Python 2.3**: Module introduced

---

## QUICK DECISION GUIDE

**Use `wrap()`** when you need a list of lines
**Use `fill()`** when you need a single string with newlines
**Use `shorten()`** when you need to truncate long text
**Use `dedent()`** when cleaning indented blocks (docstrings, multiline strings)
**Use `indent()`** when adding prefixes to lines (quoting, commenting)
**Use `TextWrapper`** when processing multiple texts with same settings

