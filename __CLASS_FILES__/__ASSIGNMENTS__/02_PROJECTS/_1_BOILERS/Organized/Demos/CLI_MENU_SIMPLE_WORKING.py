"""
SIMPLE WORKING CLI MENU DEMO
=============================
Lightweight, flicker-free menu system with keyboard controls.
No complex mouse handling - just clean, responsive menus.

Author: GitHub Copilot
Date: December 1, 2025
Platform: Windows
Python: 3.6+

Features:
- Arrow key navigation
- Enter to select
- ESC to exit
- No screen flickering
- Clean rendering
- Multiple demo menus
"""

import os
import sys
import msvcrt
import time

# ANSI escape codes
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
UNDERLINE = '\033[4m'
REVERSE = '\033[7m'

# Colors
FG_BLACK = '\033[30m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'
FG_YELLOW = '\033[33m'
FG_BLUE = '\033[34m'
FG_MAGENTA = '\033[35m'
FG_CYAN = '\033[36m'
FG_WHITE = '\033[37m'

FG_BRIGHT_BLACK = '\033[90m'
FG_BRIGHT_RED = '\033[91m'
FG_BRIGHT_GREEN = '\033[92m'
FG_BRIGHT_YELLOW = '\033[93m'
FG_BRIGHT_BLUE = '\033[94m'
FG_BRIGHT_MAGENTA = '\033[95m'
FG_BRIGHT_CYAN = '\033[96m'
FG_BRIGHT_WHITE = '\033[97m'

BG_BLACK = '\033[40m'
BG_BLUE = '\033[44m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Cursor control
CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'
CLEAR_SCREEN = '\033[2J\033[H'

# Simple ASCII symbols
POINTER = '>'
CHECK = 'v'
CROSS = 'x'

# ============================================================================
# SETUP
# ============================================================================

def enable_ansi():
    """Enable ANSI on Windows"""
    if sys.platform == 'win32':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except:
            pass

def get_key():
    """Get a single keypress"""
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key in (b'\x00', b'\xe0'):  # Special key
            key += msvcrt.getch()
        return key
    return None

def wait_key():
    """Wait for a keypress"""
    while True:
        key = get_key()
        if key:
            return key
        time.sleep(0.05)

# ============================================================================
# MENU CLASS
# ============================================================================

class SimpleMenu:
    """Simple, flicker-free menu"""
    
    def __init__(self, title, items):
        """
        items: list of tuples (label, callback_function)
        """
        self.title = title
        self.items = items
        self.selected = 0
    
    def render(self):
        """Render the menu once"""
        print(CLEAR_SCREEN + CURSOR_HIDE, end='', flush=True)
        
        # Title
        print(f"\n{BOLD}{FG_BRIGHT_CYAN}{'=' * 60}{RESET}")
        print(f"{BOLD}{FG_BRIGHT_CYAN}  {self.title}{RESET}")
        print(f"{BOLD}{FG_BRIGHT_CYAN}{'=' * 60}{RESET}\n")
        
        # Menu items
        for i, (label, _) in enumerate(self.items):
            if i == self.selected:
                print(f"  {FG_BRIGHT_GREEN}{POINTER} {BG_CYAN}{FG_BLACK} {label} {RESET}")
            else:
                print(f"    {FG_WHITE}{label}{RESET}")
        
        # Instructions
        print(f"\n{FG_BRIGHT_BLACK}{'─' * 60}{RESET}")
        print(f"{FG_BRIGHT_YELLOW}↑/↓: Navigate  |  Enter: Select  |  ESC: Exit{RESET}")
    
    def run(self):
        """Run the menu loop"""
        while True:
            self.render()
            
            key = wait_key()
            
            if key == b'\xe0H':  # Up arrow
                self.selected = (self.selected - 1) % len(self.items)
            
            elif key == b'\xe0P':  # Down arrow
                self.selected = (self.selected + 1) % len(self.items)
            
            elif key == b'\r':  # Enter
                _, callback = self.items[self.selected]
                if callback:
                    print(CLEAR_SCREEN + CURSOR_SHOW, end='', flush=True)
                    result = callback()
                    if result == 'exit':
                        break
                    if result != 'continue':
                        input(f"\n{FG_BRIGHT_CYAN}Press Enter to continue...{RESET}")
            
            elif key == b'\x1b':  # ESC
                break
        
        print(CLEAR_SCREEN + CURSOR_SHOW, end='', flush=True)

# ============================================================================
# DEMO FUNCTIONS
# ============================================================================

def demo_simple_list():
    """Demo: Simple list selection"""
    items = [
        f"Option {i+1}" for i in range(10)
    ]
    
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}Simple List Demo{RESET}\n")
    
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")
    
    print(f"\n{FG_BRIGHT_GREEN}This demonstrates a static list.{RESET}")
    print(f"{FG_BRIGHT_GREEN}In a real app, you could select from these items.{RESET}")

def demo_colored_output():
    """Demo: Colored text"""
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}Colored Output Demo{RESET}\n")
    
    colors = [
        (FG_RED, "Red"),
        (FG_GREEN, "Green"),
        (FG_YELLOW, "Yellow"),
        (FG_BLUE, "Blue"),
        (FG_MAGENTA, "Magenta"),
        (FG_CYAN, "Cyan"),
        (FG_WHITE, "White"),
    ]
    
    for color, name in colors:
        print(f"  {color}{BOLD}{name:10}{RESET} - This is {color}{name.lower()}{RESET} text")
    
    print(f"\n{FG_BRIGHT_GREEN}ANSI colors work!{RESET}")

def demo_text_styles():
    """Demo: Text formatting"""
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}Text Styles Demo{RESET}\n")
    
    print(f"  {BOLD}Bold text{RESET}")
    print(f"  {DIM}Dim text{RESET}")
    print(f"  {UNDERLINE}Underlined text{RESET}")
    print(f"  {REVERSE}Reversed text{RESET}")
    print(f"  {BOLD}{UNDERLINE}Bold + Underline{RESET}")
    print(f"  {FG_RED}{BG_WHITE}{BOLD} Red on White {RESET}")
    
    print(f"\n{FG_BRIGHT_GREEN}Multiple styles can be combined!{RESET}")

def demo_progress_bar():
    """Demo: Simple progress bar"""
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}Progress Bar Demo{RESET}\n")
    
    total = 50
    for i in range(total + 1):
        percent = int(100 * i / total)
        filled = int(40 * i / total)
        bar = '█' * filled + '─' * (40 - filled)
        
        print(f"\r  [{FG_BRIGHT_GREEN}{bar}{RESET}] {percent}%", end='', flush=True)
        time.sleep(0.05)
    
    print(f"\n\n{FG_BRIGHT_GREEN}Progress complete!{RESET}")
    time.sleep(1)

def demo_spinner():
    """Demo: Loading spinner"""
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}Spinner Demo{RESET}\n")
    
    frames = ['|', '/', '-', '\\']
    
    for _ in range(20):
        for frame in frames:
            print(f"\r  {FG_BRIGHT_YELLOW}{frame}{RESET} Loading...", end='', flush=True)
            time.sleep(0.1)
    
    print(f"\r  {FG_BRIGHT_GREEN}{CHECK}{RESET} Complete!     ")
    time.sleep(1)

def demo_box_drawing():
    """Demo: ASCII box drawing"""
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}Box Drawing Demo{RESET}\n")
    
    width = 40
    
    # Simple box
    print(f"  +{'-' * width}+")
    print(f"  |{' ' * width}|")
    print(f"  |  {'Simple ASCII Box':^{width-4}}  |")
    print(f"  |{' ' * width}|")
    print(f"  +{'-' * width}+")
    
    print()
    
    # Double box
    print(f"  ╔{'═' * width}╗")
    print(f"  ║{' ' * width}║")
    print(f"  ║  {'Fancy Box (if supported)':^{width-4}}  ║")
    print(f"  ║{' ' * width}║")
    print(f"  ╚{'═' * width}╝")
    
    print(f"\n{FG_BRIGHT_GREEN}Box characters display based on terminal support{RESET}")

def demo_table():
    """Demo: Simple table"""
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}Table Demo{RESET}\n")
    
    # Header
    print(f"  {BOLD}{'ID':<5} {'Name':<15} {'Score':<10} {'Grade':<5}{RESET}")
    print(f"  {'-' * 40}")
    
    # Data
    data = [
        (1, "Alice", 95, "A"),
        (2, "Bob", 87, "B"),
        (3, "Charlie", 92, "A"),
        (4, "David", 78, "C"),
        (5, "Eve", 88, "B"),
    ]
    
    for id, name, score, grade in data:
        if grade == "A":
            color = FG_BRIGHT_GREEN
        elif grade == "B":
            color = FG_BRIGHT_CYAN
        else:
            color = FG_BRIGHT_YELLOW
        
        print(f"  {id:<5} {name:<15} {score:<10} {color}{grade:<5}{RESET}")
    
    print(f"\n{FG_BRIGHT_GREEN}Tables make data easy to read!{RESET}")

def demo_input():
    """Demo: User input"""
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}Input Demo{RESET}\n")
    
    name = input(f"  {FG_BRIGHT_YELLOW}Enter your name: {RESET}")
    age = input(f"  {FG_BRIGHT_YELLOW}Enter your age: {RESET}")
    
    print(f"\n  {FG_BRIGHT_GREEN}Hello, {BOLD}{name}{RESET}{FG_BRIGHT_GREEN}!{RESET}")
    print(f"  {FG_BRIGHT_GREEN}You are {BOLD}{age}{RESET}{FG_BRIGHT_GREEN} years old.{RESET}")

def show_submenu():
    """Demo: Nested submenu"""
    submenu = SimpleMenu("Submenu Example", [
        ("Submenu Option 1", lambda: print(f"\n{FG_BRIGHT_GREEN}You selected Submenu Option 1!{RESET}")),
        ("Submenu Option 2", lambda: print(f"\n{FG_BRIGHT_GREEN}You selected Submenu Option 2!{RESET}")),
        ("Submenu Option 3", lambda: print(f"\n{FG_BRIGHT_GREEN}You selected Submenu Option 3!{RESET}")),
        ("Back to Main Menu", lambda: 'exit'),
    ])
    submenu.run()
    return 'continue'

def exit_program():
    """Exit the program"""
    print(f"\n{FG_BRIGHT_GREEN}Thank you for using the CLI Menu Demo!{RESET}\n")
    return 'exit'

# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main program"""
    enable_ansi()
    
    menu = SimpleMenu("CLI Menu Demo - Simple & Working", [
        ("Simple List", demo_simple_list),
        ("Colored Output", demo_colored_output),
        ("Text Styles", demo_text_styles),
        ("Progress Bar", demo_progress_bar),
        ("Loading Spinner", demo_spinner),
        ("Box Drawing", demo_box_drawing),
        ("Table Display", demo_table),
        ("User Input", demo_input),
        ("Submenu Example", show_submenu),
        ("Exit", exit_program),
    ])
    
    try:
        menu.run()
    except KeyboardInterrupt:
        print(f"\n\n{FG_BRIGHT_YELLOW}Interrupted by user{RESET}\n")
    finally:
        print(CURSOR_SHOW, end='', flush=True)

if __name__ == "__main__":
    main()
