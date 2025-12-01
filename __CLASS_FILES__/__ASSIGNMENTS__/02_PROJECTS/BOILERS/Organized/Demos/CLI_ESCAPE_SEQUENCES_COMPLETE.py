"""
COMPLETE CLI ESCAPE SEQUENCES & STYLING REFERENCE
==================================================
Comprehensive collection of ANSI escape codes, sequences, and CLI styling
for high-compatibility terminal applications.

Author: GitHub Copilot
Date: 2025-11-30
Compatibility: Windows (cmd, PowerShell), Linux, macOS terminals
"""

import os
import sys
import time

# ============================================================================
# SECTION 1: ANSI ESCAPE CODE BASICS
# ============================================================================

# Escape sequence prefix
ESC = '\033'
CSI = '\033['  # Control Sequence Introducer

# Alternative escape methods
ESC_HEX = '\x1b'
ESC_OCTAL = '\033'
ESC_UNICODE = '\u001b'

# ============================================================================
# SECTION 2: TEXT FORMATTING & STYLES
# ============================================================================

# Reset
RESET = '\033[0m'
RESET_ALL = '\033[0m'

# Text Styles
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
BLINK_FAST = '\033[6m'
REVERSE = '\033[7m'  # Inverse/Reverse video
HIDDEN = '\033[8m'
STRIKETHROUGH = '\033[9m'

# Reset Individual Styles
RESET_BOLD = '\033[21m'
RESET_DIM = '\033[22m'
RESET_ITALIC = '\033[23m'
RESET_UNDERLINE = '\033[24m'
RESET_BLINK = '\033[25m'
RESET_REVERSE = '\033[27m'
RESET_HIDDEN = '\033[28m'
RESET_STRIKETHROUGH = '\033[29m'

# ============================================================================
# SECTION 3: FOREGROUND (TEXT) COLORS - STANDARD
# ============================================================================

# Standard Foreground Colors (30-37)
FG_BLACK = '\033[30m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'
FG_YELLOW = '\033[33m'
FG_BLUE = '\033[34m'
FG_MAGENTA = '\033[35m'
FG_CYAN = '\033[36m'
FG_WHITE = '\033[37m'
FG_DEFAULT = '\033[39m'

# Bright/Intense Foreground Colors (90-97)
FG_BRIGHT_BLACK = '\033[90m'
FG_BRIGHT_RED = '\033[91m'
FG_BRIGHT_GREEN = '\033[92m'
FG_BRIGHT_YELLOW = '\033[93m'
FG_BRIGHT_BLUE = '\033[94m'
FG_BRIGHT_MAGENTA = '\033[95m'
FG_BRIGHT_CYAN = '\033[96m'
FG_BRIGHT_WHITE = '\033[97m'

# ============================================================================
# SECTION 4: BACKGROUND COLORS - STANDARD
# ============================================================================

# Standard Background Colors (40-47)
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'
BG_DEFAULT = '\033[49m'

# Bright/Intense Background Colors (100-107)
BG_BRIGHT_BLACK = '\033[100m'
BG_BRIGHT_RED = '\033[101m'
BG_BRIGHT_GREEN = '\033[102m'
BG_BRIGHT_YELLOW = '\033[103m'
BG_BRIGHT_BLUE = '\033[104m'
BG_BRIGHT_MAGENTA = '\033[105m'
BG_BRIGHT_CYAN = '\033[106m'
BG_BRIGHT_WHITE = '\033[107m'

# ============================================================================
# SECTION 5: 256-COLOR PALETTE
# ============================================================================

def fg_256(color_code):
    """Set foreground color using 256-color palette (0-255)"""
    return f'\033[38;5;{color_code}m'

def bg_256(color_code):
    """Set background color using 256-color palette (0-255)"""
    return f'\033[48;5;{color_code}m'

# Common 256-color codes
FG_ORANGE = fg_256(214)
FG_PINK = fg_256(213)
FG_PURPLE = fg_256(135)
FG_GRAY = fg_256(244)
FG_DARK_GRAY = fg_256(236)

# ============================================================================
# SECTION 6: TRUE COLOR (24-bit RGB)
# ============================================================================

def fg_rgb(r, g, b):
    """Set foreground color using RGB values (0-255)"""
    return f'\033[38;2;{r};{g};{b}m'

def bg_rgb(r, g, b):
    """Set background color using RGB values (0-255)"""
    return f'\033[48;2;{r};{g};{b}m'

# Pre-defined RGB colors
FG_RGB_GOLD = fg_rgb(255, 215, 0)
FG_RGB_SILVER = fg_rgb(192, 192, 192)
FG_RGB_BRONZE = fg_rgb(205, 127, 50)

# ============================================================================
# SECTION 7: CURSOR CONTROL
# ============================================================================

# Cursor Movement
CURSOR_UP = lambda n=1: f'\033[{n}A'
CURSOR_DOWN = lambda n=1: f'\033[{n}B'
CURSOR_FORWARD = lambda n=1: f'\033[{n}C'
CURSOR_BACK = lambda n=1: f'\033[{n}D'

# Cursor Next/Previous Line
CURSOR_NEXT_LINE = lambda n=1: f'\033[{n}E'
CURSOR_PREV_LINE = lambda n=1: f'\033[{n}F'

# Cursor Horizontal Position
CURSOR_COLUMN = lambda n=1: f'\033[{n}G'

# Cursor Absolute Position
CURSOR_POS = lambda row=1, col=1: f'\033[{row};{col}H'
CURSOR_HOME = '\033[H'

# Save and Restore Cursor Position
CURSOR_SAVE = '\033[s'
CURSOR_RESTORE = '\033[u'
CURSOR_SAVE_ALT = '\0337'  # Alternative save
CURSOR_RESTORE_ALT = '\0338'  # Alternative restore

# Cursor Visibility
CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'

# ============================================================================
# SECTION 8: SCREEN/DISPLAY CONTROL
# ============================================================================

# Clear Screen
CLEAR_SCREEN = '\033[2J'
CLEAR_SCREEN_AFTER = '\033[0J'  # Clear from cursor to end
CLEAR_SCREEN_BEFORE = '\033[1J'  # Clear from cursor to beginning

# Clear Line
CLEAR_LINE = '\033[2K'
CLEAR_LINE_AFTER = '\033[0K'  # Clear from cursor to end of line
CLEAR_LINE_BEFORE = '\033[1K'  # Clear from cursor to start of line

# Scroll
SCROLL_UP = lambda n=1: f'\033[{n}S'
SCROLL_DOWN = lambda n=1: f'\033[{n}T'

# ============================================================================
# SECTION 9: INPUT CONTROL SEQUENCES
# ============================================================================

# Special Input Keys (for detection in raw mode)
KEY_UP = '\033[A'
KEY_DOWN = '\033[B'
KEY_RIGHT = '\033[C'
KEY_LEFT = '\033[D'

KEY_HOME = '\033[H'
KEY_END = '\033[F'
KEY_INSERT = '\033[2~'
KEY_DELETE = '\033[3~'
KEY_PAGE_UP = '\033[5~'
KEY_PAGE_DOWN = '\033[6~'

# Function Keys
KEY_F1 = '\033OP'
KEY_F2 = '\033OQ'
KEY_F3 = '\033OR'
KEY_F4 = '\033OS'
KEY_F5 = '\033[15~'
KEY_F6 = '\033[17~'
KEY_F7 = '\033[18~'
KEY_F8 = '\033[19~'
KEY_F9 = '\033[20~'
KEY_F10 = '\033[21~'
KEY_F11 = '\033[23~'
KEY_F12 = '\033[24~'

# Control Characters
CTRL_C = '\x03'
CTRL_D = '\x04'
CTRL_Z = '\x1a'
BACKSPACE = '\x08'
TAB = '\t'
ENTER = '\r'
NEWLINE = '\n'
ESC_KEY = '\x1b'

# ============================================================================
# SECTION 10: TERMINAL MODE CONTROL
# ============================================================================

# Alternate Screen Buffer
ALT_SCREEN_ENABLE = '\033[?1049h'
ALT_SCREEN_DISABLE = '\033[?1049l'

# Mouse Tracking
MOUSE_ENABLE = '\033[?1000h'
MOUSE_DISABLE = '\033[?1000l'
MOUSE_ENABLE_FULL = '\033[?1003h'
MOUSE_DISABLE_FULL = '\033[?1003l'

# Bracketed Paste Mode
BRACKETED_PASTE_ON = '\033[?2004h'
BRACKETED_PASTE_OFF = '\033[?2004l'

# ============================================================================
# SECTION 11: HELPER FUNCTIONS
# ============================================================================

def enable_ansi_windows():
    """Enable ANSI escape sequences on Windows 10+"""
    if sys.platform == 'win32':
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def clear_screen():
    """Cross-platform screen clear"""
    os.system('cls' if os.name == 'nt' else 'clear')

def move_cursor(row, col):
    """Move cursor to specific position"""
    print(f'\033[{row};{col}H', end='')

def hide_cursor():
    """Hide the cursor"""
    print('\033[?25l', end='')

def show_cursor():
    """Show the cursor"""
    print('\033[?25h', end='')

def colored_text(text, fg=None, bg=None, style=None):
    """
    Create colored text with optional styling
    
    Args:
        text: Text to color
        fg: Foreground color code (e.g., FG_RED)
        bg: Background color code (e.g., BG_BLUE)
        style: Style code (e.g., BOLD)
    """
    result = ''
    if style:
        result += style
    if fg:
        result += fg
    if bg:
        result += bg
    result += text + RESET
    return result

# ============================================================================
# SECTION 12: PROGRESS INDICATORS
# ============================================================================

def progress_bar(current, total, width=50, char='█'):
    """
    Create a progress bar
    
    Args:
        current: Current progress value
        total: Total/max value
        width: Width of the bar in characters
        char: Character to use for filled portion
    """
    filled = int(width * current / total)
    bar = char * filled + '-' * (width - filled)
    percent = int(100 * current / total)
    return f'[{bar}] {percent}%'

def spinner_frames():
    """Return list of spinner animation frames"""
    return ['|', '/', '-', '\\']

def loading_dots():
    """Return list of loading dot frames"""
    return ['   ', '.  ', '.. ', '...']

def progress_spinner():
    """Return list of circle spinner frames"""
    return ['◐', '◓', '◑', '◒']

def braille_spinner():
    """Return list of braille spinner frames"""
    return ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']

# ============================================================================
# SECTION 13: BOX DRAWING CHARACTERS
# ============================================================================

# Single Line Box Drawing
BOX_SINGLE_H = '─'  # Horizontal
BOX_SINGLE_V = '│'  # Vertical
BOX_SINGLE_TL = '┌'  # Top-left
BOX_SINGLE_TR = '┐'  # Top-right
BOX_SINGLE_BL = '└'  # Bottom-left
BOX_SINGLE_BR = '┘'  # Bottom-right
BOX_SINGLE_T = '┬'   # T junction down
BOX_SINGLE_B = '┴'   # T junction up
BOX_SINGLE_L = '├'   # T junction right
BOX_SINGLE_R = '┤'   # T junction left
BOX_SINGLE_CROSS = '┼'  # Cross

# Double Line Box Drawing
BOX_DOUBLE_H = '═'
BOX_DOUBLE_V = '║'
BOX_DOUBLE_TL = '╔'
BOX_DOUBLE_TR = '╗'
BOX_DOUBLE_BL = '╚'
BOX_DOUBLE_BR = '╝'
BOX_DOUBLE_T = '╦'
BOX_DOUBLE_B = '╩'
BOX_DOUBLE_L = '╠'
BOX_DOUBLE_R = '╣'
BOX_DOUBLE_CROSS = '╬'

# Heavy/Bold Line Box Drawing
BOX_HEAVY_H = '━'
BOX_HEAVY_V = '┃'
BOX_HEAVY_TL = '┏'
BOX_HEAVY_TR = '┓'
BOX_HEAVY_BL = '┗'
BOX_HEAVY_BR = '┛'

# ============================================================================
# SECTION 14: BLOCK ELEMENTS
# ============================================================================

BLOCK_FULL = '█'
BLOCK_DARK = '▓'
BLOCK_MEDIUM = '▒'
BLOCK_LIGHT = '░'

BLOCK_UPPER_HALF = '▀'
BLOCK_LOWER_HALF = '▄'
BLOCK_LEFT_HALF = '▌'
BLOCK_RIGHT_HALF = '▐'

BLOCK_QUARTER_TL = '▘'
BLOCK_QUARTER_TR = '▝'
BLOCK_QUARTER_BL = '▖'
BLOCK_QUARTER_BR = '▗'

# ============================================================================
# SECTION 15: GEOMETRIC SHAPES
# ============================================================================

SHAPE_CIRCLE = '●'
SHAPE_CIRCLE_EMPTY = '○'
SHAPE_SQUARE = '■'
SHAPE_SQUARE_EMPTY = '□'
SHAPE_TRIANGLE_UP = '▲'
SHAPE_TRIANGLE_DOWN = '▼'
SHAPE_TRIANGLE_LEFT = '◀'
SHAPE_TRIANGLE_RIGHT = '▶'
SHAPE_DIAMOND = '◆'
SHAPE_DIAMOND_EMPTY = '◇'

# ============================================================================
# SECTION 16: ARROWS & POINTERS
# ============================================================================

ARROW_UP = '↑'
ARROW_DOWN = '↓'
ARROW_LEFT = '←'
ARROW_RIGHT = '→'
ARROW_UP_DOWN = '↕'
ARROW_LEFT_RIGHT = '↔'

ARROW_DOUBLE_UP = '⇑'
ARROW_DOUBLE_DOWN = '⇓'
ARROW_DOUBLE_LEFT = '⇐'
ARROW_DOUBLE_RIGHT = '⇒'

POINTER_RIGHT = '▶'
POINTER_RIGHT_HOLLOW = '▷'

# ============================================================================
# SECTION 17: SPECIAL SYMBOLS
# ============================================================================

CHECK_MARK = '✓'
CHECK_MARK_HEAVY = '✔'
CROSS_MARK = '✗'
CROSS_MARK_HEAVY = '✘'
BALLOT_X = '☒'
BALLOT_CHECK = '☑'
BALLOT_EMPTY = '☐'

STAR_FILLED = '★'
STAR_EMPTY = '☆'
HEART = '♥'
HEART_EMPTY = '♡'
SPADE = '♠'
CLUB = '♣'
DIAMOND_CARD = '♦'

WARNING = '⚠'
INFO = 'ℹ'
QUESTION = '?'
EXCLAMATION = '!'

# ============================================================================
# SECTION 18: FRACTION & MATH SYMBOLS
# ============================================================================

FRACTION_HALF = '½'
FRACTION_THIRD = '⅓'
FRACTION_QUARTER = '¼'
FRACTION_THREE_QUARTERS = '¾'

PLUS_MINUS = '±'
MULTIPLY = '×'
DIVIDE = '÷'
DEGREE = '°'
INFINITY = '∞'

# ============================================================================
# SECTION 19: CURRENCY & SPECIAL CHARS
# ============================================================================

CURRENCY_DOLLAR = '$'
CURRENCY_EURO = '€'
CURRENCY_POUND = '£'
CURRENCY_YEN = '¥'
CURRENCY_CENT = '¢'

COPYRIGHT = '©'
REGISTERED = '®'
TRADEMARK = '™'
SECTION_SIGN = '§'
PARAGRAPH = '¶'

# ============================================================================
# SECTION 20: DEMONSTRATION FUNCTIONS
# ============================================================================

def demo_colors():
    """Demonstrate all standard colors"""
    print(f"\n{BOLD}STANDARD FOREGROUND COLORS:{RESET}")
    colors = [
        (FG_BLACK, "Black"),
        (FG_RED, "Red"),
        (FG_GREEN, "Green"),
        (FG_YELLOW, "Yellow"),
        (FG_BLUE, "Blue"),
        (FG_MAGENTA, "Magenta"),
        (FG_CYAN, "Cyan"),
        (FG_WHITE, "White"),
    ]
    for color, name in colors:
        print(f"{color}  {name:10}{RESET}", end='  ')
        print(f"{color}{BG_WHITE}  {name:10}{RESET}")
    
    print(f"\n{BOLD}BRIGHT FOREGROUND COLORS:{RESET}")
    bright_colors = [
        (FG_BRIGHT_BLACK, "Bright Black"),
        (FG_BRIGHT_RED, "Bright Red"),
        (FG_BRIGHT_GREEN, "Bright Green"),
        (FG_BRIGHT_YELLOW, "Bright Yellow"),
        (FG_BRIGHT_BLUE, "Bright Blue"),
        (FG_BRIGHT_MAGENTA, "Bright Magenta"),
        (FG_BRIGHT_CYAN, "Bright Cyan"),
        (FG_BRIGHT_WHITE, "Bright White"),
    ]
    for color, name in bright_colors:
        print(f"{color}  {name:15}{RESET}")

def demo_styles():
    """Demonstrate text styles"""
    print(f"\n{BOLD}TEXT STYLES:{RESET}")
    print(f"{BOLD}Bold text{RESET}")
    print(f"{DIM}Dim text{RESET}")
    print(f"{ITALIC}Italic text{RESET}")
    print(f"{UNDERLINE}Underlined text{RESET}")
    print(f"{REVERSE}Reversed text{RESET}")
    print(f"{STRIKETHROUGH}Strikethrough text{RESET}")
    print(f"{BOLD}{UNDERLINE}Bold + Underline{RESET}")
    print(f"{FG_RED}{BG_YELLOW}{BOLD}Red on Yellow Bold{RESET}")

def demo_box_drawing():
    """Demonstrate box drawing characters"""
    print(f"\n{BOLD}BOX DRAWING CHARACTERS:{RESET}\n")
    
    # Single line box
    print("Single Line Box:")
    print(f"{BOX_SINGLE_TL}{BOX_SINGLE_H * 20}{BOX_SINGLE_TR}")
    print(f"{BOX_SINGLE_V}{' ' * 20}{BOX_SINGLE_V}")
    print(f"{BOX_SINGLE_L}{BOX_SINGLE_H * 20}{BOX_SINGLE_R}")
    print(f"{BOX_SINGLE_V}{' ' * 20}{BOX_SINGLE_V}")
    print(f"{BOX_SINGLE_BL}{BOX_SINGLE_H * 20}{BOX_SINGLE_BR}\n")
    
    # Double line box
    print("Double Line Box:")
    print(f"{BOX_DOUBLE_TL}{BOX_DOUBLE_H * 20}{BOX_DOUBLE_TR}")
    print(f"{BOX_DOUBLE_V}{' ' * 20}{BOX_DOUBLE_V}")
    print(f"{BOX_DOUBLE_V}{' ' * 20}{BOX_DOUBLE_V}")
    print(f"{BOX_DOUBLE_BL}{BOX_DOUBLE_H * 20}{BOX_DOUBLE_BR}\n")

def demo_progress():
    """Demonstrate progress indicators"""
    print(f"\n{BOLD}PROGRESS INDICATORS:{RESET}\n")
    
    # Progress bar
    print("Progress Bar:")
    for i in range(0, 101, 20):
        print(f"\r{progress_bar(i, 100)}", end='', flush=True)
        time.sleep(0.3)
    print("\n")
    
    # Spinner
    print("Spinner Animation:")
    frames = spinner_frames()
    for _ in range(12):
        for frame in frames:
            print(f"\r  Loading {frame}", end='', flush=True)
            time.sleep(0.1)
    print(f"\r  Loading {CHECK_MARK} Done!\n")
    
    # Braille spinner
    print("Braille Spinner:")
    frames = braille_spinner()
    for _ in range(3):
        for frame in frames:
            print(f"\r  {frame} Processing...", end='', flush=True)
            time.sleep(0.08)
    print(f"\r  {CHECK_MARK} Complete!\n")

def demo_symbols():
    """Demonstrate special symbols"""
    print(f"\n{BOLD}SPECIAL SYMBOLS:{RESET}\n")
    print(f"  {CHECK_MARK} Task completed")
    print(f"  {CROSS_MARK} Task failed")
    print(f"  {WARNING} Warning message")
    print(f"  {INFO} Information")
    print(f"  {STAR_FILLED} Favorite")
    print(f"  {HEART} Like")
    print(f"  {ARROW_RIGHT} Next step")
    print(f"  {POINTER_RIGHT} Selected item")
    
def demo_blocks():
    """Demonstrate block elements"""
    print(f"\n{BOLD}BLOCK ELEMENTS:{RESET}\n")
    print(f"Full blocks: {BLOCK_FULL * 10}")
    print(f"Dark shade:  {BLOCK_DARK * 10}")
    print(f"Medium shade:{BLOCK_MEDIUM * 10}")
    print(f"Light shade: {BLOCK_LIGHT * 10}")
    print(f"Upper half:  {BLOCK_UPPER_HALF * 10}")
    print(f"Lower half:  {BLOCK_LOWER_HALF * 10}")

def demo_256_colors():
    """Demonstrate 256-color palette"""
    print(f"\n{BOLD}256-COLOR PALETTE SAMPLE:{RESET}\n")
    
    # Show a sample of 256 colors
    print("Standard colors (0-15):")
    for i in range(16):
        print(f"{bg_256(i)}  {RESET}", end='')
        if (i + 1) % 8 == 0:
            print()
    
    print("\nGrayscale (232-255):")
    for i in range(232, 256):
        print(f"{bg_256(i)}  {RESET}", end='')
    print()

def demo_rgb_colors():
    """Demonstrate RGB (true color) support"""
    print(f"\n{BOLD}RGB TRUE COLOR GRADIENT:{RESET}\n")
    
    # Red to green gradient
    for i in range(0, 256, 8):
        r = 255 - i
        g = i
        b = 0
        print(f"{bg_rgb(r, g, b)}  {RESET}", end='')
    print()
    
    # Rainbow effect
    for i in range(0, 100, 2):
        r = int(255 * abs((i % 50) / 50 - 0.5) * 2)
        g = int(255 * (1 - abs((i % 50) / 50 - 0.5) * 2))
        b = int(128 + 127 * ((i % 25) / 25))
        print(f"{bg_rgb(r, g, b)} {RESET}", end='')
    print("\n")

# ============================================================================
# SECTION 21: MAIN DEMO FUNCTION
# ============================================================================

def run_all_demos():
    """Run all demonstration functions"""
    enable_ansi_windows()  # Enable ANSI on Windows
    
    print(f"\n{BOLD}{FG_CYAN}{'=' * 60}{RESET}")
    print(f"{BOLD}{FG_CYAN}  CLI ESCAPE SEQUENCES & STYLING - COMPLETE DEMONSTRATION{RESET}")
    print(f"{BOLD}{FG_CYAN}{'=' * 60}{RESET}\n")
    
    demo_colors()
    demo_styles()
    demo_box_drawing()
    demo_progress()
    demo_symbols()
    demo_blocks()
    demo_256_colors()
    demo_rgb_colors()
    
    print(f"\n{BOLD}{FG_GREEN}All demonstrations complete!{RESET}\n")

# ============================================================================
# SECTION 22: UTILITY CLASSES
# ============================================================================

class Style:
    """Convenient style combination class"""
    @staticmethod
    def error(text):
        return f"{FG_RED}{BOLD}{text}{RESET}"
    
    @staticmethod
    def success(text):
        return f"{FG_GREEN}{BOLD}{text}{RESET}"
    
    @staticmethod
    def warning(text):
        return f"{FG_YELLOW}{BOLD}{text}{RESET}"
    
    @staticmethod
    def info(text):
        return f"{FG_CYAN}{text}{RESET}"
    
    @staticmethod
    def highlight(text):
        return f"{BG_YELLOW}{FG_BLACK}{BOLD}{text}{RESET}"
    
    @staticmethod
    def header(text):
        return f"{FG_BRIGHT_CYAN}{BOLD}{UNDERLINE}{text}{RESET}"

# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Uncomment to run demonstrations
    run_all_demos()
    
    # Example usage
    print(f"\n{BOLD}QUICK USAGE EXAMPLES:{RESET}\n")
    print(Style.success(f"{CHECK_MARK} Operation completed successfully"))
    print(Style.error(f"{CROSS_MARK} Error: File not found"))
    print(Style.warning(f"{WARNING} Warning: Low disk space"))
    print(Style.info(f"{INFO} Tip: Use Ctrl+C to exit"))
    print(Style.highlight("  HIGHLIGHTED TEXT  "))
    print(Style.header("Section Header"))
    
    print(f"\n{FG_BRIGHT_YELLOW}Documentation: See inline comments for all constants and functions{RESET}\n")
