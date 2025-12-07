"""
BRAIN BUILDER - Learn by doing, not reading
Run each exercise. See it work. Understand it viscerally.
"""

import sys
import os
import time

# Enable ANSI
os.system('')

def pause(msg="Press Enter to continue..."):
    input(f"\n{msg}")

def clear():
    print('\033[2J\033[H', end='')

# ============================================================================
# EXERCISE 1: See the problem
# ============================================================================
def exercise_1():
    clear()
    print("EXERCISE 1: The Problem Without ANSI\n")
    print("Watch what happens when we try to update a counter...\n")
    pause()
    
    # This is what you've been doing
    for i in range(20):
        print(f"Count: {i}")
        time.sleep(0.1)
    
    print("\n^ That's 20 lines. Scrolling. Ugly.")
    pause()

# ============================================================================
# EXERCISE 2: See the solution
# ============================================================================
def exercise_2():
    clear()
    print("EXERCISE 2: The Solution With ANSI\n")
    print("Same counter, but watch THIS...\n")
    pause()
    
    # This is what ANSI gives you
    print("Count: 0", end='', flush=True)
    for i in range(1, 20):
        print('\033[1G', end='')  # Move to start of line
        print(f"Count: {i}", end='', flush=True)
        time.sleep(0.1)
    
    print("\n\n^ ONE line. Updated in place. Clean.")
    pause()

# ============================================================================
# EXERCISE 3: Understand positioning
# ============================================================================
def exercise_3():
    clear()
    print("EXERCISE 3: Absolute Positioning\n")
    print("I can write ANYWHERE on screen...\n")
    pause()
    
    # Write at specific coordinates
    print('\033[5;10H' + "← Row 5, Column 10", end='', flush=True)
    time.sleep(1)
    
    print('\033[10;20H' + "← Row 10, Column 20", end='', flush=True)
    time.sleep(1)
    
    print('\033[15;5H' + "← Row 15, Column 5", end='', flush=True)
    time.sleep(1)
    
    print('\033[3;30H' + "← Row 3, Column 30 (went backwards!)", end='', flush=True)
    
    print('\033[20;1H')  # Move cursor out of the way
    pause()

# ============================================================================
# EXERCISE 4: Build mental model
# ============================================================================
def exercise_4():
    clear()
    print("EXERCISE 4: The Grid Mental Model\n")
    pause()
    
    # Show the grid
    print("The terminal is a GRID:")
    print()
    for row in range(1, 11):
        for col in range(1, 21):
            print('\033[{};{}H'.format(row + 2, col * 3), end='')
            print('·', end='', flush=True)
            time.sleep(0.02)
    
    print('\033[15;1H')
    print("\nEach dot is a CELL you can write to.")
    print("ANSI lets you jump to any cell instantly.")
    pause()

# ============================================================================
# EXERCISE 5: See surgical updates
# ============================================================================
def exercise_5():
    clear()
    print("EXERCISE 5: Surgical Updates\n")
    print("Watch me update JUST the parts that changed...\n")
    pause()
    
    # Draw initial UI
    print('\033[5;1H' + "CPU:  0%")
    print('\033[6;1H' + "RAM:  0%")
    print('\033[7;1H' + "DISK: 0%")
    time.sleep(1)
    
    # Update only CPU
    for i in range(0, 101, 10):
        print('\033[5;7H' + f"{i:3d}%", end='', flush=True)
        time.sleep(0.2)
    
    # Update only RAM
    for i in range(0, 101, 10):
        print('\033[6;7H' + f"{i:3d}%", end='', flush=True)
        time.sleep(0.2)
    
    # Update only DISK
    for i in range(0, 101, 10):
        print('\033[7;7H' + f"{i:3d}%", end='', flush=True)
        time.sleep(0.2)
    
    print('\033[10;1H')
    print("^ Each line updated INDEPENDENTLY.")
    print("No redrawing the whole screen.")
    pause()

# ============================================================================
# EXERCISE 6: Colors make meaning
# ============================================================================
def exercise_6():
    clear()
    print("EXERCISE 6: Colors Add Meaning\n")
    pause()
    
    # Show status with colors
    print('\033[5;1H' + '\033[31m' + "ERROR: Connection failed" + '\033[0m')
    time.sleep(1)
    
    print('\033[6;1H' + '\033[33m' + "WARNING: Low disk space" + '\033[0m')
    time.sleep(1)
    
    print('\033[7;1H' + '\033[32m' + "SUCCESS: Upload complete" + '\033[0m')
    time.sleep(1)
    
    print('\033[10;1H')
    print("^ Red = danger, Yellow = caution, Green = good")
    print("Your brain processes this INSTANTLY.")
    pause()

# ============================================================================
# EXERCISE 7: Build a simple UI
# ============================================================================
def exercise_7():
    clear()
    print("EXERCISE 7: Your First UI\n")
    print("Watch me build a menu...\n")
    pause()
    
    clear()
    
    # Draw box
    print('\033[2;5H' + "┌" + "─" * 30 + "┐")
    for i in range(3, 9):
        print(f'\033[{i};5H' + "│" + " " * 30 + "│")
    print('\033[9;5H' + "└" + "─" * 30 + "┘")
    time.sleep(0.5)
    
    # Add title
    print('\033[3;8H' + '\033[1m' + "MAIN MENU" + '\033[0m')
    time.sleep(0.5)
    
    # Add options
    options = ["1. New File", "2. Open File", "3. Save File", "4. Exit"]
    for i, opt in enumerate(options, start=5):
        print(f'\033[{i};8H' + opt)
        time.sleep(0.3)
    
    print('\033[12;1H')
    print("^ Built piece by piece, exactly where I wanted each part.")
    pause()

# ============================================================================
# EXERCISE 8: Make it interactive
# ============================================================================
def exercise_8():
    clear()
    print("EXERCISE 8: Interactive Selection\n")
    print("Now let's make it RESPOND to you...\n")
    pause()
    
    clear()
    
    # Draw menu
    options = ["Start Game", "Load Game", "Options", "Quit"]
    selected = 0
    
    def draw_menu():
        print('\033[3;10H' + '\033[1m' + "GAME MENU" + '\033[0m')
        for i, opt in enumerate(options):
            print(f'\033[{5+i};10H', end='')
            if i == selected:
                print('\033[7m' + f" {opt} " + '\033[0m', end='')
            else:
                print(f"  {opt}  ", end='')
        sys.stdout.flush()
    
    draw_menu()
    print('\033[15;1H' + "Use W/S to move, Enter to select, Q to quit")
    
    while True:
        print('\033[16;1H\033[K', end='')  # Clear status line
        key = input().lower()
        
        if key == 'w' and selected > 0:
            selected -= 1
            draw_menu()
        elif key == 's' and selected < len(options) - 1:
            selected += 1
            draw_menu()
        elif key == '\r' or key == '':
            break
        elif key == 'q':
            selected = -1
            break
    
    print('\033[17;1H')
    if selected >= 0:
        print(f"You selected: {options[selected]}")
    pause()

# ============================================================================
# EXERCISE 9: The UI class
# ============================================================================
def exercise_9():
    clear()
    print("EXERCISE 9: Encapsulate It\n")
    print("Turn what you learned into a TOOL...\n")
    pause()
    
    class UI:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            os.system('')
            print('\033[2J\033[H', end='')
        
        def __setitem__(self, line, text):
            print(f'\033[{line+1};1H' + text[:self.width].ljust(self.width), end='')
            sys.stdout.flush()
    
    # Now use it
    ui = UI(50, 20)
    
    ui[0] = "═" * 50
    ui[1] = "MY APPLICATION".center(50)
    ui[2] = "═" * 50
    
    for i in range(10):
        ui[5] = f"  Processing item {i+1}/10..."
        time.sleep(0.3)
    
    ui[5] = "  ✓ Complete!".ljust(50)
    
    print('\033[15;1H')
    print("^ THIS is what you've been building toward.")
    print("Specify height. Fill by index. Update anytime.")
    pause()

# ============================================================================
# EXERCISE 10: The insight
# ============================================================================
def exercise_10():
    clear()
    print("EXERCISE 10: The Moment of Clarity\n")
    pause()
    
    print("Before ANSI, you thought:")
    print("  print() → text goes out → scrolls up → gone")
    print()
    time.sleep(2)
    
    print("After ANSI, you understand:")
    print("  Terminal is a 2D grid")
    print("  Each cell is addressable")
    print("  Cursor moves to any cell")
    print("  Print overwrites that cell")
    print("  Previous content stays")
    print()
    time.sleep(2)
    
    print("This means:")
    print("  ✓ Update any line anytime")
    print("  ✓ Build persistent UIs")
    print("  ✓ Create smooth animations")
    print("  ✓ Make interactive apps")
    print("  ✓ Professional-looking tools")
    print()
    time.sleep(2)
    
    print('\033[32m\033[1m' + "You now have the ability." + '\033[0m')
    pause()

# ============================================================================
# MAIN MENU
# ============================================================================
def main():
    exercises = [
        ("See the problem", exercise_1),
        ("See the solution", exercise_2),
        ("Understand positioning", exercise_3),
        ("Build mental model", exercise_4),
        ("See surgical updates", exercise_5),
        ("Colors make meaning", exercise_6),
        ("Build a simple UI", exercise_7),
        ("Make it interactive", exercise_8),
        ("The UI class", exercise_9),
        ("The insight", exercise_10),
    ]
    
    while True:
        clear()
        print("BRAIN BUILDER - ANSI Terminal UI Mastery\n")
        print("Learn by experiencing, not memorizing.\n")
        
        for i, (name, _) in enumerate(exercises, 1):
            print(f"  {i:2d}. {name}")
        
        print(f"\n  {len(exercises)+1:2d}. Run all exercises")
        print("   Q. Quit")
        
        choice = input("\nChoose: ").strip().lower()
        
        if choice == 'q':
            break
        elif choice == str(len(exercises) + 1):
            for name, func in exercises:
                func()
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(exercises):
                    exercises[idx][1]()
            except ValueError:
                pass

if __name__ == "__main__":
    main()
    clear()
    print("The ability is now in your brain. Use it.")
