"""
terminal.py - Simple terminal control using Python doc style ASCII

Usage:
    from terminal import move, clear, write
    
    move(5, 10)
    print("Hello")
    clear()
"""

import sys
import os

# Enable ANSI on Windows
if sys.platform == 'win32':
    os.system('')

# =============================================================================
# TERMINAL INFO
# =============================================================================

def get_size():
    """Get terminal size as (width, height) tuple"""
    import shutil
    return shutil.get_terminal_size()

def get_width():
    """Get terminal width"""
    return get_size()[0]

def get_height():
    """Get terminal height"""
    return get_size()[1]

# =============================================================================
# CURSOR MOVEMENT
# =============================================================================

def move(row, col):
    """Move cursor to position
    
    Args:
        row: Row (1-based) OR percentage (0.0-1.0)
        col: Column (1-based) OR percentage (0.0-1.0)
    """
    if isinstance(row, float) and 0 <= row <= 1:
        row = int(row * get_height())
    if isinstance(col, float) and 0 <= col <= 1:
        col = int(col * get_width())
    
    row = max(1, min(row, get_height()))
    col = max(1, min(col, get_width()))
    
    print(f'\033[{row};{col}H', end='')
    sys.stdout.flush()

def home():
    """Move to top-left"""
    print('\033[H', end='')
    sys.stdout.flush()

# =============================================================================
# CLEARING
# =============================================================================

def clear():
    """Clear screen"""
    print('\033[2J', end='')
    sys.stdout.flush()

def clear_line():
    """Clear current line"""
    print('\033[2K', end='')
    sys.stdout.flush()

# =============================================================================
# CURSOR VISIBILITY
# =============================================================================

def hide_cursor():
    """Hide cursor"""
    print('\033[?25l', end='')
    sys.stdout.flush()

def show_cursor():
    """Show cursor"""
    print('\033[?25h', end='')
    sys.stdout.flush()

# =============================================================================
# CONVENIENCE
# =============================================================================

def write(row, col, text):
    """Write text at position"""
    move(row, col)
    print(text, end='')
    sys.stdout.flush()

def write_line(row, text):
    """Write text at start of row"""
    move(row, 1)
    clear_line()
    print(text, end='')
    sys.stdout.flush()

# =============================================================================
# ASCII CHARACTERS (from Python docs)
# =============================================================================

class ASCII:
    """Standard ASCII characters used in Python documentation
    
    Source: cpython/Lib/dataclasses.py and other official files
    """
    # Box corners and lines
    CORNER = '+'
    HLINE = '-'
    HLINE_HEAVY = '='
    VLINE = '|'
    
    # Arrows
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'
    
    # Markers
    BULLET = '*'
    HASH = '#'

# =============================================================================
# DRAWING
# =============================================================================

def draw_box(row, col, width, height):
    """Draw box using Python doc style ASCII
    
    Args:
        row: Top-left row (1-based) OR percentage (0.0-1.0)
        col: Top-left column (1-based) OR percentage (0.0-1.0) 
        width: Width OR percentage (0.0-1.0)
        height: Height OR percentage (0.0-1.0)
    """
    # Convert percentages
    if isinstance(row, float) and 0 <= row <= 1:
        row = int(row * get_height())
    if isinstance(col, float) and 0 <= col <= 1:
        col = int(col * get_width())
    if isinstance(width, float) and 0 <= width <= 1:
        width = int(width * get_width())
    if isinstance(height, float) and 0 <= height <= 1:
        height = int(height * get_height())
    
    # Top
    write(row, col, ASCII.CORNER + ASCII.HLINE * width + ASCII.CORNER)
    
    # Sides
    for i in range(1, height + 1):
        write(row + i, col, ASCII.VLINE)
        write(row + i, col + width + 1, ASCII.VLINE)
    
    # Bottom
    write(row + height + 1, col, ASCII.CORNER + ASCII.HLINE * width + ASCII.CORNER)

def draw_hline(row, col, length, heavy=False):
    """Draw horizontal line"""
    if isinstance(length, float) and 0 <= length <= 1:
        length = int(length * get_width())
    
    char = ASCII.HLINE_HEAVY if heavy else ASCII.HLINE
    write(row, col, char * length)

def center_text(row, text):
    """Center text on row"""
    width = get_width()
    padding = (width - len(text)) // 2
    write(row, max(1, padding), text)

# =============================================================================
# LAYOUT HELPERS
# =============================================================================

def pct(value, of_width=True):
    """Convert percentage to absolute value
    
    Args:
        value: Percentage (0.0-1.0) OR integer
        of_width: True for width, False for height
    
    Returns:
        Absolute position as integer
    """
    if isinstance(value, float) and 0 <= value <= 1:
        return int(value * (get_width() if of_width else get_height()))
    return value

class Grid:
    """Grid layout helper"""
    
    def __init__(self, rows, cols, padding=1):
        self.rows = rows
        self.cols = cols
        self.padding = padding
        
        w = get_width()
        h = get_height()
        
        self.cell_width = (w - (cols + 1) * padding) // cols
        self.cell_height = (h - (rows + 1) * padding) // rows
    
    def cell(self, row, col):
        """Get position of cell"""
        y = self.padding + row * (self.cell_height + self.padding)
        x = self.padding + col * (self.cell_width + self.padding)
        return (y, x)
    
    def cell_size(self):
        """Get cell dimensions"""
        return (self.cell_width, self.cell_height)

# =============================================================================
# CONTEXT MANAGERS
# =============================================================================

class hidden_cursor:
    """Context manager to hide cursor
    
    Usage:
        with hidden_cursor():
            # cursor hidden
            pass
    """
    def __enter__(self):
        hide_cursor()
        return self
    
    def __exit__(self, *args):
        show_cursor()

# =============================================================================
# DEMO
# =============================================================================

def demo():
    """Demo using Python doc style ASCII"""
    
    clear()
    hide_cursor()
    
    # Title
    center_text(2, "TERMINAL MODULE - PYTHON DOC STYLE")
    draw_hline(3, 1, 0.95, heavy=True)
    
    # Main box
    draw_box(5, 5, 60, 10)
    
    # Content
    write(7, 8, "Box drawn with Python doc ASCII:")
    write(8, 8, f"  {ASCII.CORNER} (corners)")
    write(9, 8, f"  {ASCII.HLINE} (horizontal lines)")
    write(10, 8, f"  {ASCII.VLINE} (vertical lines)")
    write(11, 8, f"  {ASCII.HLINE_HEAVY} (heavy lines)")
    
    write(13, 8, "Arrows: {0} {1} {2} {3}".format(
        ASCII.UP, ASCII.DOWN, ASCII.LEFT, ASCII.RIGHT))
    
    # Footer
    center_text(18, "Press Enter to exit...")
    
    move(20, 1)
    show_cursor()
    input()
    clear()

# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == '__main__':
    """
    Simple and elegant - Python doc style ASCII only
    
    from terminal import move, write, clear, draw_box, ASCII
    from terminal import center_text, hidden_cursor
    
    with hidden_cursor():
        clear()
        
        # Responsive layout with percentages
        draw_box(0.1, 0.1, 0.8, 0.6)
        center_text(0.15, "My Application")
        write(0.3, 0.15, f"{ASCII.RIGHT} Next step")
        
        input()
    """
    demo()
