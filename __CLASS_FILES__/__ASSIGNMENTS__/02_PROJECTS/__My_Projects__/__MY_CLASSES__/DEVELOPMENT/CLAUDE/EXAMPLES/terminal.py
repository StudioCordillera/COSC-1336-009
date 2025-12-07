"""
terminal.py - Import and use like the standard library

Usage:
    from terminal import move, clear, hide_cursor, show_cursor
    
    move(5, 10)
    print("Hello")
    clear()
"""

import sys
import os

# Enable ANSI on Windows
if sys.platform == 'win32':
    os.system('')

# ============================================================================
# TERMINAL INFO - Must be defined first for percentage conversions
# ============================================================================

def get_size():
    """Get terminal size as (width, height) tuple"""
    import shutil
    return shutil.get_terminal_size()

def get_width():
    """Get terminal width in characters"""
    return get_size()[0]

def get_height():
    """Get terminal height in lines"""
    return get_size()[1]

# ============================================================================
# CURSOR MOVEMENT - Like built-in functions
# ============================================================================

def move(row, col):
    """Move cursor to absolute position
    
    Args:
        row: Row number (1-based) OR percentage (0.0-1.0)
        col: Column number (1-based) OR percentage (0.0-1.0)
    
    Examples:
        move(5, 10)      # Absolute: row 5, col 10
        move(0.5, 0.5)   # Relative: center of screen
        move(0.25, 10)   # Mixed: 25% down, col 10
    """
    # Convert percentages to absolute positions
    if isinstance(row, float) and 0 <= row <= 1:
        row = int(row * get_height())
    if isinstance(col, float) and 0 <= col <= 1:
        col = int(col * get_width())
    
    # Clamp to valid range
    row = max(1, min(row, get_height()))
    col = max(1, min(col, get_width()))
    
    print(f'\033[{row};{col}H', end='')
    sys.stdout.flush()

def home():
    """Move cursor to top-left (1,1)"""
    print('\033[H', end='')
    sys.stdout.flush()

def up(n=1):
    """Move cursor up n lines"""
    print(f'\033[{n}A', end='')
    sys.stdout.flush()

def down(n=1):
    """Move cursor down n lines"""
    print(f'\033[{n}B', end='')
    sys.stdout.flush()

def right(n=1):
    """Move cursor right n columns"""
    print(f'\033[{n}C', end='')
    sys.stdout.flush()

def left(n=1):
    """Move cursor left n columns"""
    print(f'\033[{n}D', end='')
    sys.stdout.flush()

def column(n):
    """Move cursor to column n (same row)"""
    print(f'\033[{n}G', end='')
    sys.stdout.flush()

# ============================================================================
# CLEARING - Like built-in functions
# ============================================================================

def clear():
    """Clear entire screen"""
    print('\033[2J', end='')
    sys.stdout.flush()

def clear_screen():
    """Clear entire screen (alias)"""
    clear()

def clear_line():
    """Clear entire line"""
    print('\033[2K', end='')
    sys.stdout.flush()

def clear_to_end():
    """Clear from cursor to end of line"""
    print('\033[0K', end='')
    sys.stdout.flush()

def clear_to_start():
    """Clear from cursor to start of line"""
    print('\033[1K', end='')
    sys.stdout.flush()

def clear_below():
    """Clear from cursor to end of screen"""
    print('\033[0J', end='')
    sys.stdout.flush()

def clear_above():
    """Clear from cursor to start of screen"""
    print('\033[1J', end='')
    sys.stdout.flush()

# ============================================================================
# CURSOR VISIBILITY - Like built-in functions
# ============================================================================

def hide_cursor():
    """Hide blinking cursor"""
    print('\033[?25l', end='')
    sys.stdout.flush()

def show_cursor():
    """Show blinking cursor"""
    print('\033[?25h', end='')
    sys.stdout.flush()

# ============================================================================
# CONVENIENCE FUNCTIONS - Like built-in functions
# ============================================================================

def write(row, col, text):
    """Write text at position
    
    Args:
        row: Row number (1-based) OR percentage (0.0-1.0)
        col: Column number (1-based) OR percentage (0.0-1.0)
        text: Text to write
    """
    move(row, col)
    print(text, end='')
    sys.stdout.flush()

def write_line(row, text):
    """Write text at start of row
    
    Args:
        row: Row number (1-based) OR percentage (0.0-1.0)
        text: Text to write
    """
    move(row, 1)
    clear_line()
    print(text, end='')
    sys.stdout.flush()

def flush():
    """Force output to screen"""
    sys.stdout.flush()

# ============================================================================
# BOX DRAWING - Pre-defined character sets
# ============================================================================

class Box:
    """Box drawing characters as constants"""
    # Single line
    SINGLE_TL = '┌'  # Top-left
    SINGLE_TR = '┐'  # Top-right
    SINGLE_BL = '└'  # Bottom-left
    SINGLE_BR = '┘'  # Bottom-right
    SINGLE_H = '─'   # Horizontal
    SINGLE_V = '│'   # Vertical
    SINGLE_CROSS = '┼'
    SINGLE_T_DOWN = '┬'
    SINGLE_T_UP = '┴'
    SINGLE_T_RIGHT = '├'
    SINGLE_T_LEFT = '┤'
    
    # Double line
    DOUBLE_TL = '╔'
    DOUBLE_TR = '╗'
    DOUBLE_BL = '╚'
    DOUBLE_BR = '╝'
    DOUBLE_H = '═'
    DOUBLE_V = '║'
    DOUBLE_CROSS = '╬'
    DOUBLE_T_DOWN = '╦'
    DOUBLE_T_UP = '╩'
    DOUBLE_T_RIGHT = '╠'
    DOUBLE_T_LEFT = '╣'
    
    # Rounded
    ROUND_TL = '╭'
    ROUND_TR = '╮'
    ROUND_BL = '╰'
    ROUND_BR = '╯'
    
    # Blocks
    FULL = '█'
    DARK = '▓'
    MEDIUM = '▒'
    LIGHT = '░'
    TOP_HALF = '▀'
    BOTTOM_HALF = '▄'
    LEFT_HALF = '▌'
    RIGHT_HALF = '▐'

class Symbol:
    """Common UI symbols as constants"""
    CHECK = '✓'
    X = '✗'
    CROSS = '✕'
    HEAVY_X = '✖'
    BULLET = '•'
    CIRCLE = '○'
    FILLED_CIRCLE = '●'
    SQUARE = '□'
    FILLED_SQUARE = '■'
    DIAMOND = '◇'
    FILLED_DIAMOND = '◆'
    ARROW_RIGHT = '→'
    ARROW_LEFT = '←'
    ARROW_UP = '↑'
    ARROW_DOWN = '↓'
    DOUBLE_ARROW_RIGHT = '⇒'
    DOUBLE_ARROW_LEFT = '⇐'
    WARNING = '⚠'
    INFO = 'ℹ'
    MAIL = '✉'
    MENU = '☰'

# ============================================================================
# HIGHER-LEVEL FUNCTIONS
# ============================================================================

def draw_box(row, col, width, height, style='single'):
    """Draw a box at position with given dimensions
    
    Args:
        row: Top-left row (1-based) OR percentage (0.0-1.0)
        col: Top-left column (1-based) OR percentage (0.0-1.0)
        width: Internal width (characters) OR percentage (0.0-1.0)
        height: Internal height (lines) OR percentage (0.0-1.0)
        style: 'single', 'double', or 'round'
    
    Examples:
        draw_box(5, 10, 40, 10)           # Absolute positioning
        draw_box(0.1, 0.1, 0.8, 0.8)      # 10% from edges, 80% size
        draw_box(0.5, 20, 0.3, 5)         # Mixed units
    """
    # Convert percentages to absolute values
    if isinstance(row, float) and 0 <= row <= 1:
        row = int(row * get_height())
    if isinstance(col, float) and 0 <= col <= 1:
        col = int(col * get_width())
    if isinstance(width, float) and 0 <= width <= 1:
        width = int(width * get_width())
    if isinstance(height, float) and 0 <= height <= 1:
        height = int(height * get_height())
    
    if style == 'double':
        tl, tr, bl, br = Box.DOUBLE_TL, Box.DOUBLE_TR, Box.DOUBLE_BL, Box.DOUBLE_BR
        h, v = Box.DOUBLE_H, Box.DOUBLE_V
    elif style == 'round':
        tl, tr, bl, br = Box.ROUND_TL, Box.ROUND_TR, Box.ROUND_BL, Box.ROUND_BR
        h, v = Box.SINGLE_H, Box.SINGLE_V
    else:  # single
        tl, tr, bl, br = Box.SINGLE_TL, Box.SINGLE_TR, Box.SINGLE_BL, Box.SINGLE_BR
        h, v = Box.SINGLE_H, Box.SINGLE_V
    
    # Top
    write(row, col, tl + h * width + tr)
    
    # Sides
    for i in range(1, height + 1):
        write(row + i, col, v)
        write(row + i, col + width + 1, v)
    
    # Bottom
    write(row + height + 1, col, bl + h * width + br)

def draw_hline(row, col, length, style='single'):
    """Draw horizontal line
    
    Args:
        row: Row number (1-based) OR percentage (0.0-1.0)
        col: Start column (1-based) OR percentage (0.0-1.0)
        length: Length in characters OR percentage (0.0-1.0)
        style: 'single' or 'double'
    """
    # Convert percentages
    if isinstance(length, float) and 0 <= length <= 1:
        length = int(length * get_width())
    
    char = Box.DOUBLE_H if style == 'double' else Box.SINGLE_H
    write(row, col, char * length)

def draw_vline(row, col, length, style='single'):
    """Draw vertical line
    
    Args:
        row: Start row (1-based) OR percentage (0.0-1.0)
        col: Column number (1-based) OR percentage (0.0-1.0)
        length: Length in lines OR percentage (0.0-1.0)
        style: 'single' or 'double'
    """
    # Convert percentages
    if isinstance(length, float) and 0 <= length <= 1:
        length = int(length * get_height())
    
    char = Box.DOUBLE_V if style == 'double' else Box.SINGLE_V
    for i in range(length):
        write(row + i, col, char)

def center_text(row, text, width=None):
    """Write centered text on row
    
    Args:
        row: Row number (1-based) OR percentage (0.0-1.0)
        text: Text to center
        width: Total width (default: terminal width) OR percentage (0.0-1.0)
    """
    if width is None:
        width = get_width()
    elif isinstance(width, float) and 0 <= width <= 1:
        width = int(width * get_width())
    
    padding = (width - len(text)) // 2
    write(row, max(1, padding), text)

# ============================================================================
# PERCENTAGE-BASED LAYOUT HELPERS
# ============================================================================

def pct(value, of_width=True):
    """Convert percentage to absolute value
    
    Args:
        value: Percentage as 0.0-1.0 OR integer (returned as-is)
        of_width: True for width-based, False for height-based
    
    Returns:
        Absolute position/size as integer
    
    Examples:
        col = pct(0.5)              # 50% of width
        row = pct(0.25, False)       # 25% of height
        size = pct(40)               # 40 (unchanged)
    """
    if isinstance(value, float) and 0 <= value <= 1:
        return int(value * (get_width() if of_width else get_height()))
    return value

def layout(row=None, col=None, width=None, height=None):
    """Convert percentage-based layout to absolute coordinates
    
    Args:
        row: Row (int) OR percentage (float 0.0-1.0) OR None
        col: Column (int) OR percentage (float 0.0-1.0) OR None
        width: Width (int) OR percentage (float 0.0-1.0) OR None
        height: Height (int) OR percentage (float 0.0-1.0) OR None
    
    Returns:
        Dictionary with absolute values: {'row': int, 'col': int, 'width': int, 'height': int}
    
    Examples:
        # Center box, 50% width, 30% height
        pos = layout(row=0.35, col=0.25, width=0.5, height=0.3)
        draw_box(**pos)
        
        # Top bar across full width
        pos = layout(row=1, col=1, width=1.0, height=3)
        draw_box(**pos)
    """
    result = {}
    
    if row is not None:
        result['row'] = pct(row, False) if isinstance(row, float) else row
    
    if col is not None:
        result['col'] = pct(col, True) if isinstance(col, float) else col
    
    if width is not None:
        result['width'] = pct(width, True) if isinstance(width, float) else width
    
    if height is not None:
        result['height'] = pct(height, False) if isinstance(height, float) else height
    
    return result

class Grid:
    """Helper for grid-based layouts
    
    Examples:
        grid = Grid(rows=3, cols=2)
        
        # Get position of cell (0, 0) - top-left
        row, col = grid.cell(0, 0)
        
        # Get dimensions of each cell
        w, h = grid.cell_size()
    """
    def __init__(self, rows, cols, padding=1):
        self.rows = rows
        self.cols = cols
        self.padding = padding
        
        self.term_width = get_width()
        self.term_height = get_height()
        
        self.cell_width = (self.term_width - (cols + 1) * padding) // cols
        self.cell_height = (self.term_height - (rows + 1) * padding) // rows
    
    def cell(self, row, col):
        """Get top-left position of cell at (row, col)"""
        y = self.padding + row * (self.cell_height + self.padding)
        x = self.padding + col * (self.cell_width + self.padding)
        return (y, x)
    
    def cell_size(self):
        """Get (width, height) of each cell"""
        return (self.cell_width, self.cell_height)
    
    def cell_box(self, row, col):
        """Get full box parameters for cell: (row, col, width, height)"""
        y, x = self.cell(row, col)
        return (y, x, self.cell_width, self.cell_height)

# ============================================================================
# CONTEXT MANAGERS - Pythonic usage
# ============================================================================

class hidden_cursor:
    """Context manager to temporarily hide cursor
    
    Usage:
        with hidden_cursor():
            # cursor hidden here
            pass
        # cursor shown again
    """
    def __enter__(self):
        hide_cursor()
        return self
    
    def __exit__(self, *args):
        show_cursor()

class alternate_screen:
    """Context manager for alternate screen buffer
    
    Usage:
        with alternate_screen():
            # full screen app here
            pass
        # returns to normal screen
    """
    def __enter__(self):
        print('\033[?1049h', end='')
        sys.stdout.flush()
        return self
    
    def __exit__(self, *args):
        print('\033[?1049l', end='')
        sys.stdout.flush()

class raw_mode:
    """Context manager for raw terminal input (Unix only)
    
    Usage:
        with raw_mode():
            key = sys.stdin.read(1)
    """
    def __enter__(self):
        if sys.platform != 'win32':
            import tty
            import termios
            self.fd = sys.stdin.fileno()
            self.old_settings = termios.tcgetattr(self.fd)
            tty.setraw(self.fd)
        return self
    
    def __exit__(self, *args):
        if sys.platform != 'win32':
            import termios
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

# ============================================================================
# DEMO
# ============================================================================

def demo():
    """Demonstrate terminal library usage with percentage-based layout"""
    
    clear()
    hide_cursor()
    
    # Title - centered
    center_text(0.05, "TERMINAL LIBRARY - PERCENTAGE LAYOUT DEMO")
    draw_hline(0.08, 0.0, 1.0)
    
    # Main content box - 80% width, 60% height, centered
    draw_box(0.15, 0.1, 0.8, 0.6, 'double')
    
    # Left column - box drawing examples
    write(0.2, 0.15, "Box drawing:")
    draw_box(0.25, 0.15, 0.25, 0.15, 'single')
    write(0.27, 0.18, "Single line")
    
    draw_box(0.25, 0.45, 0.25, 0.15, 'round')
    write(0.27, 0.48, "Rounded")
    
    # Right column - symbols
    write(0.45, 0.15, f"Symbols: {Symbol.CHECK} {Symbol.X} {Symbol.BULLET} {Symbol.ARROW_RIGHT}")
    write(0.5, 0.15, f"Blocks:  {Box.FULL}{Box.DARK}{Box.MEDIUM}{Box.LIGHT}")
    
    # Grid example
    write(0.55, 0.15, "Grid layout (3x2):")
    grid = Grid(rows=3, cols=2)
    for r in range(2):
        for c in range(2):
            row, col = grid.cell(r, c)
            w, h = grid.cell_size()
            if row > 0.8 * get_height():  # Skip if too low
                break
            draw_box(row, col, min(w, 20), min(h, 3), 'single')
    
    # Footer - centered at bottom
    write(0.9, 0.0, "")  # Position for centering
    center_text(0.92, "Press Enter to exit...")
    
    move(0.95, 1)
    show_cursor()
    input()
    
    clear()

# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == '__main__':
    """
    Example of how clean the API is with percentage-based layout:
    
    from terminal import move, write, clear, Box, Symbol
    from terminal import draw_box, center_text, hidden_cursor, layout, Grid
    
    with hidden_cursor():
        clear()
        
        # Percentage-based layout - responsive to terminal size!
        draw_box(0.1, 0.1, 0.8, 0.6, 'double')  # 80% width, 60% height, centered
        
        center_text(0.15, "My Application")
        
        write(0.3, 0.15, f"{Symbol.CHECK} Task complete")
        write(0.35, 0.15, f"{Symbol.ARROW_RIGHT} Next step")
        
        # Or use layout() helper for explicit conversions
        pos = layout(row=0.5, col=0.2, width=0.6, height=0.3)
        draw_box(**pos, style='round')
        
        # Grid for structured layouts
        grid = Grid(rows=2, cols=3)
        for r in range(2):
            for c in range(3):
                draw_box(*grid.cell_box(r, c), style='single')
        
        input()
    """
    demo()
