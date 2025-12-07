"""
YOUR PYTHON TOOLKIT - Simple patterns you'll use every day

Copy these patterns. Use them. Build from them.
No theory. Just practical code you can modify.
"""

import sys
import os
import time

# ============================================================================
# PATTERN 1: Setup (Copy this to every file)
# ============================================================================

def setup_terminal():
    """Call this once at the start of your program"""
    os.system('')  # Enable ANSI on Windows
    print('\033[2J\033[H\033[?25l', end='')  # Clear, home, hide cursor
    sys.stdout.flush()

def cleanup_terminal():
    """Call this at the end of your program"""
    print('\033[?25h\033[0m', end='')  # Show cursor, reset colors
    sys.stdout.flush()

# ============================================================================
# PATTERN 2: The UI class (Copy this, use everywhere)
# ============================================================================

class UI:
    """Dead simple UI. That's all you need."""
    
    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height
        setup_terminal()
    
    def __setitem__(self, line, text):
        """ui[5] = "text" - write to line 5"""
        if 0 <= line < self.height:
            text = str(text)[:self.width].ljust(self.width)
            print(f'\033[{line+1};1H{text}', end='')
            sys.stdout.flush()
    
    def write(self, line, col, text):
        """ui.write(5, 10, "text") - write at specific position"""
        if 0 <= line < self.height and 0 <= col < self.width:
            print(f'\033[{line+1};{col+1}H{text}', end='')
            sys.stdout.flush()
    
    def clear_line(self, line):
        """ui.clear_line(5) - erase line 5"""
        self[line] = ''
    
    def clear(self):
        """ui.clear() - erase everything"""
        print('\033[2J\033[H', end='')
        sys.stdout.flush()
    
    def close(self):
        """ui.close() - cleanup when done"""
        cleanup_terminal()

# ============================================================================
# PATTERN 3: Building a static screen
# ============================================================================

def static_screen_example():
    """Build a screen once, no updates"""
    ui = UI(60, 20)
    
    # Header
    ui[0] = "═" * 60
    ui[1] = "MY APPLICATION".center(60)
    ui[2] = "═" * 60
    
    # Content
    ui[5] = "  Welcome to my app!"
    ui[6] = "  This is line 6"
    ui[7] = "  This is line 7"
    
    # Footer
    ui[18] = "─" * 60
    ui[19] = "[Press Enter to continue]".center(60)
    
    input()
    ui.close()

# ============================================================================
# PATTERN 4: Updating one thing over time
# ============================================================================

def progress_bar_example():
    """Update a single line repeatedly"""
    ui = UI(60, 20)
    
    ui[0] = "Processing..."
    ui[2] = "Progress: [" + " " * 30 + "]"
    
    for i in range(31):
        # Build the bar
        filled = "█" * i
        empty = " " * (30 - i)
        ui[2] = f"Progress: [{filled}{empty}] {i*3}%"
        time.sleep(0.1)
    
    ui[4] = "Complete!".center(60)
    input()
    ui.close()

# ============================================================================
# PATTERN 5: Updating multiple things independently
# ============================================================================

def dashboard_example():
    """Update different sections at different times"""
    ui = UI(60, 20)
    
    # Setup sections
    ui[0] = "DASHBOARD".center(60)
    ui[1] = "─" * 60
    
    ui[3] = "  CPU:  0%"
    ui[4] = "  RAM:  0%"
    ui[5] = "  DISK: 0%"
    
    ui[7] = "  Status: Initializing..."
    
    # Update CPU
    for i in range(0, 101, 20):
        ui.write(3, 8, f"{i:3d}%")
        time.sleep(0.2)
    
    ui[7] = "  Status: CPU check complete"
    time.sleep(0.5)
    
    # Update RAM
    for i in range(0, 101, 20):
        ui.write(4, 8, f"{i:3d}%")
        time.sleep(0.2)
    
    ui[7] = "  Status: RAM check complete"
    time.sleep(0.5)
    
    # Update DISK
    for i in range(0, 101, 20):
        ui.write(5, 8, f"{i:3d}%")
        time.sleep(0.2)
    
    ui[7] = "  Status: All checks complete"
    
    input()
    ui.close()

# ============================================================================
# PATTERN 6: Menu with selection
# ============================================================================

def menu_example():
    """Simple menu you can navigate"""
    ui = UI(60, 20)
    
    options = ["New File", "Open File", "Save File", "Exit"]
    selected = 0
    
    def draw_menu():
        ui[0] = "MAIN MENU".center(60)
        ui[1] = "═" * 60
        
        for i, option in enumerate(options):
            if i == selected:
                # Highlight selected
                ui[3 + i] = f"  ► {option}"
            else:
                ui[3 + i] = f"    {option}"
        
        ui[18] = "─" * 60
        ui[19] = "W/S to move, Enter to select".center(60)
    
    draw_menu()
    
    while True:
        key = input().strip().lower()
        
        if key == 'w' and selected > 0:
            selected -= 1
            draw_menu()
        elif key == 's' and selected < len(options) - 1:
            selected += 1
            draw_menu()
        elif key == '' or key == '\n':  # Enter
            break
        elif key == 'q':
            selected = -1
            break
    
    ui.close()
    return options[selected] if selected >= 0 else None

# ============================================================================
# PATTERN 7: Form with fields
# ============================================================================

def form_example():
    """Collect user input with a form"""
    ui = UI(60, 20)
    
    ui[0] = "USER REGISTRATION".center(60)
    ui[1] = "═" * 60
    
    fields = ["Username", "Email", "Password"]
    values = {}
    
    for i, field in enumerate(fields):
        ui[3 + i] = f"  {field}: "
    
    # Collect input for each field
    for i, field in enumerate(fields):
        ui[18] = f"Enter {field}:".center(60)
        
        # Move cursor to input position
        print(f'\033[{4+i};{len(field)+4}H', end='')
        print('\033[?25h', end='')  # Show cursor
        sys.stdout.flush()
        
        value = input()
        ui.write(3 + i, len(field) + 4, value)
        values[field] = value
        
        print('\033[?25l', end='')  # Hide cursor
    
    ui[18] = "Registration complete!".center(60)
    input()
    ui.close()
    
    return values

# ============================================================================
# PATTERN 8: Status messages with colors
# ============================================================================

def status_example():
    """Show status with colors"""
    ui = UI(60, 20)
    
    def show_status(line, msg, status='info'):
        colors = {
            'error': '\033[31m',    # Red
            'warning': '\033[33m',  # Yellow
            'success': '\033[32m',  # Green
            'info': '\033[36m'      # Cyan
        }
        color = colors.get(status, '')
        ui[line] = f"{color}  {msg}\033[0m"
    
    ui[0] = "SYSTEM STATUS".center(60)
    ui[1] = "═" * 60
    
    show_status(3, "Connecting to server...", 'info')
    time.sleep(1)
    
    show_status(4, "Connection failed", 'error')
    time.sleep(1)
    
    show_status(5, "Retrying connection...", 'warning')
    time.sleep(1)
    
    show_status(6, "Connected successfully!", 'success')
    
    input()
    ui.close()

# ============================================================================
# PATTERN 9: Live data feed
# ============================================================================

def live_feed_example():
    """Scrolling list of updates"""
    ui = UI(60, 20)
    
    ui[0] = "LIVE ACTIVITY FEED".center(60)
    ui[1] = "═" * 60
    
    # Activity lines: rows 3-17 (15 lines)
    activities = []
    max_lines = 15
    
    def add_activity(msg):
        activities.append(msg)
        if len(activities) > max_lines:
            activities.pop(0)
        
        # Redraw all visible activities
        for i, activity in enumerate(activities):
            ui[3 + i] = f"  {activity}"
        
        # Clear any extra lines
        for i in range(len(activities), max_lines):
            ui[3 + i] = ""
    
    # Simulate activity
    events = [
        "User alice logged in",
        "File uploaded: report.pdf",
        "New comment on Issue #42",
        "Build completed successfully",
        "User bob logged out",
        "Error in payment processor",
        "Database backup started",
        "Email sent to 150 users",
        "Cache cleared",
        "System restart scheduled"
    ]
    
    for event in events:
        add_activity(event)
        time.sleep(0.5)
    
    input()
    ui.close()

# ============================================================================
# PATTERN 10: Your template (Start every project with this)
# ============================================================================

def your_template():
    """Copy this structure for new projects"""
    ui = UI(80, 24)
    
    try:
        # Your code here
        ui[0] = "MY APP".center(80)
        ui[2] = "Ready!"
        
        # Do your thing...
        
        input()
    
    finally:
        # Always cleanup
        ui.close()

# ============================================================================
# YOUR WORKFLOW - The methodology
# ============================================================================

"""
METHODOLOGY: How to build any terminal UI

STEP 1: Plan your layout
    - Sketch on paper: where does each thing go?
    - Assign line numbers: header=0, menu=5-10, status=20, etc.

STEP 2: Create the UI
    ui = UI(width, height)

STEP 3: Draw static parts once
    ui[0] = "Title"
    ui[1] = "═" * 80
    ui[20] = "Footer"

STEP 4: Update dynamic parts as needed
    ui[5] = f"Count: {count}"
    ui[7] = f"Status: {status}"

STEP 5: Cleanup when done
    ui.close()

THAT'S IT. Every UI follows this pattern.
"""

# ============================================================================
# QUICK REFERENCE - Patterns you'll memorize
# ============================================================================

"""
PATTERN: Create UI
    ui = UI(80, 24)

PATTERN: Write full line
    ui[5] = "text here"

PATTERN: Write at position
    ui.write(5, 10, "text")

PATTERN: Update repeatedly
    for i in range(100):
        ui[5] = f"Count: {i}"

PATTERN: Multiple independent updates
    ui[5] = "Section A"
    ui[10] = "Section B"
    ui[15] = "Section C"

PATTERN: Colors
    ui[5] = "\033[31mRed text\033[0m"
    ui[6] = "\033[32mGreen text\033[0m"

PATTERN: Menu
    options = ["A", "B", "C"]
    selected = 0
    for i, opt in enumerate(options):
        mark = "►" if i == selected else " "
        ui[i] = f"  {mark} {opt}"

PATTERN: Form
    ui[5] = "Name: "
    name = input()

PATTERN: Status with color
    def status(msg, color='\033[36m'):
        ui[20] = f"{color}{msg}\033[0m"

PATTERN: Always cleanup
    try:
        # your code
    finally:
        ui.close()
"""

# ============================================================================
# DEMO ALL PATTERNS
# ============================================================================

if __name__ == "__main__":
    print("Choose a pattern to see:")
    print("1. Static screen")
    print("2. Progress bar")
    print("3. Dashboard")
    print("4. Menu")
    print("5. Form")
    print("6. Status messages")
    print("7. Live feed")
    print("8. Run all")
    
    choice = input("\nChoice: ").strip()
    
    if choice == '1':
        static_screen_example()
    elif choice == '2':
        progress_bar_example()
    elif choice == '3':
        dashboard_example()
    elif choice == '4':
        result = menu_example()
        print(f"Selected: {result}")
    elif choice == '5':
        data = form_example()
        print(f"Collected: {data}")
    elif choice == '6':
        status_example()
    elif choice == '7':
        live_feed_example()
    elif choice == '8':
        static_screen_example()
        progress_bar_example()
        dashboard_example()
        menu_example()
        form_example()
        status_example()
        live_feed_example()
