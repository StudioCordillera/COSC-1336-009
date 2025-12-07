import sys
import os

def move(line, col):
    """Move cursor to position"""
    return f'\033[{line};{col}H'

class UI:
    """Specify height. Fill by index. Done."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lines = [' ' * width] * height
        os.system('')  # Enable ANSI on Windows
        print('\033[2J\033[H', end='')  # Clear screen
    
    def __setitem__(self, line, text):
        """ui[5] = "text" - that's it"""
        self.lines[line] = text[:self.width].ljust(self.width)
        print(move(line + 1, 1) + text[:self.width].ljust(self.width), end='')
        sys.stdout.flush()
    
    def __str__(self):
        return '\n'.join(self.lines)


# Example
ui = UI(width=50, height=20)

ui[0] = "═" * 50
ui[1] = "My App".center(50)
ui[2] = "═" * 50
ui[5] = "  Item 1"
ui[6] = "  Item 2"
ui[19] = "[OK]".center(50)

input("\nPress Enter...")
