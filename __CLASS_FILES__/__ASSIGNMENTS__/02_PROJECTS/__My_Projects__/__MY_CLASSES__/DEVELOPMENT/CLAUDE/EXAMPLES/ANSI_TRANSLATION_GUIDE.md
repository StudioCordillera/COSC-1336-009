# TRANSLATION GUIDE
## From What You Want → To ANSI Code

Stop thinking. Look up what you want. Copy the code.

---

## I WANT TO... → CODE

### Position & Movement

| I want to... | Code | Example |
|-------------|------|---------|
| Go to row 5, column 10 | `print(f'\033[{row};{col}H', end='')` | `print('\033[5;10H', end='')` |
| Go to top-left corner | `print('\033[H', end='')` | `print('\033[H', end='')` |
| Move up 3 lines | `print('\033[3A', end='')` | `print('\033[3A', end='')` |
| Move down 3 lines | `print('\033[3B', end='')` | `print('\033[3B', end='')` |
| Move right 5 chars | `print('\033[5C', end='')` | `print('\033[5C', end='')` |
| Move left 5 chars | `print('\033[5D', end='')` | `print('\033[5D', end='')` |
| Move to column 20 (same row) | `print('\033[20G', end='')` | `print('\033[20G', end='')` |
| Move to start of current line | `print('\r', end='')` | `print('\r', end='')` |

### Clearing

| I want to... | Code | Example |
|-------------|------|---------|
| Clear entire screen | `print('\033[2J', end='')` | `print('\033[2J', end='')` |
| Clear from cursor to end of screen | `print('\033[0J', end='')` | `print('\033[0J', end='')` |
| Clear from start to cursor | `print('\033[1J', end='')` | `print('\033[1J', end='')` |
| Clear entire line | `print('\033[2K', end='')` | `print('\033[2K', end='')` |
| Clear from cursor to end of line | `print('\033[0K', end='')` | `print('\033[0K', end='')` |
| Clear from start of line to cursor | `print('\033[1K', end='')` | `print('\033[1K', end='')` |

### Colors - Foreground (Text)

| I want to... | Code | Example |
|-------------|------|---------|
| Black text | `'\033[30m'` | `print('\033[30mBlack\033[0m')` |
| Red text | `'\033[31m'` | `print('\033[31mRed\033[0m')` |
| Green text | `'\033[32m'` | `print('\033[32mGreen\033[0m')` |
| Yellow text | `'\033[33m'` | `print('\033[33mYellow\033[0m')` |
| Blue text | `'\033[34m'` | `print('\033[34mBlue\033[0m')` |
| Magenta text | `'\033[35m'` | `print('\033[35mMagenta\033[0m')` |
| Cyan text | `'\033[36m'` | `print('\033[36mCyan\033[0m')` |
| White text | `'\033[37m'` | `print('\033[37mWhite\033[0m')` |
| Bright red text | `'\033[91m'` | `print('\033[91mBright Red\033[0m')` |
| Bright green text | `'\033[92m'` | `print('\033[92mBright Green\033[0m')` |
| Bright yellow text | `'\033[93m'` | `print('\033[93mBright Yellow\033[0m')` |
| Bright blue text | `'\033[94m'` | `print('\033[94mBright Blue\033[0m')` |
| Bright magenta text | `'\033[95m'` | `print('\033[95mBright Magenta\033[0m')` |
| Bright cyan text | `'\033[96m'` | `print('\033[96mBright Cyan\033[0m')` |
| Bright white text | `'\033[97m'` | `print('\033[97mBright White\033[0m')` |

### Colors - Background

| I want to... | Code | Example |
|-------------|------|---------|
| Black background | `'\033[40m'` | `print('\033[40m\033[97mText\033[0m')` |
| Red background | `'\033[41m'` | `print('\033[41m\033[97mText\033[0m')` |
| Green background | `'\033[42m'` | `print('\033[42m\033[30mText\033[0m')` |
| Yellow background | `'\033[43m'` | `print('\033[43m\033[30mText\033[0m')` |
| Blue background | `'\033[44m'` | `print('\033[44m\033[97mText\033[0m')` |
| Magenta background | `'\033[45m'` | `print('\033[45m\033[97mText\033[0m')` |
| Cyan background | `'\033[46m'` | `print('\033[46m\033[30mText\033[0m')` |
| White background | `'\033[47m'` | `print('\033[47m\033[30mText\033[0m')` |

### Colors - RGB (True Color)

| I want to... | Code | Example |
|-------------|------|---------|
| Custom RGB foreground | `f'\033[38;2;{r};{g};{b}m'` | `print('\033[38;2;255;100;50mOrange\033[0m')` |
| Custom RGB background | `f'\033[48;2;{r};{g};{b}m'` | `print('\033[48;2;100;200;255mSky\033[0m')` |

### Text Styles

| I want to... | Code | Example |
|-------------|------|---------|
| Bold text | `'\033[1m'` | `print('\033[1mBold\033[0m')` |
| Dim text | `'\033[2m'` | `print('\033[2mDim\033[0m')` |
| Italic text | `'\033[3m'` | `print('\033[3mItalic\033[0m')` |
| Underline text | `'\033[4m'` | `print('\033[4mUnderline\033[0m')` |
| Blinking text | `'\033[5m'` | `print('\033[5mBlink\033[0m')` |
| Reverse colors (swap fg/bg) | `'\033[7m'` | `print('\033[7mReverse\033[0m')` |
| Strikethrough text | `'\033[9m'` | `print('\033[9mStrike\033[0m')` |
| Reset ALL styles | `'\033[0m'` | `print('\033[31mRed\033[0m Normal')` |

### Cursor Visibility

| I want to... | Code | Example |
|-------------|------|---------|
| Hide cursor | `print('\033[?25l', end='')` | `print('\033[?25l', end='')` |
| Show cursor | `print('\033[?25h', end='')` | `print('\033[?25h', end='')` |

---

## COMMON COMBINATIONS

### Error Message (Red + Bold)
```python
print('\033[31m\033[1mERROR: File not found\033[0m')
```

### Success Message (Green + Bold)
```python
print('\033[32m\033[1m✓ Success!\033[0m')
```

### Warning Message (Yellow + Bold)
```python
print('\033[33m\033[1m⚠ Warning: Low disk space\033[0m')
```

### Info Message (Cyan)
```python
print('\033[36mℹ Info: Update available\033[0m')
```

### Highlighted Selection (Reverse Video)
```python
print('\033[7m  Selected Item  \033[0m')
```

### Button (Bold + Cyan)
```python
print('\033[1m\033[36m[  OK  ]\033[0m')
```

### Disabled Item (Dim)
```python
print('\033[2m  (Disabled Option)\033[0m')
```

### Title Bar (White on Blue + Bold)
```python
print('\033[44m\033[97m\033[1m     MY APPLICATION     \033[0m')
```

---

## FORM PATTERNS - What You Loved

### Basic Input Field
```python
print('\033[5;1H', end='')  # Position
print('Name: [                    ]', end='')
print('\033[5;8H', end='')  # Position cursor in field
name = input()
```

### Field with Label
```python
label = "Email:"
print(f'\033[5;1H{label} [', end='')
print('\033[?25h', end='')  # Show cursor
value = input()
print('\033[?25l', end='')  # Hide cursor
print(f'\033[5;{len(label)+3}H{value}]', end='')
```

### Multi-Field Form
```python
fields = {
    'Username': (5, ''),
    'Email': (7, ''),
    'Password': (9, '')
}

for label, (row, value) in fields.items():
    print(f'\033[{row};1H{label}: [', end='')

# Collect each
for label, (row, _) in fields.items():
    print(f'\033[{row};{len(label)+4}H', end='')
    print('\033[?25h', end='')
    fields[label] = (row, input())
    print('\033[?25l', end='')
```

### Field with Validation Feedback
```python
row = 5
label = "Email:"

print(f'\033[{row};1H{label} [', end='')
print('\033[?25h', end='')
value = input()
print('\033[?25l', end='')

# Validate
if '@' in value:
    print(f'\033[{row+1};{len(label)+3}H\033[32m✓ Valid\033[0m', end='')
else:
    print(f'\033[{row+1};{len(label)+3}H\033[31m✗ Invalid email\033[0m', end='')
```

### Password Field (Hidden Input)
```python
import getpass

row = 7
label = "Password:"

print(f'\033[{row};1H{label} [', end='')
print('\033[{};{}H'.format(row, len(label)+4), end='')
print('\033[?25h', end='')
password = getpass.getpass('')
print('\033[?25l', end='')

# Show dots
print(f'\033[{row};{len(label)+4}H{"•" * len(password)}]', end='')
```

### Checkbox Field
```python
row = 10
checked = False

def draw_checkbox():
    mark = '✓' if checked else ' '
    print(f'\033[{row};1H[{mark}] Accept terms', end='')

draw_checkbox()

# Toggle with keypress
key = input()
if key.lower() == 'y':
    checked = True
    draw_checkbox()
```

### Dropdown/Select Field
```python
options = ['Option 1', 'Option 2', 'Option 3']
selected = 0
row = 5

def draw_select():
    print(f'\033[{row};1HSelect: [{options[selected]}]', end='')
    for i, opt in enumerate(options):
        print(f'\033[{row+2+i};3H{"►" if i == selected else " "} {opt}', end='')

draw_select()

# Navigate with w/s
while True:
    key = input().lower()
    if key == 'w' and selected > 0:
        selected -= 1
        draw_select()
    elif key == 's' and selected < len(options) - 1:
        selected += 1
        draw_select()
    elif key == '\n':
        break
```

### Slider/Range Field
```python
row = 8
value = 50  # 0-100
width = 30

def draw_slider():
    pos = int((value / 100) * width)
    bar = '─' * pos + '●' + '─' * (width - pos)
    print(f'\033[{row};1HVolume: [{bar}] {value}%', end='')

draw_slider()

# Adjust with keys
while True:
    key = input().lower()
    if key == 'a' and value > 0:
        value -= 5
        draw_slider()
    elif key == 'd' and value < 100:
        value += 5
        draw_slider()
    elif key == '\n':
        break
```

### Text Area (Multi-line)
```python
start_row = 5
max_lines = 5
lines = [''] * max_lines
current_line = 0

# Draw border
print(f'\033[{start_row-1};1H┌{"─" * 50}┐')
for i in range(max_lines):
    print(f'\033[{start_row+i};1H│{" " * 50}│')
print(f'\033[{start_row+max_lines};1H└{"─" * 50}┘')

# Collect input
for i in range(max_lines):
    print(f'\033[{start_row+i};2H', end='')
    print('\033[?25h', end='')
    lines[i] = input()[:50]  # Limit width
    print('\033[?25l', end='')
```

### Date Picker
```python
row = 10
day = 1
month = 1
year = 2024

def draw_date():
    print(f'\033[{row};1HDate: [', end='')
    print(f'{day:02d}', end='')
    print(' / ', end='')
    print(f'{month:02d}', end='')
    print(' / ', end='')
    print(f'{year}', end='')
    print(']', end='')

draw_date()

# Navigate between fields with tab, adjust with up/down
```

### Auto-Complete Field
```python
suggestions = ['apple', 'apricot', 'avocado', 'banana', 'berry']
row = 5
input_text = ''

def draw_suggestions():
    matches = [s for s in suggestions if s.startswith(input_text)]
    for i, match in enumerate(matches[:5]):
        print(f'\033[{row+2+i};3H{match}', end='')
    # Clear rest
    for i in range(len(matches), 5):
        print(f'\033[{row+2+i};3H{" " * 20}', end='')

# As user types, update suggestions
```

---

## PYTHON SHORTCUTS

### All-in-One Position + Write
```python
def write_at(row, col, text):
    print(f'\033[{row};{col}H{text}', end='')
    sys.stdout.flush()

write_at(5, 10, "Hello")
```

### Colored Text Helper
```python
def colored(text, color):
    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'cyan': '\033[36m',
    }
    return f"{colors[color]}{text}\033[0m"

print(colored("Error!", "red"))
```

### Box Drawing Helper
```python
def draw_box(row, col, width, height):
    # Top
    write_at(row, col, '┌' + '─' * width + '┐')
    # Sides
    for i in range(1, height + 1):
        write_at(row + i, col, '│' + ' ' * width + '│')
    # Bottom
    write_at(row + height + 1, col, '└' + '─' * width + '┘')
```

### Center Text Helper
```python
def center_text(row, text, width=80):
    padding = (width - len(text)) // 2
    write_at(row, padding, text)
```

---

## CHEAT SHEET - Print & Tape to Wall

```
MOVE:    \033[{row};{col}H     Go to position
CLEAR:   \033[2J               Clear screen
         \033[2K               Clear line

COLOR:   \033[31m              Red
         \033[32m              Green
         \033[33m              Yellow
         \033[36m              Cyan
         \033[0m               Reset

STYLE:   \033[1m               Bold
         \033[2m               Dim
         \033[7m               Reverse

CURSOR:  \033[?25l             Hide
         \033[?25h             Show

FORM:    print(f'\033[{r};{c}H{label}: [')
         value = input()
```

---

## TESTING REFERENCE

Want to see what a code does? Run this:

```python
# Test any ANSI code
code = '\033[31m'  # Put code here
print(f"{code}This is the effect\033[0m")
```

Or test positioning:

```python
# See where position goes
row, col = 10, 20
print(f'\033[{row};{col}H' + '⬤')  # Puts dot at that spot
input()  # Pause to see it
```
