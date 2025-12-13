# TEXT_FORMATTING

## Core Definition
**Text Formatting** encompasses all methods and techniques for controlling output display, string representation, alignment, precision, and visual presentation in Python. Includes string formatting syntax, f-strings, format specifications, and alignment techniques.

**Tags**: #formatting #strings #output #display #alignment #precision

---

## COMPLETE TEXT FORMATTING QUICK REFERENCE

### FORMATTING METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# F-STRING FORMATTING (Python 3.6+)
# ═══════════════════════════════════════════════════════════════════════════
f"{var}"                     # Variable | Inline interpolation | Returns string with value
f"{expr}"                    # Expression | Evaluate and insert | Returns string with result
f"{var!r}"                   # Variable | repr() representation | Returns quoted/escaped string
f"{var!s}"                   # Variable | str() representation | Returns string conversion
f"{var!a}"                   # Variable | ascii() representation | Returns ASCII-only string
f"{var=}"                    # Variable (3.8+) | Debug format | Returns "var=value"
f"{expr=}"                   # Expression (3.8+) | Debug expression | Returns "expr=result"
f"{{var}}"                   # Literal braces | Escape braces | Returns "{var}" literally

# ═══════════════════════════════════════════════════════════════════════════
# FORMAT SPECIFICATION MINI-LANGUAGE
# ═══════════════════════════════════════════════════════════════════════════
f"{var:spec}"                # Variable + spec | Apply format spec | Returns formatted string
f"{var:width}"               # Variable + int | Minimum field width | Returns padded string
f"{var:<width}"              # Variable | Left align in width | Returns left-aligned string
f"{var:>width}"              # Variable | Right align in width | Returns right-aligned string
f"{var:^width}"              # Variable | Center in width | Returns centered string
f"{var:=width}"              # Number | Padding after sign | Returns sign + padding + number
f"{var:0width}"              # Number | Zero-padding | Returns zero-padded number
f"{var:+}"                   # Number | Force sign display | Returns +/- prefixed number
f"{var:-}"                   # Number | Sign only for negative | Returns number with - if negative
f"{var: }"                   # Number | Space for positive | Returns space/- prefixed number

# ═══════════════════════════════════════════════════════════════════════════
# NUMERIC FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
f"{num:d}"                   # Integer | Decimal format | Returns integer as string
f"{num:b}"                   # Integer | Binary format | Returns binary representation
f"{num:o}"                   # Integer | Octal format | Returns octal representation
f"{num:x}"                   # Integer | Hex lowercase | Returns hex (lowercase)
f"{num:X}"                   # Integer | Hex uppercase | Returns hex (uppercase)
f"{num:#b}"                  # Integer | Binary with prefix | Returns "0b..." format
f"{num:#o}"                  # Integer | Octal with prefix | Returns "0o..." format
f"{num:#x}"                  # Integer | Hex with prefix | Returns "0x..." format
f"{num:#X}"                  # Integer | Hex with prefix (upper) | Returns "0X..." format

# ═══════════════════════════════════════════════════════════════════════════
# FLOATING POINT FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
f"{float:.nf}"               # Float + precision | Fixed decimal places | Returns float with n decimals
f"{float:f}"                 # Float | Default fixed-point | Returns float with 6 decimals
f"{float:.2f}"               # Float | Two decimal places | Returns float with 2 decimals
f"{float:e}"                 # Float | Scientific notation | Returns exponential format
f"{float:.2e}"               # Float | Scientific with precision | Returns exponential with 2 decimals
f"{float:E}"                 # Float | Scientific uppercase | Returns exponential with uppercase E
f"{float:g}"                 # Float | General format | Returns shortest representation
f"{float:G}"                 # Float | General uppercase | Returns shortest with uppercase E
f"{float:%}"                 # Float | Percentage | Returns float * 100 with % sign
f"{float:.2%}"               # Float | Percentage with precision | Returns percentage with 2 decimals

# ═══════════════════════════════════════════════════════════════════════════
# THOUSAND SEPARATORS
# ═══════════════════════════════════════════════════════════════════════════
f"{num:,}"                   # Number | Comma separator | Returns number with commas
f"{num:_}"                   # Number (3.6+) | Underscore separator | Returns number with underscores
f"{num:,.2f}"                # Float | Comma + precision | Returns formatted float with commas
f"{num:_d}"                  # Integer | Underscore separator | Returns integer with underscores

# ═══════════════════════════════════════════════════════════════════════════
# ALIGNMENT WITH FILL CHARACTERS
# ═══════════════════════════════════════════════════════════════════════════
f"{var:*<width}"             # Variable | Left align with * | Returns left-aligned with * fill
f"{var:*>width}"             # Variable | Right align with * | Returns right-aligned with * fill
f"{var:*^width}"             # Variable | Center with * | Returns centered with * fill
f"{var:=>width}"             # Number | Align after sign with = | Returns sign + = fill + number
f"{var:0>width}"             # Variable | Right align with zeros | Returns zero-padded string

# ═══════════════════════════════════════════════════════════════════════════
# .FORMAT() METHOD
# ═══════════════════════════════════════════════════════════════════════════
"{}".format(val)             # Positional | Single replacement | Returns formatted string
"{} {}".format(a, b)         # Positional | Multiple replacements | Returns formatted string
"{0} {1}".format(a, b)       # Indexed | Positional by index | Returns formatted string
"{1} {0}".format(a, b)       # Indexed | Reversed order | Returns formatted string
"{0} {0}".format(a)          # Indexed | Repeated value | Returns formatted string
"{name}".format(name=val)    # Named | Keyword replacement | Returns formatted string
"{x} {y}".format(x=1, y=2)   # Named | Multiple keywords | Returns formatted string
"{0.attr}".format(obj)       # Attribute | Access object attribute | Returns attribute value
"{0[key]}".format(dict)      # Item | Access dict/list item | Returns item value
"{0[0]}".format(list)        # Index | Access by index | Returns indexed item
"{val:spec}".format(val=x)   # Named + spec | Named with format spec | Returns formatted value

# ═══════════════════════════════════════════════════════════════════════════
# %-FORMATTING (OLD STYLE)
# ═══════════════════════════════════════════════════════════════════════════
"%s" % val                   # String | String substitution | Returns string
"%d" % val                   # Integer | Integer substitution | Returns integer string
"%i" % val                   # Integer | Integer substitution | Returns integer string
"%f" % val                   # Float | Float substitution | Returns float string
"%e" % val                   # Float | Exponential notation | Returns scientific notation
"%g" % val                   # Float | General format | Returns shortest representation
"%x" % val                   # Integer | Hex lowercase | Returns hex string
"%X" % val                   # Integer | Hex uppercase | Returns hex string (upper)
"%o" % val                   # Integer | Octal | Returns octal string
"%c" % val                   # Integer | Character | Returns character from code
"%r" % val                   # Any | repr() format | Returns repr string
"%.nf" % val                 # Float | Precision | Returns float with n decimals
"%nd" % val                  # Integer | Width | Returns padded integer
"%0nd" % val                 # Integer | Zero-padded width | Returns zero-padded integer
"%(name)s" % dict            # Dict | Named substitution | Returns value from dict

# ═══════════════════════════════════════════════════════════════════════════
# STRING TEMPLATE (string.Template)
# ═══════════════════════════════════════════════════════════════════════════
Template("$var")             # Template | Simple substitution | Returns string with value
Template("${var}")           # Template | Braced substitution | Returns string with value
Template("$var").substitute(var=val)  # Template | Safe substitution | Returns formatted string
Template("$var").safe_substitute(var=val)  # Template | Ignore missing | Returns partial format

# ═══════════════════════════════════════════════════════════════════════════
# PRINT FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
print(val)                   # Value | Default print | Outputs to stdout with newline
print(val, end='')           # Value | No newline | Outputs without trailing newline
print(val, end='...')        # Value | Custom ending | Outputs with custom ending
print(a, b, c)               # Multiple | Space separated | Outputs multiple values
print(a, b, sep=', ')        # Multiple | Custom separator | Outputs with custom separator
print(val, file=f)           # Value | To file | Outputs to file object
print(val, flush=True)       # Value | Force flush | Outputs and flushes buffer

# ═══════════════════════════════════════════════════════════════════════════
# DATETIME FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
f"{dt:%Y}"                   # datetime | Year 4-digit | Returns "2025"
f"{dt:%y}"                   # datetime | Year 2-digit | Returns "25"
f"{dt:%m}"                   # datetime | Month 2-digit | Returns "01" to "12"
f"{dt:%B}"                   # datetime | Month full name | Returns "January"
f"{dt:%b}"                   # datetime | Month abbrev | Returns "Jan"
f"{dt:%d}"                   # datetime | Day of month | Returns "01" to "31"
f"{dt:%A}"                   # datetime | Weekday full | Returns "Monday"
f"{dt:%a}"                   # datetime | Weekday abbrev | Returns "Mon"
f"{dt:%H}"                   # datetime | Hour 24-hour | Returns "00" to "23"
f"{dt:%I}"                   # datetime | Hour 12-hour | Returns "01" to "12"
f"{dt:%M}"                   # datetime | Minute | Returns "00" to "59"
f"{dt:%S}"                   # datetime | Second | Returns "00" to "59"
f"{dt:%p}"                   # datetime | AM/PM | Returns "AM" or "PM"
f"{dt:%Y-%m-%d}"             # datetime | ISO date | Returns "2025-01-15"
f"{dt:%B %d, %Y}"            # datetime | Long date | Returns "January 15, 2025"
f"{dt:%I:%M %p}"             # datetime | 12-hour time | Returns "03:45 PM"
dt.strftime("%Y-%m-%d")      # datetime | Format method | Returns formatted date string

# ═══════════════════════════════════════════════════════════════════════════
# STRING ALIGNMENT METHODS
# ═══════════════════════════════════════════════════════════════════════════
str.center(width)            # String | Center in width | Returns centered string with spaces
str.center(width, fill)      # String | Center with fill char | Returns centered string with fill
str.ljust(width)             # String | Left justify | Returns left-aligned string
str.ljust(width, fill)       # String | Left justify with fill | Returns left-aligned with fill
str.rjust(width)             # String | Right justify | Returns right-aligned string
str.rjust(width, fill)       # String | Right justify with fill | Returns right-aligned with fill
str.zfill(width)             # String | Zero-pad left | Returns zero-padded string
str.expandtabs()             # String | Expand tabs to spaces | Returns string with spaces
str.expandtabs(tabsize)      # String | Custom tab size | Returns string with custom spacing

# ═══════════════════════════════════════════════════════════════════════════
# SPECIAL CHARACTERS & ESCAPE SEQUENCES
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
\xhh                         # Escape | Hex value | Character from hex code
\ooo                         # Escape | Octal value | Character from octal code
\uhhhh                       # Escape | Unicode 16-bit | Unicode character (4 hex digits)
\Uhhhhhhhh                   # Escape | Unicode 32-bit | Unicode character (8 hex digits)
\N{name}                     # Escape | Named Unicode | Unicode character by name

# ═══════════════════════════════════════════════════════════════════════════
# UNICODE & RAW STRINGS
# ═══════════════════════════════════════════════════════════════════════════
r"text"                      # Raw string | No escape processing | Returns literal string
R"text"                      # Raw string | No escape processing | Returns literal string
u"text"                      # Unicode string | Explicit Unicode (Py2) | Returns Unicode string
f"text"                      # F-string | Formatted string | Returns formatted string
fr"text"                     # Raw f-string | Raw + formatted | Returns raw formatted string
rf"text"                     # Raw f-string | Raw + formatted | Returns raw formatted string

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM FORMAT SPECIFIERS (__format__ method)
# ═══════════════════════════════════════════════════════════════════════════
class.__format__(self, spec) # Object | Custom formatting | Returns formatted object string
format(obj, spec)            # Object + spec | Apply format spec | Returns formatted string
f"{obj:spec}"                # Object + spec | F-string format | Returns custom formatted object

# ═══════════════════════════════════════════════════════════════════════════
# TEXTWRAP MODULE - Text Wrapping & Filling
# ═══════════════════════════════════════════════════════════════════════════
textwrap.wrap(text, width)   # Text + width | Wrap to width | Returns list of lines
textwrap.wrap(text, width, break_long_words=False)  # Text | Wrap no word break | Returns list
textwrap.wrap(text, width, break_on_hyphens=False)  # Text | Don't break on hyphens | Returns list
textwrap.wrap(text, width, initial_indent=str)  # Text | Indent first line | Returns list
textwrap.wrap(text, width, subsequent_indent=str)  # Text | Indent other lines | Returns list
textwrap.wrap(text, width, expand_tabs=True)  # Text | Expand tabs first | Returns list
textwrap.wrap(text, width, replace_whitespace=True)  # Text | Normalize whitespace | Returns list
textwrap.wrap(text, width, drop_whitespace=True)  # Text | Drop leading/trailing | Returns list
textwrap.wrap(text, width, max_lines=n)  # Text | Limit lines | Returns list with max lines
textwrap.wrap(text, width, placeholder='...')  # Text | Truncation indicator | Returns list

textwrap.fill(text, width)   # Text + width | Wrap and join | Returns single string
textwrap.fill(text, width, **kwargs)  # Text | Same as wrap options | Returns wrapped string

textwrap.shorten(text, width)  # Text + width | Shorten to fit | Returns truncated string
textwrap.shorten(text, width, placeholder='...')  # Text | Custom placeholder | Returns string

textwrap.dedent(text)        # Text | Remove common indentation | Returns dedented string
textwrap.indent(text, prefix)  # Text + prefix | Add prefix to lines | Returns indented string
textwrap.indent(text, prefix, predicate)  # Text | Conditional indent | Returns indented string

TextWrapper(width)           # Width | Create wrapper object | Returns TextWrapper instance
TextWrapper.wrap(text)       # Text | Wrap using config | Returns list of lines
TextWrapper.fill(text)       # Text | Fill using config | Returns single string

# ═══════════════════════════════════════════════════════════════════════════
# PPRINT MODULE - Pretty Printing
# ═══════════════════════════════════════════════════════════════════════════
pprint.pprint(obj)           # Object | Pretty print | Outputs formatted to stdout
pprint.pprint(obj, stream=f)  # Object | Print to stream | Outputs to file object
pprint.pprint(obj, indent=n)  # Object | Indentation level | Outputs with indent
pprint.pprint(obj, width=n)  # Object | Max width | Outputs within width
pprint.pprint(obj, depth=n)  # Object | Max nesting depth | Outputs with depth limit
pprint.pprint(obj, compact=True)  # Object | Compact format | Outputs compactly
pprint.pprint(obj, sort_dicts=True)  # Object | Sort dict keys | Outputs sorted
pprint.pprint(obj, underscore_numbers=True)  # Object (3.10+) | Underscore separator | Outputs with _

pprint.pformat(obj)          # Object | Format as string | Returns formatted string
pprint.pformat(obj, **kwargs)  # Object | Same as pprint options | Returns formatted string

pprint.pp(obj)               # Object (3.8+) | Pretty print shorthand | Outputs formatted
pprint.pp(obj, **kwargs)     # Object | Same options as pprint | Outputs formatted

pprint.isreadable(obj)       # Object | Check if readable | Returns True/False
pprint.isrecursive(obj)      # Object | Check if recursive | Returns True/False

PrettyPrinter(indent)        # Indent | Create printer object | Returns PrettyPrinter instance
PrettyPrinter.pprint(obj)    # Object | Print with config | Outputs formatted
PrettyPrinter.pformat(obj)   # Object | Format with config | Returns formatted string

pprint.saferepr(obj)         # Object | Safe representation | Returns repr string

# ═══════════════════════════════════════════════════════════════════════════
# REPRLIB MODULE - Controlled Repr Output
# ═══════════════════════════════════════════════════════════════════════════
reprlib.repr(obj)            # Object | Limited repr | Returns abbreviated repr string
Repr()                       # None | Create custom repr | Returns Repr instance
Repr.repr(obj)               # Object | Custom repr | Returns repr string
Repr.maxlevel                # Attribute | Max recursion depth | Controls nesting limit
Repr.maxdict                 # Attribute | Max dict items | Controls dict display
Repr.maxlist                 # Attribute | Max list items | Controls list display
Repr.maxstring               # Attribute | Max string length | Controls string display
Repr.maxlong                 # Attribute | Max long int digits | Controls number display
Repr.maxother                # Attribute | Max other items | Controls other types
Repr.maxtuple                # Attribute | Max tuple items | Controls tuple display
Repr.maxset                  # Attribute | Max set items | Controls set display
Repr.maxfrozenset            # Attribute | Max frozenset items | Controls frozenset display
Repr.maxdeque                # Attribute | Max deque items | Controls deque display
Repr.maxarray                # Attribute | Max array items | Controls array display

reprlib.recursive_repr(fillvalue)  # Fill value | Decorator for recursive | Returns decorator

# ═══════════════════════════════════════════════════════════════════════════
# STRING.FORMATTER CLASS - Custom Formatters
# ═══════════════════════════════════════════════════════════════════════════
string.Formatter()           # None | Create formatter | Returns Formatter instance
Formatter.format(fmt, *args, **kwargs)  # Format string | Format with args | Returns formatted string
Formatter.vformat(fmt, args, kwargs)  # Format + sequences | Format with sequences | Returns formatted
Formatter.parse(fmt)         # Format string | Parse format string | Returns iterator of tuples
Formatter.get_field(field, args, kwargs)  # Field | Get field value | Returns (value, key) tuple
Formatter.get_value(key, args, kwargs)  # Key | Get value by key | Returns value
Formatter.check_unused_args(used, args, kwargs)  # Args | Check unused | Raises if unused
Formatter.format_field(value, spec)  # Value + spec | Format field | Returns formatted string
Formatter.convert_field(value, conversion)  # Value + conversion | Apply conversion | Returns converted

# ═══════════════════════════════════════════════════════════════════════════
# LOCALE MODULE - Locale-Specific Formatting
# ═══════════════════════════════════════════════════════════════════════════
locale.setlocale(category, locale)  # Category + locale | Set locale | Returns locale string
locale.format_string(fmt, val, grouping=False)  # Format + value | Format with locale | Returns string
locale.format_string(fmt, val, grouping=True)  # Format + value | Format with thousands | Returns string
locale.currency(val)         # Number | Format as currency | Returns currency string
locale.currency(val, symbol=True)  # Number | With currency symbol | Returns formatted currency
locale.currency(val, grouping=True)  # Number | With thousands separator | Returns formatted currency
locale.currency(val, international=True)  # Number | International format | Returns ISO currency
locale.str(float)            # Float | Locale-aware string | Returns formatted number
locale.atof(string)          # String | Parse locale float | Returns float
locale.atoi(string)          # String | Parse locale int | Returns int
locale.localeconv()          # None | Get locale conventions | Returns dict of conventions
locale.nl_langinfo(option)   # Option | Get locale info | Returns locale information

# ═══════════════════════════════════════════════════════════════════════════
# BYTES FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
b"text"                      # Bytes literal | Byte string | Returns bytes object
b"%s" % val                  # Bytes format | Old-style bytes format | Returns bytes
b"%d" % val                  # Bytes format | Integer to bytes | Returns bytes
b"%.2f" % val                # Bytes format | Float to bytes | Returns bytes
bytes(string, encoding)      # String + encoding | Encode string | Returns bytes
bytes(iterable)              # Iterable of ints | Create from ints | Returns bytes
bytes(size)                  # Integer | Create zero-filled | Returns bytes of size
bytearray(source)            # Source | Mutable bytes | Returns bytearray
bytes.decode(encoding)       # Bytes + encoding | Decode to string | Returns string
bytes.decode(encoding, errors)  # Bytes | Decode with error handling | Returns string
bytes.hex()                  # Bytes | Convert to hex string | Returns hex string
bytes.hex(sep)               # Bytes | Hex with separator | Returns separated hex
bytes.hex(sep, bytes_per_sep)  # Bytes | Hex with spacing | Returns formatted hex
bytes.fromhex(string)        # Hex string | Create from hex | Returns bytes

# ═══════════════════════════════════════════════════════════════════════════
# UNICODE OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
unicodedata.normalize(form, string)  # Form + string | Normalize Unicode | Returns normalized string
unicodedata.normalize('NFC', s)  # String | Canonical composition | Returns NFC form
unicodedata.normalize('NFD', s)  # String | Canonical decomposition | Returns NFD form
unicodedata.normalize('NFKC', s)  # String | Compatibility composition | Returns NFKC form
unicodedata.normalize('NFKD', s)  # String | Compatibility decomposition | Returns NFKD form
unicodedata.name(char)       # Character | Get Unicode name | Returns name string
unicodedata.lookup(name)     # Name | Get char by name | Returns character
unicodedata.category(char)   # Character | Get category | Returns category code
unicodedata.east_asian_width(char)  # Character | Get East Asian width | Returns width code
unicodedata.bidirectional(char)  # Character | Get bidirectional class | Returns class code
unicodedata.combining(char)  # Character | Get combining class | Returns integer
unicodedata.decimal(char)    # Character | Get decimal value | Returns int or ValueError
unicodedata.digit(char)      # Character | Get digit value | Returns int or ValueError
unicodedata.numeric(char)    # Character | Get numeric value | Returns float or ValueError
unicodedata.is_normalized(form, string)  # Form + string | Check if normalized | Returns True/False

str.encode(encoding)         # String | Encode to bytes | Returns bytes
str.encode(encoding, errors='strict')  # String | Encode with error handling | Returns bytes
str.encode('utf-8')          # String | UTF-8 encoding | Returns bytes
str.encode('utf-16')         # String | UTF-16 encoding | Returns bytes
str.encode('utf-32')         # String | UTF-32 encoding | Returns bytes
str.encode('ascii')          # String | ASCII encoding | Returns bytes
str.encode('latin-1')        # String | Latin-1 encoding | Returns bytes
str.encode('cp1252')         # String | Windows-1252 encoding | Returns bytes

# ═══════════════════════════════════════════════════════════════════════════
# ANSI ESCAPE CODES - Terminal Colors & Formatting
# ═══════════════════════════════════════════════════════════════════════════
"\033[0m"                    # ANSI code | Reset all | Returns reset code
"\033[1m"                    # ANSI code | Bold | Returns bold code
"\033[2m"                    # ANSI code | Dim | Returns dim code
"\033[3m"                    # ANSI code | Italic | Returns italic code
"\033[4m"                    # ANSI code | Underline | Returns underline code
"\033[5m"                    # ANSI code | Blink | Returns blink code
"\033[7m"                    # ANSI code | Reverse | Returns reverse code
"\033[8m"                    # ANSI code | Hidden | Returns hidden code
"\033[9m"                    # ANSI code | Strikethrough | Returns strikethrough code

"\033[30m"                   # ANSI code | Black foreground | Returns black code
"\033[31m"                   # ANSI code | Red foreground | Returns red code
"\033[32m"                   # ANSI code | Green foreground | Returns green code
"\033[33m"                   # ANSI code | Yellow foreground | Returns yellow code
"\033[34m"                   # ANSI code | Blue foreground | Returns blue code
"\033[35m"                   # ANSI code | Magenta foreground | Returns magenta code
"\033[36m"                   # ANSI code | Cyan foreground | Returns cyan code
"\033[37m"                   # ANSI code | White foreground | Returns white code
"\033[90m"                   # ANSI code | Bright black (gray) | Returns gray code
"\033[91m"                   # ANSI code | Bright red | Returns bright red code
"\033[92m"                   # ANSI code | Bright green | Returns bright green code
"\033[93m"                   # ANSI code | Bright yellow | Returns bright yellow code
"\033[94m"                   # ANSI code | Bright blue | Returns bright blue code
"\033[95m"                   # ANSI code | Bright magenta | Returns bright magenta code
"\033[96m"                   # ANSI code | Bright cyan | Returns bright cyan code
"\033[97m"                   # ANSI code | Bright white | Returns bright white code

"\033[40m"                   # ANSI code | Black background | Returns black bg code
"\033[41m"                   # ANSI code | Red background | Returns red bg code
"\033[42m"                   # ANSI code | Green background | Returns green bg code
"\033[43m"                   # ANSI code | Yellow background | Returns yellow bg code
"\033[44m"                   # ANSI code | Blue background | Returns blue bg code
"\033[45m"                   # ANSI code | Magenta background | Returns magenta bg code
"\033[46m"                   # ANSI code | Cyan background | Returns cyan bg code
"\033[47m"                   # ANSI code | White background | Returns white bg code
"\033[100m"                  # ANSI code | Bright black bg | Returns gray bg code
"\033[101m"                  # ANSI code | Bright red bg | Returns bright red bg code
"\033[102m"                  # ANSI code | Bright green bg | Returns bright green bg code
"\033[103m"                  # ANSI code | Bright yellow bg | Returns bright yellow bg code
"\033[104m"                  # ANSI code | Bright blue bg | Returns bright blue bg code
"\033[105m"                  # ANSI code | Bright magenta bg | Returns bright magenta bg code
"\033[106m"                  # ANSI code | Bright cyan bg | Returns bright cyan bg code
"\033[107m"                  # ANSI code | Bright white bg | Returns bright white bg code

"\033[38;5;{n}m"             # ANSI code | 256 color foreground | Returns color code (0-255)
"\033[48;5;{n}m"             # ANSI code | 256 color background | Returns bg color code (0-255)
"\033[38;2;{r};{g};{b}m"     # ANSI code | RGB foreground | Returns RGB color code
"\033[48;2;{r};{g};{b}m"     # ANSI code | RGB background | Returns RGB bg code

"\033[nA"                    # ANSI code | Cursor up n lines | Moves cursor up
"\033[nB"                    # ANSI code | Cursor down n lines | Moves cursor down
"\033[nC"                    # ANSI code | Cursor forward n cols | Moves cursor right
"\033[nD"                    # ANSI code | Cursor back n cols | Moves cursor left
"\033[H"                     # ANSI code | Cursor home | Moves to top-left
"\033[{row};{col}H"          # ANSI code | Cursor position | Moves to position
"\033[2J"                    # ANSI code | Clear screen | Clears entire screen
"\033[K"                     # ANSI code | Clear line | Clears to end of line

# ═══════════════════════════════════════════════════════════════════════════
# ASCII ART & BOX DRAWING CHARACTERS
# ═══════════════════════════════════════════════════════════════════════════
"─"                          # Unicode U+2500 | Horizontal line | Box drawing
"│"                          # Unicode U+2502 | Vertical line | Box drawing
"┌"                          # Unicode U+250C | Top-left corner | Box drawing
"┐"                          # Unicode U+2510 | Top-right corner | Box drawing
"└"                          # Unicode U+2514 | Bottom-left corner | Box drawing
"┘"                          # Unicode U+2518 | Bottom-right corner | Box drawing
"├"                          # Unicode U+251C | Left T-junction | Box drawing
"┤"                          # Unicode U+2524 | Right T-junction | Box drawing
"┬"                          # Unicode U+252C | Top T-junction | Box drawing
"┴"                          # Unicode U+2534 | Bottom T-junction | Box drawing
"┼"                          # Unicode U+253C | Cross junction | Box drawing

"═"                          # Unicode U+2550 | Double horizontal | Box drawing
"║"                          # Unicode U+2551 | Double vertical | Box drawing
"╔"                          # Unicode U+2554 | Double top-left | Box drawing
"╗"                          # Unicode U+2557 | Double top-right | Box drawing
"╚"                          # Unicode U+255A | Double bottom-left | Box drawing
"╝"                          # Unicode U+255D | Double bottom-right | Box drawing
"╠"                          # Unicode U+2560 | Double left T | Box drawing
"╣"                          # Unicode U+2563 | Double right T | Box drawing
"╦"                          # Unicode U+2566 | Double top T | Box drawing
"╩"                          # Unicode U+2569 | Double bottom T | Box drawing
"╬"                          # Unicode U+256C | Double cross | Box drawing

"░"                          # Unicode U+2591 | Light shade | Block drawing
"▒"                          # Unicode U+2592 | Medium shade | Block drawing
"▓"                          # Unicode U+2593 | Dark shade | Block drawing
"█"                          # Unicode U+2588 | Full block | Block drawing
"▀"                          # Unicode U+2580 | Upper half block | Block drawing
"▄"                          # Unicode U+2584 | Lower half block | Block drawing
"▌"                          # Unicode U+258C | Left half block | Block drawing
"▐"                          # Unicode U+2590 | Right half block | Block drawing

"▲"                          # Unicode U+25B2 | Up triangle | Geometric
"▼"                          # Unicode U+25BC | Down triangle | Geometric
"◄"                          # Unicode U+25C4 | Left triangle | Geometric
"►"                          # Unicode U+25BA | Right triangle | Geometric
"●"                          # Unicode U+25CF | Circle | Geometric
"○"                          # Unicode U+25CB | Open circle | Geometric
"■"                          # Unicode U+25A0 | Square | Geometric
"□"                          # Unicode U+25A1 | Open square | Geometric
"★"                          # Unicode U+2605 | Filled star | Geometric
"☆"                          # Unicode U+2606 | Open star | Geometric

"✓"                          # Unicode U+2713 | Check mark | Symbol
"✗"                          # Unicode U+2717 | X mark | Symbol
"✘"                          # Unicode U+2718 | Heavy X mark | Symbol
"→"                          # Unicode U+2192 | Right arrow | Symbol
"←"                          # Unicode U+2190 | Left arrow | Symbol
"↑"                          # Unicode U+2191 | Up arrow | Symbol
"↓"                          # Unicode U+2193 | Down arrow | Symbol
"↔"                          # Unicode U+2194 | Left-right arrow | Symbol
"↕"                          # Unicode U+2195 | Up-down arrow | Symbol

# ═══════════════════════════════════════════════════════════════════════════
# ADDITIONAL STRING FORMATTING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
ascii(obj)                   # Object | ASCII repr | Returns ASCII-safe repr string
repr(obj)                    # Object | Official repr | Returns repr string
str(obj)                     # Object | String conversion | Returns string representation
chr(i)                       # Integer | Code to char | Returns character
ord(c)                       # Character | Char to code | Returns Unicode code point
hex(n)                       # Integer | To hex string | Returns hex string with 0x
oct(n)                       # Integer | To octal string | Returns octal string with 0o
bin(n)                       # Integer | To binary string | Returns binary string with 0b
format(obj)                  # Object | Format with __format__ | Returns formatted string
format(obj, spec)            # Object + spec | Format with spec | Returns formatted string

vars(obj)                    # Object | Get __dict__ | Returns dict of attributes
dir(obj)                     # Object | Get attributes | Returns list of attribute names
type(obj).__name__           # Object | Get type name | Returns type name string
id(obj)                      # Object | Get object ID | Returns unique identifier
hash(obj)                    # Object | Get hash value | Returns hash integer

# ═══════════════════════════════════════════════════════════════════════════
# JSON FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
json.dumps(obj)              # Object | JSON string | Returns JSON string
json.dumps(obj, indent=n)    # Object | Pretty JSON | Returns indented JSON
json.dumps(obj, indent=n, sort_keys=True)  # Object | Sorted JSON | Returns sorted JSON
json.dumps(obj, separators=(',', ':'))  # Object | Compact JSON | Returns compact JSON
json.dumps(obj, ensure_ascii=False)  # Object | Unicode JSON | Returns Unicode JSON
json.dumps(obj, default=func)  # Object | Custom serializer | Returns JSON with custom handling
json.dump(obj, file)         # Object + file | Write JSON to file | Writes to file object
json.dump(obj, file, indent=n)  # Object + file | Pretty JSON to file | Writes indented

json.loads(string)           # String | Parse JSON | Returns Python object
json.load(file)              # File | Parse JSON from file | Returns Python object

JSONEncoder(indent=n)        # Indent | Create encoder | Returns encoder instance
JSONEncoder.encode(obj)      # Object | Encode to JSON | Returns JSON string
JSONEncoder.iterencode(obj)  # Object | Iterate encoding | Returns iterator of chunks

# ═══════════════════════════════════════════════════════════════════════════
# XML/HTML FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
html.escape(text)            # Text | Escape HTML | Returns escaped string
html.escape(text, quote=True)  # Text | Escape HTML + quotes | Returns escaped string
html.unescape(text)          # Text | Unescape HTML | Returns unescaped string

xml.etree.ElementTree.tostring(element)  # Element | XML to bytes | Returns bytes
xml.etree.ElementTree.tostring(element, encoding='unicode')  # Element | XML to string | Returns string
xml.etree.ElementTree.tostring(element, method='html')  # Element | HTML output | Returns HTML string

# ═══════════════════════════════════════════════════════════════════════════
# CSV FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
csv.writer(file)             # File | Create CSV writer | Returns writer object
writer.writerow(row)         # Row | Write single row | Writes to file
writer.writerows(rows)       # Rows | Write multiple rows | Writes to file

csv.DictWriter(file, fieldnames)  # File + fields | Create dict writer | Returns writer object
DictWriter.writeheader()     # None | Write header row | Writes field names
DictWriter.writerow(dict)    # Dict | Write dict as row | Writes to file
DictWriter.writerows(dicts)  # Dicts | Write multiple dicts | Writes to file

# ═══════════════════════════════════════════════════════════════════════════
# ADVANCED ESCAPE SEQUENCES (Extended)
# ═══════════════════════════════════════════════════════════════════════════
\a                           # Escape | Bell/alert | Produces beep sound
\N{EMOJI_NAME}               # Escape | Named emoji | Unicode emoji by name
"\N{GRINNING FACE}"          # Escape | Grinning emoji | Returns 😀
"\N{THUMBS UP SIGN}"         # Escape | Thumbs up | Returns 👍
"\N{CHECK MARK}"             # Escape | Check mark | Returns ✓
"\N{MULTIPLICATION SIGN}"    # Escape | Multiply symbol | Returns ×
"\N{DIVISION SIGN}"          # Escape | Division symbol | Returns ÷
"\N{DEGREE SIGN}"            # Escape | Degree symbol | Returns °
"\N{MICRO SIGN}"             # Escape | Micro symbol | Returns µ
"\N{SUPERSCRIPT TWO}"        # Escape | Superscript 2 | Returns ²
"\N{SUPERSCRIPT THREE}"      # Escape | Superscript 3 | Returns ³
"\N{VULGAR FRACTION ONE HALF}"  # Escape | One half fraction | Returns ½
"\N{VULGAR FRACTION ONE QUARTER}"  # Escape | One quarter fraction | Returns ¼
```

### COMMON FORMATTING EXAMPLES

```python
# Basic f-string interpolation
name = "Alice"
age = 30
f"Name: {name}, Age: {age}"                    # → "Name: Alice, Age: 30"

# Expressions in f-strings
f"Next year: {age + 1}"                        # → "Next year: 31"
f"Double: {age * 2}"                           # → "Double: 60"

# Number formatting
pi = 3.14159265359
f"{pi:.2f}"                                    # → "3.14"
f"{pi:.4f}"                                    # → "3.1416"
f"{pi:10.2f}"                                  # → "      3.14"

# Integer formatting
num = 42
f"{num:d}"                                     # → "42"
f"{num:5d}"                                    # → "   42"
f"{num:05d}"                                   # → "00042"

# Bases
f"{num:b}"                                     # → "101010"
f"{num:o}"                                     # → "52"
f"{num:x}"                                     # → "2a"
f"{num:X}"                                     # → "2A"
f"{num:#x}"                                    # → "0x2a"

# Alignment
f"{name:<10}"                                  # → "Alice     "
f"{name:>10}"                                  # → "     Alice"
f"{name:^10}"                                  # → "  Alice   "
f"{name:*^10}"                                 # → "**Alice***"

# Thousand separators
large = 1234567.89
f"{large:,}"                                   # → "1,234,567.89"
f"{large:_.2f}"                                # → "1_234_567.89"

# Percentage
ratio = 0.875
f"{ratio:.2%}"                                 # → "87.50%"

# Sign formatting
pos = 42
neg = -42
f"{pos:+d}"                                    # → "+42"
f"{neg:+d}"                                    # → "-42"
f"{pos: d}"                                    # → " 42"

# Debug format (Python 3.8+)
x = 42
f"{x=}"                                        # → "x=42"
f"{x + 10=}"                                   # → "x + 10=52"
```

---

## DETAILED FORMATTING OPERATIONS

### 1. F-STRING FORMATTING (Python 3.6+)

```python
# Basic interpolation
name = "Alice"
age = 30
f"Hello, {name}!"                              # → "Hello, Alice!"
f"{name} is {age} years old"                   # → "Alice is 30 years old"

# Expressions
a = 5
b = 10
f"Sum: {a + b}"                                # → "Sum: 15"
f"Product: {a * b}"                            # → "Product: 50"
f"Average: {(a + b) / 2}"                      # → "Average: 7.5"

# Calling functions
def greet(name):
    return f"Hello, {name}"
f"{greet('Bob')}"                              # → "Hello, Bob"

# Method calls
text = "hello"
f"{text.upper()}"                              # → "HELLO"
f"{text.capitalize()}"                         # → "Hello"

# Accessing attributes/items
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
f"{p.name} is {p.age}"                         # → "Alice is 30"

data = {"name": "Bob", "age": 25}
f"{data['name']} is {data['age']}"             # → "Bob is 25"

# List/tuple access
nums = [10, 20, 30]
f"First: {nums[0]}, Last: {nums[-1]}"          # → "First: 10, Last: 30"

# Conversion flags
value = "hello"
f"{value!s}"                                   # → "hello" (str())
f"{value!r}"                                   # → "'hello'" (repr())
f"{value!a}"                                   # → "'hello'" (ascii())

# Debug format (Python 3.8+)
x = 42
y = 100
f"{x=}"                                        # → "x=42"
f"{x=} {y=}"                                   # → "x=42 y=100"
f"{x + y=}"                                    # → "x + y=142"

# Escaping braces
f"{{not a variable}}"                          # → "{not a variable}"
f"{{{x}}}"                                     # → "{42}"

# Nested f-strings
width = 10
precision = 2
value = 3.14159
f"{value:{width}.{precision}f}"                # → "      3.14"

# Multiline f-strings
message = f"""
Name: {name}
Age: {age}
Status: {'Active' if age < 65 else 'Retired'}
"""
```

### 2. FORMAT SPECIFICATION MINI-LANGUAGE

```python
# Format spec structure: [[fill]align][sign][#][0][width][,][.precision][type]

value = 42
text = "Hello"

# Width
f"{value:5}"                                   # → "   42" (default right-align for numbers)
f"{text:10}"                                   # → "Hello     " (default left-align for strings)

# Alignment
f"{value:<5}"                                  # → "42   " (left)
f"{value:>5}"                                  # → "   42" (right)
f"{value:^5}"                                  # → " 42  " (center)
f"{value:=5}"                                  # → "   42" (padding after sign)

# Fill character
f"{value:*<5}"                                 # → "42***"
f"{value:*>5}"                                 # → "***42"
f"{value:*^5}"                                 # → "*42**"
f"{value:0>5}"                                 # → "00042"

# Sign
f"{value:+}"                                   # → "+42"
f"{-value:+}"                                  # → "-42"
f"{value: }"                                   # → " 42" (space for positive)
f"{-value: }"                                  # → "-42"
f"{value:-}"                                   # → "42" (default, sign only for negative)

# Alternate form (#)
num = 255
f"{num:#b}"                                    # → "0b11111111"
f"{num:#o}"                                    # → "0o377"
f"{num:#x}"                                    # → "0xff"
f"{num:#X}"                                    # → "0XFF"

# Zero padding
f"{value:05}"                                  # → "00042"
f"{value:05d}"                                 # → "00042"

# Thousand separator
large = 1234567890
f"{large:,}"                                   # → "1,234,567,890"
f"{large:_}"                                   # → "1_234_567_890"

# Precision
pi = 3.14159265359
f"{pi:.2f}"                                    # → "3.14"
f"{pi:.4f}"                                    # → "3.1416"
f"{pi:.0f}"                                    # → "3"

# Type
f"{value:d}"                                   # → "42" (decimal)
f"{value:b}"                                   # → "101010" (binary)
f"{value:o}"                                   # → "52" (octal)
f"{value:x}"                                   # → "2a" (hex)
f"{value:X}"                                   # → "2A" (HEX)

# Combining specifiers
f"{value:+05d}"                                # → "+0042" (sign + zero-pad + width)
f"{pi:10.2f}"                                  # → "      3.14" (width + precision)
f"{large:15,.2f}"                              # → " 1,234,567,890.00" (width + comma + precision)
f"{value:*^+10d}"                              # → "***+42****" (fill + center + sign + width)
```

### 3. NUMERIC FORMATTING

```python
# Integer formatting
num = 42

# Decimal
f"{num:d}"                                     # → "42"
f"{num:5d}"                                    # → "   42"
f"{num:05d}"                                   # → "00042"

# Binary
f"{num:b}"                                     # → "101010"
f"{num:#b}"                                    # → "0b101010"
f"{num:010b}"                                  # → "0000101010"

# Octal
f"{num:o}"                                     # → "52"
f"{num:#o}"                                    # → "0o52"

# Hexadecimal
f"{num:x}"                                     # → "2a"
f"{num:X}"                                     # → "2A"
f"{num:#x}"                                    # → "0x2a"
f"{num:#X}"                                    # → "0X2A"

# Character
f"{num:c}"                                     # → "*" (ASCII 42)

# Floating point formatting
pi = 3.14159265359

# Fixed-point
f"{pi:f}"                                      # → "3.141593" (default 6 decimals)
f"{pi:.2f}"                                    # → "3.14"
f"{pi:.8f}"                                    # → "3.14159265"
f"{pi:10.2f}"                                  # → "      3.14"

# Exponential
f"{pi:e}"                                      # → "3.141593e+00"
f"{pi:.2e}"                                    # → "3.14e+00"
f"{pi:E}"                                      # → "3.141593E+00"

# General format
f"{pi:g}"                                      # → "3.14159"
f"{pi:.2g}"                                    # → "3.1"
f"{0.00001:g}"                                 # → "1e-05"

# Percentage
ratio = 0.875
f"{ratio:%}"                                   # → "87.500000%"
f"{ratio:.2%}"                                 # → "87.50%"
f"{ratio:6.1%}"                                # → "  87.5%"

# Large numbers with separators
big = 1234567890
f"{big:,}"                                     # → "1,234,567,890"
f"{big:_}"                                     # → "1_234_567_890"
f"{big:,.2f}"                                  # → "1,234,567,890.00"
f"{big:_.2f}"                                  # → "1_234_567_890.00"

# Sign display
pos = 42
neg = -42
zero = 0

f"{pos:+d}"                                    # → "+42"
f"{neg:+d}"                                    # → "-42"
f"{zero:+d}"                                   # → "+0"

f"{pos: d}"                                    # → " 42"
f"{neg: d}"                                    # → "-42"
f"{zero: d}"                                   # → " 0"

# Padding after sign
f"{pos:=+5d}"                                  # → "+  42"
f"{neg:=+5d}"                                  # → "-  42"
```

### 4. STRING ALIGNMENT & PADDING

```python
text = "Python"

# Left alignment (default for strings)
f"{text:10}"                                   # → "Python    "
f"{text:<10}"                                  # → "Python    "
f"{text:*<10}"                                 # → "Python****"

# Right alignment
f"{text:>10}"                                  # → "    Python"
f"{text:*>10}"                                 # → "****Python"
f"{text:0>10}"                                 # → "0000Python"

# Center alignment
f"{text:^10}"                                  # → "  Python  "
f"{text:*^10}"                                 # → "**Python**"
f"{text:-^10}"                                 # → "--Python--"

# Using string methods
text.ljust(10)                                 # → "Python    "
text.ljust(10, '*')                            # → "Python****"
text.rjust(10)                                 # → "    Python"
text.rjust(10, '*')                            # → "****Python"
text.center(10)                                # → "  Python  "
text.center(10, '*')                           # → "**Python**"

# Zero fill (numbers)
num = 42
f"{num:05d}"                                   # → "00042"
str(num).zfill(5)                              # → "00042"
"-42".zfill(5)                                 # → "-0042"

# Tab expansion
"a\tb\tc".expandtabs()                         # → "a       b       c"
"a\tb\tc".expandtabs(4)                        # → "a   b   c"
```

### 5. .format() METHOD

```python
# Positional arguments
"Hello {}".format("World")                     # → "Hello World"
"{} + {} = {}".format(2, 3, 5)                 # → "2 + 3 = 5"

# Indexed arguments
"{0} {1}".format("Hello", "World")             # → "Hello World"
"{1} {0}".format("Hello", "World")             # → "World Hello"
"{0} {0} {1}".format("Hi", "Bye")              # → "Hi Hi Bye"

# Named arguments
"{name} is {age} years old".format(name="Alice", age=30)  # → "Alice is 30 years old"
"{x} + {y} = {sum}".format(x=5, y=3, sum=8)    # → "5 + 3 = 8"

# Mixed positional and named
"{0} is {age} years old".format("Bob", age=25) # → "Bob is 25 years old"

# Accessing attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
"{0.name} is {0.age}".format(p)                # → "Alice is 30"
"{p.name} is {p.age}".format(p=p)              # → "Alice is 30"

# Accessing dict/list items
data = {"name": "Bob", "age": 25}
"{0[name]} is {0[age]}".format(data)           # → "Bob is 25"

nums = [10, 20, 30]
"{0[0]} {0[1]} {0[2]}".format(nums)            # → "10 20 30"

# Format specifications
"{:10}".format("Hi")                           # → "Hi        "
"{:>10}".format("Hi")                          # → "        Hi"
"{:^10}".format("Hi")                          # → "    Hi    "
"{:*^10}".format("Hi")                         # → "****Hi****"

"{:.2f}".format(3.14159)                       # → "3.14"
"{:05d}".format(42)                            # → "00042"
"{:,}".format(1234567)                         # → "1,234,567"

# Named with format spec
"{value:10.2f}".format(value=3.14159)          # → "      3.14"
"{num:05d}".format(num=42)                     # → "00042"

# Nested replacement fields
width = 10
precision = 2
"{value:{w}.{p}f}".format(value=3.14159, w=width, p=precision)  # → "      3.14"
```

### 6. %-FORMATTING (OLD STYLE)

```python
# String
"%s" % "hello"                                 # → "hello"
"Hello %s" % "World"                           # → "Hello World"
"%s %s" % ("Hello", "World")                   # → "Hello World"

# Integer
"%d" % 42                                      # → "42"
"%i" % 42                                      # → "42"
"%5d" % 42                                     # → "   42"
"%05d" % 42                                    # → "00042"

# Float
"%f" % 3.14159                                 # → "3.141590"
"%.2f" % 3.14159                               # → "3.14"
"%10.2f" % 3.14159                             # → "      3.14"

# Exponential
"%e" % 1234.5                                  # → "1.234500e+03"
"%.2e" % 1234.5                                # → "1.23e+03"
"%E" % 1234.5                                  # → "1.234500E+03"

# Hex/Octal
"%x" % 255                                     # → "ff"
"%X" % 255                                     # → "FF"
"%o" % 255                                     # → "377"
"%#x" % 255                                    # → "0xff"

# Character
"%c" % 65                                      # → "A"
"%c" % 'A'                                     # → "A"

# Repr
"%r" % "hello"                                 # → "'hello'"

# Named placeholders (dict)
"%(name)s is %(age)d years old" % {"name": "Alice", "age": 30}  # → "Alice is 30 years old"
"%(x).2f + %(y).2f = %(sum).2f" % {"x": 1.5, "y": 2.3, "sum": 3.8}  # → "1.50 + 2.30 = 3.80"

# Multiple values
"%s %d %.2f" % ("text", 42, 3.14159)           # → "text 42 3.14"

# Escape %%
"50%% complete" % ()                           # → "50% complete"
"100%%" % ()                                   # → "100%"
```

### 7. STRING TEMPLATE (string.Template)

```python
from string import Template

# Simple substitution
t = Template("Hello $name")
t.substitute(name="Alice")                     # → "Hello Alice"

# Braced substitution
t = Template("Hello ${name}!")
t.substitute(name="Bob")                       # → "Hello Bob!"

# Multiple substitutions
t = Template("$greeting $name, you are $age years old")
t.substitute(greeting="Hello", name="Alice", age=30)  # → "Hello Alice, you are 30 years old"

# Using dict
data = {"name": "Bob", "age": 25}
t = Template("$name is $age")
t.substitute(data)                             # → "Bob is 25"

# safe_substitute (doesn't raise KeyError)
t = Template("$name is $age years old")
t.safe_substitute(name="Alice")                # → "Alice is $age years old"
t.substitute(name="Alice")                     # → KeyError: 'age'

# Escape $
t = Template("$$price is $amount")
t.substitute(amount=100)                       # → "$price is 100"

# Custom delimiter
class MyTemplate(Template):
    delimiter = '@'

t = MyTemplate("Hello @name")
t.substitute(name="Alice")                     # → "Hello Alice"
```

### 8. PRINT FORMATTING

```python
# Basic print
print("Hello World")                           # → Hello World (with newline)

# Multiple values
print("Hello", "World")                        # → Hello World (space-separated)
print(1, 2, 3, 4, 5)                           # → 1 2 3 4 5

# Custom separator
print("a", "b", "c", sep=", ")                 # → a, b, c
print("a", "b", "c", sep="-")                  # → a-b-c
print("a", "b", "c", sep="")                   # → abc

# Custom ending
print("Hello", end="")                         # → Hello (no newline)
print("Line 1", end=" | ")
print("Line 2")                                # → Line 1 | Line 2

print("Loading", end="...")
print("Done")                                  # → Loading...Done

# Combine sep and end
print("a", "b", "c", sep="-", end="!\n")       # → a-b-c!

# Print to file
with open("output.txt", "w") as f:
    print("Hello World", file=f)

# Force flush
import time
print("Loading", end="", flush=True)
time.sleep(1)
print(".", end="", flush=True)
time.sleep(1)
print(".", end="", flush=True)
print(" Done")

# Print with formatting
name = "Alice"
age = 30
print(f"{name} is {age} years old")            # → Alice is 30 years old
print("{} is {} years old".format(name, age))  # → Alice is 30 years old
print("%s is %d years old" % (name, age))      # → Alice is 30 years old
```

### 9. DATETIME FORMATTING

```python
from datetime import datetime

dt = datetime(2025, 1, 15, 15, 45, 30)

# F-string formatting
f"{dt:%Y}"                                     # → "2025"
f"{dt:%y}"                                     # → "25"
f"{dt:%m}"                                     # → "01"
f"{dt:%d}"                                     # → "15"
f"{dt:%B}"                                     # → "January"
f"{dt:%b}"                                     # → "Jan"
f"{dt:%A}"                                     # → "Wednesday"
f"{dt:%a}"                                     # → "Wed"
f"{dt:%H}"                                     # → "15" (24-hour)
f"{dt:%I}"                                     # → "03" (12-hour)
f"{dt:%M}"                                     # → "45"
f"{dt:%S}"                                     # → "30"
f"{dt:%p}"                                     # → "PM"

# Common date formats
f"{dt:%Y-%m-%d}"                               # → "2025-01-15" (ISO format)
f"{dt:%m/%d/%Y}"                               # → "01/15/2025" (US format)
f"{dt:%d/%m/%Y}"                               # → "15/01/2025" (European format)
f"{dt:%B %d, %Y}"                              # → "January 15, 2025"
f"{dt:%b %d, %Y}"                              # → "Jan 15, 2025"
f"{dt:%A, %B %d, %Y}"                          # → "Wednesday, January 15, 2025"

# Common time formats
f"{dt:%H:%M:%S}"                               # → "15:45:30" (24-hour)
f"{dt:%I:%M %p}"                               # → "03:45 PM" (12-hour)
f"{dt:%I:%M:%S %p}"                            # → "03:45:30 PM"

# Combined date/time
f"{dt:%Y-%m-%d %H:%M:%S}"                      # → "2025-01-15 15:45:30"
f"{dt:%B %d, %Y at %I:%M %p}"                  # → "January 15, 2025 at 03:45 PM"

# Using strftime method
dt.strftime("%Y-%m-%d")                        # → "2025-01-15"
dt.strftime("%B %d, %Y")                       # → "January 15, 2025"
dt.strftime("%I:%M %p")                        # → "03:45 PM"

# ISO format methods
dt.isoformat()                                 # → "2025-01-15T15:45:30"
dt.date().isoformat()                          # → "2025-01-15"
dt.time().isoformat()                          # → "15:45:30"
```

### 10. CUSTOM FORMATTING (__format__ method)

```python
# Define custom formatting for classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __format__(self, spec):
        if spec == 'short':
            return self.name
        elif spec == 'long':
            return f"{self.name} ({self.age})"
        elif spec == 'upper':
            return self.name.upper()
        else:
            return str(self)
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Alice", 30)

f"{p}"                                         # → "Person(name=Alice, age=30)"
f"{p:short}"                                   # → "Alice"
f"{p:long}"                                    # → "Alice (30)"
f"{p:upper}"                                   # → "ALICE"

format(p, 'short')                             # → "Alice"
format(p, 'long')                              # → "Alice (30)"

# Complex custom formatting
class Money:
    def __init__(self, amount, currency='USD'):
        self.amount = amount
        self.currency = currency
    
    def __format__(self, spec):
        if not spec:
            spec = '.2f'
        
        formatted_amount = format(self.amount, spec)
        
        symbols = {'USD': '$', 'EUR': '€', 'GBP': '£'}
        symbol = symbols.get(self.currency, self.currency)
        
        return f"{symbol}{formatted_amount}"

m = Money(1234.5, 'USD')

f"{m}"                                         # → "$1234.50"
f"{m:.0f}"                                     # → "$1234"
f"{m:,.2f}"                                    # → "$1,234.50"

m_eur = Money(999.99, 'EUR')
f"{m_eur:,.2f}"                                # → "€999.99"
```

### 11. TEXTWRAP MODULE

```python
import textwrap

# Basic wrapping
long_text = "This is a very long line of text that needs to be wrapped into multiple lines for better readability."

# Wrap to list of lines
lines = textwrap.wrap(long_text, width=40)
# → ['This is a very long line of text that',
#    'needs to be wrapped into multiple',
#    'lines for better readability.']

# Wrap and join into single string
wrapped = textwrap.fill(long_text, width=40)
# → "This is a very long line of text that\nneeds to be wrapped into multiple\nlines for better readability."

# With initial indent
wrapped = textwrap.fill(long_text, width=40, 
                        initial_indent="  * ")
# → "  * This is a very long line of text\nthat needs to be wrapped into..."

# With subsequent indent (hanging indent)
wrapped = textwrap.fill(long_text, width=40,
                        initial_indent="1. ",
                        subsequent_indent="   ")
# → "1. This is a very long line of text\n   that needs to be wrapped..."

# Shorten text with ellipsis
short = textwrap.shorten(long_text, width=30)
# → "This is a very long [...]"

short = textwrap.shorten(long_text, width=30, placeholder="...")
# → "This is a very long..."

# Dedent (remove common leading whitespace)
indented = """
    def hello():
        print("Hello")
        print("World")
"""
dedented = textwrap.dedent(indented)
# → "\ndef hello():\n    print(\"Hello\")\n    print(\"World\")\n"

# Indent (add prefix to lines)
code = "print('Hello')\nprint('World')"
indented = textwrap.indent(code, "    ")
# → "    print('Hello')\n    print('World')"

# Conditional indenting
def should_indent(line):
    return not line.startswith('#')

code = "# Comment\nprint('Hello')\n# Another comment\nprint('World')"
indented = textwrap.indent(code, "    ", predicate=should_indent)
# → "# Comment\n    print('Hello')\n# Another comment\n    print('World')"

# Using TextWrapper class for repeated wrapping
wrapper = textwrap.TextWrapper(
    width=40,
    initial_indent=">> ",
    subsequent_indent="   ",
    break_long_words=False
)

text1 = "First paragraph of text that needs wrapping."
text2 = "Second paragraph with different content."

print(wrapper.fill(text1))
print(wrapper.fill(text2))

# More TextWrapper options
wrapper = textwrap.TextWrapper(
    width=50,
    max_lines=2,              # Limit to 2 lines
    placeholder=" [...]"      # Custom truncation
)
long = "This is a very long text that will be truncated after two lines."
print(wrapper.fill(long))
```

### 12. PPRINT MODULE

```python
import pprint

# Basic pretty printing
data = {'name': 'Alice', 'age': 30, 'scores': [95, 87, 92], 'active': True}

# Regular print
print(data)
# → {'name': 'Alice', 'age': 30, 'scores': [95, 87, 92], 'active': True}

# Pretty print
pprint.pprint(data)
# → {'active': True,
#    'age': 30,
#    'name': 'Alice',
#    'scores': [95, 87, 92]}

# Complex nested structure
complex_data = {
    'users': [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'roles': ['admin', 'user']},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'roles': ['user']},
    ],
    'config': {
        'debug': True,
        'settings': {'timeout': 30, 'retries': 3, 'endpoints': ['api1', 'api2']}
    }
}

pprint.pprint(complex_data)
# → {'config': {'debug': True,
#              'settings': {'endpoints': ['api1', 'api2'],
#                          'retries': 3,
#                          'timeout': 30}},
#    'users': [{'email': 'alice@example.com',
#               'id': 1,
#               'name': 'Alice',
#               'roles': ['admin', 'user']}, ...]}

# Control indentation
pprint.pprint(data, indent=4)
# → {   'active': True,
#       'age': 30, ...}

# Control width
pprint.pprint(complex_data, width=40)  # Narrower output

# Control depth (limit nesting)
pprint.pprint(complex_data, depth=2)
# → {'config': {'debug': True, 'settings': {...}},
#    'users': [{...}, {...}]}

# Compact format (multiple items per line if they fit)
numbers = list(range(20))
pprint.pprint(numbers, compact=True)
# → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Get formatted string instead of printing
formatted = pprint.pformat(data)
with open('output.txt', 'w') as f:
    f.write(formatted)

# Python 3.8+ shorthand
pprint.pp(data)  # Same as pprint.pprint with better defaults

# Underscore numbers (Python 3.10+)
large_nums = {'revenue': 1234567890, 'users': 9876543}
pprint.pprint(large_nums, underscore_numbers=True)
# → {'revenue': 1_234_567_890, 'users': 9_876_543}

# Check if readable/recursive
pprint.isreadable(data)      # → True
recursive_list = [1, 2]
recursive_list.append(recursive_list)
pprint.isrecursive(recursive_list)  # → True

# Using PrettyPrinter class for custom config
pp = pprint.PrettyPrinter(indent=4, width=60, depth=3, compact=True)
pp.pprint(complex_data)

# Safe repr (handles recursive structures)
safe = pprint.saferepr(recursive_list)
# → "[1, 2, <Recursion on list with id=...>]"
```

### 13. REPRLIB MODULE

```python
import reprlib

# Default repr vs reprlib.repr
long_list = list(range(100))
print(repr(long_list))        # → [0, 1, 2, 3, ..., 99] (full)
print(reprlib.repr(long_list))  # → [0, 1, 2, 3, 4, 5, ...] (abbreviated)

# Long string
long_string = "a" * 100
print(reprlib.repr(long_string))  # → 'aaaaaaaaaa...aaaa' (truncated)

# Nested structures
nested = {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
          'b': {'x': list(range(20)), 'y': list(range(30))}}
print(reprlib.repr(nested))
# → {'a': [1, 2, 3, 4, 5, 6, ...], 'b': {'x': [0, 1, 2, 3, 4, 5, ...], ...}}

# Custom Repr object
r = reprlib.Repr()
r.maxlist = 3        # Show only 3 list items
r.maxstring = 10     # Show only 10 chars
r.maxdict = 2        # Show only 2 dict items

data = {'items': [1, 2, 3, 4, 5, 6], 'text': 'Very long text here'}
print(r.repr(data))
# → {'items': [1, 2, 3, ...], 'text': 'Very long ...'}

# Control all types
r.maxlevel = 2       # Max recursion depth
r.maxtuple = 4       # Max tuple items
r.maxset = 3         # Max set items
r.maxfrozenset = 3   # Max frozenset items
r.maxdeque = 4       # Max deque items
r.maxarray = 5       # Max array items

# Recursive repr decorator
from reprlib import recursive_repr

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    @recursive_repr()
    def __repr__(self):
        return f"Node({self.value!r}, {self.next!r})"

# Create circular reference
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

print(node1)  # → Node(1, Node(2, ...)) (instead of infinite recursion)
```

### 14. STRING.FORMATTER CLASS

```python
import string

# Basic Formatter usage
formatter = string.Formatter()

# Format with positional and keyword args
result = formatter.format("{0} is {1} years old", "Alice", 30)
# → "Alice is 30 years old"

result = formatter.format("{name} lives in {city}", name="Bob", city="NYC")
# → "Bob lives in NYC"

# vformat (takes sequences instead of *args)
args = ("Alice", 30)
kwargs = {}
result = formatter.vformat("{0} is {1} years old", args, kwargs)
# → "Alice is 30 years old"

# Parse format string
fmt = "Hello {name}, you have {count:d} messages"
for literal, field_name, format_spec, conversion in formatter.parse(fmt):
    print(f"Literal: {literal!r}, Field: {field_name!r}, Spec: {format_spec!r}")
# → Literal: 'Hello ', Field: 'name', Spec: ''
#   Literal: ', you have ', Field: 'count', Spec: 'd'
#   Literal: ' messages', Field: None, Spec: ''

# Custom Formatter subclass
class UpperFormatter(string.Formatter):
    def convert_field(self, value, conversion):
        if conversion == 'u':
            return str(value).upper()
        return super().convert_field(value, conversion)

fmt = UpperFormatter()
result = fmt.format("Hello {name!u}", name="alice")
# → "Hello ALICE"

# Custom field getter
class DictFormatter(string.Formatter):
    def get_value(self, key, args, kwargs):
        if isinstance(key, int):
            return args[key]
        else:
            return kwargs.get(key, f"<missing {key}>")

fmt = DictFormatter()
result = fmt.format("{name} from {city}", name="Alice")
# → "Alice from <missing city>"

# Format field directly
formatter.format_field(42, "05d")      # → "00042"
formatter.format_field(3.14159, ".2f") # → "3.14"

# Get field from nested structures
data = {"user": {"name": "Alice", "age": 30}}
value, key = formatter.get_field("user.name", (), data)
# → value="Alice", key="name"
```

### 15. LOCALE MODULE

```python
import locale

# Set locale
locale.setlocale(locale.LC_ALL, '')  # Use user's default

# Format numbers with thousands separator
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
formatted = locale.format_string("%d", 1234567, grouping=True)
# → "1,234,567"

formatted = locale.format_string("%.2f", 1234.56, grouping=True)
# → "1,234.56"

# Currency formatting
amount = 1234.56
formatted = locale.currency(amount)
# → "$1234.56" (US)

formatted = locale.currency(amount, grouping=True)
# → "$1,234.56"

formatted = locale.currency(amount, symbol=True, grouping=True)
# → "$1,234.56"

# International currency format
formatted = locale.currency(amount, international=True)
# → "USD 1234.56"

# Different locales
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
formatted = locale.currency(amount, grouping=True)
# → "1.234,56 €" (German format)

locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
formatted = locale.currency(amount, symbol=True, grouping=True)
# → "£1,234.56" (British)

# Locale-aware string conversion
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
s = locale.str(12345.67)
# → "12345.67"

# Parse locale-specific numbers
num = locale.atof("1,234.56")   # → 1234.56
num = locale.atoi("1,234")      # → 1234

# Get locale conventions
conv = locale.localeconv()
print(conv['currency_symbol'])   # → "$"
print(conv['thousands_sep'])     # → ","
print(conv['decimal_point'])     # → "."
```

### 16. BYTES FORMATTING

```python
# Bytes literals
b = b"Hello"
print(b)  # → b'Hello'

# Old-style formatting with bytes
result = b"%s %s" % (b"Hello", b"World")
# → b'Hello World'

result = b"%d" % 42
# → b'42'

result = b"%.2f" % 3.14159
# → b'3.14'

# Create bytes from string
text = "Hello"
b = bytes(text, 'utf-8')
# → b'Hello'

b = "Hello".encode('utf-8')
# → b'Hello'

# Different encodings
text = "Héllo"
b = text.encode('utf-8')      # → b'H\xc3\xa9llo'
b = text.encode('latin-1')    # → b'H\xe9llo'
# b = text.encode('ascii')    # → UnicodeEncodeError

# Error handling
b = text.encode('ascii', errors='ignore')     # → b'Hllo'
b = text.encode('ascii', errors='replace')    # → b'H?llo'
b = text.encode('ascii', errors='xmlcharrefreplace')  # → b'H&#233;llo'
b = text.encode('ascii', errors='backslashreplace')   # → b'H\\xe9llo'

# Decode back to string
b = b'Hello'
s = b.decode('utf-8')         # → "Hello"

# Hex representation
b = bytes([255, 254, 253])
hex_str = b.hex()             # → "fffefd"
hex_str = b.hex(' ')          # → "ff fe fd"
hex_str = b.hex(':', 1)       # → "ff:fe:fd"
hex_str = b.hex('-', 2)       # → "fffe-fd"

# Create from hex
b = bytes.fromhex("48656c6c6f")
# → b'Hello'

# Bytearray (mutable)
ba = bytearray(b"Hello")
ba[0] = ord('J')
print(ba)  # → bytearray(b'Jello')
```

### 17. UNICODE OPERATIONS

```python
import unicodedata

# Normalize Unicode
text1 = "café"  # é as single character
text2 = "café"  # e + combining accent

print(text1 == text2)  # → False (different representations)

# Normalize to same form
norm1 = unicodedata.normalize('NFC', text1)
norm2 = unicodedata.normalize('NFC', text2)
print(norm1 == norm2)  # → True

# Different normalization forms
text = "Ω"  # Greek Omega
print(unicodedata.normalize('NFC', text))   # Composed
print(unicodedata.normalize('NFD', text))   # Decomposed
print(unicodedata.normalize('NFKC', text))  # Compatibility composed
print(unicodedata.normalize('NFKD', text))  # Compatibility decomposed

# Get Unicode character name
char = "é"
name = unicodedata.name(char)
# → "LATIN SMALL LETTER E WITH ACUTE"

char = "∑"
name = unicodedata.name(char)
# → "N-ARY SUMMATION"

# Look up character by name
char = unicodedata.lookup("SNOWMAN")
# → "☃"

char = unicodedata.lookup("CHECK MARK")
# → "✓"

# Character categories
print(unicodedata.category('A'))    # → "Lu" (Uppercase letter)
print(unicodedata.category('a'))    # → "Ll" (Lowercase letter)
print(unicodedata.category('5'))    # → "Nd" (Decimal number)
print(unicodedata.category(' '))    # → "Zs" (Space separator)
print(unicodedata.category('!'))    # → "Po" (Other punctuation)

# Numeric values
print(unicodedata.decimal('5'))     # → 5
print(unicodedata.digit('⁵'))       # → 5
print(unicodedata.numeric('½'))     # → 0.5

# Check if normalized
text = "café"
print(unicodedata.is_normalized('NFC', text))   # → True or False

# Bidirectional properties
print(unicodedata.bidirectional('A'))   # → "L" (Left-to-right)
print(unicodedata.bidirectional('א'))   # → "R" (Right-to-left)

# Combining class
print(unicodedata.combining('\u0301'))  # → 230 (combining accent)

# East Asian width
print(unicodedata.east_asian_width('A'))   # → "Na" (Narrow)
print(unicodedata.east_asian_width('中'))  # → "W" (Wide)

# Encode/decode various formats
text = "Hello 世界"
print(text.encode('utf-8'))      # → b'Hello \xe4\xb8\x96\xe7\x95\x8c'
print(text.encode('utf-16'))     # → b'\xff\xfeH\x00e\x00l\x00l\x00o\x00 \x00\x16N\x8c\xe4'
print(text.encode('utf-32'))     # Full 4-byte encoding
```

### 18. ANSI COLOR CODES

```python
# Color formatting
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

print(f"{RED}Error message{RESET}")
print(f"{GREEN}Success message{RESET}")
print(f"{YELLOW}Warning message{RESET}")

# Background colors
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"

print(f"{BG_RED}Red background{RESET}")

# Text styles
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m"

print(f"{BOLD}Bold text{RESET}")
print(f"{UNDERLINE}Underlined text{RESET}")
print(f"{ITALIC}Italic text{RESET}")

# Combine styles
print(f"{BOLD}{RED}Bold red text{RESET}")
print(f"{GREEN}{UNDERLINE}Green underlined{RESET}")

# 256 colors
def color_256(code, text):
    return f"\033[38;5;{code}m{text}\033[0m"

print(color_256(196, "Bright red"))
print(color_256(21, "Deep blue"))
print(color_256(226, "Bright yellow"))

# RGB colors (true color)
def color_rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

print(color_rgb(255, 100, 50, "Custom orange"))
print(color_rgb(50, 200, 100, "Custom green"))

# Complete color helper class
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

# Usage
print(f"{Colors.BOLD}{Colors.RED}Bold red text{Colors.RESET}")
print(f"{Colors.BG_BLUE}{Colors.WHITE}White on blue{Colors.RESET}")

# Cursor movement
print("\033[2J")       # Clear screen
print("\033[H")        # Move cursor to home
print("\033[10A")      # Move up 10 lines
print("\033[5B")       # Move down 5 lines
print("\033[20C")      # Move right 20 columns
print("\033[10D")      # Move left 10 columns
print("\033[10;20H")   # Move to row 10, column 20
print("\033[K")        # Clear to end of line
```

### 19. BOX DRAWING & ASCII ART

```python
# Simple box
def draw_box(text, width=None):
    """Draw a box around text"""
    if width is None:
        width = len(text) + 4
    
    top = "┌" + "─" * (width - 2) + "┐"
    middle = "│ " + text.ljust(width - 4) + " │"
    bottom = "└" + "─" * (width - 2) + "┘"
    
    return f"{top}\n{middle}\n{bottom}"

print(draw_box("Hello World"))
# ┌──────────────┐
# │ Hello World  │
# └──────────────┘

# Double-line box
def draw_double_box(text, width=None):
    if width is None:
        width = len(text) + 4
    
    top = "╔" + "═" * (width - 2) + "╗"
    middle = "║ " + text.ljust(width - 4) + " ║"
    bottom = "╚" + "═" * (width - 2) + "╝"
    
    return f"{top}\n{middle}\n{bottom}"

print(draw_double_box("Important"))
# ╔════════════╗
# ║ Important  ║
# ╚════════════╝

# Table with box drawing
def draw_table(headers, rows):
    """Draw table with box characters"""
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Top border
    top = "┌" + "┬".join("─" * (w + 2) for w in col_widths) + "┐"
    
    # Header
    header = "│ " + " │ ".join(h.ljust(w) for h, w in zip(headers, col_widths)) + " │"
    
    # Separator
    sep = "├" + "┼".join("─" * (w + 2) for w in col_widths) + "┤"
    
    # Rows
    body = []
    for row in rows:
        line = "│ " + " │ ".join(str(c).ljust(w) for c, w in zip(row, col_widths)) + " │"
        body.append(line)
    
    # Bottom border
    bottom = "└" + "┴".join("─" * (w + 2) for w in col_widths) + "┘"
    
    return "\n".join([top, header, sep] + body + [bottom])

headers = ["Name", "Age", "City"]
rows = [
    ["Alice", 30, "NYC"],
    ["Bob", 25, "LA"],
    ["Charlie", 35, "Chicago"]
]
print(draw_table(headers, rows))
# ┌─────────┬─────┬─────────┐
# │ Name    │ Age │ City    │
# ├─────────┼─────┼─────────┤
# │ Alice   │ 30  │ NYC     │
# │ Bob     │ 25  │ LA      │
# │ Charlie │ 35  │ Chicago │
# └─────────┴─────┴─────────┘

# Progress bar with blocks
def progress_bar_blocks(percent):
    """Progress bar with Unicode blocks"""
    filled = int(percent / 10)
    empty = 10 - filled
    bar = "█" * filled + "░" * empty
    return f"[{bar}] {percent}%"

print(progress_bar_blocks(70))
# [███████░░░] 70%

# Spinners
spinners = {
    'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
    'line': ['|', '/', '-', '\\'],
    'arrow': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
    'circle': ['◐', '◓', '◑', '◒'],
    'square': ['◰', '◳', '◲', '◱'],
    'dots_pulse': ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
}

# Stars and symbols
stars = "★" * 5 + "☆" * 3  # Rating: ★★★★★☆☆☆
checkmark = "✓ Complete"
xmark = "✗ Failed"
arrow = "→ Next step"

# Emoji-like symbols
symbols = {
    'info': 'ℹ',
    'warning': '⚠',
    'error': '✖',
    'success': '✔',
    'question': '?',
    'star': '★',
    'heart': '♥',
    'music': '♪',
    'gear': '⚙',
    'lock': '🔒',
    'key': '🔑'
}
```

### 20. JSON & OTHER FORMATS

```python
import json

# Basic JSON formatting
data = {'name': 'Alice', 'age': 30, 'scores': [95, 87, 92]}

# Compact JSON
compact = json.dumps(data)
# → '{"name": "Alice", "age": 30, "scores": [95, 87, 92]}'

# Pretty JSON
pretty = json.dumps(data, indent=2)
# → {
#     "name": "Alice",
#     "age": 30,
#     "scores": [
#       95,
#       87,
#       92
#     ]
#   }

# Custom indent
pretty = json.dumps(data, indent=4)

# Sorted keys
sorted_json = json.dumps(data, indent=2, sort_keys=True)
# → {
#     "age": 30,
#     "name": "Alice",
#     "scores": [...]
#   }

# Very compact (no spaces)
compact = json.dumps(data, separators=(',', ':'))
# → '{"name":"Alice","age":30,"scores":[95,87,92]}'

# Unicode handling
data = {'message': 'Hello 世界'}
json_unicode = json.dumps(data, ensure_ascii=False)
# → '{"message": "Hello 世界"}'

json_ascii = json.dumps(data, ensure_ascii=True)
# → '{"message": "Hello \\u4e16\\u754c"}'

# Custom serialization
from datetime import datetime

def date_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} not serializable")

data = {'timestamp': datetime.now()}
json_str = json.dumps(data, default=date_handler)

# HTML escaping
import html

text = '<script>alert("XSS")</script>'
escaped = html.escape(text)
# → '&lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;'

escaped_quotes = html.escape(text, quote=True)
# → '&lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;'

# Unescape
original = html.unescape(escaped)
# → '<script>alert("XSS")</script>'

# CSV formatting
import csv
from io import StringIO

# Write CSV
output = StringIO()
writer = csv.writer(output)
writer.writerow(['Name', 'Age', 'City'])
writer.writerow(['Alice', 30, 'NYC'])
writer.writerow(['Bob', 25, 'LA'])

csv_string = output.getvalue()
# → 'Name,Age,City\nAlice,30,NYC\nBob,25,LA\n'

# Dict writer
output = StringIO()
writer = csv.DictWriter(output, fieldnames=['Name', 'Age', 'City'])
writer.writeheader()
writer.writerow({'Name': 'Alice', 'Age': 30, 'City': 'NYC'})
writer.writerow({'Name': 'Bob', 'Age': 25, 'City': 'LA'})

csv_string = output.getvalue()
```

---

## PRACTICAL PROJECT PATTERNS

### Pattern 1: Table Formatting
```python
def format_table(headers, rows):
    """Create formatted ASCII table"""
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Format header
    header = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    separator = "-+-".join("-" * w for w in col_widths)
    
    # Format rows
    body = "\n".join(
        " | ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths))
        for row in rows
    )
    
    return f"{header}\n{separator}\n{body}"

# Usage
headers = ["Name", "Age", "GPA"]
rows = [
    ["Alice", 20, 3.8],
    ["Bob", 22, 3.5],
    ["Charlie", 21, 3.9]
]
print(format_table(headers, rows))
# Name    | Age | GPA
# --------+-----+----
# Alice   | 20  | 3.8
# Bob     | 22  | 3.5
# Charlie | 21  | 3.9
```

### Pattern 2: Progress Bar
```python
def progress_bar(current, total, width=50):
    """Display progress bar"""
    percent = current / total
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {percent:6.1%} ({current}/{total})"

# Usage
for i in range(101):
    print(f"\r{progress_bar(i, 100)}", end="", flush=True)
    time.sleep(0.05)
print()  # New line after complete
```

### Pattern 3: Aligned Output
```python
def print_record(label, value, width=20):
    """Print label-value pairs with alignment"""
    print(f"{label:.<{width}}: {value}")

# Usage
print_record("Name", "Alice Johnson", 30)
print_record("Age", 30, 30)
print_record("GPA", 3.85, 30)
print_record("Status", "Active", 30)
# Name........................: Alice Johnson
# Age.........................: 30
# GPA.........................: 3.85
# Status......................: Active
```

### Pattern 4: Currency Formatting
```python
def format_currency(amount, currency="USD"):
    """Format currency with symbol"""
    symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥"
    }
    symbol = symbols.get(currency, currency)
    
    if currency == "JPY":
        return f"{symbol}{amount:,.0f}"
    else:
        return f"{symbol}{amount:,.2f}"

# Usage
print(format_currency(1234.5))                 # → $1,234.50
print(format_currency(1234.5, "EUR"))          # → €1,234.50
print(format_currency(1234.5, "JPY"))          # → ¥1,235
```

### Pattern 5: Report Header
```python
def report_header(title, width=60):
    """Create centered report header"""
    border = "=" * width
    padded_title = f" {title} "
    
    return f"""
{border}
{padded_title:^{width}}
{border}
"""

# Usage
print(report_header("STUDENT GRADE REPORT"))
print(report_header("SALES SUMMARY - Q4 2025", 70))
```

### Pattern 6: Multiline Formatting
```python
def format_invoice(customer, items):
    """Format invoice with multiple items"""
    header = f"""
{'INVOICE':^50}
{'='*50}
Customer: {customer}
{'='*50}
{'Item':<30} {'Qty':>5} {'Price':>7} {'Total':>7}
{'-'*50}
"""
    
    lines = []
    total = 0
    for item, qty, price in items:
        subtotal = qty * price
        total += subtotal
        lines.append(f"{item:<30} {qty:>5} ${price:>6.2f} ${subtotal:>6.2f}")
    
    footer = f"""
{'-'*50}
{'TOTAL':>43} ${total:>6.2f}
{'='*50}
"""
    
    return header + "\n".join(lines) + footer

# Usage
items = [
    ("Widget A", 2, 19.99),
    ("Gadget B", 1, 49.99),
    ("Tool C", 5, 9.99)
]
print(format_invoice("Alice Johnson", items))
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: Missing Closing Brace
```python
# WRONG
f"Hello {name"                                 # SyntaxError

# RIGHT
f"Hello {name}"
```

### Error 2: Wrong Conversion Flag
```python
# WRONG
f"{value!x}"                                   # ValueError (x not valid)

# RIGHT
f"{value!r}"                                   # repr
f"{value!s}"                                   # str
f"{value!a}"                                   # ascii
```

### Error 3: Invalid Format Spec
```python
# WRONG
f"{value:abc}"                                 # ValueError

# RIGHT
f"{value:d}"                                   # integer
f"{value:.2f}"                                 # float with precision
f"{value:>10}"                                 # aligned
```

### Error 4: Type Mismatch
```python
# WRONG
value = "hello"
f"{value:d}"                                   # ValueError (can't format string as int)

# RIGHT
f"{value}"                                     # String as string
f"{value:>10}"                                 # String with alignment

num = 42
f"{num:d}"                                     # Integer as integer
```

### Error 5: Missing Argument
```python
# WRONG
"Hello {}".format()                            # IndexError

# RIGHT
"Hello {}".format("World")
"Hello {name}".format(name="World")
```

---

## PERFORMANCE TIPS

1. **F-strings are fastest** (Python 3.6+)
   ```python
   # FASTEST
   f"{name} is {age}"
   
   # SLOWER
   "{} is {}".format(name, age)
   
   # SLOWEST
   "%s is %s" % (name, age)
   ```

2. **Pre-compile format strings for repeated use**
   ```python
   # If formatting same pattern many times
   fmt = "{:<20} {:>10.2f}".format
   for name, value in data:
       print(fmt(name, value))
   ```

3. **Use join() for building large strings**
   ```python
   # EFFICIENT
   parts = []
   for item in items:
       parts.append(f"{item}")
   result = "\n".join(parts)
   
   # INEFFICIENT
   result = ""
   for item in items:
       result += f"{item}\n"
   ```

4. **Cache frequently used formats**
   ```python
   # Cache format strings
   DATE_FORMAT = "%Y-%m-%d"
   TIME_FORMAT = "%H:%M:%S"
   
   # Reuse
   dt.strftime(DATE_FORMAT)
   ```

---

## QUICK REFERENCE CHEAT SHEET

```python
# F-STRINGS (Preferred)
f"{var}"                    # Basic interpolation
f"{var:.2f}"                # Format specification
f"{var=}"                   # Debug format (3.8+)
f"{var!r}"                  # Repr conversion

# ALIGNMENT
f"{var:<10}"                # Left align
f"{var:>10}"                # Right align
f"{var:^10}"                # Center
f"{var:*^10}"               # Center with fill

# NUMBERS
f"{num:d}"                  # Integer
f"{num:05d}"                # Zero-padded
f"{num:,}"                  # Thousands separator
f"{num:.2f}"                # 2 decimal places
f"{num:+.2f}"               # Force sign
f"{num:#x}"                 # Hex with prefix
f"{num:.2%}"                # Percentage

# .format()
"{}".format(val)            # Positional
"{0} {1}".format(a, b)      # Indexed
"{name}".format(name=val)   # Named
"{:.2f}".format(pi)         # With format spec

# %-formatting
"%s" % val                  # String
"%d" % val                  # Integer
"%.2f" % val                # Float
"%(name)s" % {"name": val}  # Dict

# DATES
f"{dt:%Y-%m-%d}"            # ISO date
f"{dt:%B %d, %Y}"           # Long date
f"{dt:%I:%M %p}"            # 12-hour time
```

---

## Related Concepts
- [[STRING_METHODS]] - String manipulation methods
- [[INPUT_OUTPUT_OPERATIONS]] - Reading/writing formatted data
- [[DATA_TYPES]] - Type conversions for formatting
- [[FUNCTIONS]] - Custom formatting functions

---

## Metadata
**Created**: 2025-01-15
**Last Updated**: 2025-01-15
**Category**: Core Python
**Difficulty**: Intermediate
**Prerequisites**: Variables, Strings, Data Types
