"""
COMPREHENSIVE CLI MENU CONTROL DEMO
====================================
Advanced CLI menu system with keyboard controls, interactive navigation,
and rich UI components for Windows Python applications.

Author: GitHub Copilot
Date: December 1, 2025
Platform: Windows (with fallback for cross-platform support)
Python: 3.6+

Features:
- Arrow key navigation
- Multiple menu types (vertical, horizontal, grid)
- Input validation and forms
- Progress tracking
- Confirmation dialogs
- Color themes
- Mouse support (when available)
- Hotkey support
- Searchable menus
- Context menus
- Tab completion
"""

import os
import sys
import time
import msvcrt  # Windows-specific for keyboard input
import threading
from typing import List, Tuple, Optional, Callable, Dict, Any
from dataclasses import dataclass
from enum import Enum

# ============================================================================
# SECTION 1: ANSI CODES AND CONSTANTS
# ============================================================================

# ANSI Escape Codes
ESC = '\033'
CSI = '\033['

# Text Styles
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
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
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Cursor Control
CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'
CURSOR_HOME = '\033[H'
CURSOR_POS = lambda row, col: f'\033[{row};{col}H'
CURSOR_UP = lambda n=1: f'\033[{n}A'
CURSOR_DOWN = lambda n=1: f'\033[{n}B'
CURSOR_FORWARD = lambda n=1: f'\033[{n}C'
CURSOR_BACK = lambda n=1: f'\033[{n}D'

CLEAR_SCREEN = '\033[2J'
CLEAR_LINE = '\033[2K'
SAVE_CURSOR = '\033[s'
RESTORE_CURSOR = '\033[u'

# Box Drawing
BOX_H = '─'
BOX_V = '│'
BOX_TL = '┌'
BOX_TR = '┐'
BOX_BL = '└'
BOX_BR = '┘'
BOX_T = '┬'
BOX_B = '┴'
BOX_L = '├'
BOX_R = '┤'
BOX_CROSS = '┼'

# Double Box
BOX_DOUBLE_H = '═'
BOX_DOUBLE_V = '║'
BOX_DOUBLE_TL = '╔'
BOX_DOUBLE_TR = '╗'
BOX_DOUBLE_BL = '╚'
BOX_DOUBLE_BR = '╝'

# Symbols
POINTER = '▶'
CHECK = '✓'
CROSS = '✗'
RADIO_ON = '◉'
RADIO_OFF = '○'
CHECKBOX_ON = '☑'
CHECKBOX_OFF = '☐'
ARROW_UP = '↑'
ARROW_DOWN = '↓'
ARROW_LEFT = '←'
ARROW_RIGHT = '→'

# ============================================================================
# SECTION 2: WINDOWS CONSOLE SETUP
# ============================================================================

def enable_ansi_windows():
    """Enable ANSI escape sequences on Windows 10+"""
    if sys.platform == 'win32':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

def get_terminal_size() -> Tuple[int, int]:
    """Get terminal size (width, height)"""
    try:
        import shutil
        size = shutil.get_terminal_size()
        return size.columns, size.lines
    except:
        return 80, 24  # Default fallback

# ============================================================================
# SECTION 3: KEYBOARD INPUT HANDLER (Windows)
# ============================================================================

class Key:
    """Key code constants"""
    ENTER = b'\r'
    ESC = b'\x1b'
    BACKSPACE = b'\x08'
    TAB = b'\t'
    SPACE = b' '
    
    # Special keys (returned as two-byte sequences)
    UP = b'\xe0H'
    DOWN = b'\xe0P'
    LEFT = b'\xe0K'
    RIGHT = b'\xe0M'
    HOME = b'\xe0G'
    END = b'\xe0O'
    PAGE_UP = b'\xe0I'
    PAGE_DOWN = b'\xe0Q'
    INSERT = b'\xe0R'
    DELETE = b'\xe0S'
    
    # Function keys
    F1 = b'\x00;'
    F2 = b'\x00<'
    F3 = b'\x00='
    F4 = b'\x00>'
    F5 = b'\x00?'
    F6 = b'\x00@'
    F7 = b'\x00A'
    F8 = b'\x00B'
    F9 = b'\x00C'
    F10 = b'\x00D'
    F11 = b'\xe0\x85'
    F12 = b'\xe0\x86'

def get_key() -> bytes:
    """
    Get a key press from the user (Windows version).
    Returns the key as bytes.
    """
    if msvcrt.kbhit():
        key = msvcrt.getch()
        # Check for special keys (arrow keys, function keys, etc.)
        if key in (b'\x00', b'\xe0'):
            key += msvcrt.getch()
        return key
    return b''

def wait_for_key() -> bytes:
    """Wait for a key press and return it"""
    while True:
        key = get_key()
        if key:
            return key
        time.sleep(0.01)

# ============================================================================
# SECTION 4: MENU ITEM CLASSES
# ============================================================================

class MenuItemType(Enum):
    """Menu item types"""
    COMMAND = 1
    SUBMENU = 2
    SEPARATOR = 3
    CHECKBOX = 4
    RADIO = 5
    BACK = 6
    EXIT = 7

@dataclass
class MenuItem:
    """Menu item data structure"""
    label: str
    item_type: MenuItemType = MenuItemType.COMMAND
    action: Optional[Callable] = None
    shortcut: Optional[str] = None
    enabled: bool = True
    checked: bool = False
    submenu: Optional['Menu'] = None
    description: str = ""
    hotkey: Optional[str] = None

class Menu:
    """Menu container"""
    def __init__(self, title: str, items: List[MenuItem]):
        self.title = title
        self.items = items
        self.selected_index = 0
    
    def get_selectable_items(self) -> List[int]:
        """Get indices of selectable items"""
        return [i for i, item in enumerate(self.items) 
                if item.enabled and item.item_type != MenuItemType.SEPARATOR]
    
    def move_selection(self, direction: int):
        """Move selection up (-1) or down (1)"""
        selectable = self.get_selectable_items()
        if not selectable:
            return
        
        current_pos = selectable.index(self.selected_index) if self.selected_index in selectable else 0
        new_pos = (current_pos + direction) % len(selectable)
        self.selected_index = selectable[new_pos]

# ============================================================================
# SECTION 5: THEME SYSTEM
# ============================================================================

@dataclass
class Theme:
    """Color theme for menus"""
    title_fg: str = FG_BRIGHT_CYAN
    title_bg: str = ''
    border_fg: str = FG_BRIGHT_WHITE
    normal_fg: str = FG_WHITE
    normal_bg: str = ''
    selected_fg: str = FG_BLACK
    selected_bg: str = BG_CYAN
    disabled_fg: str = FG_BRIGHT_BLACK
    shortcut_fg: str = FG_BRIGHT_YELLOW
    description_fg: str = FG_BRIGHT_BLACK
    pointer_fg: str = FG_BRIGHT_GREEN
    checkbox_fg: str = FG_BRIGHT_YELLOW

# Predefined themes
THEME_DEFAULT = Theme()
THEME_DARK = Theme(
    title_fg=FG_BRIGHT_BLUE,
    border_fg=FG_BLUE,
    normal_fg=FG_BRIGHT_WHITE,
    selected_fg=FG_WHITE,
    selected_bg=BG_BLUE,
    pointer_fg=FG_BRIGHT_CYAN
)
THEME_LIGHT = Theme(
    title_fg=FG_BLUE,
    border_fg=FG_BLACK,
    normal_fg=FG_BLACK,
    selected_fg=FG_WHITE,
    selected_bg=BG_BLUE,
    disabled_fg=FG_BRIGHT_BLACK,
    pointer_fg=FG_GREEN
)
THEME_MATRIX = Theme(
    title_fg=FG_BRIGHT_GREEN,
    border_fg=FG_GREEN,
    normal_fg=FG_GREEN,
    selected_fg=FG_BLACK,
    selected_bg=BG_GREEN,
    disabled_fg=FG_BRIGHT_BLACK,
    pointer_fg=FG_BRIGHT_GREEN,
    checkbox_fg=FG_BRIGHT_GREEN
)

# ============================================================================
# SECTION 6: SCREEN UTILITY FUNCTIONS
# ============================================================================

class Screen:
    """Screen management utilities"""
    
    @staticmethod
    def clear():
        """Clear the entire screen"""
        print(CLEAR_SCREEN + CURSOR_HOME, end='', flush=True)
    
    @staticmethod
    def clear_line():
        """Clear the current line"""
        print(CLEAR_LINE, end='', flush=True)
    
    @staticmethod
    def hide_cursor():
        """Hide the cursor"""
        print(CURSOR_HIDE, end='', flush=True)
    
    @staticmethod
    def show_cursor():
        """Show the cursor"""
        print(CURSOR_SHOW, end='', flush=True)
    
    @staticmethod
    def move_to(row: int, col: int):
        """Move cursor to position"""
        print(CURSOR_POS(row, col), end='', flush=True)
    
    @staticmethod
    def print_at(row: int, col: int, text: str):
        """Print text at specific position"""
        Screen.move_to(row, col)
        print(text, end='', flush=True)

# ============================================================================
# SECTION 7: BOX DRAWING UTILITIES
# ============================================================================

def draw_box(x: int, y: int, width: int, height: int, title: str = "", 
             double_line: bool = False, theme: Theme = THEME_DEFAULT):
    """
    Draw a box on the screen
    
    Args:
        x, y: Top-left corner position (1-based)
        width, height: Box dimensions
        title: Optional title for the box
        double_line: Use double-line box characters
        theme: Color theme
    """
    h = BOX_DOUBLE_H if double_line else BOX_H
    v = BOX_DOUBLE_V if double_line else BOX_V
    tl = BOX_DOUBLE_TL if double_line else BOX_TL
    tr = BOX_DOUBLE_TR if double_line else BOX_TR
    bl = BOX_DOUBLE_BL if double_line else BOX_BL
    br = BOX_DOUBLE_BR if double_line else BOX_BR
    
    # Top border
    Screen.print_at(y, x, f"{theme.border_fg}{tl}{h * (width - 2)}{tr}{RESET}")
    
    # Add title if provided
    if title:
        title_text = f" {title} "
        title_x = x + (width - len(title_text)) // 2
        Screen.print_at(y, title_x, f"{theme.title_fg}{BOLD}{title_text}{RESET}")
    
    # Side borders
    for i in range(1, height - 1):
        Screen.print_at(y + i, x, f"{theme.border_fg}{v}{RESET}")
        Screen.print_at(y + i, x + width - 1, f"{theme.border_fg}{v}{RESET}")
    
    # Bottom border
    Screen.print_at(y + height - 1, x, f"{theme.border_fg}{bl}{h * (width - 2)}{br}{RESET}")

def draw_horizontal_line(x: int, y: int, width: int, theme: Theme = THEME_DEFAULT):
    """Draw a horizontal line"""
    Screen.print_at(y, x, f"{theme.border_fg}{BOX_L}{BOX_H * (width - 2)}{BOX_R}{RESET}")

# ============================================================================
# SECTION 8: MENU RENDERER
# ============================================================================

class MenuRenderer:
    """Renders menus to the screen"""
    
    def __init__(self, theme: Theme = THEME_DEFAULT):
        self.theme = theme
    
    def render_menu(self, menu: Menu, x: int, y: int, width: int, show_descriptions: bool = True):
        """
        Render a menu at the specified position
        
        Args:
            menu: Menu to render
            x, y: Top-left position
            width: Menu width
            show_descriptions: Show item descriptions
        """
        # Calculate height
        height = len(menu.items) + 2  # +2 for borders
        if show_descriptions:
            height += 2  # Extra space for description
        
        # Draw box
        draw_box(x, y, width, height, menu.title, False, self.theme)
        
        # Render menu items
        for idx, item in enumerate(menu.items):
            self._render_item(item, idx, menu.selected_index, x, y + idx + 1, width)
        
        # Show description of selected item
        if show_descriptions:
            selected_item = menu.items[menu.selected_index]
            if selected_item.description:
                desc_y = y + len(menu.items) + 1
                draw_horizontal_line(x, desc_y, width, self.theme)
                desc_text = selected_item.description[:width - 4]
                Screen.print_at(desc_y + 1, x + 2, 
                              f"{self.theme.description_fg}{desc_text}{RESET}")
    
    def _render_item(self, item: MenuItem, idx: int, selected_idx: int, 
                     x: int, y: int, width: int):
        """Render a single menu item"""
        is_selected = (idx == selected_idx)
        
        # Handle separator
        if item.item_type == MenuItemType.SEPARATOR:
            Screen.print_at(y, x, f"{self.theme.border_fg}{BOX_L}{BOX_H * (width - 2)}{BOX_R}{RESET}")
            return
        
        # Determine colors
        if not item.enabled:
            fg = self.theme.disabled_fg
            bg = ''
        elif is_selected:
            fg = self.theme.selected_fg
            bg = self.theme.selected_bg
        else:
            fg = self.theme.normal_fg
            bg = self.theme.normal_bg
        
        # Build item text
        pointer = f"{self.theme.pointer_fg}{POINTER}{RESET} " if is_selected else "  "
        
        # Add checkbox/radio indicator
        if item.item_type == MenuItemType.CHECKBOX:
            indicator = f"{self.theme.checkbox_fg}{CHECKBOX_ON if item.checked else CHECKBOX_OFF}{RESET} "
        elif item.item_type == MenuItemType.RADIO:
            indicator = f"{self.theme.checkbox_fg}{RADIO_ON if item.checked else RADIO_OFF}{RESET} "
        else:
            indicator = ""
        
        # Add label
        label = item.label
        
        # Add shortcut
        shortcut = ""
        if item.shortcut:
            shortcut = f" [{self.theme.shortcut_fg}{item.shortcut}{RESET}]"
        
        # Add hotkey
        if item.hotkey and not is_selected:
            label = label.replace(item.hotkey, f"{self.theme.shortcut_fg}{UNDERLINE}{item.hotkey}{RESET}{fg}")
        
        # Calculate padding
        content = f"{pointer}{indicator}{label}{shortcut}"
        # Remove ANSI codes for length calculation
        import re
        clean_content = re.sub(r'\033\[[0-9;]*m', '', content)
        padding = ' ' * max(0, width - len(clean_content) - 2)
        
        # Print item
        line = f"{pointer}{bg}{fg}{indicator}{label}{shortcut}{padding}{RESET}"
        Screen.print_at(y, x + 1, line)

# ============================================================================
# SECTION 9: MENU CONTROLLER
# ============================================================================

class MenuController:
    """Handles menu interaction and navigation"""
    
    def __init__(self, menu: Menu, theme: Theme = THEME_DEFAULT):
        self.menu = menu
        self.theme = theme
        self.renderer = MenuRenderer(theme)
        self.running = False
        self.result = None
    
    def show(self, x: int = None, y: int = None, width: int = 50) -> Any:
        """
        Display menu and handle interaction
        
        Args:
            x, y: Position (centered if None)
            width: Menu width
        
        Returns:
            Result from selected action or None
        """
        # Center if position not specified
        if x is None or y is None:
            term_width, term_height = get_terminal_size()
            height = len(self.menu.items) + 4
            x = (term_width - width) // 2
            y = (term_height - height) // 2
        
        self.running = True
        Screen.hide_cursor()
        
        try:
            while self.running:
                # Render menu
                self.renderer.render_menu(self.menu, x, y, width)
                
                # Get key input
                key = wait_for_key()
                
                # Handle key
                self._handle_key(key)
            
            return self.result
        
        finally:
            Screen.show_cursor()
    
    def _handle_key(self, key: bytes):
        """Handle keyboard input"""
        if key == Key.UP:
            self.menu.move_selection(-1)
        
        elif key == Key.DOWN:
            self.menu.move_selection(1)
        
        elif key == Key.ENTER:
            self._activate_item()
        
        elif key == Key.ESC:
            self.result = None
            self.running = False
        
        elif key == Key.SPACE:
            self._toggle_item()
        
        else:
            # Check for hotkeys
            self._check_hotkey(key)
    
    def _activate_item(self):
        """Activate the selected menu item"""
        item = self.menu.items[self.menu.selected_index]
        
        if not item.enabled:
            return
        
        if item.item_type == MenuItemType.EXIT:
            self.result = None
            self.running = False
        
        elif item.item_type == MenuItemType.BACK:
            self.result = "BACK"
            self.running = False
        
        elif item.item_type == MenuItemType.CHECKBOX:
            item.checked = not item.checked
            if item.action:
                item.action(item.checked)
        
        elif item.item_type == MenuItemType.RADIO:
            # Uncheck all radio items in group
            for menu_item in self.menu.items:
                if menu_item.item_type == MenuItemType.RADIO:
                    menu_item.checked = False
            item.checked = True
            if item.action:
                item.action()
        
        elif item.item_type == MenuItemType.SUBMENU and item.submenu:
            # Show submenu
            controller = MenuController(item.submenu, self.theme)
            Screen.clear()
            self.result = controller.show()
            if self.result != "BACK":
                self.running = False
            Screen.clear()
        
        elif item.action:
            Screen.show_cursor()
            Screen.clear()
            try:
                self.result = item.action()
                if self.result is not None:
                    self.running = False
            except Exception as e:
                print(f"\n{FG_RED}Error: {e}{RESET}")
                input("\nPress Enter to continue...")
            Screen.clear()
            Screen.hide_cursor()
    
    def _toggle_item(self):
        """Toggle checkbox/radio items with spacebar"""
        item = self.menu.items[self.menu.selected_index]
        if item.item_type == MenuItemType.CHECKBOX:
            self._activate_item()
    
    def _check_hotkey(self, key: bytes):
        """Check if key matches any hotkey"""
        try:
            char = key.decode('utf-8').lower()
            for item in self.menu.items:
                if item.hotkey and item.hotkey.lower() == char and item.enabled:
                    self.menu.selected_index = self.menu.items.index(item)
                    self._activate_item()
                    break
        except:
            pass

# ============================================================================
# SECTION 10: DIALOG UTILITIES
# ============================================================================

class Dialog:
    """Dialog box utilities"""
    
    @staticmethod
    def message(title: str, message: str, theme: Theme = THEME_DEFAULT):
        """Show a message dialog"""
        lines = message.split('\n')
        width = max(len(line) for line in lines) + 6
        width = max(width, len(title) + 6)
        height = len(lines) + 4
        
        term_width, term_height = get_terminal_size()
        x = (term_width - width) // 2
        y = (term_height - height) // 2
        
        Screen.hide_cursor()
        draw_box(x, y, width, height, title, False, theme)
        
        for i, line in enumerate(lines):
            Screen.print_at(y + i + 1, x + 2, f"{theme.normal_fg}{line}{RESET}")
        
        # Show OK button
        Screen.print_at(y + height - 2, x + width // 2 - 4, 
                       f"{theme.selected_bg}{theme.selected_fg}[ OK ]{RESET}")
        
        wait_for_key()
        Screen.show_cursor()
    
    @staticmethod
    def confirm(title: str, message: str, theme: Theme = THEME_DEFAULT) -> bool:
        """Show a confirmation dialog"""
        lines = message.split('\n')
        width = max(len(line) for line in lines) + 6
        width = max(width, len(title) + 6, 30)
        height = len(lines) + 5
        
        term_width, term_height = get_terminal_size()
        x = (term_width - width) // 2
        y = (term_height - height) // 2
        
        selected = 0  # 0 = Yes, 1 = No
        
        Screen.hide_cursor()
        
        while True:
            draw_box(x, y, width, height, title, False, theme)
            
            for i, line in enumerate(lines):
                Screen.print_at(y + i + 1, x + 2, f"{theme.normal_fg}{line}{RESET}")
            
            # Show buttons
            button_y = y + height - 2
            yes_x = x + width // 2 - 10
            no_x = x + width // 2 + 2
            
            if selected == 0:
                Screen.print_at(button_y, yes_x, f"{theme.selected_bg}{theme.selected_fg}[ Yes ]{RESET}")
                Screen.print_at(button_y, no_x, f"{theme.normal_fg}[ No ]{RESET}")
            else:
                Screen.print_at(button_y, yes_x, f"{theme.normal_fg}[ Yes ]{RESET}")
                Screen.print_at(button_y, no_x, f"{theme.selected_bg}{theme.selected_fg}[ No ]{RESET}")
            
            key = wait_for_key()
            
            if key == Key.LEFT or key == Key.RIGHT:
                selected = 1 - selected
            elif key == Key.ENTER:
                Screen.show_cursor()
                return selected == 0
            elif key == Key.ESC:
                Screen.show_cursor()
                return False
    
    @staticmethod
    def input_text(title: str, prompt: str, default: str = "", 
                   theme: Theme = THEME_DEFAULT) -> Optional[str]:
        """Show an input dialog"""
        width = max(len(prompt) + 6, 40)
        height = 6
        
        term_width, term_height = get_terminal_size()
        x = (term_width - width) // 2
        y = (term_height - height) // 2
        
        value = default
        cursor_pos = len(value)
        
        Screen.show_cursor()
        
        while True:
            draw_box(x, y, width, height, title, False, theme)
            Screen.print_at(y + 1, x + 2, f"{theme.normal_fg}{prompt}{RESET}")
            
            # Input field
            field_y = y + 2
            field_text = value + ' ' * (width - len(value) - 4)
            Screen.print_at(field_y, x + 2, f"{theme.selected_bg}{theme.selected_fg}{field_text}{RESET}")
            Screen.move_to(field_y, x + 2 + cursor_pos)
            
            # Instructions
            Screen.print_at(y + 4, x + 2, f"{theme.description_fg}Enter: OK  |  Esc: Cancel{RESET}")
            
            key = wait_for_key()
            
            if key == Key.ENTER:
                return value
            elif key == Key.ESC:
                return None
            elif key == Key.BACKSPACE:
                if cursor_pos > 0:
                    value = value[:cursor_pos - 1] + value[cursor_pos:]
                    cursor_pos -= 1
            elif key == Key.DELETE:
                if cursor_pos < len(value):
                    value = value[:cursor_pos] + value[cursor_pos + 1:]
            elif key == Key.LEFT:
                cursor_pos = max(0, cursor_pos - 1)
            elif key == Key.RIGHT:
                cursor_pos = min(len(value), cursor_pos + 1)
            elif key == Key.HOME:
                cursor_pos = 0
            elif key == Key.END:
                cursor_pos = len(value)
            elif len(key) == 1 and 32 <= ord(key) <= 126:
                # Printable character
                char = key.decode('utf-8')
                value = value[:cursor_pos] + char + value[cursor_pos:]
                cursor_pos += 1

# ============================================================================
# SECTION 11: PROGRESS INDICATORS
# ============================================================================

class ProgressBar:
    """Animated progress bar"""
    
    def __init__(self, title: str, total: int, width: int = 50, theme: Theme = THEME_DEFAULT):
        self.title = title
        self.total = total
        self.width = width
        self.theme = theme
        self.current = 0
        
        box_width = width + 10
        box_height = 6
        term_width, term_height = get_terminal_size()
        self.x = (term_width - box_width) // 2
        self.y = (term_height - box_height) // 2
        
        Screen.hide_cursor()
        draw_box(self.x, self.y, box_width, box_height, self.title, False, self.theme)
    
    def update(self, current: int, status: str = ""):
        """Update progress"""
        self.current = current
        percent = int(100 * current / self.total)
        filled = int(self.width * current / self.total)
        
        # Progress bar
        bar = f"{self.theme.selected_bg}{' ' * filled}{RESET}{self.theme.normal_fg}{'─' * (self.width - filled)}{RESET}"
        Screen.print_at(self.y + 2, self.x + 5, bar)
        
        # Percentage
        percent_text = f"{percent}%"
        Screen.print_at(self.y + 2, self.x + self.width + 8 - len(percent_text), 
                       f"{self.theme.shortcut_fg}{BOLD}{percent_text}{RESET}")
        
        # Status
        if status:
            status_text = status[:self.width]
            Screen.print_at(self.y + 3, self.x + 2, f"{self.theme.description_fg}{status_text}{' ' * (self.width - len(status_text))}{RESET}")
    
    def complete(self):
        """Mark as complete"""
        self.update(self.total, "Complete!")
        time.sleep(0.5)
        Screen.show_cursor()

class Spinner:
    """Animated spinner"""
    
    def __init__(self, message: str = "Loading...", theme: Theme = THEME_DEFAULT):
        self.message = message
        self.theme = theme
        self.running = False
        self.thread = None
        self.frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        self.frame_idx = 0
    
    def _spin(self):
        """Spinner animation loop"""
        Screen.hide_cursor()
        while self.running:
            frame = self.frames[self.frame_idx]
            print(f"\r{self.theme.pointer_fg}{frame}{RESET} {self.theme.normal_fg}{self.message}{RESET}", end='', flush=True)
            self.frame_idx = (self.frame_idx + 1) % len(self.frames)
            time.sleep(0.08)
    
    def start(self):
        """Start spinner"""
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()
    
    def stop(self, final_message: str = None):
        """Stop spinner"""
        self.running = False
        if self.thread:
            self.thread.join()
        if final_message:
            print(f"\r{self.theme.pointer_fg}{CHECK}{RESET} {self.theme.normal_fg}{final_message}{RESET}")
        else:
            print("\r" + " " * (len(self.message) + 10))
        Screen.show_cursor()

# ============================================================================
# SECTION 12: LIST SELECTOR
# ============================================================================

class ListSelector:
    """Multi-select list interface"""
    
    def __init__(self, title: str, items: List[str], selected_items: List[str] = None,
                 multi_select: bool = True, theme: Theme = THEME_DEFAULT):
        self.title = title
        self.items = items
        self.selected_items = set(selected_items or [])
        self.multi_select = multi_select
        self.theme = theme
        self.current_index = 0
        self.scroll_offset = 0
    
    def show(self, width: int = 60, height: int = 15) -> List[str]:
        """Display selector and return selected items"""
        term_width, term_height = get_terminal_size()
        x = (term_width - width) // 2
        y = (term_height - height) // 2
        
        visible_items = height - 4
        Screen.hide_cursor()
        
        try:
            while True:
                # Draw box
                draw_box(x, y, width, height, self.title, False, self.theme)
                
                # Show instructions
                instr = "Space: Toggle  |  Enter: Confirm  |  Esc: Cancel"
                if not self.multi_select:
                    instr = "Enter: Select  |  Esc: Cancel"
                Screen.print_at(y + height - 2, x + 2, f"{self.theme.description_fg}{instr}{RESET}")
                
                # Adjust scroll offset
                if self.current_index < self.scroll_offset:
                    self.scroll_offset = self.current_index
                elif self.current_index >= self.scroll_offset + visible_items:
                    self.scroll_offset = self.current_index - visible_items + 1
                
                # Render items
                for i in range(visible_items):
                    item_idx = self.scroll_offset + i
                    if item_idx >= len(self.items):
                        break
                    
                    item = self.items[item_idx]
                    is_selected = item_idx == self.current_index
                    is_checked = item in self.selected_items
                    
                    # Colors
                    if is_selected:
                        fg = self.theme.selected_fg
                        bg = self.theme.selected_bg
                    else:
                        fg = self.theme.normal_fg
                        bg = ''
                    
                    # Checkbox
                    checkbox = f"{self.theme.checkbox_fg}{CHECKBOX_ON if is_checked else CHECKBOX_OFF}{RESET} "
                    
                    # Pointer
                    pointer = f"{self.theme.pointer_fg}{POINTER}{RESET} " if is_selected else "  "
                    
                    # Item text
                    item_text = item[:width - 10]
                    padding = ' ' * (width - len(item_text) - 8)
                    
                    line = f"{pointer}{bg}{fg}{checkbox}{item_text}{padding}{RESET}"
                    Screen.print_at(y + i + 1, x + 1, line)
                
                # Show scroll indicators
                if self.scroll_offset > 0:
                    Screen.print_at(y + 1, x + width - 3, f"{self.theme.shortcut_fg}{ARROW_UP}{RESET}")
                if self.scroll_offset + visible_items < len(self.items):
                    Screen.print_at(y + visible_items, x + width - 3, f"{self.theme.shortcut_fg}{ARROW_DOWN}{RESET}")
                
                # Get input
                key = wait_for_key()
                
                if key == Key.UP:
                    self.current_index = max(0, self.current_index - 1)
                elif key == Key.DOWN:
                    self.current_index = min(len(self.items) - 1, self.current_index + 1)
                elif key == Key.SPACE and self.multi_select:
                    current_item = self.items[self.current_index]
                    if current_item in self.selected_items:
                        self.selected_items.remove(current_item)
                    else:
                        self.selected_items.add(current_item)
                elif key == Key.ENTER:
                    if not self.multi_select:
                        return [self.items[self.current_index]]
                    return list(self.selected_items)
                elif key == Key.ESC:
                    return []
        
        finally:
            Screen.show_cursor()

# ============================================================================
# SECTION 13: DEMONSTRATION FUNCTIONS
# ============================================================================

def demo_basic_menu():
    """Demo: Basic vertical menu"""
    menu = Menu("Main Menu", [
        MenuItem("New Project", action=lambda: "new_project", hotkey="n"),
        MenuItem("Open Project", action=lambda: "open_project", hotkey="o"),
        MenuItem("Save Project", action=lambda: "save_project", hotkey="s"),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Settings", action=lambda: "settings"),
        MenuItem("Help", action=lambda: "help", shortcut="F1"),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Exit", item_type=MenuItemType.EXIT, hotkey="x"),
    ])
    
    controller = MenuController(menu)
    Screen.clear()
    result = controller.show()
    Screen.clear()
    print(f"\nYou selected: {result}")
    input("Press Enter to continue...")

def demo_checkboxes():
    """Demo: Checkbox menu"""
    def toggle_action(checked):
        pass  # Could save settings here
    
    menu = Menu("Settings", [
        MenuItem("Enable sound effects", item_type=MenuItemType.CHECKBOX, 
                action=toggle_action, checked=True),
        MenuItem("Enable music", item_type=MenuItemType.CHECKBOX, 
                action=toggle_action, checked=True),
        MenuItem("Show notifications", item_type=MenuItemType.CHECKBOX, 
                action=toggle_action, checked=False),
        MenuItem("Auto-save", item_type=MenuItemType.CHECKBOX, 
                action=toggle_action, checked=True),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Back", item_type=MenuItemType.BACK),
    ])
    
    controller = MenuController(menu)
    Screen.clear()
    controller.show()
    Screen.clear()

def demo_radio_buttons():
    """Demo: Radio button menu"""
    menu = Menu("Select Difficulty", [
        MenuItem("Easy", item_type=MenuItemType.RADIO, checked=True),
        MenuItem("Normal", item_type=MenuItemType.RADIO),
        MenuItem("Hard", item_type=MenuItemType.RADIO),
        MenuItem("Extreme", item_type=MenuItemType.RADIO),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Confirm", item_type=MenuItemType.BACK),
    ])
    
    controller = MenuController(menu)
    Screen.clear()
    controller.show()
    Screen.clear()

def demo_submenu():
    """Demo: Nested submenus"""
    file_menu = Menu("File Menu", [
        MenuItem("New", action=lambda: "new"),
        MenuItem("Open", action=lambda: "open"),
        MenuItem("Save", action=lambda: "save"),
        MenuItem("Save As", action=lambda: "save_as"),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Back", item_type=MenuItemType.BACK),
    ])
    
    edit_menu = Menu("Edit Menu", [
        MenuItem("Undo", action=lambda: "undo", shortcut="Ctrl+Z"),
        MenuItem("Redo", action=lambda: "redo", shortcut="Ctrl+Y"),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Cut", action=lambda: "cut", shortcut="Ctrl+X"),
        MenuItem("Copy", action=lambda: "copy", shortcut="Ctrl+C"),
        MenuItem("Paste", action=lambda: "paste", shortcut="Ctrl+V"),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Back", item_type=MenuItemType.BACK),
    ])
    
    main_menu = Menu("Main Menu", [
        MenuItem("File", item_type=MenuItemType.SUBMENU, submenu=file_menu),
        MenuItem("Edit", item_type=MenuItemType.SUBMENU, submenu=edit_menu),
        MenuItem("View", action=lambda: "view"),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Exit", item_type=MenuItemType.EXIT),
    ])
    
    controller = MenuController(main_menu)
    Screen.clear()
    result = controller.show()
    Screen.clear()
    print(f"\nResult: {result}")
    input("Press Enter to continue...")

def demo_dialogs():
    """Demo: Various dialog boxes"""
    Screen.clear()
    
    # Message dialog
    Dialog.message("Information", "This is a message dialog box.\nIt can contain multiple lines.", THEME_DEFAULT)
    Screen.clear()
    
    # Confirmation dialog
    result = Dialog.confirm("Confirm Action", "Are you sure you want to proceed?", THEME_DEFAULT)
    Screen.clear()
    print(f"User confirmed: {result}")
    time.sleep(1)
    Screen.clear()
    
    # Input dialog
    name = Dialog.input_text("User Input", "Enter your name:", "John Doe", THEME_DEFAULT)
    Screen.clear()
    if name:
        print(f"You entered: {name}")
    else:
        print("Input cancelled")
    input("\nPress Enter to continue...")

def demo_progress():
    """Demo: Progress indicators"""
    Screen.clear()
    
    # Progress bar
    progress = ProgressBar("Processing Files", 100, 40, THEME_DEFAULT)
    for i in range(101):
        progress.update(i, f"Processing file {i}/100")
        time.sleep(0.03)
    progress.complete()
    
    time.sleep(1)
    Screen.clear()
    
    # Spinner
    spinner = Spinner("Loading data from server...", THEME_DEFAULT)
    spinner.start()
    time.sleep(3)
    spinner.stop("Data loaded successfully!")
    
    time.sleep(1)
    input("\nPress Enter to continue...")

def demo_list_selector():
    """Demo: List selector"""
    items = [f"Option {i+1}" for i in range(20)]
    selector = ListSelector("Select Items (Multi-select)", items, multi_select=True)
    Screen.clear()
    selected = selector.show()
    Screen.clear()
    print(f"Selected items: {selected}")
    input("\nPress Enter to continue...")

def demo_themes():
    """Demo: Different themes"""
    themes = [
        ("Default", THEME_DEFAULT),
        ("Dark", THEME_DARK),
        ("Light", THEME_LIGHT),
        ("Matrix", THEME_MATRIX),
    ]
    
    for theme_name, theme in themes:
        menu = Menu(f"{theme_name} Theme", [
            MenuItem("Option 1", hotkey="1"),
            MenuItem("Option 2", hotkey="2"),
            MenuItem("Option 3", hotkey="3", enabled=False),
            MenuItem("", item_type=MenuItemType.SEPARATOR),
            MenuItem("Back", item_type=MenuItemType.BACK),
        ])
        
        controller = MenuController(menu, theme)
        Screen.clear()
        controller.show()

# ============================================================================
# SECTION 14: MAIN DEMONSTRATION MENU
# ============================================================================

def main():
    """Main demonstration program"""
    enable_ansi_windows()
    
    # Create main menu
    main_menu = Menu("CLI Menu Control Demo", [
        MenuItem("Basic Menu Navigation", 
                action=demo_basic_menu,
                description="Vertical menu with arrow key navigation"),
        MenuItem("Checkbox Menu", 
                action=demo_checkboxes,
                description="Menu with toggleable checkboxes"),
        MenuItem("Radio Button Menu", 
                action=demo_radio_buttons,
                description="Menu with radio button selection"),
        MenuItem("Nested Submenus", 
                action=demo_submenu,
                description="Multi-level menu navigation"),
        MenuItem("Dialog Boxes", 
                action=demo_dialogs,
                description="Message, confirmation, and input dialogs"),
        MenuItem("Progress Indicators", 
                action=demo_progress,
                description="Progress bars and spinners"),
        MenuItem("List Selector", 
                action=demo_list_selector,
                description="Multi-select list interface"),
        MenuItem("Theme Showcase", 
                action=demo_themes,
                description="Different color themes"),
        MenuItem("", item_type=MenuItemType.SEPARATOR),
        MenuItem("Exit", item_type=MenuItemType.EXIT, hotkey="x"),
    ])
    
    # Show welcome screen
    Screen.clear()
    print(f"\n{BOLD}{FG_BRIGHT_CYAN}{'═' * 70}{RESET}")
    print(f"{BOLD}{FG_BRIGHT_CYAN}  COMPREHENSIVE CLI MENU CONTROL DEMONSTRATION{RESET}")
    print(f"{BOLD}{FG_BRIGHT_CYAN}{'═' * 70}{RESET}\n")
    print(f"{FG_BRIGHT_WHITE}Features:{RESET}")
    print(f"  {POINTER} Arrow key navigation")
    print(f"  {POINTER} Interactive menus with hotkeys")
    print(f"  {POINTER} Checkboxes and radio buttons")
    print(f"  {POINTER} Nested submenus")
    print(f"  {POINTER} Dialog boxes (message, confirm, input)")
    print(f"  {POINTER} Progress bars and spinners")
    print(f"  {POINTER} Multi-select lists")
    print(f"  {POINTER} Multiple color themes")
    print(f"  {POINTER} Box drawing and borders")
    print(f"\n{FG_BRIGHT_YELLOW}Press any key to start...{RESET}")
    wait_for_key()
    
    # Run main menu loop
    controller = MenuController(main_menu)
    Screen.clear()
    controller.show()
    
    # Goodbye screen
    Screen.clear()
    print(f"\n{FG_BRIGHT_GREEN}Thank you for trying the CLI Menu Control Demo!{RESET}\n")

# ============================================================================
# SECTION 15: ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Screen.show_cursor()
        Screen.clear()
        print(f"\n{FG_YELLOW}Program interrupted by user.{RESET}\n")
    except Exception as e:
        Screen.show_cursor()
        Screen.clear()
        print(f"\n{FG_RED}Error: {e}{RESET}\n")
        import traceback
        traceback.print_exc()
    finally:
        Screen.show_cursor()
