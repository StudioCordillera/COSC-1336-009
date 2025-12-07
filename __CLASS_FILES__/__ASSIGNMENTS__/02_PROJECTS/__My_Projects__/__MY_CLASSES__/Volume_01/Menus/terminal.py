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
# ALL ARGUMENTS USED IN THIS MODULE
# =============================================================================
"""
CURSOR & DISPLAY:
    move(row, col) - Move cursor
    write(row, col, text) - Write text at position
    write_line(row, text) - Write text at start of row
    center_text(row, text) - Center text on row
    home() - Move to top-left
    clear() - Clear screen
    clear_line() - Clear current line
    hide_cursor() - Hide cursor
    show_cursor() - Show cursor

DRAWING:
    draw_box(row, col, width, height) - Draw box
    draw_hline(row, col, length, heavy=False) - Draw horizontal line

TERMINAL INFO:
    get_size() - Returns (width, height)
    get_width() - Returns width
    get_height() - Returns height

RESPONSIVE LAYOUT (Web-style):
    pct(value, of_width=True) - Convert percentage to absolute
    margin(top, right, bottom, left) - CSS-style margins → (row, col, width, height)
    padding(amount) - Uniform padding → (row, col, width, height)
    center_box(width, height) - Center box → (row, col)
    offset_from(row, col, offset_row, offset_col) - Relative positioning → (row, col)
    inset(row, col, width, height, amount) - Inner box → (row, col, width, height)
    split_horizontal(row, col, width, height, ratio) - Split area → two tuples
    split_vertical(row, col, width, height, ratio) - Split area → two tuples

GRID LAYOUT:
    Grid(rows, cols, padding=1) - Create grid
    Grid.cell(row, col) - Get cell position → (y, x)
    Grid.cell_size() - Get cell dimensions → (width, height)

DEMO:
    demo() - Run demo
"""

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

def margin(top=0, right=0, bottom=0, left=0):
    """Calculate content area with margins (CSS-style)
    
    Args:
        top, right, bottom, left: Margins (percentage 0.0-1.0 OR absolute)
    
    Returns:
        (row, col, width, height) tuple for content area
    """
    t = pct(top, of_width=False)
    r = pct(right, of_width=True)
    b = pct(bottom, of_width=False)
    l = pct(left, of_width=True)
    
    row = t + 1
    col = l + 1
    width = get_width() - l - r - 2
    height = get_height() - t - b - 2
    
    return (row, col, width, height)

def padding(amount):
    """Uniform padding from all edges
    
    Args:
        amount: Padding (percentage 0.0-1.0 OR absolute)
    
    Returns:
        (row, col, width, height) tuple for content area
    """
    return margin(amount, amount, amount, amount)

def center_box(width, height):
    """Calculate centered position for a box
    
    Args:
        width: Box width (percentage 0.0-1.0 OR absolute)
        height: Box height (percentage 0.0-1.0 OR absolute)
    
    Returns:
        (row, col) tuple for top-left corner
    """
    w = pct(width, of_width=True)
    h = pct(height, of_width=False)
    
    row = (get_height() - h) // 2
    col = (get_width() - w) // 2
    
    return (max(1, row), max(1, col))

def offset_from(row, col, offset_row=0, offset_col=0):
    """Calculate position relative to another element
    
    Args:
        row, col: Base position
        offset_row, offset_col: Offset (percentage 0.0-1.0 OR absolute)
    
    Returns:
        (row, col) tuple for new position
    """
    dr = pct(offset_row, of_width=False)
    dc = pct(offset_col, of_width=True)
    
    return (row + dr, col + dc)

def inset(row, col, width, height, amount):
    """Calculate inset box inside another box
    
    Args:
        row, col: Outer box position
        width, height: Outer box dimensions
        amount: Inset amount (percentage 0.0-1.0 OR absolute)
    
    Returns:
        (row, col, width, height) tuple for inner box
    """
    inset_amt = pct(amount, of_width=True)
    
    return (
        row + inset_amt,
        col + inset_amt,
        width - (inset_amt * 2),
        height - (inset_amt * 2)
    )

def split_horizontal(row, col, width, height, ratio=0.5):
    """Split area horizontally
    
    Args:
        row, col: Area position
        width, height: Area dimensions
        ratio: Split ratio 0.0-1.0 (default: 0.5 for equal split)
    
    Returns:
        Two tuples: (row1, col1, w1, h1), (row2, col2, w2, h2)
    """
    split_h = int(height * ratio)
    
    top = (row, col, width, split_h)
    bottom = (row + split_h + 1, col, width, height - split_h - 1)
    
    return (top, bottom)

def split_vertical(row, col, width, height, ratio=0.5):
    """Split area vertically
    
    Args:
        row, col: Area position
        width, height: Area dimensions
        ratio: Split ratio 0.0-1.0 (default: 0.5 for equal split)
    
    Returns:
        Two tuples: (row1, col1, w1, h1), (row2, col2, w2, h2)
    """
    split_w = int(width * ratio)
    
    left = (row, col, split_w, height)
    right = (row, col + split_w + 1, width - split_w - 1, height)
    
    return (left, right)

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
    """Demo using Python doc style ASCII with responsive layout"""
    
    clear()
    hide_cursor()
    
    # Title
    center_text(2, "TERMINAL MODULE - RESPONSIVE LAYOUT DEMO")
    draw_hline(3, 1, 0.95, heavy=True)
    
    # Using margin() for outer container
    outer_r, outer_c, outer_w, outer_h = margin(0.1, 0.1, 0.15, 0.1)
    draw_box(outer_r, outer_c, outer_w, outer_h)
    
    # Using inset() for inner content area
    inner_r, inner_c, inner_w, inner_h = inset(outer_r, outer_c, outer_w, outer_h, 2)
    
    # Split horizontally - header and body
    header, body = split_horizontal(inner_r, inner_c, inner_w, inner_h, 0.2)
    h_r, h_c, h_w, h_h = header
    b_r, b_c, b_w, b_h = body
    
    # Header content
    center_text(h_r + 1, "ASCII Characters")
    
    # Split body vertically - two columns
    left_col, right_col = split_vertical(b_r, b_c, b_w, b_h, 0.5)
    l_r, l_c, l_w, l_h = left_col
    r_r, r_c, r_w, r_h = right_col
    
    # Left column content
    write(l_r + 1, l_c, f"Corners: {ASCII.CORNER}")
    write(l_r + 2, l_c, f"H-Line:  {ASCII.HLINE}")
    write(l_r + 3, l_c, f"V-Line:  {ASCII.VLINE}")
    write(l_r + 4, l_c, f"Heavy:   {ASCII.HLINE_HEAVY}")
    
    # Right column content
    write(r_r + 1, r_c, f"Up:    {ASCII.UP}")
    write(r_r + 2, r_c, f"Down:  {ASCII.DOWN}")
    write(r_r + 3, r_c, f"Left:  {ASCII.LEFT}")
    write(r_r + 4, r_c, f"Right: {ASCII.RIGHT}")
    
    # Centered box using center_box()
    box_w, box_h = 30, 3
    box_r, box_c = center_box(box_w, box_h)
    draw_box(box_r, box_c, box_w, box_h)
    center_text(box_r + 1, "Centered with center_box()")
    
    # Footer
    center_text(get_height() - 2, "Press Enter to exit...")
    
    move(get_height(), 1)
    show_cursor()
    input()
    clear()

# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == '__main__':
    """
    RESPONSIVE LAYOUT EXAMPLES
    ==========================
    
    # Basic percentages
    from terminal import *
    
    with hidden_cursor():
        clear()
        draw_box(0.1, 0.1, 0.8, 0.6)  # 10% margins, 80% width, 60% height
        center_text(5, "My Application")
    
    # Web-style margins
    row, col, width, height = margin(0.1, 0.05, 0.1, 0.05)  # top, right, bottom, left
    draw_box(row, col, width, height)
    
    # Uniform padding
    row, col, width, height = padding(0.05)  # 5% padding all sides
    
    # Center a box
    row, col = center_box(40, 10)  # width=40, height=10
    draw_box(row, col, 40, 10)
    
    # Nested boxes with inset
    outer = (5, 10, 60, 20)
    inner_r, inner_c, inner_w, inner_h = inset(*outer, 2)  # 2 char inset
    
    # Split layouts
    left, right = split_vertical(5, 10, 60, 20, ratio=0.7)  # 70/30 split
    top, bottom = split_horizontal(5, 10, 60, 20, ratio=0.3)  # 30/70 split
    
    # Relative positioning
    base_row, base_col = 10, 20
    new_row, new_col = offset_from(base_row, base_col, offset_row=5, offset_col=0.1)
    """
    demo()
