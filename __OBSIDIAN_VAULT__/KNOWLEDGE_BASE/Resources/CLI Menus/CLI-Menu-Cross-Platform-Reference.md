# CLI Menu Cross-Platform Reference

> **Curses + ASCII mappings for menu functionality: keyboard events, mouse events, and interactivity**

---

## Table of Contents

1. [Curses Module Overview](#curses-module-overview)
2. [ASCII Character Mappings](#ascii-character-mappings)
3. [Keyboard Event Handling](#keyboard-event-handling)
4. [Mouse Event Handling](#mouse-event-handling)
5. [Cross-Platform Implementation](#cross-platform-implementation)
6. [Integration Examples](#integration-examples)

---

## Curses Module Overview

### CURSES MODULE (Linux/macOS/Codespaces) - Function | Parameters | Action | Returns

```python
# ═══════════════════════════════════════════════════════════════════════════
# INITIALIZATION & CLEANUP
# ═══════════════════════════════════════════════════════════════════════════
import curses

curses.initscr()             # None | Initialize curses library | Returns window object (stdscr)
curses.wrapper(func)         # func:callable | Initialize, call func with stdscr, cleanup | Returns func result
curses.endwin()              # None | Restore terminal to normal state | Returns None
stdscr.keypad(True)          # flag:bool | Enable special key interpretation | Returns None
curses.noecho()              # None | Disable key echo to screen | Returns None
curses.echo()                # None | Enable key echo to screen | Returns None
curses.cbreak()              # None | Disable line buffering (immediate key response) | Returns None
curses.nocbreak()            # None | Enable line buffering | Returns None
curses.raw()                 # None | Raw mode (no special key processing) | Returns None
curses.noraw()               # None | Disable raw mode | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN CONTROL
# ═══════════════════════════════════════════════════════════════════════════
stdscr.clear()               # None | Clear entire screen | Returns None
stdscr.erase()               # None | Clear screen (without forcing repaint) | Returns None
stdscr.clrtobot()            # None | Clear from cursor to bottom | Returns None
stdscr.clrtoeol()            # None | Clear from cursor to end of line | Returns None
stdscr.refresh()             # None | Update physical screen with virtual screen | Returns None
stdscr.noutrefresh()         # None | Update virtual screen (call doupdate later) | Returns None
curses.doupdate()            # None | Update physical screen (after noutrefresh) | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# CURSOR CONTROL
# ═══════════════════════════════════════════════════════════════════════════
stdscr.move(y, x)            # y:int, x:int | Move cursor to (y, x) 0-based | Returns None
stdscr.getyx()               # None | Get current cursor position | Returns tuple (y, x)
stdscr.getmaxyx()            # None | Get screen dimensions | Returns tuple (rows, cols)
stdscr.getbegyx()            # None | Get window origin | Returns tuple (y, x)
curses.curs_set(visibility)  # visibility:int (0=invisible, 1=normal, 2=very visible) | Set cursor visibility | Returns previous state

# ═══════════════════════════════════════════════════════════════════════════
# TEXT OUTPUT
# ═══════════════════════════════════════════════════════════════════════════
stdscr.addstr(str)           # str:str | Print string at cursor | Returns None
stdscr.addstr(y, x, str)     # y:int, x:int, str:str | Print string at position | Returns None
stdscr.addstr(y, x, str, attr) # y:int, x:int, str:str, attr:int | Print with attributes | Returns None
stdscr.addch(ch)             # ch:str/int | Print single character at cursor | Returns None
stdscr.addch(y, x, ch)       # y:int, x:int, ch:str/int | Print character at position | Returns None
stdscr.addch(y, x, ch, attr) # y:int, x:int, ch:str/int, attr:int | Print with attributes | Returns None
stdscr.insstr(str)           # str:str | Insert string at cursor | Returns None
stdscr.insstr(y, x, str)     # y:int, x:int, str:str | Insert string at position | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# KEYBOARD INPUT
# ═══════════════════════════════════════════════════════════════════════════
stdscr.getch()               # None (blocking) | Read single key | Returns int (key code)
stdscr.getch(y, x)           # y:int, x:int | Move cursor then read key | Returns int
stdscr.getkey()              # None (blocking) | Read single key | Returns str (key name)
stdscr.getkey(y, x)          # y:int, x:int | Move cursor then read key | Returns str
stdscr.get_wch()             # None (blocking) | Read wide character | Returns str or int
stdscr.nodelay(flag)         # flag:bool | Set non-blocking input (True) or blocking (False) | Returns None
stdscr.timeout(delay)        # delay:int | Set input timeout in ms (-1=blocking, 0=non-block) | Returns None

# Key constants
curses.KEY_UP                # Arrow up key code
curses.KEY_DOWN              # Arrow down key code
curses.KEY_LEFT              # Arrow left key code
curses.KEY_RIGHT             # Arrow right key code
curses.KEY_HOME              # Home key
curses.KEY_END               # End key
curses.KEY_PPAGE             # Page up
curses.KEY_NPAGE             # Page down
curses.KEY_BACKSPACE         # Backspace key
curses.KEY_DC                # Delete key
curses.KEY_IC                # Insert key
curses.KEY_ENTER             # Enter key
curses.KEY_F1                # Function key F1 (F1-F12 available)
curses.KEY_MOUSE             # Mouse event occurred

# ═══════════════════════════════════════════════════════════════════════════
# MOUSE INPUT (Full Support in Codespaces!)
# ═══════════════════════════════════════════════════════════════════════════
curses.mousemask(mousemask)  # mousemask:int | Set mouse events to report | Returns tuple (availmask, oldmask)
curses.getmouse()            # None | Get queued mouse event | Returns tuple (id, x, y, z, bstate)
curses.mouseinterval(interval) # interval:int | Set click detection time (ms) | Returns previous interval
curses.ungetmouse(id, x, y, z, bstate) # Mouse event data | Push mouse event back | Returns None

# Mouse event constants
curses.BUTTON1_PRESSED       # Left button pressed
curses.BUTTON1_RELEASED      # Left button released
curses.BUTTON1_CLICKED       # Left button clicked
curses.BUTTON1_DOUBLE_CLICKED # Left button double-clicked
curses.BUTTON1_TRIPLE_CLICKED # Left button triple-clicked
curses.BUTTON2_PRESSED       # Middle button pressed
curses.BUTTON2_RELEASED      # Middle button released
curses.BUTTON2_CLICKED       # Middle button clicked
curses.BUTTON3_PRESSED       # Right button pressed
curses.BUTTON3_RELEASED      # Right button released
curses.BUTTON3_CLICKED       # Right button clicked
curses.BUTTON4_PRESSED       # Scroll wheel up
curses.BUTTON5_PRESSED       # Scroll wheel down
curses.BUTTON_SHIFT          # Shift key held during mouse event
curses.BUTTON_CTRL           # Ctrl key held during mouse event
curses.BUTTON_ALT            # Alt key held during mouse event
curses.REPORT_MOUSE_POSITION # Mouse movement tracking
curses.ALL_MOUSE_EVENTS      # All mouse events combined

# ═══════════════════════════════════════════════════════════════════════════
# COLORS & ATTRIBUTES
# ═══════════════════════════════════════════════════════════════════════════
curses.start_color()         # None | Initialize color support | Returns None
curses.has_colors()          # None | Check if terminal supports colors | Returns bool
curses.can_change_color()    # None | Check if can modify color definitions | Returns bool
curses.init_pair(pair, fg, bg) # pair:int, fg:int, bg:int | Define color pair | Returns None
curses.pair_number(attr)     # attr:int | Extract pair number from attribute | Returns int
curses.color_pair(n)         # n:int | Get attribute for color pair n | Returns int
curses.pair_content(pair)    # pair:int | Get colors for pair | Returns tuple (fg, bg)

# Color constants
curses.COLOR_BLACK           # 0 - Black color
curses.COLOR_RED             # 1 - Red color
curses.COLOR_GREEN           # 2 - Green color
curses.COLOR_YELLOW          # 3 - Yellow color
curses.COLOR_BLUE            # 4 - Blue color
curses.COLOR_MAGENTA         # 5 - Magenta color
curses.COLOR_CYAN            # 6 - Cyan color
curses.COLOR_WHITE           # 7 - White color
curses.COLORS                # Total colors available (8 or 256)
curses.COLOR_PAIRS           # Total color pairs available

# Attribute constants
curses.A_NORMAL              # Normal display (no attributes)
curses.A_STANDOUT            # Best highlighting mode
curses.A_UNDERLINE           # Underline text
curses.A_REVERSE             # Reverse video (swap fg/bg)
curses.A_BLINK               # Blinking text
curses.A_DIM                 # Half-bright text
curses.A_BOLD                # Bold text
curses.A_ALTCHARSET          # Alternate character set (line drawing)
curses.A_INVIS               # Invisible text
curses.A_PROTECT             # Protected mode
curses.A_HORIZONTAL          # Horizontal highlight
curses.A_LEFT                # Left highlight
curses.A_LOW                 # Low highlight
curses.A_RIGHT               # Right highlight
curses.A_TOP                 # Top highlight
curses.A_VERTICAL            # Vertical highlight
curses.A_ITALIC              # Italic text

# Attribute manipulation
stdscr.attron(attr)          # attr:int | Enable attributes | Returns None
stdscr.attroff(attr)         # attr:int | Disable attributes | Returns None
stdscr.attrset(attr)         # attr:int | Set attributes (replace all) | Returns None
stdscr.bkgd(ch, attr)        # ch:str/int, attr:int | Set background char/attr | Returns None

# ═══════════════════════════════════════════════════════════════════════════
# WINDOWS & PANELS
# ═══════════════════════════════════════════════════════════════════════════
curses.newwin(nlines, ncols) # nlines:int, ncols:int | Create window at cursor | Returns window object
curses.newwin(nlines, ncols, begin_y, begin_x) # With position | Create window at position | Returns window object
win.subwin(nlines, ncols, begin_y, begin_x) # Create subwindow | Create derived window | Returns window object
win.derwin(nlines, ncols, begin_y, begin_x) # Relative coords | Create derived window (relative) | Returns window object
win.mvwin(new_y, new_x)      # new_y:int, new_x:int | Move window | Returns None
win.resize(nlines, ncols)    # nlines:int, ncols:int | Resize window | Returns None
curses.newpad(nlines, ncols) # nlines:int, ncols:int | Create pad (large virtual window) | Returns pad object

# ═══════════════════════════════════════════════════════════════════════════
# BORDERS & BOX DRAWING
# ═══════════════════════════════════════════════════════════════════════════
stdscr.border()              # None | Draw border using default chars | Returns None
stdscr.border(ls, rs, ts, bs, tl, tr, bl, br) # Custom border chars | Draw custom border | Returns None
stdscr.box()                 # None | Draw box with default chars | Returns None
stdscr.box(vertch, horch)    # vertch:str, horch:str | Draw box with custom chars | Returns None
stdscr.hline(ch, n)          # ch:str/int, n:int | Draw horizontal line | Returns None
stdscr.vline(ch, n)          # ch:str/int, n:int | Draw vertical line | Returns None

# Box drawing characters (ACS_*)
curses.ACS_ULCORNER          # Upper-left corner
curses.ACS_URCORNER          # Upper-right corner
curses.ACS_LLCORNER          # Lower-left corner
curses.ACS_LRCORNER          # Lower-right corner
curses.ACS_HLINE             # Horizontal line
curses.ACS_VLINE             # Vertical line
curses.ACS_LTEE              # Left tee (├)
curses.ACS_RTEE              # Right tee (┤)
curses.ACS_TTEE              # Top tee (┬)
curses.ACS_BTEE              # Bottom tee (┴)
curses.ACS_PLUS              # Plus/cross (┼)

# ═══════════════════════════════════════════════════════════════════════════
# SPECIAL FEATURES
# ═══════════════════════════════════════════════════════════════════════════
curses.beep()                # None | Emit audible beep | Returns None
curses.flash()               # None | Flash screen | Returns None
curses.napms(ms)             # ms:int | Sleep for milliseconds | Returns None
stdscr.scrollok(flag)        # flag:bool | Enable/disable scrolling | Returns None
stdscr.scroll(lines)         # lines:int | Scroll window by lines | Returns None
stdscr.idlok(flag)           # flag:bool | Enable/disable hardware line insert/delete | Returns None
stdscr.leaveok(flag)         # flag:bool | Leave cursor at current position after refresh | Returns None
```

### WINDOWS CONSOLE API (ctypes + kernel32) - Function | Parameters | Action | Returns

```python
# ═══════════════════════════════════════════════════════════════════════════
# SETUP (Windows Only)
# ═══════════════════════════════════════════════════════════════════════════
import ctypes
from ctypes import wintypes

kernel32 = ctypes.windll.kernel32

# ═══════════════════════════════════════════════════════════════════════════
# CONSOLE HANDLES
# ═══════════════════════════════════════════════════════════════════════════
kernel32.GetStdHandle(-10)   # STD_INPUT_HANDLE | Get stdin handle | Returns HANDLE
kernel32.GetStdHandle(-11)   # STD_OUTPUT_HANDLE | Get stdout handle | Returns HANDLE
kernel32.GetStdHandle(-12)   # STD_ERROR_HANDLE | Get stderr handle | Returns HANDLE

# ═══════════════════════════════════════════════════════════════════════════
# CONSOLE MODE
# ═══════════════════════════════════════════════════════════════════════════
kernel32.GetConsoleMode(handle, mode_ptr) # handle:HANDLE, mode_ptr:ptr | Get console mode flags | Returns bool
kernel32.SetConsoleMode(handle, mode)     # handle:HANDLE, mode:DWORD | Set console mode flags | Returns bool

# Mode flags
ENABLE_PROCESSED_INPUT       # 0x0001 | Ctrl+C processing enabled
ENABLE_LINE_INPUT            # 0x0002 | Line buffering enabled
ENABLE_ECHO_INPUT            # 0x0004 | Input echo enabled
ENABLE_WINDOW_INPUT          # 0x0008 | Window resize events enabled
ENABLE_MOUSE_INPUT           # 0x0010 | Mouse input events enabled
ENABLE_QUICK_EDIT_MODE       # 0x0040 | QuickEdit mode (MUST DISABLE for mouse)
ENABLE_EXTENDED_FLAGS        # 0x0080 | Required for QuickEdit modification
ENABLE_VIRTUAL_TERMINAL_PROCESSING # 0x0004 | Enable ANSI escape sequences (output mode)

# ═══════════════════════════════════════════════════════════════════════════
# STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════
class COORD(ctypes.Structure):
    _fields_ = [('X', ctypes.c_short), ('Y', ctypes.c_short)]

class MOUSE_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ('dwMousePosition', COORD),      # Mouse position (0-based)
        ('dwButtonState', wintypes.DWORD),
        ('dwControlKeyState', wintypes.DWORD),
        ('dwEventFlags', wintypes.DWORD)
    ]

class INPUT_RECORD(ctypes.Structure):
    class _EVENT(ctypes.Union):
        _fields_ = [('MouseEvent', MOUSE_EVENT_RECORD)]
    _fields_ = [('EventType', wintypes.WORD), ('Event', _EVENT)]

# ═══════════════════════════════════════════════════════════════════════════
# INPUT READING
# ═══════════════════════════════════════════════════════════════════════════
kernel32.ReadConsoleInputW(handle, buffer, length, read_ptr)
    # handle:HANDLE, buffer:ptr, length:int, read_ptr:ptr
    # Action: Read console input events (keyboard, mouse)
    # Returns: bool (success/failure)

# Event types
KEY_EVENT                    # 1 | Keyboard event
MOUSE_EVENT                  # 2 | Mouse event

# Mouse button states (dwButtonState)
FROM_LEFT_1ST_BUTTON_PRESSED # 0x0001 | Left button
RIGHTMOST_BUTTON_PRESSED     # 0x0002 | Right button
FROM_LEFT_2ND_BUTTON_PRESSED # 0x0004 | Middle button

# Mouse event flags (dwEventFlags)
MOUSE_MOVED                  # 0x0001 | Mouse moved
DOUBLE_CLICK                 # 0x0002 | Double click
MOUSE_WHEELED                # 0x0004 | Mouse wheel scrolled
MOUSE_HWHEELED               # 0x0008 | Horizontal wheel scrolled

# ═══════════════════════════════════════════════════════════════════════════
# KEYBOARD INPUT (msvcrt - Simple Alternative)
# ═══════════════════════════════════════════════════════════════════════════
import msvcrt

msvcrt.kbhit()               # None | Check if key is waiting | Returns bool
msvcrt.getch()               # None (blocking) | Read single byte | Returns bytes
msvcrt.getwch()              # None (blocking) | Read wide character | Returns str
msvcrt.ungetch(byte)         # byte:bytes | Push byte back to buffer | Returns None

# Special keys (two-byte sequences)
# Arrow keys: b'\xe0' or b'\x00' followed by:
#   b'H' = Up (0x48)
#   b'P' = Down (0x50)
#   b'K' = Left (0x4B)
#   b'M' = Right (0x4D)
```

### CROSS-PLATFORM MAPPINGS - Operation | Windows (msvcrt/ctypes) | Linux/Codespaces (curses)

```python
# ═══════════════════════════════════════════════════════════════════════════
# INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════
Initialize terminal           | enable_ansi_windows() via SetConsoleMode | curses.initscr()
Cleanup terminal              | show_cursor(), restore mode | curses.endwin()
Enable special keys           | N/A (direct byte reading) | stdscr.keypad(True)
Disable echo                  | N/A (no automatic echo) | curses.noecho()
Immediate key response        | N/A (msvcrt.getch is immediate) | curses.cbreak()

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN CONTROL
# ═══════════════════════════════════════════════════════════════════════════
Clear screen                  | print('\033[2J\033[H') | stdscr.clear()
Clear to end of line          | print('\033[K') | stdscr.clrtoeol()
Clear to bottom               | print('\033[J') | stdscr.clrtobot()
Refresh screen                | sys.stdout.flush() | stdscr.refresh()

# ═══════════════════════════════════════════════════════════════════════════
# CURSOR CONTROL
# ═══════════════════════════════════════════════════════════════════════════
Move cursor                   | print(f'\033[{y};{x}H') | stdscr.move(y, x)
Hide cursor                   | print('\033[?25l') | curses.curs_set(0)
Show cursor                   | print('\033[?25h') | curses.curs_set(1)
Get cursor position           | Manual tracking | stdscr.getyx()
Get screen size               | shutil.get_terminal_size() | stdscr.getmaxyx()

# ═══════════════════════════════════════════════════════════════════════════
# TEXT OUTPUT
# ═══════════════════════════════════════════════════════════════════════════
Print at position             | print(f'\033[{y};{x}H{text}') | stdscr.addstr(y, x, text)
Print with color              | print(f'\033[{color}m{text}\033[0m') | stdscr.addstr(y, x, text, curses.color_pair(n))
Print with attributes         | ANSI codes (\033[1m = bold) | stdscr.addstr(y, x, text, curses.A_BOLD)

# ═══════════════════════════════════════════════════════════════════════════
# KEYBOARD INPUT
# ═══════════════════════════════════════════════════════════════════════════
Check if key pressed          | msvcrt.kbhit() | stdscr.nodelay(True); getch() != -1
Read single key (blocking)    | msvcrt.getch() | stdscr.getch()
Read key name                 | Manual mapping | stdscr.getkey()
Non-blocking input            | msvcrt.kbhit() + getch() | stdscr.nodelay(True)

# Key mappings
Up arrow                      | b'\xe0' + b'H' | curses.KEY_UP
Down arrow                    | b'\xe0' + b'P' | curses.KEY_DOWN
Left arrow                    | b'\xe0' + b'K' | curses.KEY_LEFT
Right arrow                   | b'\xe0' + b'M' | curses.KEY_RIGHT
Enter                         | b'\r' | curses.KEY_ENTER or ord('\n')
Escape                        | b'\x1b' | 27
Backspace                     | b'\x08' | curses.KEY_BACKSPACE
Delete                        | b'\xe0' + b'S' | curses.KEY_DC

# ═══════════════════════════════════════════════════════════════════════════
# MOUSE INPUT
# ═══════════════════════════════════════════════════════════════════════════
Enable mouse                  | SetConsoleMode with ENABLE_MOUSE_INPUT | curses.mousemask(curses.ALL_MOUSE_EVENTS)
Disable QuickEdit (Windows)   | SetConsoleMode clear QUICK_EDIT_MODE | N/A (not needed)
Read mouse event              | ReadConsoleInputW → MOUSE_EVENT_RECORD | getch() == KEY_MOUSE; getmouse()
Get mouse coordinates         | dwMousePosition.X, .Y (0-based) | getmouse() returns (id, x, y, z, bstate) (0-based)
Coordinate conversion         | Add +1 for ANSI (1-based) | Use as-is (0-based)

# Mouse events
Left click                    | dwButtonState & 0x0001 | bstate & BUTTON1_CLICKED
Right click                   | dwButtonState & 0x0002 | bstate & BUTTON3_CLICKED
Middle click                  | dwButtonState & 0x0004 | bstate & BUTTON2_CLICKED
Double click                  | dwEventFlags & 0x0002 | bstate & BUTTON1_DOUBLE_CLICKED
Mouse move                    | dwEventFlags & 0x0001 | bstate & REPORT_MOUSE_POSITION
Scroll up                     | dwEventFlags & 0x0004 (wheel delta > 0) | bstate & BUTTON4_PRESSED
Scroll down                   | dwEventFlags & 0x0004 (wheel delta < 0) | bstate & BUTTON5_PRESSED

# ═══════════════════════════════════════════════════════════════════════════
# COLORS
# ═══════════════════════════════════════════════════════════════════════════
Initialize colors             | N/A (ANSI codes work directly) | curses.start_color()
Define color pair             | N/A (use ANSI codes) | curses.init_pair(n, fg, bg)
Use color pair                | print(f'\033[{fg}m\033[{bg+10}m') | curses.color_pair(n)

# Standard colors
Black                         | '\033[30m' | curses.COLOR_BLACK (0)
Red                           | '\033[31m' | curses.COLOR_RED (1)
Green                         | '\033[32m' | curses.COLOR_GREEN (2)
Yellow                        | '\033[33m' | curses.COLOR_YELLOW (3)
Blue                          | '\033[34m' | curses.COLOR_BLUE (4)
Magenta                       | '\033[35m' | curses.COLOR_MAGENTA (5)
Cyan                          | '\033[36m' | curses.COLOR_CYAN (6)
White                         | '\033[37m' | curses.COLOR_WHITE (7)

# ═══════════════════════════════════════════════════════════════════════════
# TEXT ATTRIBUTES
# ═══════════════════════════════════════════════════════════════════════════
Normal                        | '\033[0m' | curses.A_NORMAL
Bold                          | '\033[1m' | curses.A_BOLD
Dim                           | '\033[2m' | curses.A_DIM
Italic                        | '\033[3m' | curses.A_ITALIC
Underline                     | '\033[4m' | curses.A_UNDERLINE
Blink                         | '\033[5m' | curses.A_BLINK
Reverse                       | '\033[7m' | curses.A_REVERSE
Reset attributes              | '\033[0m' | curses.A_NORMAL

# ═══════════════════════════════════════════════════════════════════════════
# SPECIAL FEATURES
# ═══════════════════════════════════════════════════════════════════════════
Beep                          | print('\a') | curses.beep()
Flash screen                  | Manual implementation | curses.flash()
Sleep                         | time.sleep(ms/1000) | curses.napms(ms)
```

---

## Cross-Platform Implementation

### Complete Unified Menu System (Windows + Codespaces)

```python
#!/usr/bin/env python3
"""
Cross-Platform CLI Menu System
Works on: Windows (msvcrt/ctypes) and Linux/macOS/Codespaces (curses)
Standard library only - no pip installs required
"""

import sys
import platform

# ═══════════════════════════════════════════════════════════════════════════
# PLATFORM DETECTION
# ═══════════════════════════════════════════════════════════════════════════

IS_WINDOWS = sys.platform == 'win32'
IS_UNIX = not IS_WINDOWS

# ═══════════════════════════════════════════════════════════════════════════
# PLATFORM-SPECIFIC IMPORTS
# ═══════════════════════════════════════════════════════════════════════════

if IS_WINDOWS:
    import msvcrt
    import ctypes
    from ctypes import wintypes
else:
    import curses

# ═══════════════════════════════════════════════════════════════════════════
# UNIFIED MENU API
# ═══════════════════════════════════════════════════════════════════════════

class CrossPlatformMenu:
    """Unified menu interface for Windows and Unix systems"""
    
    def __init__(self, items, title="Menu"):
        self.items = items
        self.title = title
        self.selected = 0
        self.running = False
        
        if IS_WINDOWS:
            self._init_windows()
        else:
            self._init_curses()
    
    # ═══════════════════════════════════════════════════════════════════════
    # WINDOWS IMPLEMENTATION
    # ═══════════════════════════════════════════════════════════════════════
    
    def _init_windows(self):
        """Initialize Windows console"""
        self.kernel32 = ctypes.windll.kernel32
        
        # Enable ANSI escape sequences
        stdout_handle = self.kernel32.GetStdHandle(-11)
        mode = wintypes.DWORD()
        self.kernel32.GetConsoleMode(stdout_handle, ctypes.byref(mode))
        mode.value |= 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
        self.kernel32.SetConsoleMode(stdout_handle, mode.value)
        
        # Enable mouse input
        self.stdin_handle = self.kernel32.GetStdHandle(-10)
        stdin_mode = wintypes.DWORD()
        self.kernel32.GetConsoleMode(self.stdin_handle, ctypes.byref(stdin_mode))
        stdin_mode.value |= 0x0010   # ENABLE_MOUSE_INPUT
        stdin_mode.value |= 0x0080   # ENABLE_EXTENDED_FLAGS
        stdin_mode.value &= ~0x0040  # Disable ENABLE_QUICK_EDIT_MODE
        self.kernel32.SetConsoleMode(self.stdin_handle, stdin_mode.value)
        
        # Hide cursor
        print('\033[?25l', end='', flush=True)
    
    def _cleanup_windows(self):
        """Restore Windows console"""
        print('\033[?25h', end='', flush=True)  # Show cursor
        print('\033[0m', end='', flush=True)    # Reset colors
    
    def _clear_windows(self):
        """Clear screen on Windows"""
        print('\033[2J\033[H', end='', flush=True)
    
    def _draw_windows(self):
        """Draw menu on Windows"""
        self._clear_windows()
        
        # Title
        print(f'\033[1m\033[36m{self.title}\033[0m\n')
        
        # Menu items
        for i, item in enumerate(self.items):
            if i == self.selected:
                # Selected item (reverse video)
                print(f'\033[7m> {item}\033[0m')
            else:
                print(f'  {item}')
        
        # Instructions
        print(f'\n\033[90m↑↓: Navigate | Enter: Select | Mouse: Click | Q: Quit\033[0m')
        sys.stdout.flush()
    
    def _get_input_windows(self):
        """Get input on Windows (keyboard + mouse)"""
        # Check keyboard
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            # Arrow keys
            if key in (b'\xe0', b'\x00'):
                arrow = msvcrt.getch()
                if arrow == b'H':  # Up
                    self.selected = (self.selected - 1) % len(self.items)
                    return 'redraw'
                elif arrow == b'P':  # Down
                    self.selected = (self.selected + 1) % len(self.items)
                    return 'redraw'
            
            # Enter
            elif key == b'\r':
                return 'select'
            
            # Quit
            elif key in (b'q', b'Q'):
                return 'quit'
        
        # Check mouse
        input_record = ctypes.c_uint * 128
        events_read = wintypes.DWORD()
        
        class COORD(ctypes.Structure):
            _fields_ = [('X', ctypes.c_short), ('Y', ctypes.c_short)]
        
        class MOUSE_EVENT_RECORD(ctypes.Structure):
            _fields_ = [
                ('dwMousePosition', COORD),
                ('dwButtonState', wintypes.DWORD),
                ('dwControlKeyState', wintypes.DWORD),
                ('dwEventFlags', wintypes.DWORD)
            ]
        
        class INPUT_RECORD(ctypes.Structure):
            class _EVENT(ctypes.Union):
                _fields_ = [('MouseEvent', MOUSE_EVENT_RECORD)]
            _fields_ = [('EventType', wintypes.WORD), ('Event', _EVENT)]
        
        record = INPUT_RECORD()
        if self.kernel32.ReadConsoleInputW(
            self.stdin_handle,
            ctypes.byref(record),
            1,
            ctypes.byref(events_read)
        ):
            if record.EventType == 2:  # MOUSE_EVENT
                mouse = record.Event.MouseEvent
                
                # Left click
                if mouse.dwButtonState & 0x0001:
                    y = mouse.dwMousePosition.Y
                    # Title is at line 0-1, items start at line 2
                    # Account for title + blank line
                    item_index = y - 2
                    
                    if 0 <= item_index < len(self.items):
                        self.selected = item_index
                        return 'select'
        
        return None
    
    # ═══════════════════════════════════════════════════════════════════════
    # CURSES IMPLEMENTATION (Linux/macOS/Codespaces)
    # ═══════════════════════════════════════════════════════════════════════
    
    def _init_curses(self):
        """Initialize curses (handled by wrapper)"""
        pass
    
    def _cleanup_curses(self):
        """Cleanup curses (handled by wrapper)"""
        pass
    
    def _draw_curses(self, stdscr):
        """Draw menu with curses"""
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        # Title
        title_x = (w - len(self.title)) // 2
        stdscr.addstr(0, max(0, title_x), self.title, 
                     curses.A_BOLD | curses.color_pair(1))
        
        # Menu items
        start_y = 2
        for i, item in enumerate(self.items):
            y = start_y + i
            x = 2
            
            if i == self.selected:
                stdscr.addstr(y, x, f"> {item}", curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"  {item}")
        
        # Instructions
        inst = "↑↓: Navigate | Enter: Select | Mouse: Click | Q: Quit"
        inst_y = start_y + len(self.items) + 2
        stdscr.addstr(inst_y, 2, inst, curses.A_DIM)
        
        stdscr.refresh()
    
    def _get_input_curses(self, stdscr):
        """Get input with curses (keyboard + mouse)"""
        key = stdscr.getch()
        
        # Arrow keys
        if key == curses.KEY_UP:
            self.selected = (self.selected - 1) % len(self.items)
            return 'redraw'
        elif key == curses.KEY_DOWN:
            self.selected = (self.selected + 1) % len(self.items)
            return 'redraw'
        
        # Enter
        elif key in (curses.KEY_ENTER, ord('\n'), ord('\r')):
            return 'select'
        
        # Quit
        elif key in (ord('q'), ord('Q')):
            return 'quit'
        
        # Mouse
        elif key == curses.KEY_MOUSE:
            try:
                _, x, y, _, bstate = curses.getmouse()
                
                if bstate & curses.BUTTON1_CLICKED:
                    # Items start at y=2
                    item_index = y - 2
                    
                    if 0 <= item_index < len(self.items):
                        self.selected = item_index
                        return 'select'
            except:
                pass
        
        return None
    
    def _run_curses(self, stdscr):
        """Main loop for curses"""
        # Setup
        curses.curs_set(0)  # Hide cursor
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        stdscr.keypad(True)
        curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
        stdscr.nodelay(True)  # Non-blocking input
        
        self.running = True
        
        while self.running:
            self._draw_curses(stdscr)
            
            action = self._get_input_curses(stdscr)
            
            if action == 'select':
                return self.selected
            elif action == 'quit':
                return None
            
            curses.napms(10)  # Small delay to reduce CPU
        
        return None
    
    # ═══════════════════════════════════════════════════════════════════════
    # UNIFIED PUBLIC API
    # ═══════════════════════════════════════════════════════════════════════
    
    def run(self):
        """
        Run menu and return selected index or None if quit
        Works on both Windows and Unix systems
        """
        if IS_WINDOWS:
            try:
                self.running = True
                self._draw_windows()
                
                while self.running:
                    action = self._get_input_windows()
                    
                    if action == 'redraw':
                        self._draw_windows()
                    elif action == 'select':
                        return self.selected
                    elif action == 'quit':
                        return None
                
            finally:
                self._cleanup_windows()
        
        else:  # Unix (curses)
            return curses.wrapper(self._run_curses)

# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE USAGE
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Example menu application"""
    
    menu_items = [
        "🚀 Start New Project",
        "📂 Open Existing Project",
        "⚙️  Settings",
        "📊 View Statistics",
        "❓ Help",
        "❌ Exit"
    ]
    
    menu = CrossPlatformMenu(
        items=menu_items,
        title="=== Main Menu ==="
    )
    
    result = menu.run()
    
    if result is not None:
        print(f"\n\033[32m✓\033[0m Selected: {menu_items[result]}")
    else:
        print("\n\033[33m!\033[0m Quit without selection")

if __name__ == '__main__':
    main()
```

---

## Platform-Specific Details

### Windows-Specific Considerations

```python
# ═══════════════════════════════════════════════════════════════════════════
# WINDOWS CONSOLE SETUP
# ═══════════════════════════════════════════════════════════════════════════

import ctypes
from ctypes import wintypes

def setup_windows_console():
    """Complete Windows console setup for advanced features"""
    kernel32 = ctypes.windll.kernel32
    
    # Enable ANSI escape sequences (output)
    stdout_handle = kernel32.GetStdHandle(-11)
    mode = wintypes.DWORD()
    kernel32.GetConsoleMode(stdout_handle, ctypes.byref(mode))
    mode.value |= 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
    kernel32.SetConsoleMode(stdout_handle, mode.value)
    
    # Enable mouse input + disable QuickEdit (input)
    stdin_handle = kernel32.GetStdHandle(-10)
    stdin_mode = wintypes.DWORD()
    kernel32.GetConsoleMode(stdin_handle, ctypes.byref(stdin_mode))
    stdin_mode.value |= 0x0010   # ENABLE_MOUSE_INPUT
    stdin_mode.value |= 0x0080   # ENABLE_EXTENDED_FLAGS
    stdin_mode.value &= ~0x0040  # Disable ENABLE_QUICK_EDIT_MODE
    kernel32.SetConsoleMode(stdin_handle, stdin_mode.value)
    
    return kernel32, stdin_handle

# ═══════════════════════════════════════════════════════════════════════════
# MOUSE EVENT HANDLING (Windows)
# ═══════════════════════════════════════════════════════════════════════════

class WindowsMouseHandler:
    """Complete mouse handling for Windows"""
    
    def __init__(self):
        self.kernel32 = ctypes.windll.kernel32
        self.stdin = self.kernel32.GetStdHandle(-10)
        
        # Enable mouse
        mode = wintypes.DWORD()
        self.kernel32.GetConsoleMode(self.stdin, ctypes.byref(mode))
        mode.value |= 0x0010   # ENABLE_MOUSE_INPUT
        mode.value |= 0x0080   # ENABLE_EXTENDED_FLAGS
        mode.value &= ~0x0040  # Disable QuickEdit
        self.kernel32.SetConsoleMode(self.stdin, mode.value)
    
    def read_mouse_event(self):
        """
        Read mouse event from console
        Returns: dict with keys: x, y, button, action, modifiers
        """
        class COORD(ctypes.Structure):
            _fields_ = [('X', ctypes.c_short), ('Y', ctypes.c_short)]
        
        class MOUSE_EVENT_RECORD(ctypes.Structure):
            _fields_ = [
                ('dwMousePosition', COORD),
                ('dwButtonState', wintypes.DWORD),
                ('dwControlKeyState', wintypes.DWORD),
                ('dwEventFlags', wintypes.DWORD)
            ]
        
        class INPUT_RECORD(ctypes.Structure):
            class _EVENT(ctypes.Union):
                _fields_ = [('MouseEvent', MOUSE_EVENT_RECORD)]
            _fields_ = [('EventType', wintypes.WORD), ('Event', _EVENT)]
        
        record = INPUT_RECORD()
        events_read = wintypes.DWORD()
        
        if self.kernel32.ReadConsoleInputW(
            self.stdin,
            ctypes.byref(record),
            1,
            ctypes.byref(events_read)
        ):
            if record.EventType == 2:  # MOUSE_EVENT
                mouse = record.Event.MouseEvent
                
                # Parse button state
                button = None
                if mouse.dwButtonState & 0x0001:
                    button = 'left'
                elif mouse.dwButtonState & 0x0002:
                    button = 'right'
                elif mouse.dwButtonState & 0x0004:
                    button = 'middle'
                
                # Parse action
                action = None
                if mouse.dwEventFlags & 0x0001:
                    action = 'move'
                elif mouse.dwEventFlags & 0x0002:
                    action = 'double_click'
                elif mouse.dwEventFlags & 0x0004:
                    action = 'wheel'
                elif button:
                    action = 'click'
                
                # Parse modifiers
                modifiers = []
                ctrl_state = mouse.dwControlKeyState
                if ctrl_state & 0x0008:  # SHIFT_PRESSED
                    modifiers.append('shift')
                if ctrl_state & 0x0003:  # CTRL_PRESSED (left or right)
                    modifiers.append('ctrl')
                if ctrl_state & 0x0001:  # ALT_PRESSED
                    modifiers.append('alt')
                
                return {
                    'x': mouse.dwMousePosition.X,
                    'y': mouse.dwMousePosition.Y,
                    'button': button,
                    'action': action,
                    'modifiers': modifiers
                }
        
        return None
```

### Codespaces/Linux-Specific Considerations

```python
# ═══════════════════════════════════════════════════════════════════════════
# CURSES SETUP FOR CODESPACES
# ═══════════════════════════════════════════════════════════════════════════

import curses

def setup_curses_menu(stdscr):
    """Complete curses setup for Codespaces/Linux"""
    
    # Basic setup
    curses.curs_set(0)           # Hide cursor
    curses.noecho()              # Don't echo keys
    curses.cbreak()              # Immediate key response
    stdscr.keypad(True)          # Enable special keys
    stdscr.nodelay(False)        # Blocking input (or True for non-blocking)
    
    # Color setup
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
        
        # Define color pairs
        curses.init_pair(1, curses.COLOR_CYAN, -1)     # Cyan on default
        curses.init_pair(2, curses.COLOR_GREEN, -1)    # Green on default
        curses.init_pair(3, curses.COLOR_RED, -1)      # Red on default
        curses.init_pair(4, curses.COLOR_YELLOW, -1)   # Yellow on default
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Highlight
    
    # Mouse setup (works perfectly in Codespaces!)
    curses.mousemask(
        curses.BUTTON1_CLICKED |          # Left click
        curses.BUTTON1_DOUBLE_CLICKED |   # Double click
        curses.BUTTON3_CLICKED |          # Right click
        curses.BUTTON4_PRESSED |          # Scroll up
        curses.BUTTON5_PRESSED |          # Scroll down
        curses.REPORT_MOUSE_POSITION      # Movement tracking
    )
    
    return stdscr

# ═══════════════════════════════════════════════════════════════════════════
# MOUSE EVENT HANDLING (Curses)
# ═══════════════════════════════════════════════════════════════════════════

class CursesMouseHandler:
    """Complete mouse handling for curses"""
    
    def __init__(self, stdscr):
        self.stdscr = stdscr
        curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    
    def read_mouse_event(self, key):
        """
        Process mouse event from getch()
        Returns: dict with keys: x, y, button, action, modifiers
        """
        if key != curses.KEY_MOUSE:
            return None
        
        try:
            id, x, y, z, bstate = curses.getmouse()
            
            # Parse button
            button = None
            if bstate & (curses.BUTTON1_PRESSED | curses.BUTTON1_RELEASED | curses.BUTTON1_CLICKED):
                button = 'left'
            elif bstate & (curses.BUTTON2_PRESSED | curses.BUTTON2_RELEASED | curses.BUTTON2_CLICKED):
                button = 'middle'
            elif bstate & (curses.BUTTON3_PRESSED | curses.BUTTON3_RELEASED | curses.BUTTON3_CLICKED):
                button = 'right'
            elif bstate & curses.BUTTON4_PRESSED:
                button = 'wheel_up'
            elif bstate & curses.BUTTON5_PRESSED:
                button = 'wheel_down'
            
            # Parse action
            action = None
            if bstate & (curses.BUTTON1_CLICKED | curses.BUTTON2_CLICKED | curses.BUTTON3_CLICKED):
                action = 'click'
            elif bstate & (curses.BUTTON1_DOUBLE_CLICKED | curses.BUTTON2_DOUBLE_CLICKED | curses.BUTTON3_DOUBLE_CLICKED):
                action = 'double_click'
            elif bstate & (curses.BUTTON1_TRIPLE_CLICKED | curses.BUTTON2_TRIPLE_CLICKED | curses.BUTTON3_TRIPLE_CLICKED):
                action = 'triple_click'
            elif bstate & curses.REPORT_MOUSE_POSITION:
                action = 'move'
            elif button in ('wheel_up', 'wheel_down'):
                action = 'wheel'
            
            # Parse modifiers
            modifiers = []
            if bstate & curses.BUTTON_SHIFT:
                modifiers.append('shift')
            if bstate & curses.BUTTON_CTRL:
                modifiers.append('ctrl')
            if bstate & curses.BUTTON_ALT:
                modifiers.append('alt')
            
            return {
                'x': x,
                'y': y,
                'button': button,
                'action': action,
                'modifiers': modifiers
            }
        
        except curses.error:
            return None
```

---

## Integration Examples

### Example 1: Simple Menu (Works Everywhere)

```python
def simple_menu_example():
    """Minimal working example for both platforms"""
    
    items = ["Option 1", "Option 2", "Option 3", "Exit"]
    
    menu = CrossPlatformMenu(items, "Simple Menu")
    result = menu.run()
    
    if result is not None:
        print(f"Selected: {items[result]}")
```

### Example 2: Advanced Menu with Colors (Curses)

```python
def curses_colored_menu(stdscr):
    """Advanced curses menu with colors and styling"""
    
    # Setup
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
    
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    
    items = [
        "🚀 Deploy Application",
        "🔧 Configure Settings",
        "📊 View Analytics",
        "🔒 Security Options",
        "❌ Exit"
    ]
    
    selected = 0
    
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        # Title with box
        title = "Advanced Menu System"
        title_x = (w - len(title)) // 2
        stdscr.addstr(0, title_x, title, curses.A_BOLD | curses.color_pair(1))
        stdscr.addstr(1, 0, "─" * w, curses.color_pair(1))
        
        # Menu items
        start_y = 3
        for i, item in enumerate(items):
            y = start_y + i * 2
            
            if i == selected:
                # Highlighted item
                stdscr.addstr(y, 2, f"▶ {item}", 
                            curses.color_pair(4) | curses.A_BOLD)
            else:
                # Normal item
                stdscr.addstr(y, 2, f"  {item}", curses.color_pair(2))
        
        # Status bar
        status = f"Item {selected + 1}/{len(items)} | ↑↓: Navigate | Enter: Select | q: Quit"
        stdscr.addstr(h - 1, 0, status, curses.color_pair(3))
        
        stdscr.refresh()
        
        # Input
        key = stdscr.getch()
        
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(items) - 1:
            selected += 1
        elif key in (curses.KEY_ENTER, ord('\n')):
            if selected == len(items) - 1:
                break
            else:
                # Show selection
                stdscr.addstr(h - 2, 2, f"✓ Executed: {items[selected]}", 
                            curses.A_BOLD | curses.color_pair(2))
                stdscr.refresh()
                curses.napms(1000)
        elif key == curses.KEY_MOUSE:
            try:
                _, x, y, _, bstate = curses.getmouse()
                if bstate & curses.BUTTON1_CLICKED:
                    # Calculate clicked item
                    for i in range(len(items)):
                        item_y = start_y + i * 2
                        if y == item_y:
                            selected = i
                            if selected == len(items) - 1:
                                return
                            break
            except:
                pass
        elif key in (ord('q'), ord('Q')):
            break

if __name__ == '__main__':
    curses.wrapper(curses_colored_menu)
```

### Example 3: Mouse-Interactive Grid (Codespaces)

```python
def grid_demo(stdscr):
    """Interactive grid with full mouse support"""
    
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    
    # Grid state
    grid = [[False] * 20 for _ in range(10)]
    
    while True:
        stdscr.clear()
        
        # Title
        stdscr.addstr(0, 0, "Click cells to toggle! | Q: Quit", curses.A_BOLD)
        
        # Draw grid
        start_y, start_x = 2, 2
        for y in range(10):
            for x in range(20):
                cell_y = start_y + y
                cell_x = start_x + x * 2
                
                if grid[y][x]:
                    stdscr.addstr(cell_y, cell_x, "██", curses.color_pair(2))
                else:
                    stdscr.addstr(cell_y, cell_x, "░░", curses.color_pair(1))
        
        stdscr.refresh()
        
        # Input
        key = stdscr.getch()
        
        if key == curses.KEY_MOUSE:
            try:
                _, x, y, _, bstate = curses.getmouse()
                
                if bstate & curses.BUTTON1_CLICKED:
                    # Calculate grid position
                    grid_y = y - start_y
                    grid_x = (x - start_x) // 2
                    
                    if 0 <= grid_y < 10 and 0 <= grid_x < 20:
                        grid[grid_y][grid_x] = not grid[grid_y][grid_x]
            except:
                pass
        
        elif key in (ord('q'), ord('Q')):
            break

if __name__ == '__main__':
    curses.wrapper(grid_demo)
```

---

## Summary

### ✅ **What Works Where**

| Feature | Windows | Codespaces/Linux | Standard Library |
|---------|---------|------------------|------------------|
| **Keyboard input** | ✅ msvcrt | ✅ curses | ✅ Yes |
| **Arrow keys** | ✅ msvcrt | ✅ curses | ✅ Yes |
| **Mouse clicks** | ✅ ctypes + Console API | ✅ curses | ✅ Yes |
| **Mouse movement** | ✅ ctypes + Console API | ✅ curses | ✅ Yes |
| **Mouse wheel** | ✅ ctypes + Console API | ✅ curses | ✅ Yes |
| **Colors** | ✅ ANSI escape codes | ✅ curses | ✅ Yes |
| **Screen control** | ✅ ANSI escape codes | ✅ curses | ✅ Yes |
| **Non-blocking input** | ✅ msvcrt.kbhit() | ✅ curses.nodelay() | ✅ Yes |

### 🎯 **Best Practices**

1. **Use platform detection**: Check `sys.platform` to choose implementation
2. **Abstract interfaces**: Create unified API like `CrossPlatformMenu`
3. **Test on both platforms**: Windows behavior differs from Unix
4. **Handle cleanup**: Always restore terminal state on exit
5. **Use curses.wrapper()**: Automatically handles init/cleanup on Unix
6. **Disable QuickEdit on Windows**: Required for mouse support
7. **Enable ANSI on Windows**: Required for escape sequences

### 📦 **Zero Dependencies**

Everything shown uses **Python standard library only**:
- `curses` - Unix/Linux/macOS (standard)
- `msvcrt` - Windows (standard)
- `ctypes` - Windows Console API (standard)
- No pip installs required!

Works perfectly in **GitHub Codespaces** with full mouse support!
