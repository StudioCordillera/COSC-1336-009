from terminal import move, write, clear, draw_box, ASCII, hide_cursor, show_cursor
import time

# Clear screen and setup
clear()
hide_cursor()

'''
╔══════════════════════════════════════════════════════════════════════════════╗
║                                MAIN MENU                                     ║
║                        CONTENT MANAGEMENT SYSTEM                             ║ 
╚══════════════════════════════════════════════════════════════════════════════╝

    Please select an option:

    ┌──────────────────────────────────────────────────────────────────────┐
    │  1. REGISTER NEW ITEM                                                │
    │  2. VIEW COLLECTION                                                  │
    │  3. SETTINGS                                                         │
    │  4. EXIT                                                             │
    └──────────────────────────────────────────────────────────────────────┘


'''


draw_box(.6, .35, .2, .1)


corner = '+'
verLine = '-'
horLine = '|'


'''
move(row, col)
    row: Row (1-based) OR percentage (0.0-1.0)
    col: Column (1-based) OR percentage (0.0-1.0)

write(row, col, text)
    row: Row position
    col: Column position
    text: Text to write

write_line(row, text)
    row: Row position
    text: Text to write

draw_box(row, col, width, height)
    row: Top-left row (1-based) OR percentage (0.0-1.0)
    col: Top-left column (1-based) OR percentage (0.0-1.0)
    width: Width OR percentage (0.0-1.0)
    height: Height OR percentage (0.0-1.0)

draw_hline(row, col, length, heavy=False)
    row: Row position
    col: Column position
    length: Length OR percentage (0.0-1.0)
    heavy: Use heavy line style (default: False)

center_text(row, text)
    row: Row position
    text: Text to center

pct(value, of_width=True)
    value: Percentage (0.0-1.0) OR integer
    of_width: True for width, False for height (default: True)

Grid.__init__(rows, cols, padding=1)
    rows: Number of rows
    cols: Number of columns
    padding: Spacing between cells (default: 1)

Grid.cell(row, col)
    row: Grid row index
    col: Grid column index

No arguments:
    get_size() - Returns (width, height)
    get_width() - Returns width
    get_height() - Returns height
    home() - Move to top-left
    clear() - Clear screen
    clear_line() - Clear current line
    hide_cursor() - Hide cursor
    show_cursor() - Show cursor
    Grid.cell_size() - Returns (cell_width, cell_height)
    demo() - Run demo

'''




