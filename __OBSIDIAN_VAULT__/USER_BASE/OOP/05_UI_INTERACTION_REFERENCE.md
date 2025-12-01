# UI / Interaction Classes Reference

## Overview
Classes for building user interfaces and handling user interaction in console or GUI applications.

---

## 1. MENU CLASS

### Purpose
Represents a menu or navigation structure with options, choices, and commands.

### When to Use
- Building CLI applications with menu systems
- Navigation interfaces
- Command dispatchers
- Interactive wizards

### Class Anatomy

#### Instance Attributes
- `title` (str) - Menu display title
- `options` (list) - Available menu options
- `_handlers` (dict) - Maps choices to handler functions
- `_running` (bool) - Menu loop state

#### Instance Methods
- `add_option(key, label, handler)` - Register a menu option
- `display()` - Show menu to user
- `get_choice()` - Get and validate user input
- `run()` - Execute the menu loop
- `exit()` - Stop the menu loop

#### Special Methods (Dunders)
- `__init__(title)` - Initialize menu with title
- `__str__()` - String representation for debugging
- `__len__()` - Return number of options

### Complete Example

```python
class Menu:
    """A console menu with numbered options."""
    
    def __init__(self, title):
        """Initialize menu with a title.
        
        Args:
            title: Display title for the menu
        """
        self.title = title
        self.options = []  # list of (key, label) tuples
        self._handlers = {}  # dict mapping keys to handler functions
        self._running = False
    
    def add_option(self, key, label, handler):
        """Add a menu option with handler.
        
        Args:
            key: The key/number user presses
            label: Display label for the option
            handler: Function to call when selected
            
        Returns:
            Self for method chaining
        """
        self.options.append((key, label))
        self._handlers[key] = handler
        return self
    
    def display(self) -> None:
        """Display the menu to console."""
        print(f"\n{'=' * 50}")
        print(f"  {self.title}")
        print(f"{'=' * 50}")
        for key, label in self.options:
            print(f"  {key}. {label}")
        print(f"{'=' * 50}")
    
    def get_choice(self) -> str:
        """Get and validate user choice.
        
        Returns:
            Valid menu choice key
        """
        valid_keys = {key for key, _ in self.options}
        while True:
            choice = input("Enter choice: ").strip()
            if choice in valid_keys:
                return choice
            print(f"Invalid choice. Please enter one of: {', '.join(valid_keys)}")
    
    def run(self) -> None:
        """Run the menu loop."""
        self._running = True
        while self._running:
            self.display()
            choice = self.get_choice()
            handler = self._handlers.get(choice)
            if handler:
                handler()
    
    def exit(self) -> None:
        """Stop the menu loop."""
        self._running = False
    
    def __str__(self) -> str:
        return f"Menu('{self.title}', {len(self.options)} options)"
    
    def __len__(self) -> int:
        return len(self.options)


# Usage Example
def new_game():
    print("Starting new game...")

def load_game():
    print("Loading game...")

def settings():
    print("Opening settings...")

# Create and configure menu
main_menu = Menu("MAIN MENU")
main_menu.add_option("1", "New Game", new_game)
main_menu.add_option("2", "Load Game", load_game)
main_menu.add_option("3", "Settings", settings)
main_menu.add_option("4", "Exit", main_menu.exit)

# Run menu
main_menu.run()
```

### Advanced Pattern: Nested Menus

```python
class Menu:
    # ... (previous implementation)
    
    def add_submenu(self, key, label, submenu):
        """Add a submenu option.
        
        Args:
            key: Menu key
            label: Display label
            submenu: Another Menu instance
            
        Returns:
            Self for chaining
        """
        def run_submenu():
            submenu.run()
        
        return self.add_option(key, label, run_submenu)


# Usage
settings_menu = Menu("SETTINGS")
settings_menu.add_option("1", "Audio", lambda: print("Audio settings"))
settings_menu.add_option("2", "Video", lambda: print("Video settings"))
settings_menu.add_option("3", "Back", settings_menu.exit)

main_menu = Menu("MAIN MENU")
main_menu.add_submenu("3", "Settings", settings_menu)
```

---

## 2. WIDGET / ELEMENT CLASS

### Purpose
Represents a specific UI element (button, input field, panel, card) with state and behavior.

### When to Use
- Building reusable UI components
- GUI applications
- Console UI libraries
- Game interfaces

### Class Anatomy

#### Instance Attributes
- `id` (str) - Unique widget identifier
- `parent` (Widget) - Parent widget in hierarchy
- `children` (list) - Child widgets
- `visible` (bool) - Visibility state
- `enabled` (bool) - Interaction enabled/disabled
- `bounds` (tuple) - Position and size (x, y, width, height)

#### Instance Methods
- `render()` - Draw the widget
- `update(delta_time)` - Update widget state
- `handle_event(event)` - Process user events
- `add_child(widget)` - Add child widget
- `remove_child(widget)` - Remove child
- `show()` / `hide()` - Control visibility

#### Special Methods
- `__init__(id, bounds)` - Initialize widget
- `__repr__()` - Debug representation

### Complete Example

```python
class Widget:
    """Base class for UI widgets."""
    
    def __init__(self, id, bounds):
        """Initialize widget.
        
        Args:
            id: Unique widget identifier
            bounds: (x, y, width, height) tuple
        """
        self.id = id
        self.bounds = bounds  # (x, y, width, height)
        self.parent = None
        self.children = []
        self.visible = True
        self.enabled = True
    
    def add_child(self, widget):
        """Add a child widget."""
        widget.parent = self
        self.children.append(widget)
    
    def remove_child(self, widget):
        """Remove a child widget."""
        if widget in self.children:
            widget.parent = None
            self.children.remove(widget)
    
    def show(self):
        """Make widget visible."""
        self.visible = True
    
    def hide(self):
        """Hide widget."""
        self.visible = False
    
    def render(self):
        """Render the widget. Should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement render()")
    
    def update(self, delta_time):
        """Update widget state.
        
        Args:
            delta_time: Time since last update
        """
        for child in self.children:
            if child.visible:
                child.update(delta_time)
    
    def handle_event(self, event):
        """Handle input event.
        
        Args:
            event: Event dictionary with type and data
            
        Returns:
            True if event was handled
        """
        # Children handle events first (reverse order for top-to-bottom)
        for child in reversed(self.children):
            if child.visible and child.enabled:
                if child.handle_event(event):
                    return True
        return False
    
    def __repr__(self):
        return f"{self.__class__.__name__}(id='{self.id}')"


class Button(Widget):
    """A clickable button widget."""
    
    def __init__(self, id, bounds, label, on_click):
        super().__init__(id, bounds)
        self.label = label
        self.on_click = on_click
        self.pressed = False
    
    def render(self):
        """Render the button."""
        if not self.visible:
            return
        
        x, y, w, h = self.bounds
        border = "##" if self.pressed else "=="
        
        print(f"  {border * (w // 2)}")
        print(f"  | {self.label.center(w - 4)} |")
        print(f"  {border * (w // 2)}")
    
    def handle_event(self, event):
        """Handle button click."""
        if not self.enabled:
            return False
        
        if event.get('type') == 'click':
            x, y, w, h = self.bounds
            click_x, click_y = event.get('pos', (0, 0))
            
            if x <= click_x <= x + w and y <= click_y <= y + h:
                self.pressed = True
                self.on_click()
                self.pressed = False
                return True
        
        return super().handle_event(event)


class Panel(Widget):
    """A container panel widget."""
    
    def __init__(self, id, bounds, title=""):
        super().__init__(id, bounds)
        self.title = title
    
    def render(self):
        """Render the panel and its children."""
        if not self.visible:
            return
        
        x, y, w, h = self.bounds
        print(f"\n┌{'─' * (w - 2)}┐")
        if self.title:
            print(f"│ {self.title.ljust(w - 4)} │")
            print(f"├{'─' * (w - 2)}┤")
        
        for child in self.children:
            child.render()
        
        print(f"└{'─' * (w - 2)}┘")


# Usage Example
def on_start_click():
    print("Game started!")

def on_quit_click():
    print("Goodbye!")

# Create UI hierarchy
main_panel = Panel("main", (0, 0, 40, 20), "Game Menu")

start_btn = Button("start", (10, 5, 20, 3), "Start Game", on_start_click)
quit_btn = Button("quit", (10, 10, 20, 3), "Quit", on_quit_click)

main_panel.add_child(start_btn)
main_panel.add_child(quit_btn)

# Render
main_panel.render()

# Simulate click
main_panel.handle_event({'type': 'click', 'pos': (15, 6)})
```

---

## 3. SCREEN / PAGE CLASS

### Purpose
Represents a complete view/screen composed of multiple widgets or elements.

### When to Use
- Full application screens
- Multi-screen applications
- Game states (menu screen, game screen, settings screen)
- Wizard steps

### Class Anatomy

#### Instance Attributes
- `name` (str) - Screen identifier
- `widgets` (dict) - Named widget registry
- `active` (bool) - Is screen currently active
- `_transitions` (dict) - Screen transition rules

#### Instance Methods
- `on_enter()` - Called when screen becomes active
- `on_exit()` - Called when screen becomes inactive
- `on_update(dt)` - Update screen logic
- `on_render()` - Render all widgets
- `transition_to(screen_name)` - Navigate to another screen

#### Special Methods
- `__init__(name)` - Initialize screen
- `__enter__()` / `__exit__()` - Context manager support

### Complete Example

```python
class Screen:
    """Base class for application screens."""
    
    def __init__(self, name):
        """Initialize screen.
        
        Args:
            name: Unique screen identifier
        """
        self.name = name
        self.widgets = {}  # dict mapping widget IDs to widget objects
        self.active = False
        self._on_transition = None
    
    def add_widget(self, widget):
        """Add a widget to the screen."""
        self.widgets[widget.id] = widget
    
    def remove_widget(self, widget_id):
        """Remove a widget from the screen."""
        self.widgets.pop(widget_id, None)
    
    def on_enter(self):
        """Called when screen becomes active."""
        self.active = True
        print(f"[Screen] Entering: {self.name}")
    
    def on_exit(self):
        """Called when screen becomes inactive."""
        self.active = False
        print(f"[Screen] Exiting: {self.name}")
    
    def on_update(self, delta_time):
        """Update screen logic.
        
        Args:
            delta_time: Time since last update
        """
        for widget in self.widgets.values():
            widget.update(delta_time)
    
    def on_render(self):
        """Render the screen. Should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement on_render()")
    
    def handle_event(self, event):
        """Handle input events.
        
        Args:
            event: Event data
            
        Returns:
            True if event was handled
        """
        for widget in self.widgets.values():
            if widget.handle_event(event):
                return True
        return False
    
    def transition_to(self, screen_name):
        """Request transition to another screen.
        
        Args:
            screen_name: Target screen name
        """
        if self._on_transition:
            self._on_transition(screen_name)
    
    def set_transition_handler(self, handler):
        """Set the screen transition handler."""
        self._on_transition = handler
    
    def __enter__(self):
        """Context manager entry."""
        self.on_enter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.on_exit()


class MainMenuScreen(Screen):
    """Main menu screen implementation."""
    
    def __init__(self):
        super().__init__("main_menu")
        
        # Create UI
        panel = Panel("menu_panel", (0, 0, 50, 25), "MAIN MENU")
        
        start_btn = Button(
            "start", (15, 8, 20, 3), 
            "Start Game", 
            lambda: self.transition_to("game")
        )
        
        settings_btn = Button(
            "settings", (15, 12, 20, 3),
            "Settings",
            lambda: self.transition_to("settings")
        )
        
        quit_btn = Button(
            "quit", (15, 16, 20, 3),
            "Quit",
            lambda: self.transition_to("exit")
        )
        
        panel.add_child(start_btn)
        panel.add_child(settings_btn)
        panel.add_child(quit_btn)
        
        self.add_widget(panel)
    
    def on_render(self) -> None:
        """Render the main menu."""
        print("\n" * 2)
        for widget in self.widgets.values():
            widget.render()


class GameScreen(Screen):
    """Game screen implementation."""
    
    def __init__(self):
        super().__init__("game")
        self.score = 0
    
    def on_enter(self) -> None:
        """Initialize game state."""
        super().on_enter()
        self.score = 0
    
    def on_update(self, delta_time: float) -> None:
        """Update game logic."""
        super().on_update(delta_time)
        # Game logic here
    
    def on_render(self) -> None:
        """Render game state."""
        print(f"\n=== GAME ===")
        print(f"Score: {self.score}")
        print("(Press ESC to return to menu)")


# Screen Manager
class ScreenManager:
    """Manages screen transitions."""
    
    def __init__(self):
        self.screens = {}  # dict mapping screen names to Screen objects
        self.current_screen = None
    
    def add_screen(self, screen):
        """Register a screen."""
        screen.set_transition_handler(self.transition_to)
        self.screens[screen.name] = screen
    
    def transition_to(self, screen_name):
        """Transition to a different screen."""
        if screen_name == "exit":
            if self.current_screen:
                self.current_screen.on_exit()
            return
        
        new_screen = self.screens.get(screen_name)
        if not new_screen:
            print(f"Screen not found: {screen_name}")
            return
        
        if self.current_screen:
            self.current_screen.on_exit()
        
        self.current_screen = new_screen
        self.current_screen.on_enter()
    
    def update(self, delta_time):
        """Update current screen."""
        if self.current_screen and self.current_screen.active:
            self.current_screen.on_update(delta_time)
    
    def render(self):
        """Render current screen."""
        if self.current_screen and self.current_screen.active:
            self.current_screen.on_render()


# Usage
manager = ScreenManager()
manager.add_screen(MainMenuScreen())
manager.add_screen(GameScreen())

manager.transition_to("main_menu")
manager.render()
```

---

## 4. DIALOG / POPUP CLASS

### Purpose
Temporary UI overlay with its own logic and state, typically for focused user interactions.

### When to Use
- Confirmation dialogs
- Input prompts
- Error messages
- Modal windows

### Class Anatomy

#### Instance Attributes
- `title` (str) - Dialog title
- `message` (str) - Dialog content
- `buttons` (list) - Available buttons
- `result` (any) - User's choice/input
- `modal` (bool) - Blocks interaction with other UI

#### Instance Methods
- `show()` - Display the dialog
- `close(result)` - Close with result
- `add_button(label, value)` - Add button option
- `get_result()` - Retrieve user response

#### Special Methods
- `__init__(title, message)` - Initialize dialog
- `__enter__()` / `__exit__()` - Context manager

### Complete Example

```python
# Standard dialog result constants
DIALOG_OK = "ok"
DIALOG_CANCEL = "cancel"
DIALOG_YES = "yes"
DIALOG_NO = "no"
DIALOG_RETRY = "retry"
DIALOG_ABORT = "abort"

class Dialog:
    """Modal dialog/popup window."""
    
    def __init__(self, title, message, modal=True):
        """Initialize dialog.
        
        Args:
            title: Dialog title
            message: Main message/question
            modal: If True, blocks other interaction
        """
        self.title = title
        self.message = message
        self.modal = modal
        self.buttons = []  # list of (label, value) tuples
        self.result = None
        self._visible = False
    
    def add_button(self, label, value=None):
        """Add a button with result value.
        
        Args:
            label: Button text
            value: Value to return when clicked
            
        Returns:
            Self for chaining
        """
        if value is None:
            value = label.lower()
        self.buttons.append((label, value))
        return self
    
    def show(self):
        """Display dialog and wait for user response.
        
        Returns:
            Selected button value or None if cancelled
        """
        self._visible = True
        self._render()
        
        # Get user choice
        choice = self._get_choice()
        self.result = choice
        
        self._visible = False
        return self.result
    
    def close(self, result=None):
        """Close dialog with result.
        
        Args:
            result: Value to return
        """
        self.result = result
        self._visible = False
    
    def _render(self):
        """Render the dialog."""
        width = max(len(self.title), len(self.message), 40) + 4
        
        print("\n")
        print("┌" + "─" * (width - 2) + "┐")
        print("│ " + self.title.center(width - 4) + " │")
        print("├" + "─" * (width - 2) + "┤")
        print("│ " + self.message.ljust(width - 4) + " │")
        print("├" + "─" * (width - 2) + "┤")
        
        # Show buttons
        for idx, (label, _) in enumerate(self.buttons, 1):
            print(f"│ {idx}. {label.ljust(width - 7)} │")
        
        print("└" + "─" * (width - 2) + "┘")
    
    def _get_choice(self):
        """Get user button choice.
        
        Returns:
            Selected button value
        """
        while True:
            try:
                choice = input("Select option: ").strip()
                idx = int(choice) - 1
                
                if 0 <= idx < len(self.buttons):
                    return self.buttons[idx][1]
                else:
                    print(f"Please enter 1-{len(self.buttons)}")
            except ValueError:
                print("Please enter a number")
    
    def __enter__(self):
        """Context manager entry - show dialog."""
        return self.show()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close dialog."""
        if self._visible:
            self.close()


# Convenience Functions
def show_message(title, message):
    """Show an informational message."""
    dialog = Dialog(title, message)
    dialog.add_button("OK", DIALOG_OK)
    dialog.show()

def show_confirmation(title, message):
    """Show yes/no confirmation.
    
    Returns:
        True if user selected Yes
    """
    dialog = Dialog(title, message)
    dialog.add_button("Yes", DIALOG_YES)
    dialog.add_button("No", DIALOG_NO)
    result = dialog.show()
    return result == DIALOG_YES

def show_error(title, message):
    """Show error message."""
    dialog = Dialog(f"ERROR: {title}", message)
    dialog.add_button("OK", DIALOG_OK)
    dialog.show()

def prompt_input(title, prompt):
    """Prompt for text input.
    
    Returns:
        User input or None if cancelled
    """
    print(f"\n=== {title} ===")
    print(prompt)
    response = input("> ").strip()
    return response if response else None


# Usage Examples
if __name__ == "__main__":
    # Simple message
    show_message("Welcome", "Welcome to the application!")
    
    # Confirmation
    if show_confirmation("Delete File", "Are you sure you want to delete this file?"):
        print("File deleted!")
    else:
        print("Cancelled")
    
    # Custom dialog
    dialog = Dialog("Save Changes", "Do you want to save your changes?")
    dialog.add_button("Save", "save")
    dialog.add_button("Don't Save", "nosave")
    dialog.add_button("Cancel", "cancel")
    
    result = dialog.show()
    
    if result == "save":
        print("Saving...")
    elif result == "nosave":
        print("Discarding changes...")
    else:
        print("Cancelled")
    
    # Input prompt
    name = prompt_input("User Info", "Enter your name:")
    if name:
        print(f"Hello, {name}!")
    
    # Context manager usage
    with Dialog("Processing", "Operation complete!") as result:
        # Dialog automatically shows and closes
        pass
```

---

## COMPARISON SUMMARY

| Class | Scope | Duration | Primary Use |
|-------|-------|----------|-------------|
| Menu | Navigation structure | Persistent | Command selection |
| Widget | Single UI element | Persistent | Reusable components |
| Screen | Full view | Persistent | Application states |
| Dialog | Focused interaction | Temporary | User prompts |

## TYPICAL COMBINATIONS

```
Application
  └─ ScreenManager
      ├─ MainMenuScreen
      │   └─ Menu (navigation)
      ├─ GameScreen
      │   ├─ Widget (health bar)
      │   ├─ Widget (score display)
      │   └─ Dialog (pause menu)
      └─ SettingsScreen
          └─ Widget (option controls)
```

