# ASCII ESCAPE CODES REFERENCE

## Core Definition
**ANSI Escape Sequences** are special character sequences that control cursor movement, color, styling, and other terminal operations. All sequences start with ESC (ASCII 27, `\033` or `\x1b`).

**Tags**: #ansi #terminal #escape-codes #cli #formatting

---

## COMPLETE ESCAPE CODES QUICK REFERENCE

### ESCAPE CODES - Code | Operation | Description

```python
# ═══════════════════════════════════════════════════════════════════════════
# BASE ESCAPE CHARACTERS
# ═══════════════════════════════════════════════════════════════════════════
ESC = '\033'                     # Escape character (ASCII 27)
ESC = '\x1b'                     # Escape character (hex notation)
CSI = '\033['                    # Control Sequence Introducer
OSC = '\033]'                    # Operating System Command
RESET = '\033[0m'                # Reset all attributes to default
RESET_ALL = '\033[0m'            # Reset all attributes (alias)

# ═══════════════════════════════════════════════════════════════════════════
# TEXT STYLE / FORMATTING
# ═══════════════════════════════════════════════════════════════════════════
BOLD = '\033[1m'                 # Bold or increased intensity
DIM = '\033[2m'                  # Faint, decreased intensity, or dim
ITALIC = '\033[3m'               # Italic text
UNDERLINE = '\033[4m'            # Underline text
BLINK = '\033[5m'                # Slow blink (less than 150 per minute)
BLINK_FAST = '\033[6m'           # Rapid blink (MS-DOS ANSI.SYS, 150+ per minute)
REVERSE = '\033[7m'              # Reverse video (swap foreground/background)
INVERT = '\033[7m'               # Invert colors (alias for reverse)
HIDDEN = '\033[8m'               # Conceal/hide text
CONCEAL = '\033[8m'              # Conceal text (alias)
STRIKETHROUGH = '\033[9m'        # Crossed-out/strikethrough text
STRIKE = '\033[9m'               # Strikethrough (alias)

# ═══════════════════════════════════════════════════════════════════════════
# RESET INDIVIDUAL ATTRIBUTES
# ═══════════════════════════════════════════════════════════════════════════
RESET_BOLD = '\033[21m'          # Double underline or bold off (not widely supported)
RESET_INTENSITY = '\033[22m'     # Normal intensity (not bold, not dim)
RESET_ITALIC = '\033[23m'        # Not italic, not Fraktur
RESET_UNDERLINE = '\033[24m'     # Not underlined
RESET_BLINK = '\033[25m'         # Not blinking
RESET_REVERSE = '\033[27m'       # Not reversed
RESET_HIDDEN = '\033[28m'        # Not concealed/revealed
RESET_STRIKETHROUGH = '\033[29m' # Not crossed out

# ═══════════════════════════════════════════════════════════════════════════
# FOREGROUND COLORS (16-COLOR STANDARD)
# ═══════════════════════════════════════════════════════════════════════════
FG_BLACK = '\033[30m'            # Black text
FG_RED = '\033[31m'              # Red text
FG_GREEN = '\033[32m'            # Green text
FG_YELLOW = '\033[33m'           # Yellow text
FG_BLUE = '\033[34m'             # Blue text
FG_MAGENTA = '\033[35m'          # Magenta text
FG_CYAN = '\033[36m'             # Cyan text
FG_WHITE = '\033[37m'            # White text
FG_DEFAULT = '\033[39m'          # Default foreground color

# ═══════════════════════════════════════════════════════════════════════════
# BACKGROUND COLORS (16-COLOR STANDARD)
# ═══════════════════════════════════════════════════════════════════════════
BG_BLACK = '\033[40m'            # Black background
BG_RED = '\033[41m'              # Red background
BG_GREEN = '\033[42m'            # Green background
BG_YELLOW = '\033[43m'           # Yellow background
BG_BLUE = '\033[44m'             # Blue background
BG_MAGENTA = '\033[45m'          # Magenta background
BG_CYAN = '\033[46m'             # Cyan background
BG_WHITE = '\033[47m'            # White background
BG_DEFAULT = '\033[49m'          # Default background color

# ═══════════════════════════════════════════════════════════════════════════
# BRIGHT/INTENSE FOREGROUND COLORS (16-COLOR EXTENDED)
# ═══════════════════════════════════════════════════════════════════════════
FG_BRIGHT_BLACK = '\033[90m'     # Bright black (gray)
FG_GRAY = '\033[90m'             # Gray (alias for bright black)
FG_GREY = '\033[90m'             # Grey (alias for bright black)
FG_BRIGHT_RED = '\033[91m'       # Bright red
FG_BRIGHT_GREEN = '\033[92m'     # Bright green
FG_BRIGHT_YELLOW = '\033[93m'    # Bright yellow
FG_BRIGHT_BLUE = '\033[94m'      # Bright blue
FG_BRIGHT_MAGENTA = '\033[95m'   # Bright magenta
FG_BRIGHT_CYAN = '\033[96m'      # Bright cyan
FG_BRIGHT_WHITE = '\033[97m'     # Bright white

# ═══════════════════════════════════════════════════════════════════════════
# BRIGHT/INTENSE BACKGROUND COLORS (16-COLOR EXTENDED)
# ═══════════════════════════════════════════════════════════════════════════
BG_BRIGHT_BLACK = '\033[100m'    # Bright black background
BG_GRAY = '\033[100m'            # Gray background (alias)
BG_GREY = '\033[100m'            # Grey background (alias)
BG_BRIGHT_RED = '\033[101m'      # Bright red background
BG_BRIGHT_GREEN = '\033[102m'    # Bright green background
BG_BRIGHT_YELLOW = '\033[103m'   # Bright yellow background
BG_BRIGHT_BLUE = '\033[104m'     # Bright blue background
BG_BRIGHT_MAGENTA = '\033[105m'  # Bright magenta background
BG_BRIGHT_CYAN = '\033[106m'     # Bright cyan background
BG_BRIGHT_WHITE = '\033[107m'    # Bright white background

# ═══════════════════════════════════════════════════════════════════════════
# 256-COLOR PALETTE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
def fg_256(n: int) -> str:       return f'\033[38;5;{n}m'  # Foreground 256-color (n=0-255)
def bg_256(n: int) -> str:       return f'\033[48;5;{n}m'  # Background 256-color (n=0-255)

# ═══════════════════════════════════════════════════════════════════════════
# RGB TRUE COLOR (24-BIT) FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
def fg_rgb(r: int, g: int, b: int) -> str:  return f'\033[38;2;{r};{g};{b}m'  # Foreground RGB
def bg_rgb(r: int, g: int, b: int) -> str:  return f'\033[48;2;{r};{g};{b}m'  # Background RGB

# ═══════════════════════════════════════════════════════════════════════════
# HEX COLOR FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
def hex_to_rgb(hex_color: str) -> tuple:
    """Convert #RRGGBB to (r, g, b) tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def fg_hex(hex_color: str) -> str:
    """Foreground color from hex (e.g., '#FF5733')"""
    r, g, b = hex_to_rgb(hex_color)
    return f'\033[38;2;{r};{g};{b}m'

def bg_hex(hex_color: str) -> str:
    """Background color from hex (e.g., '#FF5733')"""
    r, g, b = hex_to_rgb(hex_color)
    return f'\033[48;2;{r};{g};{b}m'

# ═══════════════════════════════════════════════════════════════════════════
# CURSOR MOVEMENT
# ═══════════════════════════════════════════════════════════════════════════
def CURSOR_UP(n: int = 1) -> str:         return f'\033[{n}A'  # Move cursor up n lines
def CURSOR_DOWN(n: int = 1) -> str:       return f'\033[{n}B'  # Move cursor down n lines
def CURSOR_FORWARD(n: int = 1) -> str:    return f'\033[{n}C'  # Move cursor right n columns
def CURSOR_RIGHT(n: int = 1) -> str:      return f'\033[{n}C'  # Move cursor right (alias)
def CURSOR_BACK(n: int = 1) -> str:       return f'\033[{n}D'  # Move cursor left n columns
def CURSOR_LEFT(n: int = 1) -> str:       return f'\033[{n}D'  # Move cursor left (alias)
def CURSOR_NEXT_LINE(n: int = 1) -> str:  return f'\033[{n}E'  # Move to beginning of line, n lines down
def CURSOR_PREV_LINE(n: int = 1) -> str:  return f'\033[{n}F'  # Move to beginning of line, n lines up
def CURSOR_COL(n: int) -> str:            return f'\033[{n}G'  # Move cursor to column n (1-based)
def CURSOR_POS(row: int, col: int) -> str: return f'\033[{row};{col}H'  # Set cursor position (1-based)
def CURSOR_POSITION(row: int, col: int) -> str: return f'\033[{row};{col}f'  # Set position (alternate)

# ═══════════════════════════════════════════════════════════════════════════
# CURSOR POSITION CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════
CURSOR_HOME = '\033[H'           # Move cursor to home position (1,1)
CURSOR_HOME_ALT = '\033[;H'      # Move to home (alternate syntax)
CURSOR_SAVE = '\033[s'           # Save cursor position (DEC)
CURSOR_RESTORE = '\033[u'        # Restore cursor position (DEC)
CURSOR_SAVE_SCO = '\033[7'       # Save cursor (SCO)
CURSOR_RESTORE_SCO = '\033[8'    # Restore cursor (SCO)

# ═══════════════════════════════════════════════════════════════════════════
# CURSOR VISIBILITY
# ═══════════════════════════════════════════════════════════════════════════
CURSOR_HIDE = '\033[?25l'        # Hide cursor
CURSOR_SHOW = '\033[?25h'        # Show cursor
CURSOR_INVISIBLE = '\033[?25l'   # Make cursor invisible (alias)
CURSOR_VISIBLE = '\033[?25h'     # Make cursor visible (alias)

# ═══════════════════════════════════════════════════════════════════════════
# CURSOR SHAPE (VT520)
# ═══════════════════════════════════════════════════════════════════════════
CURSOR_BLINKING_BLOCK = '\033[1 q'        # Blinking block
CURSOR_STEADY_BLOCK = '\033[2 q'          # Steady block
CURSOR_BLINKING_UNDERLINE = '\033[3 q'    # Blinking underline
CURSOR_STEADY_UNDERLINE = '\033[4 q'      # Steady underline
CURSOR_BLINKING_BAR = '\033[5 q'          # Blinking bar (vertical line)
CURSOR_STEADY_BAR = '\033[6 q'            # Steady bar

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN CLEARING
# ═══════════════════════════════════════════════════════════════════════════
CLEAR_SCREEN = '\033[2J'         # Clear entire screen
CLEAR_SCREEN_ALL = '\033[3J'     # Clear entire screen including scrollback
CLEAR_FROM_CURSOR = '\033[0J'    # Clear from cursor to end of screen
CLEAR_TO_CURSOR = '\033[1J'      # Clear from cursor to beginning of screen
CLEAR_LINE = '\033[2K'           # Clear entire line
CLEAR_LINE_FROM_CURSOR = '\033[0K' # Clear from cursor to end of line
CLEAR_LINE_TO_CURSOR = '\033[1K' # Clear from cursor to beginning of line

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN SCROLLING
# ═══════════════════════════════════════════════════════════════════════════
def SCROLL_UP(n: int = 1) -> str:    return f'\033[{n}S'  # Scroll up n lines
def SCROLL_DOWN(n: int = 1) -> str:  return f'\033[{n}T'  # Scroll down n lines

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN BUFFER MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
SAVE_SCREEN = '\033[?47h'        # Save screen
RESTORE_SCREEN = '\033[?47l'     # Restore screen
ALT_BUFFER_ENABLE = '\033[?1049h' # Enable alternate screen buffer
ALT_BUFFER_DISABLE = '\033[?1049l' # Disable alternate screen buffer
ALT_SCREEN_ON = '\033[?1049h'    # Alternate screen on (alias)
ALT_SCREEN_OFF = '\033[?1049l'   # Alternate screen off (alias)

# ═══════════════════════════════════════════════════════════════════════════
# SCREEN MODES
# ═══════════════════════════════════════════════════════════════════════════
SET_SCREEN_MODE = lambda n: f'\033[={n}h'   # Set screen mode
RESET_SCREEN_MODE = lambda n: f'\033[={n}l' # Reset screen mode

# ═══════════════════════════════════════════════════════════════════════════
# TERMINAL TITLE & WINDOW MANIPULATION
# ═══════════════════════════════════════════════════════════════════════════
def SET_TITLE(title: str) -> str:          return f'\033]0;{title}\007'  # Set window title
def SET_TITLE_ALT(title: str) -> str:      return f'\033]2;{title}\007'  # Set window title (alt)
def SET_ICON_NAME(name: str) -> str:       return f'\033]1;{name}\007'   # Set icon name
def SET_TITLE_AND_ICON(text: str) -> str:  return f'\033]0;{text}\007'   # Set both title and icon

# ═══════════════════════════════════════════════════════════════════════════
# HYPERLINKS (OSC 8)
# ═══════════════════════════════════════════════════════════════════════════
def HYPERLINK(url: str, text: str) -> str:
    """Create clickable hyperlink"""
    return f'\033]8;;{url}\033\\{text}\033]8;;\033\\'

HYPERLINK_START = lambda url: f'\033]8;;{url}\033\\'  # Start hyperlink
HYPERLINK_END = '\033]8;;\033\\'                       # End hyperlink

# ═══════════════════════════════════════════════════════════════════════════
# KEYBOARD & MOUSE INPUT
# ═══════════════════════════════════════════════════════════════════════════
ENABLE_MOUSE = '\033[?1000h'     # Enable mouse tracking
DISABLE_MOUSE = '\033[?1000l'    # Disable mouse tracking
ENABLE_MOUSE_BUTTON = '\033[?1002h'  # Enable button event tracking
DISABLE_MOUSE_BUTTON = '\033[?1002l' # Disable button event tracking
ENABLE_MOUSE_ANY = '\033[?1003h' # Enable any mouse event tracking
DISABLE_MOUSE_ANY = '\033[?1003l' # Disable any mouse event tracking
ENABLE_MOUSE_SGR = '\033[?1006h' # Enable SGR extended mouse mode
DISABLE_MOUSE_SGR = '\033[?1006l' # Disable SGR extended mouse mode

# ═══════════════════════════════════════════════════════════════════════════
# BRACKETED PASTE MODE
# ═══════════════════════════════════════════════════════════════════════════
ENABLE_BRACKETED_PASTE = '\033[?2004h'  # Enable bracketed paste
DISABLE_BRACKETED_PASTE = '\033[?2004l' # Disable bracketed paste
PASTE_START = '\033[200~'        # Paste start marker
PASTE_END = '\033[201~'          # Paste end marker

# ═══════════════════════════════════════════════════════════════════════════
# TERMINAL QUERIES
# ═══════════════════════════════════════════════════════════════════════════
QUERY_CURSOR_POS = '\033[6n'     # Query cursor position (returns ESC[row;colR)
QUERY_DEVICE_STATUS = '\033[5n'  # Query device status (returns ESC[0n or ESC[3n)
QUERY_DEVICE_ATTRS = '\033[c'    # Query device attributes
QUERY_DEVICE_ATTRS_SEC = '\033[>c' # Query secondary device attributes

# ═══════════════════════════════════════════════════════════════════════════
# SOFT RESET
# ═══════════════════════════════════════════════════════════════════════════
SOFT_RESET = '\033[!p'           # Soft terminal reset
RESET_TERMINAL = '\033c'         # Full terminal reset (RIS)

# ═══════════════════════════════════════════════════════════════════════════
# BELL & AUDIO
# ═══════════════════════════════════════════════════════════════════════════
BELL = '\007'                    # Terminal bell (beep)
BEEP = '\007'                    # Beep (alias)
VISUAL_BELL = '\033g'            # Visual bell (flash screen)

# ═══════════════════════════════════════════════════════════════════════════
# CHARSET SELECTION (G0/G1)
# ═══════════════════════════════════════════════════════════════════════════
CHARSET_G0_ASCII = '\033(B'      # Select ASCII for G0
CHARSET_G0_GRAPHICS = '\033(0'   # Select line drawing for G0
CHARSET_G1_ASCII = '\033)B'      # Select ASCII for G1
CHARSET_G1_GRAPHICS = '\033)0'   # Select line drawing for G1

# ═══════════════════════════════════════════════════════════════════════════
# TAB STOPS
# ═══════════════════════════════════════════════════════════════════════════
TAB_SET = '\033H'                # Set tab stop at current column
TAB_CLEAR = '\033[g'             # Clear tab stop at current column
TAB_CLEAR_ALL = '\033[3g'        # Clear all tab stops
TAB_FORWARD = '\t'               # Move to next tab stop
TAB_BACKWARD = '\033[Z'          # Move to previous tab stop

# ═══════════════════════════════════════════════════════════════════════════
# MARGINS & SCROLLING REGIONS
# ═══════════════════════════════════════════════════════════════════════════
def SET_SCROLL_REGION(top: int, bottom: int) -> str:
    """Set scrolling region (top, bottom line numbers)"""
    return f'\033[{top};{bottom}r'

RESET_SCROLL_REGION = '\033[r'   # Reset scrolling region to full screen

# ═══════════════════════════════════════════════════════════════════════════
# LINE ATTRIBUTES (VT100)
# ═══════════════════════════════════════════════════════════════════════════
DOUBLE_HEIGHT_TOP = '\033#3'     # Double-height characters (top half)
DOUBLE_HEIGHT_BOTTOM = '\033#4'  # Double-height characters (bottom half)
DOUBLE_WIDTH = '\033#6'          # Double-width characters
SINGLE_WIDTH = '\033#5'          # Single-width characters (normal)

# ═══════════════════════════════════════════════════════════════════════════
# ADDITIONAL TEXT ATTRIBUTES
# ═══════════════════════════════════════════════════════════════════════════
FRAKTUR = '\033[20m'             # Fraktur (Gothic) font
FRAMED = '\033[51m'              # Framed text
ENCIRCLED = '\033[52m'           # Encircled text
OVERLINED = '\033[53m'           # Overlined text
NOT_FRAMED = '\033[54m'          # Not framed or encircled
NOT_OVERLINED = '\033[55m'       # Not overlined

# ═══════════════════════════════════════════════════════════════════════════
# UNDERLINE STYLES (Extended)
# ═══════════════════════════════════════════════════════════════════════════
UNDERLINE_DOUBLE = '\033[21m'    # Doubly underlined
UNDERLINE_CURLY = '\033[4:3m'    # Curly underline
UNDERLINE_DOTTED = '\033[4:4m'   # Dotted underline
UNDERLINE_DASHED = '\033[4:5m'   # Dashed underline

# ═══════════════════════════════════════════════════════════════════════════
# UNDERLINE COLOR (Extended)
# ═══════════════════════════════════════════════════════════════════════════
def UNDERLINE_COLOR_RGB(r: int, g: int, b: int) -> str:
    """Set underline color (RGB)"""
    return f'\033[58;2;{r};{g};{b}m'

def UNDERLINE_COLOR_256(n: int) -> str:
    """Set underline color (256-color palette)"""
    return f'\033[58;5;{n}m'

UNDERLINE_COLOR_DEFAULT = '\033[59m'  # Default underline color

# ═══════════════════════════════════════════════════════════════════════════
# FONT SELECTION (SGR)
# ═══════════════════════════════════════════════════════════════════════════
FONT_PRIMARY = '\033[10m'        # Primary font
FONT_ALT_1 = '\033[11m'          # Alternative font 1
FONT_ALT_2 = '\033[12m'          # Alternative font 2
FONT_ALT_3 = '\033[13m'          # Alternative font 3
FONT_ALT_4 = '\033[14m'          # Alternative font 4
FONT_ALT_5 = '\033[15m'          # Alternative font 5
FONT_ALT_6 = '\033[16m'          # Alternative font 6
FONT_ALT_7 = '\033[17m'          # Alternative font 7
FONT_ALT_8 = '\033[18m'          # Alternative font 8
FONT_ALT_9 = '\033[19m'          # Alternative font 9

# ═══════════════════════════════════════════════════════════════════════════
# IDEOGRAM ATTRIBUTES (Rarely supported)
# ═══════════════════════════════════════════════════════════════════════════
IDEOGRAM_UNDERLINE = '\033[60m'  # Ideogram underline or right side line
IDEOGRAM_DOUBLE_UNDERLINE = '\033[61m'  # Ideogram double underline or double line on right
IDEOGRAM_OVERLINE = '\033[62m'   # Ideogram overline or left side line
IDEOGRAM_DOUBLE_OVERLINE = '\033[63m'   # Ideogram double overline or double line on left
IDEOGRAM_STRESS = '\033[64m'     # Ideogram stress marking
IDEOGRAM_RESET = '\033[65m'      # Reset ideogram attributes

# ═══════════════════════════════════════════════════════════════════════════
# COMBINED/COMPOUND CODES
# ═══════════════════════════════════════════════════════════════════════════
def combine(*codes: str) -> str:
    """Combine multiple escape codes into one sequence"""
    # Extract numeric codes from sequences like '\033[31m'
    nums = []
    for code in codes:
        if code.startswith('\033[') and code.endswith('m'):
            nums.append(code[2:-1])
    return f'\033[{";".join(nums)}m' if nums else ''

# Example combinations:
BOLD_RED = '\033[1;31m'          # Bold + Red
BOLD_GREEN = '\033[1;32m'        # Bold + Green
UNDERLINE_BLUE = '\033[4;34m'    # Underline + Blue
BOLD_UNDERLINE_CYAN = '\033[1;4;36m'  # Bold + Underline + Cyan

# ═══════════════════════════════════════════════════════════════════════════
# BOX DRAWING CHARACTERS (ASCII SAFE)
# ═══════════════════════════════════════════════════════════════════════════
BOX_H = '-'                      # Horizontal line (ASCII)
BOX_V = '|'                      # Vertical line (ASCII)
BOX_TL = '+'                     # Top-left corner (ASCII)
BOX_TR = '+'                     # Top-right corner (ASCII)
BOX_BL = '+'                     # Bottom-left corner (ASCII)
BOX_BR = '+'                     # Bottom-right corner (ASCII)
BOX_CROSS = '+'                  # Cross/intersection (ASCII)
BOX_T_DOWN = '+'                 # T junction down (ASCII)
BOX_T_UP = '+'                   # T junction up (ASCII)
BOX_T_RIGHT = '+'                # T junction right (ASCII)
BOX_T_LEFT = '+'                 # T junction left (ASCII)

# ═══════════════════════════════════════════════════════════════════════════
# BOX DRAWING CHARACTERS (UNICODE SINGLE LINE)
# ═══════════════════════════════════════════════════════════════════════════
BOX_SINGLE_H = '─'               # ─ U+2500 Horizontal
BOX_SINGLE_V = '│'               # │ U+2502 Vertical
BOX_SINGLE_TL = '┌'              # ┌ U+250C Top-left corner
BOX_SINGLE_TR = '┐'              # ┐ U+2510 Top-right corner
BOX_SINGLE_BL = '└'              # └ U+2514 Bottom-left corner
BOX_SINGLE_BR = '┘'              # ┘ U+2518 Bottom-right corner
BOX_SINGLE_CROSS = '┼'           # ┼ U+253C Cross
BOX_SINGLE_T_DOWN = '┬'          # ┬ U+252C T down
BOX_SINGLE_T_UP = '┴'            # ┴ U+2534 T up
BOX_SINGLE_T_RIGHT = '├'         # ├ U+251C T right
BOX_SINGLE_T_LEFT = '┤'          # ┤ U+2524 T left
BOX_SINGLE_H_HEAVY = '━'         # ━ U+2501 Heavy horizontal
BOX_SINGLE_V_HEAVY = '┃'         # ┃ U+2503 Heavy vertical

# ═══════════════════════════════════════════════════════════════════════════
# BOX DRAWING CHARACTERS (UNICODE DOUBLE LINE)
# ═══════════════════════════════════════════════════════════════════════════
BOX_DOUBLE_H = '═'               # ═ U+2550 Horizontal
BOX_DOUBLE_V = '║'               # ║ U+2551 Vertical
BOX_DOUBLE_TL = '╔'              # ╔ U+2554 Top-left corner
BOX_DOUBLE_TR = '╗'              # ╗ U+2557 Top-right corner
BOX_DOUBLE_BL = '╚'              # ╚ U+255A Bottom-left corner
BOX_DOUBLE_BR = '╝'              # ╝ U+255D Bottom-right corner
BOX_DOUBLE_CROSS = '╬'           # ╬ U+256C Cross
BOX_DOUBLE_T_DOWN = '╦'          # ╦ U+2566 T down
BOX_DOUBLE_T_UP = '╩'            # ╩ U+2569 T up
BOX_DOUBLE_T_RIGHT = '╠'         # ╠ U+2560 T right
BOX_DOUBLE_T_LEFT = '╣'          # ╣ U+2563 T left

# ═══════════════════════════════════════════════════════════════════════════
# BOX DRAWING CHARACTERS (UNICODE ROUNDED)
# ═══════════════════════════════════════════════════════════════════════════
BOX_ROUNDED_TL = '╭'             # ╭ U+256D Rounded top-left
BOX_ROUNDED_TR = '╮'             # ╮ U+256E Rounded top-right
BOX_ROUNDED_BL = '╰'             # ╰ U+2570 Rounded bottom-left
BOX_ROUNDED_BR = '╯'             # ╯ U+2571 Rounded bottom-right

# ═══════════════════════════════════════════════════════════════════════════
# BLOCK ELEMENTS
# ═══════════════════════════════════════════════════════════════════════════
BLOCK_FULL = '█'                 # █ U+2588 Full block
BLOCK_DARK = '▓'                 # ▓ U+2593 Dark shade
BLOCK_MEDIUM = '▒'               # ▒ U+2592 Medium shade
BLOCK_LIGHT = '░'                # ░ U+2591 Light shade
BLOCK_TOP = '▀'                  # ▀ U+2580 Upper half block
BLOCK_BOTTOM = '▄'               # ▄ U+2584 Lower half block
BLOCK_LEFT = '▌'                 # ▌ U+258C Left half block
BLOCK_RIGHT = '▐'                # ▐ U+2590 Right half block

# ═══════════════════════════════════════════════════════════════════════════
# PROGRESS BAR BLOCKS (8ths)
# ═══════════════════════════════════════════════════════════════════════════
PROGRESS_FULL = '█'              # █ U+2588 8/8 Full
PROGRESS_SEVEN_EIGHTHS = '▉'     # ▉ U+2589 7/8
PROGRESS_THREE_QUARTERS = '▊'    # ▊ U+258A 6/8 (3/4)
PROGRESS_FIVE_EIGHTHS = '▋'      # ▋ U+258B 5/8
PROGRESS_HALF = '▌'              # ▌ U+258C 4/8 (1/2)
PROGRESS_THREE_EIGHTHS = '▍'     # ▍ U+258D 3/8
PROGRESS_QUARTER = '▎'           # ▎ U+258E 2/8 (1/4)
PROGRESS_EIGHTH = '▏'            # ▏ U+258F 1/8
PROGRESS_EMPTY = ' '             # Empty space

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIC SHAPES
# ═══════════════════════════════════════════════════════════════════════════
CIRCLE_FILLED = '●'              # ● U+25CF Filled circle
CIRCLE_EMPTY = '○'               # ○ U+25CB Empty circle
CIRCLE_DOTTED = '◌'              # ◌ U+25CC Dotted circle
SQUARE_FILLED = '■'              # ■ U+25A0 Filled square
SQUARE_EMPTY = '□'               # □ U+25A1 Empty square
DIAMOND_FILLED = '◆'             # ◆ U+25C6 Filled diamond
DIAMOND_EMPTY = '◇'              # ◇ U+25C7 Empty diamond
TRIANGLE_UP = '▲'                # ▲ U+25B2 Up triangle
TRIANGLE_DOWN = '▼'              # ▼ U+25BC Down triangle
TRIANGLE_LEFT = '◀'              # ◀ U+25C0 Left triangle
TRIANGLE_RIGHT = '▶'             # ▶ U+25B6 Right triangle
TRIANGLE_UP_EMPTY = '△'          # △ U+25B3 Empty up triangle
TRIANGLE_DOWN_EMPTY = '▽'        # ▽ U+25BD Empty down triangle

# ═══════════════════════════════════════════════════════════════════════════
# ARROWS
# ═══════════════════════════════════════════════════════════════════════════
ARROW_UP = '↑'                   # ↑ U+2191 Upwards arrow
ARROW_DOWN = '↓'                 # ↓ U+2193 Downwards arrow
ARROW_LEFT = '←'                 # ← U+2190 Leftwards arrow
ARROW_RIGHT = '→'                # → U+2192 Rightwards arrow
ARROW_UP_DOWN = '↕'              # ↕ U+2195 Up down arrow
ARROW_LEFT_RIGHT = '↔'           # ↔ U+2194 Left right arrow
ARROW_NW = '↖'                   # ↖ U+2196 Northwest arrow
ARROW_NE = '↗'                   # ↗ U+2197 Northeast arrow
ARROW_SE = '↘'                   # ↘ U+2198 Southeast arrow
ARROW_SW = '↙'                   # ↙ U+2199 Southwest arrow
ARROW_DOUBLE_UP = '⇑'            # ⇑ U+21D1 Double up
ARROW_DOUBLE_DOWN = '⇓'          # ⇓ U+21D3 Double down
ARROW_DOUBLE_LEFT = '⇐'          # ⇐ U+21D0 Double left
ARROW_DOUBLE_RIGHT = '⇒'         # ⇒ U+21D2 Double right

# ═══════════════════════════════════════════════════════════════════════════
# CHECK MARKS & STATUS SYMBOLS
# ═══════════════════════════════════════════════════════════════════════════
CHECK_MARK = '✓'                 # ✓ U+2713 Check mark
CHECK_MARK_HEAVY = '✔'           # ✔ U+2714 Heavy check mark
CROSS_MARK = '✗'                 # ✗ U+2717 Ballot X
CROSS_MARK_HEAVY = '✘'           # ✘ U+2718 Heavy ballot X
BALLOT_BOX_EMPTY = '☐'           # ☐ U+2610 Ballot box
BALLOT_BOX_CHECK = '☑'           # ☑ U+2611 Ballot box with check
BALLOT_BOX_X = '☒'               # ☒ U+2612 Ballot box with X

# ═══════════════════════════════════════════════════════════════════════════
# BULLETS & LIST MARKERS
# ═══════════════════════════════════════════════════════════════════════════
BULLET = '•'                     # • U+2022 Bullet
BULLET_WHITE = '◦'               # ◦ U+25E6 White bullet
BULLET_TRIANGULAR = '‣'          # ‣ U+2023 Triangular bullet
BULLET_HYPHEN = '⁃'              # ⁃ U+2043 Hyphen bullet

# ═══════════════════════════════════════════════════════════════════════════
# STARS & RATINGS
# ═══════════════════════════════════════════════════════════════════════════
STAR_FILLED = '★'                # ★ U+2605 Black star
STAR_EMPTY = '☆'                 # ☆ U+2606 White star
STAR_CIRCLED = '✪'               # ✪ U+272A Circled white star

# ═══════════════════════════════════════════════════════════════════════════
# MATHEMATICAL & SPECIAL SYMBOLS
# ═══════════════════════════════════════════════════════════════════════════
PLUS_MINUS = '±'                 # ± U+00B1 Plus-minus
MULTIPLY = '×'                   # × U+00D7 Multiplication
DIVIDE = '÷'                     # ÷ U+00F7 Division
EQUALS_APPROX = '≈'              # ≈ U+2248 Almost equal
NOT_EQUAL = '≠'                  # ≠ U+2260 Not equal
LESS_EQUAL = '≤'                 # ≤ U+2264 Less than or equal
GREATER_EQUAL = '≥'              # ≥ U+2265 Greater than or equal
INFINITY = '∞'                   # ∞ U+221E Infinity
DEGREE = '°'                     # ° U+00B0 Degree sign
MICRO = 'µ'                      # µ U+00B5 Micro sign
SECTION = '§'                    # § U+00A7 Section sign
PARAGRAPH = '¶'                  # ¶ U+00B6 Pilcrow sign

# ═══════════════════════════════════════════════════════════════════════════
# WARNING & INFO SYMBOLS
# ═══════════════════════════════════════════════════════════════════════════
WARNING = '⚠'                    # ⚠ U+26A0 Warning sign
INFO = 'ℹ'                       # ℹ U+2139 Information source
QUESTION = '?'                   # ? Question mark
QUESTION_ORNAMENT = '❓'         # ❓ U+2753 Question mark ornament
EXCLAMATION = '!'                # ! Exclamation mark
EXCLAMATION_ORNAMENT = '❗'      # ❗ U+2757 Exclamation mark ornament

# ═══════════════════════════════════════════════════════════════════════════
# MUSICAL SYMBOLS
# ═══════════════════════════════════════════════════════════════════════════
NOTE_EIGHTH = '♪'                # ♪ U+266A Eighth note
NOTE_BEAMED = '♫'                # ♫ U+266B Beamed eighth notes
NOTE_FLAT = '♭'                  # ♭ U+266D Flat
NOTE_NATURAL = '♮'               # ♮ U+266E Natural
NOTE_SHARP = '♯'                 # ♯ U+266F Sharp

# ═══════════════════════════════════════════════════════════════════════════
# SPINNER ANIMATION FRAMES
# ═══════════════════════════════════════════════════════════════════════════
SPINNER_DOTS = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']  # Braille dots
SPINNER_LINE = ['|', '/', '-', '\\']                                    # Line spinner
SPINNER_ARROW = ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙']              # Arrow rotation
SPINNER_BOX = ['◰', '◳', '◲', '◱']                                      # Box quarters
SPINNER_DOTS_SIMPLE = ['.  ', '.. ', '...', '   ']                     # Simple dots
SPINNER_BOUNCE = ['⠁', '⠂', '⠄', '⡀', '⢀', '⠠', '⠐', '⠈']            # Bouncing
SPINNER_CLOCK = ['🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚', '🕛']  # Clock

# ═══════════════════════════════════════════════════════════════════════════
# EMOJI INDICATORS (Common in modern terminals)
# ═══════════════════════════════════════════════════════════════════════════
EMOJI_CHECK = '✅'               # White heavy check mark
EMOJI_CROSS = '❌'               # Cross mark
EMOJI_WARNING = '⚠️'             # Warning
EMOJI_INFO = 'ℹ️'                # Information
EMOJI_FIRE = '🔥'                # Fire
EMOJI_ROCKET = '🚀'              # Rocket
EMOJI_SPARKLES = '✨'            # Sparkles
EMOJI_TADA = '🎉'                # Party popper
EMOJI_THINKING = '🤔'            # Thinking face
EMOJI_THUMBS_UP = '👍'           # Thumbs up
EMOJI_THUMBS_DOWN = '👎'         # Thumbs down
EMOJI_HOURGLASS = '⏳'           # Hourglass
EMOJI_STOPWATCH = '⏱️'           # Stopwatch

# ═══════════════════════════════════════════════════════════════════════════
# TERMINAL SIZE QUERIES
# ═══════════════════════════════════════════════════════════════════════════
import shutil
import os

def get_terminal_size() -> tuple:
    """Get terminal dimensions (width, height)"""
    return shutil.get_terminal_size()

def get_terminal_width() -> int:
    """Get terminal width in columns"""
    return shutil.get_terminal_size().columns

def get_terminal_height() -> int:
    """Get terminal height in rows"""
    return shutil.get_terminal_size().lines

# ═══════════════════════════════════════════════════════════════════════════
# PLATFORM DETECTION
# ═══════════════════════════════════════════════════════════════════════════
import sys
import platform

def is_windows() -> bool:
    """Check if running on Windows"""
    return sys.platform == 'win32' or os.name == 'nt'

def is_mac() -> bool:
    """Check if running on macOS"""
    return sys.platform == 'darwin'

def is_linux() -> bool:
    """Check if running on Linux"""
    return sys.platform.startswith('linux')

def get_platform() -> str:
    """Get platform name"""
    return platform.system()

# ═══════════════════════════════════════════════════════════════════════════
# WINDOWS ANSI ENABLER
# ═══════════════════════════════════════════════════════════════════════════
def enable_ansi_windows():
    """Enable ANSI escape sequences on Windows 10+"""
    if is_windows():
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def enable_virtual_terminal_processing():
    """Enable Virtual Terminal Processing on Windows (alias)"""
    enable_ansi_windows()

# ═══════════════════════════════════════════════════════════════════════════
# WINDOWS CONSOLE SIZE
# ═══════════════════════════════════════════════════════════════════════════
def set_console_size(width: int, height: int):
    """Set Windows console size (Windows only)"""
    if is_windows():
        os.system(f'mode con: cols={width} lines={height}')

def set_console_title(title: str):
    """Set console title (cross-platform)"""
    if is_windows():
        os.system(f'title {title}')
    else:
        print(f'\033]0;{title}\007', end='', flush=True)

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY CLASS: Screen
# ═══════════════════════════════════════════════════════════════════════════
class Screen:
    """Screen control utilities"""
    
    @staticmethod
    def clear():
        """Clear entire screen"""
        print('\033[2J\033[H', end='', flush=True)
    
    @staticmethod
    def clear_line():
        """Clear current line"""
        print('\033[2K', end='', flush=True)
    
    @staticmethod
    def move_to(row: int, col: int):
        """Move cursor to position (1-based)"""
        print(f'\033[{row};{col}H', end='', flush=True)
    
    @staticmethod
    def print_at(row: int, col: int, text: str):
        """Print text at position"""
        print(f'\033[{row};{col}H{text}', end='', flush=True)
    
    @staticmethod
    def hide_cursor():
        """Hide cursor"""
        print('\033[?25l', end='', flush=True)
    
    @staticmethod
    def show_cursor():
        """Show cursor"""
        print('\033[?25h', end='', flush=True)
    
    @staticmethod
    def save_cursor():
        """Save cursor position"""
        print('\033[s', end='', flush=True)
    
    @staticmethod
    def restore_cursor():
        """Restore cursor position"""
        print('\033[u', end='', flush=True)
    
    @staticmethod
    def home():
        """Move cursor to home (1,1)"""
        print('\033[H', end='', flush=True)

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY CLASS: Color
# ═══════════════════════════════════════════════════════════════════════════
class Color:
    """Color utility methods"""
    
    @staticmethod
    def fg(r: int, g: int, b: int) -> str:
        """Foreground RGB color"""
        return f'\033[38;2;{r};{g};{b}m'
    
    @staticmethod
    def bg(r: int, g: int, b: int) -> str:
        """Background RGB color"""
        return f'\033[48;2;{r};{g};{b}m'
    
    @staticmethod
    def fg_256(n: int) -> str:
        """Foreground 256-color"""
        return f'\033[38;5;{n}m'
    
    @staticmethod
    def bg_256(n: int) -> str:
        """Background 256-color"""
        return f'\033[48;5;{n}m'
    
    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple:
        """Convert hex to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def fg_hex(hex_color: str) -> str:
        """Foreground from hex"""
        r, g, b = Color.hex_to_rgb(hex_color)
        return Color.fg(r, g, b)
    
    @staticmethod
    def bg_hex(hex_color: str) -> str:
        """Background from hex"""
        r, g, b = Color.hex_to_rgb(hex_color)
        return Color.bg(r, g, b)

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY CLASS: Cursor
# ═══════════════════════════════════════════════════════════════════════════
class Cursor:
    """Cursor control utilities"""
    
    @staticmethod
    def up(n: int = 1):
        """Move cursor up"""
        print(f'\033[{n}A', end='', flush=True)
    
    @staticmethod
    def down(n: int = 1):
        """Move cursor down"""
        print(f'\033[{n}B', end='', flush=True)
    
    @staticmethod
    def forward(n: int = 1):
        """Move cursor right"""
        print(f'\033[{n}C', end='', flush=True)
    
    @staticmethod
    def back(n: int = 1):
        """Move cursor left"""
        print(f'\033[{n}D', end='', flush=True)
    
    @staticmethod
    def move_to(row: int, col: int):
        """Move to position"""
        print(f'\033[{row};{col}H', end='', flush=True)
    
    @staticmethod
    def hide():
        """Hide cursor"""
        print('\033[?25l', end='', flush=True)
    
    @staticmethod
    def show():
        """Show cursor"""
        print('\033[?25h', end='', flush=True)

```

---

## COMPREHENSIVE 256-COLOR PALETTE

The 256-color palette is divided into sections:
- **0-7**: Standard colors (same as 30-37 foreground codes)
- **8-15**: Bright colors (same as 90-97 foreground codes)
- **16-231**: 216-color cube (6×6×6 RGB)
- **232-255**: Grayscale ramp (24 shades)

### Standard Colors (0-15)
```
0:Black   1:Red     2:Green   3:Yellow  4:Blue    5:Magenta 6:Cyan    7:White
8:BrBlack 9:BrRed   10:BrGreen 11:BrYellow 12:BrBlue 13:BrMagenta 14:BrCyan 15:BrWhite
```

### 6×6×6 Color Cube (16-231)
Formula: `16 + 36×r + 6×g + b` where r,g,b ∈ [0,5]

### Grayscale (232-255)
24 shades from dark to light gray

---

## COMMON ANSI PATTERNS

### Text Formatting Patterns
```python
# Single attribute
f"{BOLD}text{RESET}"

# Multiple attributes
f"{BOLD}{FG_RED}text{RESET}"

# Nested formatting
f"{BOLD}Bold {ITALIC}and italic{RESET_ITALIC} just bold{RESET}"

# Complex combination
f"{combine(BOLD, UNDERLINE, FG_CYAN)}Styled text{RESET}"
```

### Cursor Movement Patterns
```python
# Clear screen and home
print(f"{CLEAR_SCREEN}{CURSOR_HOME}", end='')

# Save position, move, restore
print(f"{CURSOR_SAVE}Moving...{CURSOR_RESTORE}")

# Move to specific position
print(f"{CURSOR_POS(10, 20)}Text at row 10, col 20")

# Draw at multiple positions
Screen.print_at(5, 10, "Line 1")
Screen.print_at(6, 10, "Line 2")
```

### Progress Bar Pattern
```python
def progress_bar(percent: int, width: int = 20) -> str:
    """Create a progress bar"""
    filled = int(width * percent / 100)
    bar = PROGRESS_FULL * filled + PROGRESS_EMPTY * (width - filled)
    return f"[{bar}] {percent}%"
```

### Spinner Pattern
```python
import time

for frame in SPINNER_DOTS:
    print(f"\r{frame} Loading...", end='', flush=True)
    time.sleep(0.1)
```

### Box Drawing Pattern
```python
def draw_box(width: int, height: int) -> str:
    """Draw a box"""
    top = BOX_SINGLE_TL + BOX_SINGLE_H * width + BOX_SINGLE_TR
    mid = (BOX_SINGLE_V + ' ' * width + BOX_SINGLE_V + '\n') * height
    bot = BOX_SINGLE_BL + BOX_SINGLE_H * width + BOX_SINGLE_BR
    return top + '\n' + mid + bot
```

---

## TERMINAL COMPATIBILITY

### Windows
- **Windows 10+**: Native ANSI support via Virtual Terminal Processing
- **Older Windows**: Requires `colorama` or manual VT100 enablement
- Use `enable_ansi_windows()` to enable

### macOS / Linux
- Native ANSI support in all modern terminals
- iTerm2, Terminal.app, GNOME Terminal, etc. all support full ANSI

### Cross-Platform Best Practices
```python
# Always enable ANSI on Windows first
if is_windows():
    enable_ansi_windows()

# Use try/except for unsupported features
try:
    print(f"{fg_rgb(255, 100, 50)}RGB color{RESET}")
except:
    print(f"{FG_RED}Fallback color{RESET}")
```

---

## QUICK START TEMPLATE

```python
# Import and setup
import sys
import os

# Enable ANSI on Windows
if sys.platform == 'win32':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Basic escape codes
ESC = '\033'
RESET = '\033[0m'
BOLD = '\033[1m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'
FG_BLUE = '\033[34m'
BG_YELLOW = '\033[43m'

# Usage
print(f"{BOLD}{FG_RED}Error:{RESET} Something went wrong")
print(f"{FG_GREEN}✓{RESET} Success!")
print(f"{BG_YELLOW}{FG_BLUE}Highlighted{RESET}")
```

---

## SEE ALSO
- [CLI Menu Design Reference](CLI-Menu-Design-Reference.md)
- [CLI Cross-Platform Reference](CLI-Menu-Cross-Platform-Reference.md)
- [CLI Component Taxonomy](CLI-Menu-Component-Taxonomy.md)

---

**Last Updated**: December 8, 2025
**Tags**: #ansi #escape-codes #terminal #cli #reference
