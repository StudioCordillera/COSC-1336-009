# ANSI Terminal UI - Dynamic & Responsive

## THE FUNDAMENTAL PROBLEM

You want to build a UI in a terminal. Here's what you're fighting against:

### Without ANSI (The Nightmare):
```python
# Print a menu
print("Menu:")
print("1. Option A")
print("2. Option B")
print("3. Option C")

# User selects option 2
# Now what? You need to show it's selected!

# Your ONLY option: Print EVERYTHING AGAIN
print("\n" * 50)  # "Clear" by pushing old content up
print("Menu:")
print("1. Option A")
print("2. ► Option B ◄")  # Show selection
print("3. Option C")
```

**Problems:**
1. Screen flickers (you see old content briefly)
2. Scroll history gets polluted
3. Can't update just one line - must reprint everything
4. Can't have persistent UI - it all scrolls away
5. Animations are impossible (every frame reprints everything)

### The Mental Model You're Missing:

**WITHOUT ANSI:** The terminal is a **printer** - text goes out, scrolls up, gone forever.
- You have ONE cursor position: the end
- You can only append
- No going back
- No editing what's already printed

**WITH ANSI:** The terminal is a **screen buffer** - like a 2D array you can edit anywhere.
- The cursor is YOUR PENCIL
- You can move it anywhere: `move(5, 10)` = "go to row 5, column 10"
- You can write at that position
- Previous content stays until you overwrite it

---

## WHY CURSOR MOVEMENT IS EVERYTHING

### The "Aha!" Moment:

```python
# WITHOUT ANSI - can't do this at all:
print("Loading: 0%")
# ... how do you update that "0%" to "10%" ???
# You can't! You have to:
print("Loading: 10%")  # Prints on NEW line
print("Loading: 20%")  # Prints on ANOTHER line
# Result: 100 lines of "Loading: X%"

# WITH ANSI - THIS is why cursor movement matters:
print("Loading: 0%", end='')
# Move cursor back 3 characters
print('\033[3D', end='')  # Cursor now BEFORE "0%"
# Overwrite with new text
print("10%", end='')  # Now it shows "Loading: 10%"
# The SAME LINE updated!
```

**Without cursor movement:** Terminal is write-only, append-only
**With cursor movement:** Terminal is a 2D editor - read, write, update anywhere

---

## THE STANDARD: VT100/ANSI ESCAPE SEQUENCES

### What Are These?

In the 1970s, DEC made the VT100 terminal - a physical screen. They needed a way to tell it:
- "Move cursor to row 5"
- "Make text red"
- "Clear the screen"

They invented **escape sequences** - special codes that mean "this is a command, not text."

### The Convention:

Every ANSI command starts with: `\033[` (or `\x1b[` or `ESC[`)
- `\033` = ASCII escape character (27)
- `[` = "here comes a command"

Then: **numbers and a letter**
- Numbers = parameters
- Letter = what action to do

### How This Equips You:

```python
# The terminal has an INVISIBLE cursor position
# Everything you print appears AT that cursor, then cursor moves right

# Normal printing:
print("Hello")  # Cursor at col 0 → prints "Hello" → cursor now at col 5

# ANSI command:
print('\033[5;10H', end='')  # Move cursor to row 5, col 10
print("X")  # Prints "X" at row 5, col 10

# Now you understand:
print('\033[1;1H')   # Top-left corner
print('\033[2J')     # Clear whole screen
print('\033[10;20H') # Row 10, col 20
print("Hello")       # Prints at that exact spot!
```

---

## THE CORE MECHANICS

### 1. The Screen Is A Grid

```
     Columns →
R  ┌─────────────────────┐
o  │ (1,1)  (1,2)  (1,3) │ ← Row 1
w  │ (2,1)  (2,2)  (2,3) │ ← Row 2
s  │ (3,1)  (3,2)  (3,3) │ ← Row 3
↓  └─────────────────────┘
```

**Without ANSI:** You can only write at the bottom, everything scrolls up.
**With ANSI:** You can write at (5, 10) or (20, 3) or anywhere.

### 2. Cursor Position Is State

```python
# The terminal REMEMBERS where the cursor is
print('\033[5;10H', end='')  # Move to (5, 10)
print('A', end='')            # Prints at (5, 10), cursor now at (5, 11)
print('B', end='')            # Prints at (5, 11), cursor now at (5, 12)

# You can query: "Where is cursor now?"
# You can save: "Remember this position"
# You can restore: "Go back to saved position"
```

### 3. Writing Overwrites

```python
# Screen shows: "Hello World"
print('\033[1;1H', end='')  # Move to start
print('X', end='')          # Screen now: "Xello World"
print('\033[1;7H', end='')  # Move to position 7
print('X', end='')          # Screen now: "Xello Xorld"
```

**This is the key:** You don't "insert" or "push" - you **overwrite** what's there.

---

## WHY THIS MATTERS FOR UI

### Scenario: Progress Bar

**Without cursor control:**
```python
for i in range(101):
    print(f"Progress: {i}%")
    time.sleep(0.1)

# Result: 101 lines printed
# Screen scrolls
# Can't see beginning
# Looks terrible
```

**With cursor control:**
```python
print("Progress: 0%", end='')
for i in range(101):
    print('\033[1G', end='')  # Move to column 1
    print(f"Progress: {i}%", end='')
    sys.stdout.flush()
    time.sleep(0.1)

# Result: ONE line, updated 100 times
# Screen stays still
# Looks professional
```

### Scenario: Live Dashboard

**Without cursor control:** Impossible. You can't update multiple areas independently.

**With cursor control:**
```python
# Initial draw
print('\033[1;1H' + "CPU: 0%")
print('\033[2;1H' + "RAM: 0%")
print('\033[3;1H' + "DISK: 0%")

# Update only CPU (line 1)
print('\033[1;6H' + "45%", end='')  # Move to position, update

# Update only RAM (line 2)
print('\033[2;6H' + "78%", end='')

# Each update is SURGICAL - only changes what needs to change
```

---

## THE INTELLECTUAL FRAMEWORK

### Mental Model 1: Terminal As Canvas

```python
# Think of it like a painting canvas
canvas = [[' ' for _ in range(80)] for _ in range(24)]  # 80x24 grid

# You have a paintbrush (cursor)
brush_row = 0
brush_col = 0

# Moving cursor = moving brush
brush_row = 5
brush_col = 10

# Printing = painting at brush position
canvas[brush_row][brush_col] = 'X'

# ANSI codes = instructions to move your brush and paint
```

### Mental Model 2: Cursor As Insertion Point

```python
# Like a text editor's blinking cursor
# When you type, text appears AT the cursor
# Cursor movement = clicking different places in the document

# ANSI gives you:
print('\033[5;10H')  # Click at row 5, col 10
print('text')        # Type "text" there

# Without ANSI:
# You can only type at the END
# Can't go back and edit middle
```

### Mental Model 3: Screen As State Machine

```python
# The terminal maintains state:
state = {
    'cursor_row': 1,
    'cursor_col': 1,
    'text_color': 'white',
    'bg_color': 'black',
    'bold': False,
    'screen_buffer': [[' ' for _ in range(80)] for _ in range(24)]
}

# ANSI codes = state mutations
'\033[5;10H'  # state['cursor_row'] = 5; state['cursor_col'] = 10
'\033[31m'    # state['text_color'] = 'red'
'\033[1m'     # state['bold'] = True

# When you print, it uses current state
print('X')  # Writes 'X' at cursor position, in current color/style
```

---

## HOW THE STANDARD EQUIPS YOU

### 1. Cursor Movement (The Foundation)

```python
'\033[{row};{col}H'     # Absolute positioning - GO HERE
'\033[{n}A'             # Relative movement - UP n lines
'\033[{n}B'             # DOWN n lines
'\033[{n}C'             # RIGHT n columns
'\033[{n}D'             # LEFT n columns
'\033[{n}E'             # Down n lines, start of line
'\033[{n}F'             # Up n lines, start of line
'\033[{col}G'           # Jump to column (same row)
'\033[H'                # Home (1,1)
```

**What this gives you:**
- Update any part of screen without redrawing everything
- Build persistent UIs that don't scroll away
- Create smooth animations
- Multi-section layouts that update independently

### 2. Screen Clearing (Surgical Deletion)

```python
'\033[2J'      # Clear entire screen
'\033[0J'      # Clear from cursor to end of screen
'\033[1J'      # Clear from cursor to beginning of screen
'\033[2K'      # Clear entire line
'\033[0K'      # Clear from cursor to end of line
'\033[1K'      # Clear from cursor to start of line
```

**What this gives you:**
- Remove content without reprinting
- Clear old data before writing new
- Implement "backspace" functionality
- Clean screen sections independently

### 3. Colors (Visual Hierarchy)

```python
'\033[31m'     # Red foreground
'\033[32m'     # Green foreground
'\033[41m'     # Red background
'\033[0m'      # Reset all

# 256 colors:
'\033[38;5;{n}m'  # Foreground (n = 0-255)
'\033[48;5;{n}m'  # Background (n = 0-255)

# True color (RGB):
'\033[38;2;{r};{g};{b}m'  # Foreground
'\033[48;2;{r};{g};{b}m'  # Background
```

**What this gives you:**
- Distinguish UI elements visually
- Show status (red=error, green=success)
- Highlight selections
- Create visual hierarchy
- Brand your interface

### 4. Text Attributes (Emphasis)

```python
'\033[1m'      # Bold
'\033[2m'      # Dim
'\033[3m'      # Italic
'\033[4m'      # Underline
'\033[7m'      # Reverse (swap fg/bg)
'\033[9m'      # Strikethrough
```

**What this gives you:**
- Emphasize important text
- Show disabled items (dim)
- Indicate focus (reverse/bold)
- Create visual variety

### 5. Cursor Visibility

```python
'\033[?25l'    # Hide cursor
'\033[?25h'    # Show cursor
```

**What this gives you:**
- Hide blinking cursor during UI updates (looks cleaner)
- Show cursor only in input fields
- Prevent visual distraction

### 6. Alternate Screen Buffer

```python
'\033[?1049h'  # Switch to alternate screen
'\033[?1049l'  # Return to main screen
```

**What this gives you:**
- Run full-screen app without disrupting terminal
- When app exits, user sees their previous session
- Like `vim` or `less` - enters, shows UI, exits, original content intact

---

## THE COMPLETE PICTURE

### Before Understanding:
"Why would I move the cursor? I just print text sequentially."

### After Understanding:
"The terminal is a 2D grid I can edit. Cursor movement lets me treat it like a screen buffer where I can update any cell at any time. This is the foundation for all interactive terminal UIs."

### The Power Unlocked:

1. **Persistent UIs** - Content doesn't scroll away
2. **Partial Updates** - Change one line without redrawing others
3. **Animations** - Update frames in place
4. **Interactive Controls** - Buttons, menus, inputs that respond
5. **Real-time Data** - Dashboards that update live
6. **Professional Look** - Smooth, flicker-free, polished

### The Pattern:

```python
# 1. Position cursor where change is needed
print(f'\033[{line};{col}H', end='')

# 2. Write new content (overwrites old)
print('new text', end='')

# 3. Flush to screen immediately
sys.stdout.flush()

# Result: Surgical update, no redraw, instant, smooth
```

---

## PRACTICAL MENTAL MODEL

Think of building UI like this:

```python
# You have a GRID (the terminal screen)
# You have a PENCIL (the cursor)
# You have INSTRUCTIONS (ANSI codes)

# Instead of:
print("line 1")  # Write, cursor moves down
print("line 2")  # Write, cursor moves down
print("line 3")  # Write, cursor moves down

# You can:
move_pencil(1, 1); write("line 1")  # Write at row 1
move_pencil(5, 10); write("line 2") # Write at row 5
move_pencil(2, 5); write("line 3")  # Write at row 2

# Order doesn't matter! Position is explicit!
# You can go back and change line 1 after writing line 5!
```

### The "Video Game" Analogy:

```python
# Terminal = Your game screen (640x480 pixels)
# Cursor = Your sprite position (x, y)
# ANSI = Moving your sprite and drawing

# Frame 1:
move_sprite(100, 100)
draw("●")

# Frame 2:
move_sprite(100, 100)
draw(" ")  # Clear old position
move_sprite(110, 100)
draw("●")  # New position

# Result: Sprite moves across screen
# Same concept in terminal with ANSI
```

---

## WHY YOU COULDN'T CONCEIVE IT

The terminal LOOKS like a typewriter:
- Type → text appears → cursor advances
- Hit enter → go to next line
- Repeat

But it's actually a **programmable display device**:
- It has RAM (the screen buffer)
- It has a cursor (x, y position)
- It accepts commands (ANSI codes)
- You can read/write any position

**The missing piece:** You thought terminal = "stream of text"
**Reality:** Terminal = "addressable character grid"

Once you get that, everything clicks:
- Cursor movement = accessing different grid positions
- Colors = metadata for each cell
- Clearing = writing spaces to ranges of cells
- Your UI = strategic writes to specific grid coordinates

---

## ANSI ESCAPE CODES - Quick Reference

```python
# CURSOR MOVEMENT
f'\033[{line};{col}H'    # Move to position (1-based)
'\033[H'                 # Move to home (0,0)
'\033[2J'                # Clear entire screen
'\033[K'                 # Clear line from cursor to end

# COLORS
'\033[31m'               # Red foreground
'\033[32m'               # Green foreground
'\033[33m'               # Yellow foreground
'\033[34m'               # Blue foreground
'\033[91m'               # Bright red
'\033[92m'               # Bright green

'\033[41m'               # Red background
'\033[42m'               # Green background

f'\033[38;2;{r};{g};{b}m'  # RGB foreground (0-255 each)
f'\033[48;2;{r};{g};{b}m'  # RGB background

# STYLES
'\033[1m'                # Bold
'\033[2m'                # Dim
'\033[3m'                # Italic
'\033[4m'                # Underline
'\033[7m'                # Reverse (swap fg/bg)

# RESET
'\033[0m'                # Reset all styles
```

---

## PATH 1: STATIC UI → Set Once

```python
ui = UI(width=50, height=20)

# Build your UI by index
ui[0] = "═" * 50
ui[1] = "Header".center(50)
ui[2] = "═" * 50
ui[5] = "  Content here"
ui[19] = "[OK]".center(50)
```

**Use Case:** Menus, forms, dialogs that don't change after rendering.

---

## PATH 2: DYNAMIC UPDATE → Change Over Time

```python
ui = UI(50, 20)

# Initial state
ui[5] = "Status: Waiting..."

# Update later (only line 5 redraws)
ui[5] = "Status: Processing..."
ui[5] = "Status: Complete!"
```

**Use Case:** Status messages, progress indicators, live data displays.

### Example: Progress Bar

```python
ui = UI(60, 10)
ui[5] = "Progress: [" + " " * 30 + "]"

for i in range(30):
    # Build the bar
    bar = "█" * i + " " * (30 - i)
    ui[5] = f"Progress: [{bar}] {i*3}%"
    time.sleep(0.1)
```

---

## PATH 3: CELL-LEVEL UPDATE → Single Character Changes

**Problem:** Updating a whole line to change one character wastes time.

**Solution:** Update only the cell that changed.

```python
class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lines = [' ' * width] * height
        os.system('')
        print('\033[2J\033[H', end='')
    
    def __setitem__(self, line, text):
        self.lines[line] = text[:self.width].ljust(self.width)
        print(f'\033[{line+1};1H' + text[:self.width].ljust(self.width), end='')
        sys.stdout.flush()
    
    def set_cell(self, line, col, text):
        """Update single cell - instant!"""
        print(f'\033[{line+1};{col+1}H' + text, end='')
        sys.stdout.flush()
```

**Use Case:** Typing animation, cursor movement, single character highlights.

### Example: Typing Effect

```python
ui = UI(50, 10)
ui[5] = " " * 50

text = "Hello, World!"
for i, char in enumerate(text):
    ui.set_cell(5, i, char)
    time.sleep(0.1)
```

---

## PATH 4: STYLED UPDATES → Colors & Emphasis

```python
class UI:
    # ... previous code ...
    
    def __setitem__(self, line, text, style=''):
        """Now supports style parameter"""
        self.lines[line] = text[:self.width].ljust(self.width)
        print(f'\033[{line+1};1H' + style + text[:self.width].ljust(self.width) + '\033[0m', end='')
        sys.stdout.flush()
```

**Usage:**

```python
ui = UI(50, 20)

# Styled headers
ui[0] = ("═" * 50, '\033[36m\033[1m')  # Cyan + Bold

# Status with colors
ui[5] = ("Status: ERROR", '\033[31m')   # Red
ui[6] = ("Status: OK", '\033[32m')      # Green

# Highlighted text
ui[10] = ("IMPORTANT!", '\033[7m')      # Reverse video
```

---

## PATH 5: RESPONSIVE → React to Size Changes

**Goal:** UI adapts when terminal size changes.

```python
import shutil

class ResponsiveUI:
    def __init__(self):
        self.update_size()
        os.system('')
        print('\033[2J\033[H', end='')
    
    def update_size(self):
        """Get current terminal size"""
        self.width, self.height = shutil.get_terminal_size()
        self.lines = [' ' * self.width] * self.height
    
    def __setitem__(self, line, text):
        if line >= self.height:
            return  # Ignore if too tall
        self.lines[line] = text[:self.width].ljust(self.width)
        print(f'\033[{line+1};1H' + text[:self.width].ljust(self.width), end='')
        sys.stdout.flush()
    
    def redraw_on_resize(self):
        """Call this when terminal resizes"""
        old_width = self.width
        self.update_size()
        
        if self.width != old_width:
            # Re-center content
            for i, line in enumerate(self.lines):
                self[i] = line.strip().center(self.width)
```

**Usage:**

```python
ui = ResponsiveUI()

# Content auto-centers
ui[1] = "Header".center(ui.width)
ui[5] = "Content".center(ui.width)

# On resize (manual trigger for now)
# ui.redraw_on_resize()
```

---

## PATH 6: EVENT-DRIVEN → React to Input

**Goal:** Update UI based on user actions.

```python
import sys
import tty
import termios

class InteractiveUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lines = [' ' * width] * height
        self.cursor_line = 0
        os.system('')
        print('\033[2J\033[H\033[?25l', end='')  # Hide cursor
    
    def __setitem__(self, line, text):
        self.lines[line] = text[:self.width].ljust(self.width)
        print(f'\033[{line+1};1H' + text[:self.width].ljust(self.width), end='')
        sys.stdout.flush()
    
    def highlight_line(self, line):
        """Highlight a line (selection indicator)"""
        text = self.lines[line]
        print(f'\033[{line+1};1H\033[7m' + text + '\033[0m', end='')
        sys.stdout.flush()
    
    def unhighlight_line(self, line):
        """Remove highlight"""
        text = self.lines[line]
        print(f'\033[{line+1};1H' + text, end='')
        sys.stdout.flush()
    
    def get_key(self):
        """Get single keypress (Unix/Linux)"""
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
    
    def move_cursor(self, direction):
        """Move selection up/down"""
        self.unhighlight_line(self.cursor_line)
        
        if direction == 'up' and self.cursor_line > 0:
            self.cursor_line -= 1
        elif direction == 'down' and self.cursor_line < self.height - 1:
            self.cursor_line += 1
        
        self.highlight_line(self.cursor_line)
```

**Usage:**

```python
ui = InteractiveUI(50, 10)

# Build menu
ui[0] = "  Option 1"
ui[1] = "  Option 2"
ui[2] = "  Option 3"

ui.highlight_line(0)  # Start at first option

while True:
    key = ui.get_key()
    
    if key == 'w':
        ui.move_cursor('up')
    elif key == 's':
        ui.move_cursor('down')
    elif key == '\r':  # Enter
        selected = ui.cursor_line
        break
    elif key == 'q':
        break

print(f'\033[?25h')  # Show cursor
print(f"\nYou selected: {selected}")
```

---

## PATH 7: COMPONENT-BASED → Reusable Pieces

```python
class Component:
    """Base class for UI components"""
    def __init__(self, ui, line, col, width):
        self.ui = ui
        self.line = line
        self.col = col
        self.width = width
    
    def render(self):
        """Override in subclasses"""
        pass

class Button(Component):
    def __init__(self, ui, line, col, label):
        super().__init__(ui, line, col, len(label) + 4)
        self.label = label
        self.focused = False
    
    def render(self):
        style = '\033[7m' if self.focused else ''
        text = f"[ {self.label} ]"
        # Position at specific column
        self.ui[self.line] = " " * self.col + style + text + '\033[0m'
    
    def focus(self):
        self.focused = True
        self.render()
    
    def unfocus(self):
        self.focused = False
        self.render()

class InputField(Component):
    def __init__(self, ui, line, col, width, label):
        super().__init__(ui, line, col, width)
        self.label = label
        self.value = ""
    
    def render(self):
        display = f"{self.label}: [{self.value.ljust(self.width - len(self.label) - 4)}]"
        self.ui[self.line] = " " * self.col + display
    
    def add_char(self, char):
        if len(self.value) < self.width - len(self.label) - 4:
            self.value += char
            self.render()
```

**Usage:**

```python
ui = UI(60, 20)

# Create components
username = InputField(ui, 5, 5, 40, "Username")
password = InputField(ui, 7, 5, 40, "Password")
submit_btn = Button(ui, 10, 20, "Submit")

# Render all
username.render()
password.render()
submit_btn.render()

# Update dynamically
username.add_char('j')
username.add_char('o')
username.add_char('h')
username.add_char('n')

submit_btn.focus()  # Highlights the button
```

---

## PATH 8: STATE MANAGEMENT → Data-Driven UI

```python
class StatefulUI:
    """UI that auto-updates when state changes"""
    
    def __init__(self, width, height):
        self.ui = UI(width, height)
        self.state = {}
        self.bindings = {}  # line -> state_key
    
    def bind(self, line, state_key, formatter):
        """Bind a line to a state value"""
        self.bindings[line] = (state_key, formatter)
    
    def set_state(self, key, value):
        """Update state and auto-refresh bound lines"""
        self.state[key] = value
        
        # Find all lines bound to this key
        for line, (state_key, formatter) in self.bindings.items():
            if state_key == key:
                self.ui[line] = formatter(value)
    
    def get_state(self, key):
        return self.state.get(key)
```

**Usage:**

```python
ui = StatefulUI(50, 20)

# Bind UI lines to state
ui.bind(5, 'count', lambda v: f"Count: {v}")
ui.bind(7, 'status', lambda v: f"Status: {v}")
ui.bind(9, 'progress', lambda v: f"Progress: {'█' * v}{'░' * (20-v)}")

# Now updating state auto-updates UI!
ui.set_state('count', 0)
ui.set_state('status', 'Idle')
ui.set_state('progress', 0)

# Simulate updates
for i in range(21):
    ui.set_state('count', i)
    ui.set_state('progress', i)
    ui.set_state('status', 'Processing...' if i < 20 else 'Done!')
    time.sleep(0.1)
```

---

## PATH 9: LAYOUT SYSTEM → Auto-Positioning

```python
class Layout:
    """Automatic component positioning"""
    
    def __init__(self, ui):
        self.ui = ui
        self.current_line = 0
        self.components = []
    
    def add(self, component, spacing=1):
        """Add component and auto-position it"""
        component.line = self.current_line
        component.render()
        self.components.append(component)
        self.current_line += spacing
    
    def center_all(self):
        """Center all components horizontally"""
        for comp in self.components:
            # Re-render centered
            pass

class VBox(Layout):
    """Vertical stacking"""
    pass

class HBox(Layout):
    """Horizontal arrangement"""
    def __init__(self, ui, line):
        self.ui = ui
        self.line = line
        self.current_col = 0
    
    def add(self, component, spacing=2):
        component.line = self.line
        component.col = self.current_col
        component.render()
        self.current_col += component.width + spacing
```

**Usage:**

```python
ui = UI(80, 30)
layout = VBox(ui)

# Just add components, positioning is automatic
layout.add(Button(ui, 0, 0, "Start"))
layout.add(Button(ui, 0, 0, "Stop"))
layout.add(Button(ui, 0, 0, "Exit"))

# Horizontal layout
hbox = HBox(ui, 10)
hbox.add(Button(ui, 0, 0, "Yes"))
hbox.add(Button(ui, 0, 0, "No"))
hbox.add(Button(ui, 0, 0, "Cancel"))
```

---

## PATH 10: FULL APPLICATION → Putting It Together

```python
class App:
    """Complete application framework"""
    
    def __init__(self):
        self.ui = ResponsiveUI()
        self.state = {}
        self.components = []
        self.focused = 0
        self.running = True
    
    def render(self):
        """Render all components"""
        for comp in self.components:
            comp.render()
    
    def handle_key(self, key):
        """Route key to focused component or app"""
        if key == '\t':  # Tab to next component
            self.components[self.focused].unfocus()
            self.focused = (self.focused + 1) % len(self.components)
            self.components[self.focused].focus()
        elif key == 'q':
            self.running = False
        else:
            # Send to focused component
            self.components[self.focused].handle_key(key)
    
    def run(self):
        """Main loop"""
        self.render()
        
        while self.running:
            key = self.get_key()  # Blocking read
            self.handle_key(key)
        
        self.cleanup()
```

**Usage:**

```python
app = App()

# Add components
app.components.append(InputField(app.ui, 5, 5, 40, "Name"))
app.components.append(InputField(app.ui, 7, 5, 40, "Email"))
app.components.append(Button(app.ui, 10, 20, "Submit"))

# Run
app.run()
```

---

## PROGRESSIVE LEARNING PATH

1. **Start:** `ui[5] = "text"` - Learn indexing
2. **Then:** Update lines dynamically - See changes happen
3. **Then:** Add colors with ANSI - Make it visual
4. **Then:** Cell-level updates - Optimize performance
5. **Then:** React to input - Make it interactive
6. **Then:** Build components - Make it reusable
7. **Then:** Add state - Make it data-driven
8. **Then:** Create layouts - Make it structured
9. **Finally:** Build full app - Put it all together

---

## KEY PRINCIPLES

1. **Update only what changed** - Don't redraw everything
2. **Use ANSI for positioning** - Direct cursor control
3. **Separate state from display** - Change data, UI updates
4. **Build from components** - Compose complex from simple
5. **Handle events reactively** - UI responds to actions

---

## PERFORMANCE TIPS

```python
# SLOW - Rebuilding whole UI
for i in range(100):
    ui[5] = f"Count: {i}"
    print(ui)  # Reprints all 20 lines

# FAST - Update one line
for i in range(100):
    ui[5] = f"Count: {i}"  # Only updates line 5

# FASTEST - Update one cell
for i in range(100):
    ui.set_cell(5, 7, str(i))  # Only updates changed digits
```

---

## WINDOWS COMPATIBILITY

```python
import os
import sys

# Enable ANSI on Windows
if sys.platform == 'win32':
    os.system('')  # Magic line that enables ANSI

# Or use colorama
from colorama import init
init()  # Now ANSI works on Windows
```

---

## NEXT STEPS

- **Read input without blocking:** `select`, `msvcrt`, or threading
- **Handle terminal resize:** Catch `SIGWINCH` signal
- **Add mouse support:** ANSI mouse tracking codes
- **Build themes:** Color scheme management
- **Add animations:** Frame-by-frame updates
- **Create widgets library:** Dropdown, checkbox, radio, tabs
- **Implement focus management:** Tab order, keyboard navigation
- **Add validation:** Real-time field checking
- **Build layouts:** Grid, flexbox-like systems
- **State persistence:** Save/load app state
