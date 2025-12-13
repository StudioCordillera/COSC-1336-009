# ANSI Escape Codes - Python Guide

## Core Definition
**ANSI Escape Codes** are control sequences that manipulate the terminal cursor, colors, and formatting. They always start with the escape character (byte 27).

**Tags**: #ansi #terminal #escape-codes #python #cli

---

## THE ESCAPE CHARACTER

```python
# All three are IDENTICAL - they all represent ASCII byte 27 (ESC)
\x1b   # Hexadecimal notation (most common)
\033   # Octal notation (also common)
\e     # Escape notation (less common)
```

**Example:**
```python
'\x1b[2J'  # Clear screen
'\033[2J'  # Same thing, different notation
```

---

## MENTAL MODEL: ESCAPE CODES ARE FUNCTION CALLS

Think of escape sequences like function calls:

```
\x1b[      # Call a function
0;1;34     # Function arguments (0, 1, 34)
m          # Function name
```

This is like calling `m(0, 1, 34)` in Python.

Similarly, `\x1b[A` is just `A()` with no arguments.

---

## CONTROL SEQUENCE FORMAT

```
\x1b + "[" + <numbers separated by ";"> + <letter>
```

- **\x1b[** = CSI (Control Sequence Introducer)
- **Numbers** = Arguments to the function
- **Letter** = The function name

---

## CURSOR MOVEMENT FUNCTIONS

| Code | Name | Default Args | Description |
|------|------|--------------|-------------|
| `A` | Cursor Up | (n=1) | Move cursor up by n lines |
| `B` | Cursor Down | (n=1) | Move cursor down by n lines |
| `C` | Cursor Forward | (n=1) | Move cursor right by n columns |
| `D` | Cursor Back | (n=1) | Move cursor left by n columns |
| `E` | Cursor Next Line | (n=1) | Move to beginning of line, n lines down |
| `F` | Cursor Previous Line | (n=1) | Move to beginning of line, n lines up |
| `G` | Cursor Horizontal Absolute | (n=1) | Move cursor to column n |
| `H` | Cursor Position | (n=1, m=1) | Move to row n, column m (from top-left) |
| `s` | Save Cursor Position | () | Save current cursor position |
| `u` | Restore Cursor Position | () | Restore to saved position |

**Python Examples:**
```python
print('\x1b[5A')        # Move up 5 lines - A(5)
print('\x1b[10;20H')    # Move to row 10, col 20 - H(10, 20)
print('\x1b[s')         # Save position - s()
print('\x1b[u')         # Restore position - u()
```

---

## SCREEN CLEARING FUNCTIONS

| Code | Name | Default | Description |
|------|------|---------|-------------|
| `J` | Erase in Display | (n=0) | Clear screen (0=cursor down, 1=cursor up, 2=entire screen, 3=entire screen + scrollback) |
| `K` | Erase in Line | (n=0) | Clear line (0=cursor right, 1=cursor left, 2=entire line) |
| `S` | Scroll Up | (n=1) | Scroll window up by n lines |
| `T` | Scroll Down | (n=1) | Scroll window down by n lines |

**Python Examples:**
```python
print('\x1b[2J')        # Clear entire screen - J(2)
print('\x1b[2K')        # Clear entire line - K(2)
print('\x1b[3J')        # Clear screen + scrollback - J(3)
```

---

## SGR (SELECT GRAPHICS RENDITION) - THE `m` FUNCTION

The `m` function is special - it controls colors and text formatting.

### Text Attributes

| Code | Effect |
|------|--------|
| `0` | Reset all attributes |
| `1` | Bold (or bright) |
| `3` | Italic |
| `4` | Underline |

### Basic Colors (30-37 foreground, 40-47 background)

| Code  | Foreground | Background | Color   |
| ----- | ---------- | ---------- | ------- |
| 30/40 | `\x1b[30m` | `\x1b[40m` | Black   |
| 31/41 | `\x1b[31m` | `\x1b[41m` | Red     |
| 32/42 | `\x1b[32m` | `\x1b[42m` | Green   |
| 33/43 | `\x1b[33m` | `\x1b[43m` | Yellow  |
| 34/44 | `\x1b[34m` | `\x1b[44m` | Blue    |
| 35/45 | `\x1b[35m` | `\x1b[45m` | Magenta |
| 36/46 | `\x1b[36m` | `\x1b[46m` | Cyan    |
| 37/47 | `\x1b[37m` | `\x1b[47m` | White   |

### Bright Colors (90-97 foreground, 100-107 background)

Same colors as above but noticeably brighter.

### 256-Color Palette

```python
# Foreground: 38;5;n
print('\x1b[38;5;34m')   # Text color = palette index 34

# Background: 48;5;n  
print('\x1b[48;5;196m')  # Background = palette index 196
```

### RGB True Color (24-bit)

```python
# Foreground: 38;2;r;g;b
print('\x1b[38;2;255;100;0m')   # Text = RGB(255, 100, 0)

# Background: 48;2;r;g;b
print('\x1b[48;2;0;150;255m')   # Background = RGB(0, 150, 255)
```

### Combining SGR Arguments

Multiple SGR codes can be combined with semicolons:

```python
# Bold + Red text
print('\x1b[1;31m')      # m(1, 31)

# Reset + Bold + Italic + Magenta
print('\x1b[0;1;3;35m')  # m(0, 1, 3, 35)

# Always reset before text, then reset after
print('\x1b[0;1;32mSuccess!\x1b[0m')  # Bold green "Success!"
```

---

## COLOR PALETTE ORDERING

The basic 8 colors are ordered by usefulness:

0. **Black** - Avoid for text (may be invisible on dark terminals)
1. **Red** - Failures, errors
2. **Green** - Success, completion
3. **Yellow** - Warnings, caution
4. **Blue** - Information, less critical
5. **Magenta** - Special states
6. **Cyan** - Decoration
7. **White** - Avoid for text (may be invisible on light terminals)

---

## CURSOR VISIBILITY

```python
'\x1b[?25h'   # Show cursor (high = 1 = visible)
'\x1b[?25l'   # Hide cursor (low = 0 = invisible)
```

**Use case:** Hide cursor when redrawing menus or status lines to prevent flicker.

```python
print('\x1b[?25l', end='')  # Hide cursor
# Draw your menu
print('\x1b[?25h', end='')  # Show cursor
```

---

## CARRIAGE RETURN

```python
'\r'           # Move cursor to start of line (like \x1b[1G)
```

**Use case:** Update progress on same line without creating new lines.

```python
import time
for i in range(101):
    print(f'\rProgress: {i}%', end='', flush=True)
    time.sleep(0.05)
```

---

## PYTHON PATTERNS FOR MENUS

### Clear Screen and Reset
```python
def clear():
    print('\x1b[2J\x1b[H', end='')  # Clear + Home
```

### Draw Box
```python
def draw_box(width, height, row, col):
    # Top border
    print(f'\x1b[{row};{col}H┌{"─" * width}┐')
    
    # Sides
    for i in range(height):
        print(f'\x1b[{row + i + 1};{col}H│{" " * width}│')
    
    # Bottom border
    print(f'\x1b[{row + height + 1};{col}H└{"─" * width}┘')
```

### Colored Text Helper
```python
def colored(text, fg=None, bg=None, bold=False):
    codes = []
    if bold:
        codes.append('1')
    if fg:
        codes.append(str(30 + fg))  # fg is 0-7
    if bg:
        codes.append(str(40 + bg))
    
    if codes:
        return f'\x1b[{";".join(codes)}m{text}\x1b[0m'
    return text

# Usage
print(colored("Error!", fg=1, bold=True))  # Bold red
print(colored("Success!", fg=2))           # Green
```

### Menu with Hidden Cursor
```python
def show_menu():
    print('\x1b[?25l', end='')  # Hide cursor
    print('\x1b[2J\x1b[H', end='')  # Clear screen, home
    
    # Draw menu
    print('┌─────────────────┐')
    print('│  Main Menu      │')
    print('├─────────────────┤')
    print('│ 1. Option One   │')
    print('│ 2. Option Two   │')
    print('└─────────────────┘')
    
    print('\x1b[?25h', end='')  # Show cursor
```

---

## PRACTICE SEQUENCES

Try to decode these:

1. `\x1b[3A\x1b[4D` = Move up 3, then left 4
2. `\x1b[2J\x1b[H` = Clear screen, move to home
3. `\x1b[1;31mERROR\x1b[0m` = Bold red "ERROR", then reset
4. `\x1b[38;2;255;255;0m` = RGB yellow text
5. `\x1b[s\x1b[10;20HX\x1b[u` = Save pos, move to (10,20), print X, restore pos

---

## WINDOWS COMPATIBILITY

On Windows 10+, enable ANSI support first:

```python
import sys
import os

if sys.platform == 'win32':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
```

---

## QUICK REFERENCE TABLE

| What | Code | Example |
|------|------|---------|
| Clear screen | `\x1b[2J` | `print('\x1b[2J')` |
| Move cursor | `\x1b[{row};{col}H` | `print('\x1b[5;10H')` |
| Hide cursor | `\x1b[?25l` | `print('\x1b[?25l', end='')` |
| Show cursor | `\x1b[?25h` | `print('\x1b[?25h', end='')` |
| Red text | `\x1b[31m` | `print('\x1b[31mError\x1b[0m')` |
| Bold | `\x1b[1m` | `print('\x1b[1mBold\x1b[0m')` |
| Reset | `\x1b[0m` | `print('Text\x1b[0m')` |

---

## SEE ALSO
- Original source: https://notes.burke.libbey.me/ansi-escape-codes/
- [ASCII-ESCAPE-CODES-REFERENCE.md](ASCII-ESCAPE-CODES-REFERENCE.md) - Complete code reference
- [CLI-Terminal-Styling-Complete-Reference.md](CLI-Terminal-Styling-Complete-Reference.md) - Full terminal styling guide

---

**Last Updated**: December 8, 2025  
**Tags**: #ansi #python #terminal #cli #escape-codes #tutorial
