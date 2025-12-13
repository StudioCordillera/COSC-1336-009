"""
Render Helper Functions - Pure display utilities with no business logic
"""


def drawBox(x: int, y: int, width: int, height: int, label: str = ""):
    """Draw a box with optional label inside"""
    if width < 3 or height < 3:
        return
    
    # Top border
    print(f"\033[{y};{x}H+" + "-" * (width - 2) + "+")
    
    # First content line with label
    if label and height > 2:
        labelLine = " " * (width - 2)
        if len(label) < width - 4:
            labelLine = " " + label + " " * (width - 3 - len(label))
        print(f"\033[{y+1};{x}H|{labelLine}|")
        startEmpty = 2
    else:
        startEmpty = 1
    
    # Empty middle lines
    for i in range(startEmpty, height - 1):
        print(f"\033[{y+i};{x}H|" + " " * (width - 2) + "|")
    
    # Bottom border
    print(f"\033[{y+height-1};{x}H+" + "-" * (width - 2) + "+")


def clearScreen():
    """Clear the terminal screen"""
    print("\033[H\033[J", end='', flush=True)


def hideCursor():
    """Hide terminal cursor"""
    print("\033[?25l", end='', flush=True)


def showCursor():
    """Show terminal cursor"""
    print("\033[?25h", end='', flush=True)
