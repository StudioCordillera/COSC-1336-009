# CLI Menu Design Reference

> **ctypes, msvcrt + ASCII mappings for menu functionality: keyboard events, mouse events, and interactivity**

---

## Table of Contents

1. [Windows Console API Overview](#windows-console-api-overview)
2. [ASCII Character Mappings](#ascii-character-mappings)
3. [msvcrt Keyboard Event Handling](#msvcrt-keyboard-event-handling)
4. [ctypes Mouse Event Handling](#ctypes-mouse-event-handling)
5. [Complete Integration Patterns](#complete-integration-patterns)
6. [Implementation Examples](#implementation-examples)

---

## Windows Console API Overview

### ANSI ESCAPE SEQUENCES - Operation | Parameters | Action | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# CURSOR POSITIONING
# ═══════════════════════════════════════════════════════════════════════════
f'\033[{row};{col}H'         # row:int, col:int | Set cursor absolute position (1-based) | No output, moves cursor
f'\033[{n}A'                 # n:int | Move cursor up n lines | No output, moves cursor
f'\033[{n}B'                 # n:int | Move cursor down n lines | No output, moves cursor
f'\033[{n}C'                 # n:int | Move cursor forward n columns | No output, moves cursor
f'\033[{n}D'                 # n:int | Move cursor backward n columns | No output, moves cursor
'\033[H'                     # None | Move cursor to home (1,1) | No output, moves cursor
f'\033[{row}H'               # row:int | Move cursor to row (column 1) | No output, moves cursor
f'\033[{col}G'               # col:int | Move cursor to column (current row) | No output, moves cursor
'\033[s'                     # None | Save cursor position | No output, saves position
'\033[u'                     # None | Restore cursor position | No output, restores position

# ═══════════════════════════════════════════════════════════════════════════
# CURSOR VISIBILITY
# ═══════════════════════════════════════════════════════════════════════════
'\033[?25h'                  # None | Show cursor | No output, shows cursor
'\033[?25l'                  # None | Hide cursor | No output, hides cursor

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN CONTROL
# ═══════════════════════════════════════════════════════════════════════════
'\033[2J'                    # None | Clear entire screen | No output, clears all
'\033[H\033[2J'              # None | Clear screen + home cursor | No output, clears + moves to (1,1)
'\033[0J'                    # None | Clear from cursor to end | No output, clears below
'\033[1J'                    # None | Clear from cursor to beginning | No output, clears above
'\033[2K'                    # None | Clear entire line | No output, clears current line
'\033[0K'                    # None | Clear from cursor to end of line | No output, clears right
'\033[1K'                    # None | Clear from cursor to start of line | No output, clears left

# ═══════════════════════════════════════════════════════════════════════════
# STANDARD COLORS (30-37 foreground, 40-47 background)
# ═══════════════════════════════════════════════════════════════════════════
'\033[30m'                   # None | Set foreground black | No output, affects subsequent text
'\033[31m'                   # None | Set foreground red | No output, affects subsequent text
'\033[32m'                   # None | Set foreground green | No output, affects subsequent text
'\033[33m'                   # None | Set foreground yellow | No output, affects subsequent text
'\033[34m'                   # None | Set foreground blue | No output, affects subsequent text
'\033[35m'                   # None | Set foreground magenta | No output, affects subsequent text
'\033[36m'                   # None | Set foreground cyan | No output, affects subsequent text
'\033[37m'                   # None | Set foreground white | No output, affects subsequent text
'\033[40m'                   # None | Set background black | No output, affects subsequent text
'\033[41m'                   # None | Set background red | No output, affects subsequent text
'\033[42m'                   # None | Set background green | No output, affects subsequent text
'\033[43m'                   # None | Set background yellow | No output, affects subsequent text
'\033[44m'                   # None | Set background blue | No output, affects subsequent text
'\033[45m'                   # None | Set background magenta | No output, affects subsequent text
'\033[46m'                   # None | Set background cyan | No output, affects subsequent text
'\033[47m'                   # None | Set background white | No output, affects subsequent text

# ═══════════════════════════════════════════════════════════════════════════
# BRIGHT COLORS (90-97 foreground, 100-107 background)
# ═══════════════════════════════════════════════════════════════════════════
'\033[90m'                   # None | Set foreground bright black (gray) | No output, affects subsequent text
'\033[91m'                   # None | Set foreground bright red | No output, affects subsequent text
'\033[92m'                   # None | Set foreground bright green | No output, affects subsequent text
'\033[93m'                   # None | Set foreground bright yellow | No output, affects subsequent text
'\033[94m'                   # None | Set foreground bright blue | No output, affects subsequent text
'\033[95m'                   # None | Set foreground bright magenta | No output, affects subsequent text
'\033[96m'                   # None | Set foreground bright cyan | No output, affects subsequent text
'\033[97m'                   # None | Set foreground bright white | No output, affects subsequent text
'\033[100m'                  # None | Set background bright black (gray) | No output, affects subsequent text
'\033[101m'                  # None | Set background bright red | No output, affects subsequent text
'\033[102m'                  # None | Set background bright green | No output, affects subsequent text
'\033[103m'                  # None | Set background bright yellow | No output, affects subsequent text
'\033[104m'                  # None | Set background bright blue | No output, affects subsequent text
'\033[105m'                  # None | Set background bright magenta | No output, affects subsequent text
'\033[106m'                  # None | Set background bright cyan | No output, affects subsequent text
'\033[107m'                  # None | Set background bright white | No output, affects subsequent text

# ═══════════════════════════════════════════════════════════════════════════
# 256-COLOR PALETTE (8-bit colors)
# ═══════════════════════════════════════════════════════════════════════════
f'\033[38;5;{n}m'            # n:int (0-255) | Set foreground to 256-color palette | No output, affects subsequent text
f'\033[48;5;{n}m'            # n:int (0-255) | Set background to 256-color palette | No output, affects subsequent text

# ═══════════════════════════════════════════════════════════════════════════
# RGB TRUE COLOR (24-bit colors)
# ═══════════════════════════════════════════════════════════════════════════
f'\033[38;2;{r};{g};{b}m'   # r:int(0-255), g:int(0-255), b:int(0-255) | Set foreground RGB | No output, affects subsequent text
f'\033[48;2;{r};{g};{b}m'   # r:int(0-255), g:int(0-255), b:int(0-255) | Set background RGB | No output, affects subsequent text

# ═══════════════════════════════════════════════════════════════════════════
# TEXT FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
'\033[0m'                    # None | Reset all attributes | No output, returns to defaults
'\033[1m'                    # None | Enable bold/bright | No output, affects subsequent text
'\033[2m'                    # None | Enable dim | No output, affects subsequent text
'\033[3m'                    # None | Enable italic | No output, affects subsequent text
'\033[4m'                    # None | Enable underline | No output, affects subsequent text
'\033[5m'                    # None | Enable blink | No output, affects subsequent text
'\033[7m'                    # None | Enable reverse (invert colors) | No output, affects subsequent text
'\033[8m'                    # None | Enable hidden | No output, affects subsequent text
'\033[9m'                    # None | Enable strikethrough | No output, affects subsequent text
'\033[22m'                   # None | Disable bold/dim | No output, affects subsequent text
'\033[23m'                   # None | Disable italic | No output, affects subsequent text
'\033[24m'                   # None | Disable underline | No output, affects subsequent text
'\033[25m'                   # None | Disable blink | No output, affects subsequent text
'\033[27m'                   # None | Disable reverse | No output, affects subsequent text
'\033[28m'                   # None | Disable hidden | No output, affects subsequent text
'\033[29m'                   # None | Disable strikethrough | No output, affects subsequent text

# ═══════════════════════════════════════════════════════════════════════════
# COMBINED OPERATIONS (Common Patterns)
# ═══════════════════════════════════════════════════════════════════════════
f'\033[{row};{col}H{text}'   # row:int, col:int, text:str | Position + print text | Outputs text at position
f'\033[2J\033[H'             # None | Clear screen + home cursor | No output, fresh screen
f'\033[{color}m{text}\033[0m' # color:str, text:str | Colorize text + reset | Outputs colored text
f'\033[1m\033[4m{text}\033[0m' # text:str | Bold + underline + reset | Outputs formatted text
```

### MSVCRT MODULE - Function | Parameters | Action | Returns

```python
# ═══════════════════════════════════════════════════════════════════════════
# KEYBOARD INPUT (Non-blocking, Windows Console)
# ═══════════════════════════════════════════════════════════════════════════
import msvcrt

msvcrt.kbhit()               # None | Check if key is waiting in buffer | Returns bool (True if key pressed)
msvcrt.getch()               # None (blocking) | Read single byte from keyboard | Returns bytes (e.g., b'a', b'\r', b'\xe0')
msvcrt.getwch()              # None (blocking) | Read single Unicode char from keyboard | Returns str (e.g., 'a', '\r')
msvcrt.ungetch(byte)         # byte:bytes | Push byte back to input buffer | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# SPECIAL KEY DETECTION PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
# Arrow keys return TWO bytes: b'\xe0' (or b'\x00') followed by code
# Common codes:
#   b'H' = Up arrow (0x48)
#   b'P' = Down arrow (0x50)
#   b'K' = Left arrow (0x4B)
#   b'M' = Right arrow (0x4D)
#   b'\r' = Enter (0x0D)
#   b' ' = Space (0x20)
#   b'\x1b' = Escape (0x1B)
#   b'\x03' = Ctrl+C (0x03)

# Usage Pattern:
key = msvcrt.getch()         # Get first byte
if key in (b'\xe0', b'\x00'): # Check for special key prefix
    key = msvcrt.getch()     # Get second byte (actual key code)
```

### CTYPES WINDOWS CONSOLE API - Structure/Function | Fields/Parameters | Action | Returns

```python
# ═══════════════════════════════════════════════════════════════════════════
# SETUP & IMPORTS
# ═══════════════════════════════════════════════════════════════════════════
import ctypes
from ctypes import wintypes

kernel32 = ctypes.windll.kernel32  # Load Windows kernel32.dll

# ═══════════════════════════════════════════════════════════════════════════
# STRUCTURES (ctypes.Structure subclasses)
# ═══════════════════════════════════════════════════════════════════════════
# COORD structure (represents console coordinates)
class COORD(ctypes.Structure):
    _fields_ = [
        ('X', ctypes.c_short),   # X coordinate (0-based)
        ('Y', ctypes.c_short),   # Y coordinate (0-based)
    ]

# KEY_EVENT_RECORD structure (keyboard event data)
class KEY_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ('bKeyDown', wintypes.BOOL),          # True if key pressed, False if released
        ('wRepeatCount', wintypes.WORD),      # Repeat count
        ('wVirtualKeyCode', wintypes.WORD),   # Virtual key code
        ('wVirtualScanCode', wintypes.WORD),  # Scan code
        ('uChar', wintypes.WCHAR),            # Unicode character
        ('dwControlKeyState', wintypes.DWORD) # Control key state flags
    ]

# MOUSE_EVENT_RECORD structure (mouse event data)
class MOUSE_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ('dwMousePosition', COORD),           # Mouse position (0-based)
        ('dwButtonState', wintypes.DWORD),    # Button state flags
        ('dwControlKeyState', wintypes.DWORD),# Control key state flags
        ('dwEventFlags', wintypes.DWORD)      # Event type flags
    ]

# INPUT_RECORD union (holds any console input event)
class INPUT_RECORD(ctypes.Structure):
    class _EVENT(ctypes.Union):
        _fields_ = [
            ('KeyEvent', KEY_EVENT_RECORD),
            ('MouseEvent', MOUSE_EVENT_RECORD),
        ]
    _fields_ = [
        ('EventType', wintypes.WORD),  # Event type (1=KEY_EVENT, 2=MOUSE_EVENT)
        ('Event', _EVENT)
    ]

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS (Windows Console API)
# ═══════════════════════════════════════════════════════════════════════════
STD_INPUT_HANDLE             # -10 | Standard input handle identifier | Used with GetStdHandle()
STD_OUTPUT_HANDLE            # -11 | Standard output handle identifier | Used with GetStdHandle()
STD_ERROR_HANDLE             # -12 | Standard error handle identifier | Used with GetStdHandle()

# Console Mode Flags (for GetConsoleMode/SetConsoleMode)
ENABLE_MOUSE_INPUT           # 0x0010 | Enable mouse input events | OR with mode to enable
ENABLE_QUICK_EDIT_MODE       # 0x0040 | Enable QuickEdit (MUST DISABLE for mouse) | AND with ~0x0040 to disable
ENABLE_EXTENDED_FLAGS        # 0x0080 | Enable extended flags | Required when modifying QuickEdit
ENABLE_PROCESSED_INPUT       # 0x0001 | Enable Ctrl+C processing | Usually enabled by default
ENABLE_LINE_INPUT            # 0x0002 | Enable line buffering | Usually enabled by default
ENABLE_ECHO_INPUT            # 0x0004 | Enable input echo | Usually enabled by default
ENABLE_WINDOW_INPUT          # 0x0008 | Enable window resize events | OR with mode to enable
ENABLE_VIRTUAL_TERMINAL_PROCESSING # 0x0004 (output mode) | Enable ANSI escape sequences | OR with output mode to enable

# Event Type Constants
KEY_EVENT                    # 1 | Keyboard event | Check EventType in INPUT_RECORD
MOUSE_EVENT                  # 2 | Mouse event | Check EventType in INPUT_RECORD

# Mouse Event Flags (dwEventFlags)
FROM_LEFT_1ST_BUTTON_PRESSED # 0x0001 | Left button pressed | Check dwButtonState
RIGHTMOST_BUTTON_PRESSED     # 0x0002 | Right button pressed | Check dwButtonState
MOUSE_MOVED                  # 0x0001 | Mouse moved | Check dwEventFlags
DOUBLE_CLICK                 # 0x0002 | Double click | Check dwEventFlags
MOUSE_WHEELED                # 0x0004 | Mouse wheel scrolled | Check dwEventFlags

# ═══════════════════════════════════════════════════════════════════════════
# WINDOWS CONSOLE API FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
kernel32.GetStdHandle(handle_id)
    # handle_id:int (-10=stdin, -11=stdout, -12=stderr)
    # Action: Get handle to standard device
    # Returns: Handle (wintypes.HANDLE) or INVALID_HANDLE_VALUE on error

kernel32.GetConsoleMode(handle, mode_ptr)
    # handle:HANDLE, mode_ptr:ctypes.pointer(wintypes.DWORD)
    # Action: Retrieve current console mode flags
    # Returns: bool (True if success, False if error)
    # Side effect: Writes mode value to mode_ptr

kernel32.SetConsoleMode(handle, mode)
    # handle:HANDLE, mode:DWORD (int with flag bits)
    # Action: Set console mode flags
    # Returns: bool (True if success, False if error)
    # Example: mode = ENABLE_MOUSE_INPUT | ENABLE_EXTENDED_FLAGS

kernel32.ReadConsoleInputW(handle, buffer_ptr, length, events_read_ptr)
    # handle:HANDLE, buffer_ptr:ctypes.pointer(INPUT_RECORD), length:int, events_read_ptr:ctypes.pointer(wintypes.DWORD)
    # Action: Read console input events (keyboard, mouse, etc.)
    # Returns: bool (True if success, False if error)
    # Side effects: Writes INPUT_RECORD to buffer_ptr, writes count to events_read_ptr

kernel32.WriteConsoleW(handle, buffer, length, written_ptr, reserved)
    # handle:HANDLE, buffer:str, length:int, written_ptr:ctypes.pointer(wintypes.DWORD), reserved:None
    # Action: Write text directly to console (bypasses buffering)
    # Returns: bool (True if success, False if error)

kernel32.SetConsoleCursorPosition(handle, coord)
    # handle:HANDLE, coord:COORD(X, Y)
    # Action: Set cursor position using Windows API (0-based)
    # Returns: bool (True if success, False if error)

kernel32.GetConsoleScreenBufferInfo(handle, csbi_ptr)
    # handle:HANDLE, csbi_ptr:ctypes.pointer(CONSOLE_SCREEN_BUFFER_INFO)
    # Action: Get console window size, cursor position, attributes
    # Returns: bool (True if success, False if error)

kernel32.FillConsoleOutputCharacterW(handle, char, length, coord, written_ptr)
    # handle:HANDLE, char:wchar, length:int, coord:COORD, written_ptr:ctypes.pointer(wintypes.DWORD)
    # Action: Fill region with character (for fast clearing)
    # Returns: bool (True if success, False if error)

kernel32.FillConsoleOutputAttribute(handle, attr, length, coord, written_ptr)
    # handle:HANDLE, attr:WORD, length:int, coord:COORD, written_ptr:ctypes.pointer(wintypes.DWORD)
    # Action: Fill region with color attributes
    # Returns: bool (True if success, False if error)

kernel32.SetConsoleTextAttribute(handle, attributes)
    # handle:HANDLE, attributes:WORD (color flags)
    # Action: Set text color/background (alternative to ANSI codes)
    # Returns: bool (True if success, False if error)

# ═══════════════════════════════════════════════════════════════════════════
# COMMON USAGE PATTERNS
# ═══════════════════════════════════════════════════════════════════════════
# Pattern 1: Enable ANSI escape sequences
stdin_handle = kernel32.GetStdHandle(-11)  # Get stdout handle
mode = wintypes.DWORD()
kernel32.GetConsoleMode(stdin_handle, ctypes.byref(mode))  # Read current mode
mode.value |= 0x0004  # Enable ENABLE_VIRTUAL_TERMINAL_PROCESSING
kernel32.SetConsoleMode(stdin_handle, mode.value)  # Write mode back

# Pattern 2: Enable mouse input + disable QuickEdit
stdin = kernel32.GetStdHandle(-10)  # Get stdin handle
mode = wintypes.DWORD()
kernel32.GetConsoleMode(stdin, ctypes.byref(mode))
mode.value |= 0x0010   # Enable ENABLE_MOUSE_INPUT
mode.value |= 0x0080   # Enable ENABLE_EXTENDED_FLAGS (required for QuickEdit)
mode.value &= ~0x0040  # Disable ENABLE_QUICK_EDIT_MODE (prevents mouse capture interference)
kernel32.SetConsoleMode(stdin, mode.value)

# Pattern 3: Read mouse event
input_record = INPUT_RECORD()
events_read = wintypes.DWORD()
if kernel32.ReadConsoleInputW(stdin, ctypes.byref(input_record), 1, ctypes.byref(events_read)):
    if input_record.EventType == 2:  # MOUSE_EVENT
        mouse = input_record.Event.MouseEvent
        x = mouse.dwMousePosition.X  # 0-based Windows coordinate
        y = mouse.dwMousePosition.Y  # 0-based Windows coordinate
        # Convert to ANSI 1-based: ansi_x = x + 1, ansi_y = y + 1

# Pattern 4: Check for left click
if mouse.dwButtonState & 0x0001:  # FROM_LEFT_1ST_BUTTON_PRESSED
    print("Left button clicked")

# Pattern 5: Check for mouse movement
if mouse.dwEventFlags & 0x0001:  # MOUSE_MOVED
    print(f"Mouse moved to ({x}, {y})")
```

### COORDINATE SYSTEM CONVERSIONS - Source → Target | Formula | Result

```python
# ═══════════════════════════════════════════════════════════════════════════
# WINDOWS API (0-based) → ANSI ESCAPE (1-based)
# ═══════════════════════════════════════════════════════════════════════════
windows_x, windows_y → ansi_col, ansi_row
    # Formula: ansi_col = windows_x + 1, ansi_row = windows_y + 1
    # Example: Windows (0, 0) → ANSI (1, 1)
    # Example: Windows (24, 10) → ANSI (25, 11)
    # Usage: mouse_event.dwMousePosition.X + 1, mouse_event.dwMousePosition.Y + 1

# ═══════════════════════════════════════════════════════════════════════════
# ANSI ESCAPE (1-based) → WINDOWS API (0-based)
# ═══════════════════════════════════════════════════════════════════════════
ansi_col, ansi_row → windows_x, windows_y
    # Formula: windows_x = ansi_col - 1, windows_y = ansi_row - 1
    # Example: ANSI (1, 1) → Windows (0, 0)
    # Example: ANSI (25, 11) → Windows (24, 10)
    # Usage: COORD(ansi_col - 1, ansi_row - 1)

# ═══════════════════════════════════════════════════════════════════════════
# CRITICAL CONVERSION POINTS
# ═══════════════════════════════════════════════════════════════════════════
# Point 1: Mouse event coordinates from ReadConsoleInputW are 0-based (Windows)
#          MUST add +1 before comparing with ANSI-based UI element positions
# Point 2: ANSI escape sequences like f'\033[{row};{col}H' expect 1-based coordinates
#          MUST subtract -1 when converting UI positions to Windows API calls
# Point 3: Origin difference:
#          Windows: (0, 0) = top-left corner
#          ANSI:    (1, 1) = top-left corner
```

### INTEGRATION PATTERNS - Technique | Components | Purpose | Implementation

```python
# ═══════════════════════════════════════════════════════════════════════════
# CONSOLE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════
def enable_ansi_windows():
    """Enable ANSI escape sequences on Windows"""
    # Uses: kernel32.GetStdHandle, GetConsoleMode, SetConsoleMode
    # Enables: ENABLE_VIRTUAL_TERMINAL_PROCESSING (0x0004)
    # Returns: None
    # Side effects: Modifies stdout console mode, enables ANSI codes
    
def enable_mouse_input():
    """Enable mouse input and disable QuickEdit"""
    # Uses: kernel32.GetStdHandle, GetConsoleMode, SetConsoleMode
    # Enables: ENABLE_MOUSE_INPUT (0x0010), ENABLE_EXTENDED_FLAGS (0x0080)
    # Disables: ENABLE_QUICK_EDIT_MODE (0x0040)
    # Returns: None
    # Side effects: Modifies stdin console mode, enables mouse events

# ═══════════════════════════════════════════════════════════════════════════
# INPUT HANDLING
# ═══════════════════════════════════════════════════════════════════════════
def check_keyboard_input():
    """Non-blocking keyboard check"""
    # Uses: msvcrt.kbhit, msvcrt.getch
    # Pattern: if msvcrt.kbhit(): key = msvcrt.getch()
    # Returns: bytes (key code) or None
    # Special handling: Arrow keys return two bytes (b'\xe0' + code)
    
def check_mouse_input():
    """Non-blocking mouse event check"""
    # Uses: kernel32.ReadConsoleInputW, INPUT_RECORD structure
    # Pattern: ReadConsoleInputW → check EventType → extract MouseEvent
    # Returns: tuple(x, y, button_state, event_flags) or None
    # Coordinate conversion: Add +1 to x and y for ANSI coordinates

# ═══════════════════════════════════════════════════════════════════════════
# RENDERING OPTIMIZATIONS
# ═══════════════════════════════════════════════════════════════════════════
def conditional_render(needs_render: bool, render_type: str):
    """Render only when state changes"""
    # Purpose: Eliminate flicker from constant redrawing
    # Pattern: Track state changes, set needs_render flag, check before render
    # Types: 'full' = full screen redraw, 'hover' = partial update
    # Implementation:
    #   - on_mouse_move returns True only if hover state changed
    #   - on_mouse_click always triggers full render
    #   - Hover updates skip clear_screen() to prevent flicker

def partial_render(widget, area):
    """Render only changed screen region"""
    # Purpose: Update specific UI element without full redraw
    # Uses: ANSI cursor positioning to specific widget area
    # Pattern: Move cursor to widget position, print widget, restore cursor
    # Benefits: No screen flicker, faster updates

# ═══════════════════════════════════════════════════════════════════════════
# STATE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
def track_hover_state(widget, x, y):
    """Detect hover state changes"""
    # Purpose: Only trigger render on hover enter/exit, not continuous movement
    # Pattern:
    #   old_hover = widget.is_hovered
    #   widget.is_hovered = widget.contains_point(x, y)
    #   return old_hover != widget.is_hovered
    # Returns: bool (True if state changed, False if same)
    
def track_selection_state(menu, selected_index):
    """Detect selection changes"""
    # Purpose: Only render when selected item changes
    # Pattern:
    #   old_selection = menu.selected_index
    #   menu.selected_index = new_index
    #   return old_selection != new_index
    # Returns: bool (True if changed)

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN BUFFER MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
def clear_screen():
    """Clear entire screen"""
    # Uses: print('\033[2J\033[H', end='', flush=True)
    # Effect: Clears all content, moves cursor to (1,1)
    # When: Full renders, initial draw, mode changes
    
def clear_line():
    """Clear current line"""
    # Uses: print('\033[2K', end='', flush=True)
    # Effect: Clears entire current line, cursor stays at current position
    # When: Updating status line, clearing prompt

def hide_cursor():
    """Hide terminal cursor"""
    # Uses: print('\033[?25l', end='', flush=True)
    # When: During menu navigation, prevents cursor flicker
    
def show_cursor():
    """Show terminal cursor"""
    # Uses: print('\033[?25h', end='', flush=True)
    # When: Exiting program, restoring normal terminal state

# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE: COMPLETE MOUSE-ENABLED MENU LOOP
# ═══════════════════════════════════════════════════════════════════════════
def menu_loop():
    """Main menu event loop with keyboard and mouse"""
    enable_ansi_windows()      # Enable ANSI codes
    enable_mouse_input()       # Enable mouse + disable QuickEdit
    hide_cursor()              # Hide cursor during menu
    
    needs_render = True
    render_type = 'full'
    
    while True:
        # Conditional rendering
        if needs_render:
            if render_type == 'full':
                clear_screen()
                draw_all_widgets()
            elif render_type == 'hover':
                draw_hovered_widget()  # Partial update
            needs_render = False
        
        # Check keyboard input
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0':  # Arrow key prefix
                key = msvcrt.getch()
                if key == b'H':  # Up arrow
                    if move_selection_up():
                        needs_render = True
                        render_type = 'full'
                elif key == b'P':  # Down arrow
                    if move_selection_down():
                        needs_render = True
                        render_type = 'full'
            elif key == b'\r':  # Enter
                execute_selected_action()
            elif key == b'\x1b':  # Escape
                break
        
        # Check mouse input
        input_record = INPUT_RECORD()
        events_read = wintypes.DWORD()
        if kernel32.ReadConsoleInputW(stdin, ctypes.byref(input_record), 1, ctypes.byref(events_read)):
            if input_record.EventType == 2:  # MOUSE_EVENT
                mouse = input_record.Event.MouseEvent
                x = mouse.dwMousePosition.X + 1  # Convert to ANSI (1-based)
                y = mouse.dwMousePosition.Y + 1
                
                # Mouse movement (hover detection)
                if mouse.dwEventFlags & 0x0001:  # MOUSE_MOVED
                    if check_hover_state_change(x, y):
                        needs_render = True
                        render_type = 'hover'
                
                # Mouse click
                if mouse.dwButtonState & 0x0001:  # LEFT_CLICK
                    if handle_click(x, y):
                        needs_render = True
                        render_type = 'full'
        
        time.sleep(0.01)  # Small delay to reduce CPU usage
    
    show_cursor()  # Restore cursor on exit
```

---

## Learning Objectives (A Priori Knowledge)

### 1. ANSI Escape Sequences - Foundation of Terminal Control

**What are ANSI Escape Sequences?**
- Special character sequences that control terminal behavior (cursor movement, colors, clearing)
- Originated from ANSI X3.64 standard (1979) for video terminals
- Interpreted by terminal emulators to perform actions instead of displaying text
- Start with ESC character (ASCII 27, `\033` in octal, `\x1b` in hex)

**Where do they come from?**
- Hardware terminals (VT100, VT220) needed standard control codes
- ANSI standardized these codes for compatibility
- Modern terminals (cmd, PowerShell, bash) still implement them
- Windows 10+ supports ANSI natively in console

**Structure:**
```
ESC [ <parameters> <command>
 ↑   ↑      ↑          ↑
 |   |      |          └─ Single letter command
 |   |      └─ Optional numbers separated by ;
 |   └─ Control Sequence Introducer (CSI)
 └─ Escape character
```

**How to use with f-strings:**
```python
# Escape character
ESC = '\033'          # Octal notation
ESC = '\x1b'          # Hex notation (equivalent)

# CSI (Control Sequence Introducer)
CSI = '\033['         # ESC + [

# Build command with f-string
row, col = 5, 10
command = f'\033[{row};{col}H'  # Position cursor at row 5, col 10
print(command, end='')

# Or inline
print(f'\033[{row};{col}H', end='')
```

**Common ANSI Sequences:**
```python
# Cursor positioning
f'\033[{row};{col}H'     # Move cursor to (row, col)
f'\033[{n}A'             # Move up n lines
f'\033[{n}B'             # Move down n lines
f'\033[{n}C'             # Move right n columns
f'\033[{n}D'             # Move left n columns

# Screen clearing
'\033[2J'                # Clear entire screen
'\033[2K'                # Clear current line
'\033[0J'                # Clear from cursor to end of screen

# Colors and styling
'\033[31m'               # Red foreground
'\033[42m'               # Green background
'\033[1m'                # Bold
'\033[0m'                # Reset all attributes

# Cursor visibility
'\033[?25l'              # Hide cursor
'\033[?25h'              # Show cursor
```

---

### 2. msvcrt - Microsoft Visual C Runtime Library

**What is msvcrt?**
- Python module exposing Windows C Runtime functions
- Provides low-level console I/O operations
- Windows-only module (not available on Linux/Mac)
- Part of Python standard library

**Core Functions for CLI Menus:**

#### `msvcrt.kbhit()` → bool
```python
import msvcrt

# Check if keyboard key is pressed (non-blocking)
if msvcrt.kbhit():
    # Key is available to read
    key = msvcrt.getch()
else:
    # No key pressed, continue other work
    pass
```
- **Returns**: `True` if key press is waiting, `False` otherwise
- **Non-blocking**: Does not wait for input
- **Use case**: Check for input in game loop or live display

#### `msvcrt.getch()` → bytes
```python
# Read single character from keyboard (blocking)
key = msvcrt.getch()

# Returns bytes object
if key == b'a':           # Letter 'a'
    print("You pressed A")
elif key == b'\r':        # Enter key
    print("Enter pressed")
elif key == b'\x1b':      # ESC key
    print("Escape pressed")
```
- **Returns**: Single byte as `bytes` object
- **Blocking**: Waits until key is pressed
- **No echo**: Character not displayed on screen

#### `msvcrt.getwch()` → str
```python
# Read single wide character (Unicode)
char = msvcrt.getwch()  # Returns str instead of bytes
```
- **Returns**: Unicode string (single character)
- **Use for**: International characters

#### Special Key Handling (Arrow Keys, Function Keys)
```python
key = msvcrt.getch()

# Special keys send TWO bytes
if key == b'\xe0':        # Special key prefix (224)
    key2 = msvcrt.getch()  # Read second byte
    
    if key2 == b'H':       # Up arrow (72)
        print("Up")
    elif key2 == b'P':     # Down arrow (80)
        print("Down")
    elif key2 == b'K':     # Left arrow (75)
        print("Left")
    elif key2 == b'M':     # Right arrow (77)
        print("Right")
    elif key2 == b';':     # F1 (59)
        print("F1")
    # ... more function keys

elif key == b'\x00':      # Alternate prefix (0)
    key2 = msvcrt.getch()
    # Handle F keys, Insert, Delete, etc.
```

**Key Code Reference:**
```python
# Single-byte keys
b'\r'      # Enter (13)
b'\x1b'    # ESC (27)
b' '       # Space (32)
b'\t'      # Tab (9)
b'\x08'    # Backspace (8)

# Two-byte special keys (prefix b'\xe0')
b'H'   # 72  - Up arrow
b'P'   # 80  - Down arrow  
b'K'   # 75  - Left arrow
b'M'   # 77  - Right arrow
b'G'   # 71  - Home
b'O'   # 79  - End
b'I'   # 73  - Page Up
b'Q'   # 81  - Page Down
b'R'   # 82  - Insert
b'S'   # 83  - Delete

# Two-byte function keys (prefix b'\x00')
b';'   # 59  - F1
b'<'   # 60  - F2
b'='   # 61  - F3
b'>'   # 62  - F4
b'?'   # 63  - F5
b'@'   # 64  - F6
b'A'   # 65  - F7
b'B'   # 66  - F8
b'C'   # 67  - F9
b'D'   # 68  - F10
```

---

### 3. ctypes + Windows Console API - Mouse and Advanced Input

**What is ctypes?**
- Python standard library for calling C functions from DLLs
- Allows direct access to Windows API functions
- Provides C-compatible data types
- Required for mouse input in Windows console

**What is Windows Console API?**
- Set of functions in `kernel32.dll` for console control
- Provides input/output, screen buffer, cursor control
- Mouse events, window events, keyboard events
- More powerful than standard I/O

**Core Structures and Functions:**

#### Loading kernel32.dll
```python
import ctypes
from ctypes import wintypes

# Load Windows kernel DLL
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
```

#### Getting Console Handles
```python
# Standard handles (integer constants)
STD_INPUT_HANDLE = -10    # stdin
STD_OUTPUT_HANDLE = -11   # stdout
STD_ERROR_HANDLE = -12    # stderr

# Get handle to console input
stdin_handle = kernel32.GetStdHandle(STD_INPUT_HANDLE)
```

**Function**: `GetStdHandle(nStdHandle)`
- **Parameter**: Handle ID (-10, -11, or -12)
- **Returns**: Handle value (integer)
- **Use**: Required for all console operations

#### Console Mode Flags
```python
# Input mode flags (bitwise OR together)
ENABLE_PROCESSED_INPUT = 0x0001      # Process Ctrl+C
ENABLE_LINE_INPUT = 0x0002           # Line-based input
ENABLE_ECHO_INPUT = 0x0004           # Echo characters
ENABLE_WINDOW_INPUT = 0x0008         # Window events
ENABLE_MOUSE_INPUT = 0x0010          # Mouse events (CRITICAL!)
ENABLE_INSERT_MODE = 0x0020          # Insert vs overwrite
ENABLE_QUICK_EDIT_MODE = 0x0040      # Right-click paste (MUST DISABLE!)
ENABLE_EXTENDED_FLAGS = 0x0080       # Enable/disable flags
ENABLE_VIRTUAL_TERMINAL_INPUT = 0x0200  # ANSI input sequences
```

#### Getting/Setting Console Mode
```python
# Get current mode
mode = wintypes.DWORD()  # Create DWORD variable
success = kernel32.GetConsoleMode(stdin_handle, ctypes.byref(mode))

# Modify mode
mode.value |= ENABLE_MOUSE_INPUT     # Enable mouse (bitwise OR)
mode.value &= ~ENABLE_QUICK_EDIT_MODE  # Disable QuickEdit (bitwise AND NOT)

# Set new mode
kernel32.SetConsoleMode(stdin_handle, mode)
```

**Function**: `GetConsoleMode(hConsoleHandle, lpMode)`
- **Parameters**: 
  - `hConsoleHandle`: Console handle from GetStdHandle
  - `lpMode`: Pointer to DWORD (use `ctypes.byref()`)
- **Returns**: Non-zero on success
- **Use**: Read current console configuration

**Function**: `SetConsoleMode(hConsoleHandle, dwMode)`
- **Parameters**:
  - `hConsoleHandle`: Console handle
  - `dwMode`: New mode value (DWORD)
- **Returns**: Non-zero on success
- **Use**: Change console behavior

**Critical Step**: Disable QuickEdit Mode
```python
# QuickEdit captures mouse for copy/paste
# Your program won't receive mouse events unless you disable it!
mode.value &= ~0x0040  # Clear bit 6 (ENABLE_QUICK_EDIT_MODE)
```

#### Input Event Structures
```python
# COORD - Screen coordinate
class COORD(ctypes.Structure):
    _fields_ = [
        ("X", ctypes.c_short),  # Column (0-based)
        ("Y", ctypes.c_short)   # Row (0-based)
    ]

# MOUSE_EVENT_RECORD - Mouse event data
class MOUSE_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ("dwMousePosition", COORD),           # Where mouse is
        ("dwButtonState", wintypes.DWORD),    # Which buttons pressed
        ("dwControlKeyState", wintypes.DWORD),# Ctrl/Alt/Shift state
        ("dwEventFlags", wintypes.DWORD)      # Click/move/wheel
    ]

# KEY_EVENT_RECORD - Keyboard event data  
class KEY_EVENT_RECORD(ctypes.Structure):
    class _char(ctypes.Union):
        _fields_ = [
            ("UnicodeChar", wintypes.WCHAR),
            ("AsciiChar", wintypes.CHAR)
        ]
    _fields_ = [
        ("bKeyDown", wintypes.BOOL),          # True=press, False=release
        ("wRepeatCount", wintypes.WORD),      # How many times
        ("wVirtualKeyCode", wintypes.WORD),   # Virtual key code
        ("wVirtualScanCode", wintypes.WORD),  # Scan code
        ("uChar", _char),                     # Character value
        ("dwControlKeyState", wintypes.DWORD) # Modifiers
    ]

# INPUT_RECORD - Union of all event types
class INPUT_RECORD(ctypes.Structure):
    class _Event(ctypes.Union):
        _fields_ = [
            ("KeyEvent", KEY_EVENT_RECORD),
            ("MouseEvent", MOUSE_EVENT_RECORD)
        ]
    _fields_ = [
        ("EventType", wintypes.WORD),  # Which event type
        ("Event", _Event)               # Event data
    ]
```

#### Event Type Constants
```python
KEY_EVENT = 0x0001                    # Keyboard event
MOUSE_EVENT = 0x0002                  # Mouse event
WINDOW_BUFFER_SIZE_EVENT = 0x0004     # Window resized
```

#### Mouse Button State Flags
```python
FROM_LEFT_1ST_BUTTON_PRESSED = 0x0001  # Left button
RIGHTMOST_BUTTON_PRESSED = 0x0002      # Right button
FROM_LEFT_2ND_BUTTON_PRESSED = 0x0004  # Middle button
```

#### Mouse Event Flags
```python
MOUSE_MOVED = 0x0001                   # Mouse moved
DOUBLE_CLICK = 0x0002                  # Double-clicked
MOUSE_WHEELED = 0x0004                 # Wheel scrolled
MOUSE_HWHEELED = 0x0008                # Horizontal wheel
```

#### Reading Console Input
```python
# Create structures
input_record = INPUT_RECORD()
events_read = wintypes.DWORD()

# Read one event
success = kernel32.ReadConsoleInputW(
    stdin_handle,                    # Console handle
    ctypes.byref(input_record),      # Pointer to INPUT_RECORD
    1,                               # Number of events to read
    ctypes.byref(events_read)        # Pointer to count read
)

# Check event type
if input_record.EventType == MOUSE_EVENT:
    mouse = input_record.Event.MouseEvent
    x = mouse.dwMousePosition.X
    y = mouse.dwMousePosition.Y
    
    # Check button state
    if mouse.dwButtonState & FROM_LEFT_1ST_BUTTON_PRESSED:
        print(f"Left click at ({x}, {y})")

elif input_record.EventType == KEY_EVENT:
    key = input_record.Event.KeyEvent
    if key.bKeyDown:  # Key press (not release)
        char = key.uChar.AsciiChar
        print(f"Key pressed: {char}")
```

**Function**: `ReadConsoleInputW(hConsoleInput, lpBuffer, nLength, lpNumberOfEventsRead)`
- **Parameters**:
  - `hConsoleInput`: Console input handle
  - `lpBuffer`: Pointer to INPUT_RECORD array
  - `nLength`: Number of records to read
  - `lpNumberOfEventsRead`: Pointer to DWORD for count
- **Returns**: Non-zero on success
- **Use**: Read keyboard, mouse, window events

#### Checking for Available Events
```python
num_events = wintypes.DWORD()
kernel32.GetNumberOfConsoleInputEvents(
    stdin_handle,
    ctypes.byref(num_events)
)

if num_events.value > 0:
    # Events available to read
    kernel32.ReadConsoleInputW(...)
```

**Function**: `GetNumberOfConsoleInputEvents(hConsoleInput, lpcNumberOfEvents)`
- **Parameters**:
  - `hConsoleInput`: Console handle
  - `lpcNumberOfEvents`: Pointer to DWORD
- **Returns**: Non-zero on success
- **Use**: Check if input available (non-blocking)

---

### 4. Integration Map: msvcrt ↔ ctypes Console API

**Comparison:**

| Feature | msvcrt | ctypes + Console API |
|---------|--------|----------------------|
| **Keyboard** | `getch()`, `kbhit()` | `ReadConsoleInputW()` + KEY_EVENT |
| **Mouse** | ❌ Not supported | ✅ Full support |
| **Blocking** | `getch()` blocks | Can poll with `GetNumberOfConsoleInputEvents()` |
| **Event Types** | Keys only | Keys, mouse, window resize |
| **Platform** | Windows only | Windows only |
| **Complexity** | Simple | Complex (structs, handles) |

**When to use msvcrt:**
- Simple keyboard-only menus
- Quick prototypes
- No mouse required
- Minimal code

**When to use Console API:**
- Mouse input required
- Need mouse position/clicks
- Advanced event handling
- Full control over console

**Common Integration Pattern:**
```python
# Use msvcrt for simple keyboard
if msvcrt.kbhit():
    key = msvcrt.getch()
    handle_key(key)

# Use Console API for mouse
input_record = INPUT_RECORD()
kernel32.ReadConsoleInputW(...)
if input_record.EventType == MOUSE_EVENT:
    handle_mouse(input_record.Event.MouseEvent)
```

**Hybrid Approach:**
```python
# Enable mouse via Console API
mode = wintypes.DWORD()
kernel32.GetConsoleMode(stdin, ctypes.byref(mode))
mode.value |= ENABLE_MOUSE_INPUT
kernel32.SetConsoleMode(stdin, mode)

# Read all events via Console API
while running:
    input_record = INPUT_RECORD()
    kernel32.ReadConsoleInputW(stdin, ctypes.byref(input_record), 1, ...)
    
    if input_record.EventType == KEY_EVENT:
        # Handle keyboard
        pass
    elif input_record.EventType == MOUSE_EVENT:
        # Handle mouse
        pass
```

---

### 5. Coordinate System Morphisms

**Windows Console API → ANSI Escape Sequences**

```python
# Windows Console API uses 0-based indexing
# Top-left corner is (0, 0)
mouse_x = mouse_event.dwMousePosition.X  # 0, 1, 2, 3, 4...
mouse_y = mouse_event.dwMousePosition.Y  # 0, 1, 2, 3, 4...

# ANSI escape sequences use 1-based indexing
# Top-left corner is (1, 1)
ansi_x = mouse_x + 1  # 1, 2, 3, 4, 5...
ansi_y = mouse_y + 1  # 1, 2, 3, 4, 5...

# Use ANSI coordinates for cursor positioning
print(f'\033[{ansi_y};{ansi_x}H', end='')  # Position cursor
```

**Mapping Table:**

| Windows API | ANSI Escape | Screen Position |
|-------------|-------------|-----------------|
| (0, 0) | (1, 1) | Top-left corner |
| (79, 0) | (80, 1) | Top-right (80-col) |
| (0, 24) | (1, 25) | Bottom-left (25-row) |
| (79, 24) | (80, 25) | Bottom-right |

**Critical Rule:**
```python
# ALWAYS add 1 when converting Windows → ANSI
ansi_coordinate = windows_coordinate + 1

# ALWAYS subtract 1 when converting ANSI → Windows  
windows_coordinate = ansi_coordinate - 1
```

---

## Complete ANSI Escape Sequence Reference

### Cursor Movement
```python
f'\033[{n}A'              # Cursor up n lines
f'\033[{n}B'              # Cursor down n lines
f'\033[{n}C'              # Cursor forward (right) n columns
f'\033[{n}D'              # Cursor back (left) n columns
f'\033[{n}E'              # Cursor next line (down n, column 1)
f'\033[{n}F'              # Cursor previous line (up n, column 1)
f'\033[{n}G'              # Cursor to column n
f'\033[{row};{col}H'      # Cursor position (row, col) - 1-based
f'\033[{row};{col}f'      # Same as H (alternate)
'\033[H'                  # Cursor home (1,1)
'\033[s'                  # Save cursor position
'\033[u'                  # Restore cursor position
'\033[?25l'               # Hide cursor
'\033[?25h'               # Show cursor
```

### Screen Clearing
```python
'\033[0J'                 # Clear from cursor to end of screen
'\033[1J'                 # Clear from cursor to beginning of screen
'\033[2J'                 # Clear entire screen
'\033[0K'                 # Clear from cursor to end of line
'\033[1K'                 # Clear from cursor to beginning of line
'\033[2K'                 # Clear entire line
```

### Scrolling
```python
f'\033[{n}S'              # Scroll up n lines
f'\033[{n}T'              # Scroll down n lines
```

### Text Formatting
```python
'\033[0m'                 # Reset all attributes
'\033[1m'                 # Bold/bright
'\033[2m'                 # Dim
'\033[3m'                 # Italic
'\033[4m'                 # Underline
'\033[5m'                 # Blink slow
'\033[6m'                 # Blink fast
'\033[7m'                 # Reverse video (invert)
'\033[8m'                 # Hidden/concealed
'\033[9m'                 # Strikethrough

# Reset individual attributes
'\033[22m'                # Normal intensity (not bold/dim)
'\033[23m'                # Not italic
'\033[24m'                # Not underlined
'\033[25m'                # Not blinking
'\033[27m'                # Not reversed
'\033[28m'                # Not hidden
'\033[29m'                # Not strikethrough
```

### 16 Standard Colors
```python
# Foreground (text) colors
'\033[30m'                # Black
'\033[31m'                # Red
'\033[32m'                # Green
'\033[33m'                # Yellow
'\033[34m'                # Blue
'\033[35m'                # Magenta
'\033[36m'                # Cyan
'\033[37m'                # White
'\033[39m'                # Default (reset)

# Bright foreground colors
'\033[90m'                # Bright black (gray)
'\033[91m'                # Bright red
'\033[92m'                # Bright green
'\033[93m'                # Bright yellow
'\033[94m'                # Bright blue
'\033[95m'                # Bright magenta
'\033[96m'                # Bright cyan
'\033[97m'                # Bright white

# Background colors
'\033[40m'                # Black background
'\033[41m'                # Red background
'\033[42m'                # Green background
'\033[43m'                # Yellow background
'\033[44m'                # Blue background
'\033[45m'                # Magenta background
'\033[46m'                # Cyan background
'\033[47m'                # White background
'\033[49m'                # Default background

# Bright background colors
'\033[100m'               # Bright black background
'\033[101m'               # Bright red background
'\033[102m'               # Bright green background
'\033[103m'               # Bright yellow background
'\033[104m'               # Bright blue background
'\033[105m'               # Bright magenta background
'\033[106m'               # Bright cyan background
'\033[107m'               # Bright white background
```

### 256-Color Palette
```python
f'\033[38;5;{n}m'         # Foreground color (n = 0-255)
f'\033[48;5;{n}m'         # Background color (n = 0-255)

# Color ranges:
# 0-15:    Standard colors (same as above)
# 16-231:  216 color cube (6×6×6)
# 232-255: Grayscale (24 shades)
```

### RGB True Color (24-bit)
```python
f'\033[38;2;{r};{g};{b}m' # Foreground RGB (r,g,b = 0-255)
f'\033[48;2;{r};{g};{b}m' # Background RGB (r,g,b = 0-255)

# Example: Bright orange text
print(f'\033[38;2;255;165;0mOrange Text\033[0m')
```

### Screen Modes
```python
'\033[?47h'               # Save screen
'\033[?47l'               # Restore screen
'\033[?1049h'             # Enable alternate screen buffer
'\033[?1049l'             # Disable alternate screen buffer
```

### Query Sequences (less common)
```python
'\033[6n'                 # Query cursor position (returns ESC[row;colR)
'\033[5n'                 # Query device status (returns ESC[0n or ESC[3n)
```

---

## Quick Reference - Building Blocks

### Core Atomic Operations
```python
# ============================================================================
# SCREEN POSITIONING & CLEARING
# ============================================================================

# Move cursor to position (row, col) - 1-based indexing
print(f'\033[{row};{col}H', end='')

# Clear entire screen
print('\033[2J', end='')

# Clear current line
print('\033[2K', end='')

# Hide/show cursor
print('\033[?25l', end='')  # Hide
print('\033[?25h', end='')  # Show

# ============================================================================
# TEXT STYLING
# ============================================================================

# Apply color and style to text
styled_text = f'{FG_CYAN}{BG_BLUE}{BOLD}Text{RESET}'

# Color codes
FG_BLACK = '\033[30m'       BG_BLACK = '\033[40m'
FG_RED = '\033[31m'         BG_RED = '\033[41m'
FG_GREEN = '\033[32m'       BG_GREEN = '\033[42m'
FG_CYAN = '\033[36m'        BG_CYAN = '\033[46m'
FG_WHITE = '\033[37m'       BG_WHITE = '\033[47m'

# Style codes
BOLD = '\033[1m'            UNDERLINE = '\033[4m'
DIM = '\033[2m'             REVERSE = '\033[7m'
RESET = '\033[0m'           # Always reset after styling!

# ============================================================================
# DRAWING BOXES & BORDERS
# ============================================================================

# ASCII safe characters (work everywhere)
horizontal = '-'
vertical = '|'
corner = '+'

# Build a box (3 lines example)
top_line = f"+{'-' * (width-2)}+"
mid_line = f"|{' ' * (width-2)}|"
bot_line = f"+{'-' * (width-2)}+"

# Position and draw
print(f'\033[{y};{x}H{top_line}')
print(f'\033[{y+1};{x}H{mid_line}')
print(f'\033[{y+2};{x}H{bot_line}')

# ============================================================================
# READING KEYBOARD INPUT
# ============================================================================

import msvcrt

# Check if key is pressed (non-blocking)
if msvcrt.kbhit():
    key = msvcrt.getch()  # Read one byte
    
    # Arrow keys come as two bytes
    if key == b'\xe0':  # Special key prefix
        key = msvcrt.getch()  # Read second byte
        if key == b'H':    # Up arrow
            # Move selection up
        elif key == b'P':  # Down arrow
            # Move selection down
        elif key == b'K':  # Left arrow
            # Move left
        elif key == b'M':  # Right arrow
            # Move right
    
    # Single byte keys
    elif key == b'\r':   # Enter
        # Confirm selection
    elif key == b'\x1b': # ESC
        # Cancel/exit
    elif key == b' ':    # Space
        # Toggle selection

# ============================================================================
# READING MOUSE INPUT (Windows Console API)
# ============================================================================

import ctypes
from ctypes import wintypes

kernel32 = ctypes.WinDLL('kernel32')
stdin = kernel32.GetStdHandle(-10)

# Enable mouse input
mode = wintypes.DWORD()
kernel32.GetConsoleMode(stdin, ctypes.byref(mode))
mode.value |= 0x0010   # ENABLE_MOUSE_INPUT
mode.value &= ~0x0040  # Disable QuickEdit (critical!)
kernel32.SetConsoleMode(stdin, mode)

# Read input event
input_record = INPUT_RECORD()
events_read = wintypes.DWORD()
kernel32.ReadConsoleInputW(stdin, ctypes.byref(input_record), 1, ctypes.byref(events_read))

# Check event type
if input_record.EventType == 0x0002:  # MOUSE_EVENT
    mouse = input_record.Event.MouseEvent
    x = mouse.dwMousePosition.X + 1  # Convert 0-based to 1-based
    y = mouse.dwMousePosition.Y + 1
    
    # Check button state
    if mouse.dwButtonState & 0x0001:  # Left button pressed
        # Handle left click at (x, y)

# ============================================================================
# COORDINATE CONVERSION
# ============================================================================

# Windows API gives 0-based coordinates (0,0 = top-left)
x_from_windows = mouse.dwMousePosition.X  # 0, 1, 2, 3...
y_from_windows = mouse.dwMousePosition.Y  # 0, 1, 2, 3...

# ANSI cursor positioning uses 1-based coordinates (1,1 = top-left)
x_for_ansi = x_from_windows + 1  # 1, 2, 3, 4...
y_for_ansi = y_from_windows + 1  # 1, 2, 3, 4...

# Always add +1 when converting from Windows to ANSI!

# ============================================================================
# POINT-IN-RECTANGLE TEST
# ============================================================================

# Check if point (px, py) is inside rectangle
def point_in_rect(px, py, rect_x, rect_y, rect_width, rect_height):
    return (rect_x <= px < rect_x + rect_width and
            rect_y <= py < rect_y + rect_height)

# Usage
if point_in_rect(mouse_x, mouse_y, button_x, button_y, button_w, button_h):
    # Mouse is over button

# ============================================================================
# ANTI-FLICKER: CONDITIONAL RENDERING
# ============================================================================

needs_redraw = False

while running:
    # Only redraw when something changed
    if needs_redraw:
        # Clear and redraw
        print('\033[2J', end='')
        draw_everything()
        needs_redraw = False
    
    # Check for input
    if msvcrt.kbhit():
        handle_input()
        needs_redraw = True  # Input changed state
    else:
        time.sleep(0.05)  # Idle delay to reduce CPU
```

---

## How The Atomics Fit Together

### Pattern 1: Simple Menu Loop
```
1. Clear screen
2. Draw menu items with current selection highlighted
3. Wait for key press (up/down/enter/esc)
4. Update selection based on key
5. If enter -> return choice
6. If esc -> return None
7. Go to step 1
```

**Implementation Flow:**
```python
current = 0  # Current selection index

while True:
    # Step 1: Clear
    print('\033[2J\033[H', end='')
    
    # Step 2: Draw items
    for i, item in enumerate(items):
        if i == current:
            print(f'{BG_CYAN}{FG_BLACK}> {item}{RESET}')
        else:
            print(f'  {item}')
    
    # Step 3: Wait for key
    key = msvcrt.getch()
    
    # Step 4: Update selection
    if key == b'\xe0':
        key = msvcrt.getch()
        if key == b'H':  # Up
            current = (current - 1) % len(items)
        elif key == b'P':  # Down
            current = (current + 1) % len(items)
    
    # Step 5: Check enter
    elif key == b'\r':
        return current
    
    # Step 6: Check esc
    elif key == b'\x1b':
        return None
```

---

### Pattern 2: Mouse Click Detection
```
1. Enable mouse input mode
2. Read console input events
3. If mouse event:
   a. Get mouse position (x, y)
   b. Convert from 0-based to 1-based
   c. Check if position is inside each button
   d. If inside -> execute button action
4. Loop
```

**Implementation Flow:**
```python
# Step 1: Enable mouse
mode = wintypes.DWORD()
kernel32.GetConsoleMode(stdin, ctypes.byref(mode))
mode.value |= 0x0010   # Enable mouse
mode.value &= ~0x0040  # Disable QuickEdit
kernel32.SetConsoleMode(stdin, mode)

while running:
    # Step 2: Read event
    input_record = INPUT_RECORD()
    kernel32.ReadConsoleInputW(stdin, ctypes.byref(input_record), 1, ...)
    
    # Step 3: Check if mouse event
    if input_record.EventType == 0x0002:
        mouse = input_record.Event.MouseEvent
        
        # Step 3a: Get position
        x = mouse.dwMousePosition.X
        y = mouse.dwMousePosition.Y
        
        # Step 3b: Convert coordinates
        x += 1  # 0-based -> 1-based
        y += 1
        
        # Step 3c: Check buttons
        for button in buttons:
            if point_in_rect(x, y, button['x'], button['y'], button['w'], button['h']):
                # Step 3d: Execute action
                if mouse.dwButtonState & 0x0001:  # Left click
                    button['action']()
```

---

### Pattern 3: Anti-Flicker Rendering
```
1. Start with needs_redraw = True
2. If needs_redraw:
   a. Clear screen
   b. Draw all elements
   c. Set needs_redraw = False
3. Check for input
4. If input received:
   a. Process input
   b. Update state
   c. Set needs_redraw = True
5. If no input:
   a. Sleep briefly (0.05s)
6. Go to step 2
```

**Implementation Flow:**
```python
needs_redraw = True
state = {'selected': 0, 'hover': -1}

while running:
    # Step 2: Conditional render
    if needs_redraw:
        # Step 2a: Clear
        print('\033[2J\033[H', end='')
        
        # Step 2b: Draw
        for i, item in enumerate(items):
            bg = BG_CYAN if i == state['hover'] else ''
            print(f'{bg}{item}{RESET}')
        
        # Step 2c: Reset flag
        needs_redraw = False
    
    # Step 3: Check input
    event = read_input()  # Mouse or keyboard
    
    if event:
        # Step 4: Process
        old_hover = state['hover']
        state['hover'] = calculate_hover(event)
        
        if old_hover != state['hover']:
            needs_redraw = True  # State changed
    else:
        # Step 5: Idle
        time.sleep(0.05)
```

---

### Pattern 4: Hover State Tracking
```
1. Track old hover state
2. Calculate new hover state from mouse position
3. If old != new:
   a. Update hover state
   b. Trigger redraw
4. If old == new:
   a. Skip redraw (nothing changed)
```

**Implementation Flow:**
```python
hover_idx = -1  # No hover initially

while running:
    mouse_x, mouse_y = get_mouse_position()
    new_hover = -1
    
    # Step 2: Calculate which item mouse is over
    for i, item in enumerate(items):
        item_y = start_y + i
        if mouse_y == item_y:
            new_hover = i
            break
    
    # Step 3: Check if changed
    if new_hover != hover_idx:
        hover_idx = new_hover
        needs_redraw = True  # Trigger redraw
    # Step 4: If same, skip redraw
```

---

### Pattern 5: Drawing Text at Position
```
1. Build the text with colors/styles
2. Calculate position (row, col)
3. Output ANSI position code + text
4. Always flush immediately
```

**Implementation Flow:**
```python
def print_at(row, col, text):
    # Step 1: Text is pre-built with colors
    # text = f'{FG_CYAN}Hello{RESET}'
    
    # Step 2: Position is given
    # row=5, col=10
    
    # Step 3: Output position + text
    print(f'\033[{row};{col}H{text}', end='', flush=True)
    
    # Step 4: flush=True ensures immediate display
```

---

### Pattern 6: Building a Box
```
1. Calculate corners (x, y, width, height)
2. Draw top line at (y, x)
3. Draw middle lines at (y+1..y+height-2, x)
4. Draw bottom line at (y+height-1, x)
5. Each line: corner + horizontal + corner
```

**Implementation Flow:**
```python
def draw_box(x, y, width, height):
    # Step 1: Corners calculated from parameters
    
    # Step 2: Top line
    print(f'\033[{y};{x}H+{"-" * (width-2)}+', end='')
    
    # Step 3: Middle lines
    for i in range(1, height-1):
        print(f'\033[{y+i};{x}H|{" " * (width-2)}|', end='')
    
    # Step 4: Bottom line
    print(f'\033[{y+height-1};{x}H+{"-" * (width-2)}+', end='')
```

---

### Pattern 7: Event Loop Structure
```
1. Initialize state
2. Enable input modes (mouse, keyboard)
3. Loop while running:
   a. Render if needed
   b. Read input event
   c. Classify event (mouse/keyboard)
   d. Update state based on event
   e. Mark render needed if state changed
   f. If no event, sleep briefly
4. Cleanup (restore cursor, disable mouse)
```

**Implementation Flow:**
```python
# Step 1: Initialize
running = True
needs_render = True
selected = 0

# Step 2: Enable inputs
enable_mouse()
hide_cursor()

# Step 3: Loop
while running:
    # Step 3a: Render
    if needs_render:
        draw_everything()
        needs_render = False
    
    # Step 3b: Read input
    event = read_console_input()
    
    if event:
        # Step 3c: Classify
        if event['type'] == 'mouse':
            # Step 3d: Update state
            old_selected = selected
            selected = calculate_clicked_item(event['x'], event['y'])
            
            # Step 3e: Check if changed
            if old_selected != selected:
                needs_render = True
        
        elif event['type'] == 'key':
            handle_key(event['key'])
            needs_render = True
    else:
        # Step 3f: Sleep when idle
        time.sleep(0.05)

# Step 4: Cleanup
show_cursor()
disable_mouse()
```

---

## Composition Patterns

### Simple Menu = Position + Draw + Input + Loop
- **Position**: `\033[{row};{col}H`
- **Draw**: Styled text with color codes
- **Input**: `msvcrt.getch()` for arrow keys
- **Loop**: While true, redraw on key press

### Button = Rectangle + Hover Test + Click Action
- **Rectangle**: `(x, y, width, height)`
- **Hover Test**: `point_in_rect(mouse_x, mouse_y, x, y, w, h)`
- **Click Action**: Execute callback when clicked

### Progress Bar = Position + Width + Fill Ratio
- **Position**: Start at `(x, y)`
- **Width**: Total bar width
- **Fill Ratio**: `current / total * width`
- **Draw**: `'█' * filled + '░' * empty`

### Scrollable List = Viewport + Offset + Navigation
- **Viewport**: Visible height (e.g., 10 items)
- **Offset**: Starting index in full list
- **Navigation**: Arrow keys adjust offset
- **Draw**: Only items from `[offset : offset+viewport]`

---

## Critical Concepts Summary

1. **ANSI is 1-based, Windows is 0-based** - Always +1 when converting
2. **QuickEdit must be disabled** - Or mouse clicks won't reach your program
3. **Only redraw when state changes** - Prevents flicker
4. **Sleep when idle** - Reduces CPU usage
5. **Flush output immediately** - `flush=True` for instant display
6. **Test mouse position against all clickable areas** - In order, top to bottom

---

## Detailed Implementation Examples

### 1. Basic Menu Navigation

#### SimpleMenu Pattern
```python
class SimpleMenu:
    """Single-selection menu with keyboard navigation"""
    
    def __init__(self, title: str, items: List[str]):
        self.title = title
        self.items = items
        self.current = 0
        
    def display(self):
        """Render menu"""
        Screen.clear()
        print(f"{BOLD}{self.title}{RESET}\n")
        
        for i, item in enumerate(self.items):
            if i == self.current:
                print(f"{BG_CYAN}{FG_BLACK}> {item}{RESET}")
            else:
                print(f"  {item}")
    
    def wait_key(self) -> str:
        """Wait for arrow key or Enter"""
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                
                if key == b'\xe0':  # Arrow key prefix
                    key = msvcrt.getch()
                    if key == b'H':    # Up
                        self.current = (self.current - 1) % len(self.items)
                        return 'move'
                    elif key == b'P':  # Down
                        self.current = (self.current + 1) % len(self.items)
                        return 'move'
                        
                elif key == b'\r':  # Enter
                    return 'select'
                elif key == b'\x1b':  # ESC
                    return 'exit'
```

**Use Cases:**
- Main application menus
- Settings selection
- File/option browsers
- Any single-choice interface

**Key Features:**
- No flicker (single render per action)
- Minimal CPU usage
- Reliable keyboard detection
- Easy to implement

---

### 2. Multi-Selection Lists

#### ListSelector Pattern
```python
class ListSelector:
    """Multi-select list with checkboxes"""
    
    def __init__(self, items: List[str], selected: set = None):
        self.items = items
        self.selected = selected or set()
        self.current = 0
        
    def render(self):
        """Display list with checkmarks"""
        for i, item in enumerate(self.items):
            check = "✓" if i in self.selected else " "
            cursor = ">" if i == self.current else " "
            
            if i == self.current:
                print(f"{BG_CYAN}{cursor} [{check}] {item}{RESET}")
            else:
                print(f"{cursor} [{check}] {item}")
    
    def handle_input(self):
        """Process keyboard input"""
        key = msvcrt.getch()
        
        if key == b'\xe0':  # Arrow key
            key = msvcrt.getch()
            if key == b'H':    # Up
                self.current = max(0, self.current - 1)
            elif key == b'P':  # Down
                self.current = min(len(self.items) - 1, self.current + 1)
                
        elif key == b' ':  # Space to toggle
            if self.current in self.selected:
                self.selected.remove(self.current)
            else:
                self.selected.add(self.current)
```

**Use Cases:**
- File selection dialogs
- Feature toggles
- Batch operations
- Filtering options

**Key Features:**
- Multiple selections
- Visual feedback (checkmarks)
- Space to toggle, Enter to confirm
- Works with any list size

---

### 3. Hierarchical Menu Systems

#### MenuController Pattern
```python
class MenuController:
    """Nested menu navigation system"""
    
    def __init__(self):
        self.menu_stack = []
        self.current_menu = None
        
    def push_menu(self, menu: Menu):
        """Enter submenu"""
        if self.current_menu:
            self.menu_stack.append(self.current_menu)
        self.current_menu = menu
        
    def pop_menu(self):
        """Return to previous menu"""
        if self.menu_stack:
            self.current_menu = self.menu_stack.pop()
            return True
        return False
    
    def get_breadcrumb(self) -> str:
        """Show navigation path"""
        path = [m.title for m in self.menu_stack]
        if self.current_menu:
            path.append(self.current_menu.title)
        return " > ".join(path)

class MenuItem:
    """Single menu item with action or submenu"""
    
    def __init__(self, label: str, action=None, submenu=None):
        self.label = label
        self.action = action      # Callable function
        self.submenu = submenu    # Nested Menu object
        
    def execute(self, controller: MenuController):
        """Execute action or enter submenu"""
        if self.submenu:
            controller.push_menu(self.submenu)
        elif self.action:
            self.action()
```

**Use Cases:**
- Complex application menus
- Configuration systems
- File explorers with folders
- Multi-level settings

**Key Features:**
- Unlimited nesting depth
- Breadcrumb navigation
- Back/forward navigation
- Action callbacks

---

### 4. Mouse-Enabled Interfaces

#### Mouse Handler Setup (Windows)
```python
from ctypes import wintypes
import ctypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

class MouseHandler:
    """Windows Console API mouse support"""
    
    def __init__(self):
        self.stdin = kernel32.GetStdHandle(-10)  # STD_INPUT_HANDLE
        self.last_button_state = 0
        
    def enable(self):
        """Enable mouse input"""
        mode = wintypes.DWORD()
        kernel32.GetConsoleMode(self.stdin, ctypes.byref(mode))
        
        # Enable mouse input
        mode.value |= 0x0010  # ENABLE_MOUSE_INPUT
        mode.value |= 0x0080  # ENABLE_EXTENDED_FLAGS
        
        # CRITICAL: Disable QuickEdit mode
        mode.value &= ~0x0040  # ENABLE_QUICK_EDIT_MODE
        mode.value &= ~0x0020  # ENABLE_INSERT_MODE
        
        kernel32.SetConsoleMode(self.stdin, mode)
    
    def read_input(self) -> Optional[Tuple[str, dict]]:
        """Read mouse/keyboard events"""
        input_record = INPUT_RECORD()
        events_read = wintypes.DWORD()
        
        if kernel32.ReadConsoleInputW(
            self.stdin, 
            ctypes.byref(input_record), 
            1, 
            ctypes.byref(events_read)
        ):
            if input_record.EventType == 0x0002:  # MOUSE_EVENT
                mouse = input_record.Event.MouseEvent
                
                # IMPORTANT: Convert 0-based to 1-based coords
                x = mouse.dwMousePosition.X + 1
                y = mouse.dwMousePosition.Y + 1
                
                button_state = mouse.dwButtonState
                event_flags = mouse.dwEventFlags
                
                # Detect click type
                if event_flags & 0x0001:  # MOUSE_MOVED
                    return ('mouse_move', {'x': x, 'y': y})
                
                if button_state & 0x0001:  # Left button
                    return ('mouse_click', {
                        'x': x, 'y': y, 
                        'button': 'left', 
                        'action': 'down'
                    })
```

**Critical Mouse Setup Issues:**
1. **QuickEdit Mode**: Must be disabled or mouse events won't reach your app
2. **Coordinate System**: Windows API is 0-based, ANSI is 1-based (add +1!)
3. **Console Size**: Fix window size to prevent scrollbars interfering with clicks

---

### 5. Widget Base Classes

#### Widget Pattern
```python
class Widget:
    """Base class for all interactive widgets"""
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x          # Screen position (1-based)
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.enabled = True
        self.focused = False
        self.hover = False
        
    def contains_point(self, px: int, py: int) -> bool:
        """Check if point is inside widget"""
        return (self.x <= px < self.x + self.width and
                self.y <= py < self.y + self.height)
    
    def on_mouse_move(self, x: int, y: int) -> bool:
        """Handle mouse move. Return True if state changed."""
        new_hover = self.contains_point(x, y)
        if new_hover != self.hover:
            self.hover = new_hover
            return True  # State changed - needs render
        return False  # No change - skip render
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        """Handle mouse click. Return True if handled."""
        if self.contains_point(x, y) and self.enabled:
            # Widget-specific click logic
            return True  # Consumed event
        return False  # Pass to next widget
    
    def render(self):
        """Draw widget on screen"""
        raise NotImplementedError
```

#### Button Widget
```python
class Button(Widget):
    """Clickable button with hover effect"""
    
    def __init__(self, x: int, y: int, label: str, callback: Callable):
        super().__init__(x, y, len(label) + 4, 3)
        self.label = label
        self.callback = callback
        
    def render(self):
        """Draw button with current state"""
        if self.hover:
            bg = BG_BRIGHT_CYAN
            fg = FG_BLACK
        elif self.focused:
            bg = BG_CYAN
            fg = FG_WHITE
        else:
            bg = BG_BLUE
            fg = FG_WHITE
        
        # Draw button box
        Screen.print_at(self.y, self.x, 
            f"{bg}{fg}+{'-' * (self.width-2)}+{RESET}")
        Screen.print_at(self.y + 1, self.x, 
            f"{bg}{fg}| {self.label} |{RESET}")
        Screen.print_at(self.y + 2, self.x, 
            f"{bg}{fg}+{'-' * (self.width-2)}+{RESET}")
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        """Execute callback on click"""
        if self.contains_point(x, y) and action == 'down':
            self.callback()
            return True
        return False
```

---

### 6. Advanced Widgets

#### ScrollableList Widget
```python
class ScrollableList(Widget):
    """List with scroll support (mouse wheel + arrow keys)"""
    
    def __init__(self, x: int, y: int, width: int, height: int, items: List[str]):
        super().__init__(x, y, width, height)
        self.items = items
        self.scroll_offset = 0
        self.selected = 0
        
    def render(self):
        """Draw visible portion of list"""
        visible_height = self.height - 2  # Account for border
        
        # Draw border
        Screen.print_at(self.y, self.x, f"+{'-' * (self.width-2)}+")
        
        # Draw visible items
        for i in range(visible_height):
            item_idx = self.scroll_offset + i
            if item_idx >= len(self.items):
                break
            
            item = self.items[item_idx]
            is_selected = (item_idx == self.selected)
            
            if is_selected and self.hover:
                bg = BG_BRIGHT_CYAN
            elif is_selected:
                bg = BG_CYAN
            else:
                bg = ''
            
            # Truncate item to fit width
            display = item[:self.width-4]
            Screen.print_at(self.y + i + 1, self.x, 
                f"|{bg} {display:<{self.width-4}} {RESET}|")
        
        # Bottom border
        Screen.print_at(self.y + self.height - 1, self.x, 
            f"+{'-' * (self.width-2)}+")
    
    def on_mouse_scroll(self, direction: str):
        """Handle mouse wheel"""
        if direction == 'up':
            self.scroll_offset = max(0, self.scroll_offset - 1)
        else:
            max_offset = max(0, len(self.items) - (self.height - 2))
            self.scroll_offset = min(max_offset, self.scroll_offset + 1)
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        """Select item on click"""
        if self.contains_point(x, y):
            rel_y = y - self.y - 1  # Relative to top border
            if 0 <= rel_y < self.height - 2:
                item_idx = self.scroll_offset + rel_y
                if item_idx < len(self.items):
                    self.selected = item_idx
            return True
        return False
```

#### TreeView Widget
```python
class TreeNode:
    """Node in tree structure"""
    
    def __init__(self, label: str, children: List['TreeNode'] = None):
        self.label = label
        self.children = children or []
        self.expanded = False

class TreeView(Widget):
    """Expandable/collapsible tree hierarchy"""
    
    def __init__(self, x: int, y: int, width: int, height: int, root: TreeNode):
        super().__init__(x, y, width, height)
        self.root = root
        self.selected_node = root
        self.scroll_offset = 0
        self.flat_list = []  # Flattened view for rendering
        self._rebuild_flat_list()
    
    def _rebuild_flat_list(self):
        """Convert tree to flat list for display"""
        self.flat_list = []
        self._flatten_recursive(self.root, 0)
    
    def _flatten_recursive(self, node: TreeNode, depth: int):
        """Recursively flatten tree"""
        self.flat_list.append((node, depth))
        if node.expanded:
            for child in node.children:
                self._flatten_recursive(child, depth + 1)
    
    def render(self):
        """Draw tree structure"""
        visible_height = self.height - 2
        
        for i in range(visible_height):
            node_idx = self.scroll_offset + i
            if node_idx >= len(self.flat_list):
                break
            
            node, depth = self.flat_list[node_idx]
            is_selected = (node == self.selected_node)
            
            # Indent
            indent = '  ' * depth
            
            # Expand/collapse indicator
            if node.children:
                indicator = 'v' if node.expanded else '>'
            else:
                indicator = ' '
            
            # Colors
            bg = BG_CYAN if is_selected else ''
            
            # Build line
            line = f"{indent}{indicator} {node.label}"
            Screen.print_at(self.y + i + 1, self.x, 
                f"{bg}{line:<{self.width}}{RESET}")
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        """Toggle expand/collapse on click"""
        if self.contains_point(x, y):
            rel_y = y - self.y - 1
            if 0 <= rel_y < len(self.flat_list):
                node, depth = self.flat_list[rel_y]
                
                if node.children:
                    node.expanded = not node.expanded
                    self._rebuild_flat_list()
                
                self.selected_node = node
            return True
        return False
```

---

### 7. Progress Indicators

#### ProgressBar Pattern
```python
class ProgressBar:
    """Visual progress indicator"""
    
    def __init__(self, x: int, y: int, width: int, total: int):
        self.x = x
        self.y = y
        self.width = width
        self.total = total
        self.current = 0
        
    def update(self, value: int):
        """Update progress value"""
        self.current = min(value, self.total)
        
    def render(self):
        """Draw progress bar"""
        percent = (self.current / self.total) * 100
        filled = int((self.current / self.total) * self.width)
        bar = '█' * filled + '░' * (self.width - filled)
        
        Screen.print_at(self.y, self.x, 
            f"[{bar}] {percent:.1f}%")

# Usage
progress = ProgressBar(5, 10, 40, 100)
for i in range(101):
    progress.update(i)
    progress.render()
    time.sleep(0.05)
```

#### Spinner Pattern
```python
class Spinner:
    """Animated loading indicator"""
    
    FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    # ASCII fallback: ['|', '/', '-', '\\']
    
    def __init__(self, x: int, y: int, message: str = "Loading"):
        self.x = x
        self.y = y
        self.message = message
        self.frame = 0
        
    def render(self):
        """Draw current frame"""
        char = self.FRAMES[self.frame % len(self.FRAMES)]
        Screen.print_at(self.y, self.x, 
            f"{FG_CYAN}{char} {self.message}{RESET}")
        self.frame += 1

# Usage
spinner = Spinner(5, 10, "Processing...")
while working:
    spinner.render()
    time.sleep(0.1)
    # Do work...
```

---

### 8. Application Framework

#### Application Pattern
```python
class Application:
    """Main application controller with event loop"""
    
    def __init__(self, title: str):
        self.title = title
        self.widgets = []
        self.focused_widget = None
        self.mouse_handler = MouseHandler()
        self.running = False
        
    def add_widget(self, widget: Widget):
        """Register widget"""
        self.widgets.append(widget)
        if self.focused_widget is None and widget.enabled:
            self.focused_widget = widget
            widget.focused = True
    
    def render_all(self, full_clear=True):
        """Render all widgets"""
        if full_clear:
            Screen.clear()
            # Draw title bar
            term_width, _ = get_terminal_size()
            Screen.print_at(1, 1, 
                f"{BG_BLUE}{FG_WHITE}{BOLD} {self.title} "
                f"{' ' * (term_width - len(self.title) - 2)}{RESET}")
        
        # Draw widgets
        for widget in self.widgets:
            if widget.visible:
                widget.render()
    
    def run(self):
        """Main event loop"""
        enable_ansi_windows()
        Screen.hide_cursor()
        self.mouse_handler.enable()
        self.running = True
        
        needs_render = True
        render_type = 'full'
        
        try:
            while self.running:
                # Conditional rendering (anti-flicker)
                if needs_render:
                    self.render_all(full_clear=(render_type == 'full'))
                    needs_render = False
                
                # Process input
                event = self.mouse_handler.read_input()
                
                if event:
                    event_type, data = event
                    
                    if event_type == 'key':
                        self._handle_key(data)
                        needs_render = True
                        render_type = 'full'
                        
                    elif event_type == 'mouse_move':
                        # Only render if hover state changed
                        if self._handle_mouse_move(data['x'], data['y']):
                            needs_render = True
                            render_type = 'hover'  # Skip full clear
                            
                    elif event_type == 'mouse_click':
                        self._handle_mouse_click(
                            data['x'], data['y'], 
                            data['button'], data['action']
                        )
                        needs_render = True
                        render_type = 'full'
                        
                    elif event_type == 'mouse_scroll':
                        self._handle_mouse_scroll(
                            data['x'], data['y'], 
                            data['direction']
                        )
                        needs_render = True
                        render_type = 'full'
                else:
                    time.sleep(0.05)  # Reduce CPU when idle
        
        finally:
            self.mouse_handler.disable()
            Screen.show_cursor()
            Screen.clear()
    
    def stop(self):
        """Exit application"""
        self.running = False
    
    def _handle_mouse_move(self, x: int, y: int) -> bool:
        """Handle mouse movement. Return True if state changed."""
        state_changed = False
        for widget in self.widgets:
            if widget.on_mouse_move(x, y):
                state_changed = True
        return state_changed
    
    def _handle_mouse_click(self, x: int, y: int, button: str, action: str):
        """Route click to appropriate widget"""
        for widget in reversed(self.widgets):  # Top to bottom
            if widget.visible and widget.enabled:
                if widget.on_mouse_click(x, y, button, action):
                    # Set focus
                    if self.focused_widget:
                        self.focused_widget.focused = False
                    self.focused_widget = widget
                    widget.focused = True
                    break
```

---

## Performance Optimization Patterns

### Anti-Flicker Techniques

#### 1. Conditional Rendering
```python
# Only render when state actually changes
needs_render = False

if user_input_received:
    process_input()
    needs_render = True

if needs_render:
    render_screen()
    needs_render = False
```

#### 2. Partial Screen Updates
```python
# Skip full screen clear for minor changes (e.g., hover)
def render_all(self, full_clear=True):
    if full_clear:
        Screen.clear()  # Only clear for major updates
    
    # Always redraw widgets (they overwrite their area)
    for widget in self.widgets:
        widget.render()
```

#### 3. State Change Detection
```python
def on_mouse_move(self, x: int, y: int) -> bool:
    """Only return True if hover state changed"""
    new_hover = self.contains_point(x, y)
    if new_hover != self.hover:
        self.hover = new_hover
        return True  # Needs render
    return False  # No change, skip render
```

#### 4. Sleep When Idle
```python
# Prevent CPU spinning when no input
if event:
    process_event()
else:
    time.sleep(0.05)  # 50ms sleep when idle
```

---

## Common Pitfalls & Solutions

### Problem: Screen Flickers on Mouse Movement
**Cause:** Calling `Screen.clear()` on every mouse move event  
**Solution:** Use conditional rendering - only clear for major updates
```python
# BAD
def render():
    Screen.clear()  # Flickers every time!
    draw_widgets()

# GOOD
def render(full_clear=False):
    if full_clear:  # Only on clicks/keys
        Screen.clear()
    draw_widgets()  # Overwrite in place
```

### Problem: Mouse Clicks Don't Register
**Cause:** QuickEdit mode is enabled (Windows default)  
**Solution:** Disable QuickEdit in console mode
```python
mode = wintypes.DWORD()
kernel32.GetConsoleMode(stdin, ctypes.byref(mode))
mode.value &= ~0x0040  # Disable ENABLE_QUICK_EDIT_MODE
kernel32.SetConsoleMode(stdin, mode)
```

### Problem: Mouse Position Offset by ~1 Character
**Cause:** Coordinate system mismatch (0-based vs 1-based)  
**Solution:** Add +1 when converting Windows coords to ANSI
```python
# Windows Console API returns 0-based
x = mouse_event.dwMousePosition.X  # 0-based
y = mouse_event.dwMousePosition.Y  # 0-based

# ANSI cursor positioning is 1-based
x_ansi = x + 1  # Convert to 1-based
y_ansi = y + 1
```

### Problem: Terminal Window is Scrollable
**Cause:** Console buffer larger than window  
**Solution:** Fix console size at startup
```python
def set_console_size(width: int, height: int):
    os.system(f'mode con: cols={width} lines={height}')

# At demo start
set_console_size(90, 30)
time.sleep(0.2)  # Wait for resize
```

### Problem: High CPU Usage When Idle
**Cause:** Tight loop polling input continuously  
**Solution:** Add sleep delay when no input available
```python
event = read_input()
if event:
    process(event)
else:
    time.sleep(0.05)  # Sleep 50ms when idle
```

---

## Design Best Practices

### Visual Hierarchy
```python
# Use color intensity to show importance
Primary Action:    BG_BRIGHT_CYAN + FG_BLACK  # Bright, high contrast
Focused Element:   BG_CYAN + FG_WHITE         # Medium
Normal Element:    BG_BLUE + FG_WHITE         # Subdued
Disabled Element:  FG_BRIGHT_BLACK            # Dim gray
```

### Feedback & Affordances
```python
# Always indicate interactivity
Button: Hover changes background color
List Item: Highlight on hover, different on selection
Link: Underline or color change
Disabled: Dim/grayed out

# Provide immediate feedback
Click: Visual response (flash, press effect)
Hover: Color change or underline
Focus: Border or background change
```

### Keyboard Shortcuts
```python
# Standard conventions
ESC:     Exit/Cancel/Back
ENTER:   Select/Confirm
SPACE:   Toggle (checkboxes, expand/collapse)
TAB:     Next widget/field
SHIFT+TAB: Previous widget
Arrow Keys: Navigate lists/menus
Page Up/Down: Scroll large lists
Home/End: Jump to start/end
```

### Layout Guidelines
```python
# Leave breathing room
- 1-2 lines padding between sections
- 2-4 spaces margin from screen edge
- 1 space padding inside borders

# Alignment
- Left-align text for readability
- Center titles and headers
- Right-align numbers/values

# Sizing
- Buttons: At least 3 chars wider than text
- Lists: Show 5-10 items at a time
- Dialogs: 1/3 to 1/2 screen width
```

---

## Complete Demo Code Structure

```python
#!/usr/bin/env python3
"""
Complete CLI Menu Demo
Combines all patterns into working examples
"""

import os
import sys
import time
import msvcrt
from typing import List, Callable, Optional, Tuple
import ctypes
from ctypes import wintypes

# ============================================================================
# SECTION 1: ANSI Codes & Screen Control
# ============================================================================
ESC = '\033'
CSI = '\033['
RESET = '\033[0m'
BOLD = '\033[1m'
# ... (color definitions)

class Screen:
    @staticmethod
    def clear():
        print('\033[2J', end='')
    
    @staticmethod
    def print_at(y: int, x: int, text: str):
        print(f'\033[{y};{x}H{text}', end='')
    
    @staticmethod
    def hide_cursor():
        print('\033[?25l', end='')
    
    @staticmethod
    def show_cursor():
        print('\033[?25h', end='')

# ============================================================================
# SECTION 2: Windows Console API (Mouse Support)
# ============================================================================
# ... (MouseHandler class)

# ============================================================================
# SECTION 3: Widget Base Classes
# ============================================================================
# ... (Widget, Button, ScrollableList, etc.)

# ============================================================================
# SECTION 4: Application Framework
# ============================================================================
# ... (Application class)

# ============================================================================
# SECTION 5: Demo Functions
# ============================================================================
def demo_simple_menu():
    """Demo: Basic keyboard menu"""
    menu = SimpleMenu("Main Menu", [
        "Option 1",
        "Option 2",
        "Exit"
    ])
    # ... run loop

def demo_mouse_buttons():
    """Demo: Clickable buttons"""
    set_console_size(90, 30)
    app = Application("Button Demo")
    # ... add buttons
    app.run()

def demo_all_widgets():
    """Demo: Complete widget showcase"""
    set_console_size(120, 30)
    app = Application("Widget Showcase")
    # ... add all widget types
    app.run()

# ============================================================================
# SECTION 6: Main Menu
# ============================================================================
if __name__ == '__main__':
    demos = [
        ("Simple Menu", demo_simple_menu),
        ("Mouse Buttons", demo_mouse_buttons),
        ("All Widgets", demo_all_widgets),
    ]
    
    # Show demo selector
    # ... menu code
```

---

## Quick Start Templates

### Template 1: Simple Keyboard Menu
```python
import msvcrt
import os

def simple_menu(items):
    current = 0
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        for i, item in enumerate(items):
            prefix = "> " if i == current else "  "
            print(f"{prefix}{item}")
        
        key = msvcrt.getch()
        
        if key == b'\xe0':  # Arrow key
            key = msvcrt.getch()
            if key == b'H':  # Up
                current = (current - 1) % len(items)
            elif key == b'P':  # Down
                current = (current + 1) % len(items)
        elif key == b'\r':  # Enter
            return current
        elif key == b'\x1b':  # ESC
            return None

# Usage
choice = simple_menu(["Option 1", "Option 2", "Exit"])
```

### Template 2: Mouse-Enabled Button
```python
from ctypes import wintypes
import ctypes

# Initialize
app = Application("My App")
button = Button(10, 5, "Click Me", lambda: print("Clicked!"))
app.add_widget(button)
app.run()
```

### Template 3: Progress Bar
```python
import time

for i in range(100):
    percent = i / 100
    bar = '█' * int(40 * percent) + '░' * (40 - int(40 * percent))
    print(f'\r[{bar}] {i}%', end='')
    time.sleep(0.05)
print()
```

---

## Additional Resources

### Related Files
- `CLI_MENU_CONTROL_COMPLETE.py` - Keyboard-only menu system
- `CLI_MENU_CONTROL_ADVANCED_MOUSE.py` - Full mouse-enabled widgets
- `CLI_MENU_SIMPLE_WORKING.py` - Minimal working example
- `CLI-Terminal-Styling-Complete-Reference.md` - ANSI codes reference

### Key Libraries
- `msvcrt` - Windows keyboard input (non-blocking)
- `ctypes` - Windows API access (mouse support)
- `shutil` - Terminal size detection
- `os` - Console control (mode con)

### Windows Console API References
- `GetStdHandle(-10)` - Get input handle
- `ReadConsoleInputW()` - Read input events
- `GetConsoleMode() / SetConsoleMode()` - Configure console
- `ENABLE_MOUSE_INPUT (0x0010)` - Enable mouse events
- `ENABLE_QUICK_EDIT_MODE (0x0040)` - Must disable for mouse!

---

## Summary

This reference covers complete CLI menu systems from simple keyboard navigation to advanced mouse-enabled interfaces. Key takeaways:

1. **Start Simple**: Begin with keyboard-only menus using `msvcrt`
2. **Add Mouse Support**: Use Windows Console API with proper mode configuration
3. **Prevent Flicker**: Use conditional rendering and partial updates
4. **Widget Pattern**: Base class with `render()`, `on_click()`, `on_move()`
5. **Application Loop**: Event processing with conditional rendering
6. **Performance**: State change detection + sleep when idle = smooth UI

All patterns are production-ready and optimized for Windows terminals with Python 3.6+.
