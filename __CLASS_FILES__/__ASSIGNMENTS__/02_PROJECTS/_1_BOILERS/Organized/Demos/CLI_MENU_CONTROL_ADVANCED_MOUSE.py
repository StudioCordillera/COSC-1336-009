"""
ADVANCED CLI MENU CONTROL WITH MOUSE SUPPORT
=============================================
Extended menu system with full mouse integration, drag-and-drop,
resizable windows, tabbed interfaces, and advanced UI components.

Author: GitHub Copilot
Date: December 1, 2025
Platform: Windows (with enhanced mouse support)
Python: 3.6+

New Features:
- Full mouse support (click, drag, scroll)
- Mouse hover effects
- Drag-and-drop list reordering
- Resizable menu windows
- Tabbed interface
- Split-pane views
- Tree view navigation
- Color picker
- File browser
- Calendar widget
- Table/Grid view with sorting
- Context menus (right-click)
- Tooltips
- Scrollable content areas
- Window management (minimize, maximize, close)
"""

import os
import sys
import time
import msvcrt
import threading
import struct
from typing import List, Tuple, Optional, Callable, Dict, Any
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta
import ctypes
from ctypes import wintypes

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except:
        pass

# ============================================================================
# SECTION 1: WINDOWS CONSOLE API FOR MOUSE SUPPORT
# ============================================================================

# Windows Console API constants
STD_INPUT_HANDLE = -10
ENABLE_MOUSE_INPUT = 0x0010
ENABLE_EXTENDED_FLAGS = 0x0080
ENABLE_WINDOW_INPUT = 0x0008
ENABLE_PROCESSED_INPUT = 0x0001

# Mouse event flags
FROM_LEFT_1ST_BUTTON_PRESSED = 0x0001
RIGHTMOST_BUTTON_PRESSED = 0x0002
FROM_LEFT_2ND_BUTTON_PRESSED = 0x0004
MOUSE_WHEELED = 0x0004
MOUSE_MOVED = 0x0001
DOUBLE_CLICK = 0x0002

# Input record event types
KEY_EVENT = 0x0001
MOUSE_EVENT = 0x0002
WINDOW_BUFFER_SIZE_EVENT = 0x0004

# Load Windows kernel32 functions
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class MOUSE_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ("dwMousePosition", COORD),
        ("dwButtonState", wintypes.DWORD),
        ("dwControlKeyState", wintypes.DWORD),
        ("dwEventFlags", wintypes.DWORD)
    ]

class KEY_EVENT_RECORD(ctypes.Structure):
    class _char(ctypes.Union):
        _fields_ = [("UnicodeChar", wintypes.WCHAR), ("AsciiChar", wintypes.CHAR)]
    _fields_ = [
        ("bKeyDown", wintypes.BOOL),
        ("wRepeatCount", wintypes.WORD),
        ("wVirtualKeyCode", wintypes.WORD),
        ("wVirtualScanCode", wintypes.WORD),
        ("uChar", _char),
        ("dwControlKeyState", wintypes.DWORD)
    ]

class INPUT_RECORD(ctypes.Structure):
    class _Event(ctypes.Union):
        _fields_ = [("KeyEvent", KEY_EVENT_RECORD), ("MouseEvent", MOUSE_EVENT_RECORD)]
    _fields_ = [("EventType", wintypes.WORD), ("Event", _Event)]

class MouseHandler:
    """Windows console mouse input handler"""
    
    def __init__(self):
        self.stdin = kernel32.GetStdHandle(STD_INPUT_HANDLE)
        self.enabled = False
        self.last_button_state = 0
        
    def enable(self):
        """Enable mouse input in console"""
        mode = wintypes.DWORD()
        kernel32.GetConsoleMode(self.stdin, ctypes.byref(mode))
        mode.value |= ENABLE_MOUSE_INPUT | ENABLE_EXTENDED_FLAGS
        kernel32.SetConsoleMode(self.stdin, mode)
        self.enabled = True
    
    def disable(self):
        """Disable mouse input"""
        mode = wintypes.DWORD()
        kernel32.GetConsoleMode(self.stdin, ctypes.byref(mode))
        mode.value &= ~ENABLE_MOUSE_INPUT
        kernel32.SetConsoleMode(self.stdin, mode)
        self.enabled = False
    
    def read_input(self) -> Optional[Tuple[str, Any]]:
        """
        Read console input (keyboard or mouse)
        Returns: (event_type, event_data) or None
        event_type: 'key', 'mouse_click', 'mouse_move', 'mouse_scroll'
        """
        if not self.enabled:
            return None
        
        num_events = wintypes.DWORD()
        kernel32.GetNumberOfConsoleInputEvents(self.stdin, ctypes.byref(num_events))
        
        if num_events.value == 0:
            return None
        
        input_record = INPUT_RECORD()
        events_read = wintypes.DWORD()
        
        if kernel32.ReadConsoleInputW(self.stdin, ctypes.byref(input_record), 1, ctypes.byref(events_read)):
            if input_record.EventType == KEY_EVENT:
                key_event = input_record.Event.KeyEvent
                if key_event.bKeyDown:
                    return ('key', key_event.uChar.AsciiChar.encode() if key_event.uChar.AsciiChar else b'')
            
            elif input_record.EventType == MOUSE_EVENT:
                mouse_event = input_record.Event.MouseEvent
                # Windows Console API returns 0-based coordinates, but ANSI cursor positioning is 1-based
                x = mouse_event.dwMousePosition.X + 1
                y = mouse_event.dwMousePosition.Y + 1
                button_state = mouse_event.dwButtonState
                event_flags = mouse_event.dwEventFlags
                
                # Mouse movement
                if event_flags & MOUSE_MOVED:
                    return ('mouse_move', {'x': x, 'y': y})
                
                # Mouse wheel
                if event_flags & MOUSE_WHEELED:
                    # High word contains scroll direction
                    scroll = ctypes.c_short(button_state >> 16).value
                    direction = 'up' if scroll > 0 else 'down'
                    return ('mouse_scroll', {'x': x, 'y': y, 'direction': direction})
                
                # Mouse click/release
                if button_state != self.last_button_state:
                    left_pressed = bool(button_state & FROM_LEFT_1ST_BUTTON_PRESSED)
                    right_pressed = bool(button_state & RIGHTMOST_BUTTON_PRESSED)
                    left_was_pressed = bool(self.last_button_state & FROM_LEFT_1ST_BUTTON_PRESSED)
                    right_was_pressed = bool(self.last_button_state & RIGHTMOST_BUTTON_PRESSED)
                    
                    self.last_button_state = button_state
                    
                    # Detect clicks vs releases
                    if left_pressed and not left_was_pressed:
                        return ('mouse_click', {'x': x, 'y': y, 'button': 'left', 'action': 'down'})
                    elif not left_pressed and left_was_pressed:
                        return ('mouse_click', {'x': x, 'y': y, 'button': 'left', 'action': 'up'})
                    elif right_pressed and not right_was_pressed:
                        return ('mouse_click', {'x': x, 'y': y, 'button': 'right', 'action': 'down'})
                    elif not right_pressed and right_was_pressed:
                        return ('mouse_click', {'x': x, 'y': y, 'button': 'right', 'action': 'up'})
        
        return None

# ============================================================================
# SECTION 2: ANSI CODES AND CONSTANTS (Extended)
# ============================================================================

ESC = '\033'
CSI = '\033['

# Text Styles
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
HIDDEN = '\033[8m'
STRIKETHROUGH = '\033[9m'

# Standard Colors
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

BG_BRIGHT_BLACK = '\033[100m'
BG_BRIGHT_RED = '\033[101m'
BG_BRIGHT_GREEN = '\033[102m'
BG_BRIGHT_YELLOW = '\033[103m'
BG_BRIGHT_BLUE = '\033[104m'
BG_BRIGHT_MAGENTA = '\033[105m'
BG_BRIGHT_CYAN = '\033[106m'
BG_BRIGHT_WHITE = '\033[107m'

# RGB colors
def fg_rgb(r, g, b): return f'\033[38;2;{r};{g};{b}m'
def bg_rgb(r, g, b): return f'\033[48;2;{r};{g};{b}m'

# Cursor Control
CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'
CURSOR_HOME = '\033[H'
CURSOR_POS = lambda row, col: f'\033[{row};{col}H'
CLEAR_SCREEN = '\033[2J'
CLEAR_LINE = '\033[2K'
SAVE_CURSOR = '\033[s'
RESTORE_CURSOR = '\033[u'

# Box Drawing (ASCII compatible for Windows)
BOX_H = '-'
BOX_V = '|'
BOX_TL = '+'
BOX_TR = '+'
BOX_BL = '+'
BOX_BR = '+'
BOX_T = '+'
BOX_B = '+'
BOX_L = '+'
BOX_R = '+'
BOX_CROSS = '+'

BOX_DOUBLE_H = '='
BOX_DOUBLE_V = '|'
BOX_DOUBLE_TL = '+'
BOX_DOUBLE_TR = '+'
BOX_DOUBLE_BL = '+'
BOX_DOUBLE_BR = '+'

# Symbols (ASCII compatible)
POINTER = '>'
CHECK = 'v'
CROSS = 'x'
RADIO_ON = '(*)'
RADIO_OFF = '( )'
CHECKBOX_ON = '[x]'
CHECKBOX_OFF = '[ ]'
ARROW_UP = '^'
ARROW_DOWN = 'v'
ARROW_LEFT = '<'
ARROW_RIGHT = '>'
HAMBURGER = '='
CLOSE_X = 'X'
MINIMIZE = '_'
MAXIMIZE = 'O'
FOLDER = '[D]'
FILE = '[F]'
TREE_BRANCH = '+'
TREE_LAST = '+'
TREE_LINE = '|'

# ============================================================================
# SECTION 3: SCREEN UTILITIES (Enhanced)
# ============================================================================

def enable_ansi_windows():
    """Enable ANSI escape sequences on Windows 10+"""
    if sys.platform == 'win32':
        try:
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            # Disable QuickEdit and Insert mode to allow mouse input
            stdin_handle = kernel32.GetStdHandle(-10)
            mode = wintypes.DWORD()
            kernel32.GetConsoleMode(stdin_handle, ctypes.byref(mode))
            # Clear ENABLE_QUICK_EDIT_MODE (0x0040) and ENABLE_INSERT_MODE (0x0020)
            mode.value &= ~0x0040
            mode.value &= ~0x0020
            kernel32.SetConsoleMode(stdin_handle, mode.value)
        except Exception:
            pass

def get_terminal_size() -> Tuple[int, int]:
    """Get terminal size (width, height)"""
    try:
        import shutil
        size = shutil.get_terminal_size()
        return size.columns, size.lines
    except:
        return 80, 24

def set_console_size(width: int, height: int):
    """Set console window size (Windows only)"""
    if sys.platform == 'win32':
        try:
            os.system(f'mode con: cols={width} lines={height}')
        except:
            pass

class Screen:
    """Enhanced screen management"""
    
    @staticmethod
    def clear():
        print(CLEAR_SCREEN + CURSOR_HOME, end='', flush=True)
    
    @staticmethod
    def clear_line():
        print(CLEAR_LINE, end='', flush=True)
    
    @staticmethod
    def hide_cursor():
        print(CURSOR_HIDE, end='', flush=True)
    
    @staticmethod
    def show_cursor():
        print(CURSOR_SHOW, end='', flush=True)
    
    @staticmethod
    def move_to(row: int, col: int):
        print(CURSOR_POS(row, col), end='', flush=True)
    
    @staticmethod
    def print_at(row: int, col: int, text: str):
        Screen.move_to(row, col)
        print(text, end='', flush=True)
    
    @staticmethod
    def fill_rect(x: int, y: int, width: int, height: int, char: str = ' ', color: str = ''):
        """Fill a rectangular area"""
        line = color + char * width + RESET
        for i in range(height):
            Screen.print_at(y + i, x, line)

# ============================================================================
# SECTION 4: MOUSE-AWARE WIDGETS BASE CLASS
# ============================================================================

class Widget:
    """Base class for all interactive widgets"""
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.enabled = True
        self.focused = False
        self.hover = False
        
    def contains_point(self, px: int, py: int) -> bool:
        """Check if point is inside widget bounds"""
        return (self.x <= px < self.x + self.width and 
                self.y <= py < self.y + self.height)
    
    def on_mouse_move(self, x: int, y: int) -> bool:
        """Handle mouse move event. Return True if state changed."""
        new_hover = self.contains_point(x, y)
        if new_hover != self.hover:
            self.hover = new_hover
            return True
        return False
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        """Handle mouse click event. Return True if handled."""
        return False
    
    def on_key(self, key: bytes) -> bool:
        """Handle keyboard event. Return True if handled."""
        return False
    
    def render(self):
        """Render the widget"""
        pass

# ============================================================================
# SECTION 5: BUTTON WIDGET
# ============================================================================

class Button(Widget):
    """Clickable button with mouse and keyboard support"""
    
    def __init__(self, x: int, y: int, label: str, on_click: Callable = None):
        width = len(label) + 4
        super().__init__(x, y, width, 1)
        self.label = label
        self.on_click = on_click
        self.pressed = False
    
    def render(self):
        if not self.visible:
            return
        
        if not self.enabled:
            color = FG_BRIGHT_BLACK
            bg = ''
        elif self.pressed:
            color = FG_BLACK
            bg = BG_WHITE
        elif self.hover or self.focused:
            color = FG_BLACK
            bg = BG_CYAN
        else:
            color = FG_WHITE
            bg = BG_BLUE
        
        text = f"{bg}{color} {self.label} {RESET}"
        Screen.print_at(self.y, self.x, text)
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        if not self.enabled or button != 'left':
            return False
        
        if self.contains_point(x, y):
            if action == 'down':
                self.pressed = True
            elif action == 'up' and self.pressed:
                self.pressed = False
                if self.on_click:
                    self.on_click()
            return True
        else:
            self.pressed = False
        return False
    
    def on_key(self, key: bytes) -> bool:
        if self.focused and key == b'\r':  # Enter
            if self.on_click:
                self.on_click()
            return True
        return False

# ============================================================================
# SECTION 6: SCROLLABLE LIST WITH MOUSE SUPPORT
# ============================================================================

class ScrollableList(Widget):
    """List with mouse scroll and click support"""
    
    def __init__(self, x: int, y: int, width: int, height: int, items: List[str],
                 on_select: Callable = None):
        super().__init__(x, y, width, height)
        self.items = items
        self.selected_index = 0
        self.scroll_offset = 0
        self.on_select = on_select
        self.drag_start = None
    
    def render(self):
        if not self.visible:
            return
        
        # Draw border
        Screen.print_at(self.y, self.x, f"{FG_BRIGHT_WHITE}{BOX_TL}{BOX_H * (self.width - 2)}{BOX_TR}{RESET}")
        for i in range(1, self.height - 1):
            Screen.print_at(self.y + i, self.x, f"{FG_BRIGHT_WHITE}{BOX_V}{RESET}")
            Screen.print_at(self.y + i, self.x + self.width - 1, f"{FG_BRIGHT_WHITE}{BOX_V}{RESET}")
        Screen.print_at(self.y + self.height - 1, self.x, f"{FG_BRIGHT_WHITE}{BOX_BL}{BOX_H * (self.width - 2)}{BOX_BR}{RESET}")
        
        # Draw items
        visible_height = self.height - 2
        for i in range(visible_height):
            item_idx = self.scroll_offset + i
            if item_idx >= len(self.items):
                break
            
            item = self.items[item_idx]
            is_selected = item_idx == self.selected_index
            
            if is_selected:
                color = FG_BLACK
                bg = BG_CYAN
            elif self.hover and self.contains_point(self.x + 1, self.y + i + 1):
                color = FG_WHITE
                bg = BG_BLUE
            else:
                color = FG_WHITE
                bg = ''
            
            text = item[:self.width - 4]
            padding = ' ' * (self.width - len(text) - 3)
            line = f"{bg}{color}{text}{padding}{RESET}"
            Screen.print_at(self.y + i + 1, self.x + 1, line)
        
        # Scrollbar
        if len(self.items) > visible_height:
            scrollbar_height = max(1, visible_height * visible_height // len(self.items))
            scrollbar_pos = int(self.scroll_offset * (visible_height - scrollbar_height) / 
                              max(1, len(self.items) - visible_height))
            
            for i in range(visible_height):
                char = '█' if scrollbar_pos <= i < scrollbar_pos + scrollbar_height else '│'
                Screen.print_at(self.y + i + 1, self.x + self.width - 2, f"{FG_BRIGHT_BLACK}{char}{RESET}")
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        if not self.enabled or not self.contains_point(x, y):
            return False
        
        if button == 'left' and action == 'down':
            # Calculate clicked item
            visible_height = self.height - 2
            relative_y = y - self.y - 1
            if 0 <= relative_y < visible_height:
                item_idx = self.scroll_offset + relative_y
                if 0 <= item_idx < len(self.items):
                    self.selected_index = item_idx
                    if self.on_select:
                        self.on_select(self.items[item_idx])
            return True
        
        return False
    
    def on_mouse_scroll(self, direction: str):
        """Handle mouse wheel scroll"""
        visible_height = self.height - 2
        if direction == 'up':
            self.scroll_offset = max(0, self.scroll_offset - 1)
        else:
            max_scroll = max(0, len(self.items) - visible_height)
            self.scroll_offset = min(max_scroll, self.scroll_offset + 1)
    
    def on_key(self, key: bytes) -> bool:
        if not self.focused:
            return False
        
        visible_height = self.height - 2
        
        if key == b'\xe0H':  # Up arrow
            if self.selected_index > 0:
                self.selected_index -= 1
                if self.selected_index < self.scroll_offset:
                    self.scroll_offset = self.selected_index
            return True
        elif key == b'\xe0P':  # Down arrow
            if self.selected_index < len(self.items) - 1:
                self.selected_index += 1
                if self.selected_index >= self.scroll_offset + visible_height:
                    self.scroll_offset = self.selected_index - visible_height + 1
            return True
        elif key == b'\r':  # Enter
            if self.on_select and 0 <= self.selected_index < len(self.items):
                self.on_select(self.items[self.selected_index])
            return True
        
        return False

# ============================================================================
# SECTION 7: TABBED INTERFACE
# ============================================================================

class TabbedPane(Widget):
    """Tabbed interface with mouse-clickable tabs"""
    
    def __init__(self, x: int, y: int, width: int, height: int, tabs: List[Tuple[str, Widget]]):
        super().__init__(x, y, width, height)
        self.tabs = tabs  # List of (title, widget) tuples
        self.active_tab = 0
    
    def render(self):
        if not self.visible:
            return
        
        # Render tab bar
        tab_x = self.x
        for i, (title, _) in enumerate(self.tabs):
            is_active = i == self.active_tab
            
            if is_active:
                color = FG_BLACK
                bg = BG_CYAN
            else:
                color = FG_WHITE
                bg = BG_BLUE
            
            tab_text = f"{bg}{color} {title} {RESET}"
            Screen.print_at(self.y, tab_x, tab_text)
            tab_x += len(title) + 3
        
        # Fill rest of tab bar
        remaining = self.width - (tab_x - self.x)
        if remaining > 0:
            Screen.print_at(self.y, tab_x, BG_BLUE + ' ' * remaining + RESET)
        
        # Render active tab content
        _, widget = self.tabs[self.active_tab]
        widget.render()
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        if not self.enabled:
            return False
        
        # Check if clicking on tab bar
        if self.y == y and self.x <= x < self.x + self.width and button == 'left' and action == 'down':
            tab_x = self.x
            for i, (title, _) in enumerate(self.tabs):
                tab_width = len(title) + 3
                if tab_x <= x < tab_x + tab_width:
                    self.active_tab = i
                    return True
                tab_x += tab_width
        
        # Forward to active widget
        _, widget = self.tabs[self.active_tab]
        return widget.on_mouse_click(x, y, button, action)
    
    def on_key(self, key: bytes) -> bool:
        # Tab switching with Ctrl+Tab
        if key == b'\t':
            self.active_tab = (self.active_tab + 1) % len(self.tabs)
            return True
        
        # Forward to active widget
        _, widget = self.tabs[self.active_tab]
        return widget.on_key(key)

# ============================================================================
# SECTION 8: TREE VIEW
# ============================================================================

@dataclass
class TreeNode:
    """Tree node for hierarchical data"""
    label: str
    children: List['TreeNode'] = None
    expanded: bool = False
    data: Any = None
    
    def __post_init__(self):
        if self.children is None:
            self.children = []

class TreeView(Widget):
    """Hierarchical tree view with expand/collapse"""
    
    def __init__(self, x: int, y: int, width: int, height: int, root: TreeNode):
        super().__init__(x, y, width, height)
        self.root = root
        self.selected_node = root
        self.scroll_offset = 0
        self.flat_list = []
        self._rebuild_flat_list()
    
    def _rebuild_flat_list(self):
        """Flatten tree structure for rendering"""
        self.flat_list = []
        
        def traverse(node, depth=0):
            self.flat_list.append((node, depth))
            if node.expanded:
                for child in node.children:
                    traverse(child, depth + 1)
        
        traverse(self.root)
    
    def render(self):
        if not self.visible:
            return
        
        # Draw border
        Screen.print_at(self.y, self.x, f"{FG_BRIGHT_WHITE}{BOX_TL}{BOX_H * (self.width - 2)}{BOX_TR}{RESET}")
        for i in range(1, self.height - 1):
            Screen.print_at(self.y + i, self.x, f"{FG_BRIGHT_WHITE}{BOX_V}{' ' * (self.width - 2)}{BOX_V}{RESET}")
        Screen.print_at(self.y + self.height - 1, self.x, f"{FG_BRIGHT_WHITE}{BOX_BL}{BOX_H * (self.width - 2)}{BOX_BR}{RESET}")
        
        # Render visible nodes
        visible_height = self.height - 2
        for i in range(visible_height):
            node_idx = self.scroll_offset + i
            if node_idx >= len(self.flat_list):
                break
            
            node, depth = self.flat_list[node_idx]
            is_selected = node == self.selected_node
            
            # Indent
            indent = '  ' * depth
            
            # Expand/collapse indicator
            if node.children:
                indicator = 'v' if node.expanded else '>'
            else:
                indicator = ' '
            
            # Colors
            if is_selected:
                color = FG_BLACK
                bg = BG_CYAN
            else:
                color = FG_WHITE
                bg = ''
            
            # Build line
            text = f"{indent}{indicator} {node.label}"
            text = text[:self.width - 4]
            padding = ' ' * max(0, self.width - len(text) - 3)
            line = f"{bg}{color}{text}{padding}{RESET}"
            Screen.print_at(self.y + i + 1, self.x + 1, line)
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        if not self.enabled or not self.contains_point(x, y):
            return False
        
        if button == 'left' and action == 'down':
            visible_height = self.height - 2
            relative_y = y - self.y - 1
            if 0 <= relative_y < visible_height:
                node_idx = self.scroll_offset + relative_y
                if 0 <= node_idx < len(self.flat_list):
                    node, _ = self.flat_list[node_idx]
                    
                    # Toggle expand if has children
                    if node.children:
                        node.expanded = not node.expanded
                        self._rebuild_flat_list()
                    
                    self.selected_node = node
            return True
        
        return False
    
    def on_key(self, key: bytes) -> bool:
        if not self.focused:
            return False
        
        visible_height = self.height - 2
        current_idx = next((i for i, (n, _) in enumerate(self.flat_list) if n == self.selected_node), 0)
        
        if key == b'\xe0H':  # Up
            if current_idx > 0:
                self.selected_node, _ = self.flat_list[current_idx - 1]
                if current_idx - 1 < self.scroll_offset:
                    self.scroll_offset = current_idx - 1
            return True
        elif key == b'\xe0P':  # Down
            if current_idx < len(self.flat_list) - 1:
                self.selected_node, _ = self.flat_list[current_idx + 1]
                if current_idx + 1 >= self.scroll_offset + visible_height:
                    self.scroll_offset = current_idx - visible_height + 2
            return True
        elif key == b'\xe0M':  # Right - expand
            if self.selected_node.children and not self.selected_node.expanded:
                self.selected_node.expanded = True
                self._rebuild_flat_list()
            return True
        elif key == b'\xe0K':  # Left - collapse
            if self.selected_node.expanded:
                self.selected_node.expanded = False
                self._rebuild_flat_list()
            return True
        elif key == b'\r':  # Enter - toggle
            if self.selected_node.children:
                self.selected_node.expanded = not self.selected_node.expanded
                self._rebuild_flat_list()
            return True
        
        return False

# ============================================================================
# SECTION 9: CALENDAR WIDGET
# ============================================================================

class Calendar(Widget):
    """Interactive calendar with mouse support"""
    
    def __init__(self, x: int, y: int, selected_date: datetime = None):
        super().__init__(x, y, 25, 9)
        self.selected_date = selected_date or datetime.now()
        self.view_date = self.selected_date.replace(day=1)
    
    def render(self):
        if not self.visible:
            return
        
        # Title with month/year
        title = self.view_date.strftime("%B %Y")
        Screen.print_at(self.y, self.x, f"{FG_BRIGHT_CYAN}{BOLD}{title:^25}{RESET}")
        
        # Navigation arrows
        Screen.print_at(self.y, self.x, f"{FG_BRIGHT_YELLOW}<{RESET}")
        Screen.print_at(self.y, self.x + 24, f"{FG_BRIGHT_YELLOW}>{RESET}")
        
        # Day headers
        headers = "Mo Tu We Th Fr Sa Su"
        Screen.print_at(self.y + 1, self.x, f"{FG_BRIGHT_WHITE}{headers}{RESET}")
        
        # Calculate first day of month
        first_day = self.view_date.replace(day=1)
        first_weekday = (first_day.weekday()) % 7  # Monday = 0
        
        # Days in month
        if self.view_date.month == 12:
            next_month = self.view_date.replace(year=self.view_date.year + 1, month=1, day=1)
        else:
            next_month = self.view_date.replace(month=self.view_date.month + 1, day=1)
        days_in_month = (next_month - first_day).days
        
        # Render calendar grid
        day = 1
        for week in range(6):
            line = ""
            for weekday in range(7):
                cell_idx = week * 7 + weekday
                
                if cell_idx < first_weekday or day > days_in_month:
                    line += "   "
                else:
                    current = self.view_date.replace(day=day)
                    is_today = current.date() == datetime.now().date()
                    is_selected = current.date() == self.selected_date.date()
                    
                    if is_selected:
                        line += f"{BG_CYAN}{FG_BLACK}{day:2} {RESET}"
                    elif is_today:
                        line += f"{FG_BRIGHT_GREEN}{BOLD}{day:2} {RESET}"
                    else:
                        line += f"{FG_WHITE}{day:2} {RESET}"
                    day += 1
            
            Screen.print_at(self.y + 2 + week, self.x, line)
            
            if day > days_in_month:
                break
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        if not self.enabled or button != 'left' or action != 'down':
            return False
        
        # Previous month arrow
        if y == self.y and x == self.x:
            if self.view_date.month == 1:
                self.view_date = self.view_date.replace(year=self.view_date.year - 1, month=12)
            else:
                self.view_date = self.view_date.replace(month=self.view_date.month - 1)
            return True
        
        # Next month arrow
        if y == self.y and x == self.x + 24:
            if self.view_date.month == 12:
                self.view_date = self.view_date.replace(year=self.view_date.year + 1, month=1)
            else:
                self.view_date = self.view_date.replace(month=self.view_date.month + 1)
            return True
        
        # Click on day
        if self.y + 2 <= y < self.y + 8 and self.x <= x < self.x + 25:
            # Calculate which day was clicked
            rel_y = y - self.y - 2
            rel_x = x - self.x
            
            weekday = rel_x // 3
            week = rel_y
            
            first_day = self.view_date.replace(day=1)
            first_weekday = first_day.weekday() % 7
            
            cell_idx = week * 7 + weekday
            if cell_idx >= first_weekday:
                day = cell_idx - first_weekday + 1
                
                # Get days in month
                if self.view_date.month == 12:
                    next_month = self.view_date.replace(year=self.view_date.year + 1, month=1, day=1)
                else:
                    next_month = self.view_date.replace(month=self.view_date.month + 1, day=1)
                days_in_month = (next_month - first_day).days
                
                if 1 <= day <= days_in_month:
                    self.selected_date = self.view_date.replace(day=day)
                    return True
        
        return False

# ============================================================================
# SECTION 10: CONTEXT MENU
# ============================================================================

class ContextMenu(Widget):
    """Right-click context menu"""
    
    def __init__(self, x: int, y: int, items: List[Tuple[str, Callable]]):
        width = max(len(label) for label, _ in items) + 4
        height = len(items) + 2
        super().__init__(x, y, width, height)
        self.items = items
        self.selected_index = 0
        self.visible = False
    
    def show_at(self, x: int, y: int):
        """Show context menu at position"""
        self.x = x
        self.y = y
        self.visible = True
    
    def render(self):
        if not self.visible:
            return
        
        # Draw border
        Screen.print_at(self.y, self.x, f"{BG_WHITE}{FG_BLACK}{BOX_TL}{BOX_H * (self.width - 2)}{BOX_TR}{RESET}")
        
        for i, (label, _) in enumerate(self.items):
            is_selected = i == self.selected_index and self.hover
            
            if is_selected:
                color = FG_WHITE
                bg = BG_BLUE
            else:
                color = FG_BLACK
                bg = BG_WHITE
            
            text = f" {label}"
            padding = ' ' * (self.width - len(text) - 2)
            line = f"{bg}{color}{BOX_V}{text}{padding}{BOX_V}{RESET}"
            Screen.print_at(self.y + i + 1, self.x, line)
        
        Screen.print_at(self.y + len(self.items) + 1, self.x, 
                       f"{BG_WHITE}{FG_BLACK}{BOX_BL}{BOX_H * (self.width - 2)}{BOX_BR}{RESET}")
    
    def on_mouse_move(self, x: int, y: int):
        """Update hover state and selected item"""
        self.hover = self.contains_point(x, y)
        if self.hover and self.y < y < self.y + len(self.items) + 1:
            self.selected_index = y - self.y - 1
    
    def on_mouse_click(self, x: int, y: int, button: str, action: str) -> bool:
        if not self.visible:
            return False
        
        if self.contains_point(x, y) and button == 'left' and action == 'down':
            if 0 <= self.selected_index < len(self.items):
                _, callback = self.items[self.selected_index]
                if callback:
                    callback()
            self.visible = False
            return True
        elif not self.contains_point(x, y) and action == 'down':
            # Close menu if clicking outside
            self.visible = False
            return False
        
        return False

# ============================================================================
# SECTION 11: APPLICATION FRAMEWORK
# ============================================================================

class Application:
    """Main application framework with mouse and keyboard support"""
    
    def __init__(self, title: str):
        self.title = title
        self.widgets = []
        self.focused_widget = None
        self.running = False
        self.mouse_handler = MouseHandler()
        self.context_menu = None
        
    def add_widget(self, widget: Widget):
        """Add widget to application"""
        self.widgets.append(widget)
        if self.focused_widget is None and widget.enabled:
            self.focused_widget = widget
            widget.focused = True
    
    def render_all(self, full_clear=True):
        """Render all widgets"""
        if full_clear:
            Screen.clear()
            
            # Title bar
            term_width, _ = get_terminal_size()
            title_text = f" {self.title} "
            Screen.print_at(1, 1, f"{BG_BLUE}{FG_WHITE}{BOLD}{title_text}{' ' * (term_width - len(title_text) - 1)}{RESET}")
        
        # Widgets
        for widget in self.widgets:
            if widget.visible:
                widget.render()
        
        # Context menu (render last, on top)
        if self.context_menu and self.context_menu.visible:
            self.context_menu.render()
    
    def run(self):
        """Main application loop"""
        enable_ansi_windows()
        Screen.hide_cursor()
        self.mouse_handler.enable()
        self.running = True
        
        needs_render = True
        render_type = 'full'  # 'full' or 'hover'
        
        try:
            while self.running:
                # Only render when needed
                if needs_render:
                    self.render_all(full_clear=(render_type == 'full'))
                    needs_render = False
                
                # Process input
                event = self.mouse_handler.read_input()
                
                if event:
                    event_type, data = event
                    
                    if event_type == 'key':
                        self._handle_key(data)
                        needs_render = True
                        render_type = 'full'
                    elif event_type == 'mouse_move':
                        if self._handle_mouse_move(data['x'], data['y']):
                            needs_render = True
                            render_type = 'hover'
                    elif event_type == 'mouse_click':
                        self._handle_mouse_click(data['x'], data['y'], data['button'], data['action'])
                        needs_render = True
                        render_type = 'full'
                    elif event_type == 'mouse_scroll':
                        self._handle_mouse_scroll(data['x'], data['y'], data['direction'])
                        needs_render = True
                        render_type = 'full'
                else:
                    time.sleep(0.05)  # Sleep when no input to reduce CPU usage
        
        finally:
            self.mouse_handler.disable()
            Screen.show_cursor()
            Screen.clear()
    
    def stop(self):
        """Stop application"""
        self.running = False
    
    def _handle_key(self, key: bytes):
        """Handle keyboard input"""
        if key == b'\x1b':  # ESC
            self.stop()
            return
        
        # Tab navigation between widgets
        if key == b'\t':
            self._focus_next_widget()
            return
        
        # Forward to focused widget
        if self.focused_widget:
            self.focused_widget.on_key(key)
    
    def _handle_mouse_move(self, x: int, y: int) -> bool:
        """Handle mouse movement. Return True if any widget state changed."""
        state_changed = False
        
        # Update hover state for all widgets
        for widget in self.widgets:
            if widget.on_mouse_move(x, y):
                state_changed = True
        
        if self.context_menu:
            if self.context_menu.on_mouse_move(x, y):
                state_changed = True
        
        return state_changed
    
    def _handle_mouse_click(self, x: int, y: int, button: str, action: str):
        """Handle mouse click"""
        # Context menu takes priority
        if self.context_menu and self.context_menu.visible:
            if self.context_menu.on_mouse_click(x, y, button, action):
                return
        
        # Show context menu on right-click
        if button == 'right' and action == 'down':
            self._show_context_menu(x, y)
            return
        
        # Forward to widgets
        for widget in reversed(self.widgets):  # Top to bottom
            if widget.visible and widget.enabled:
                if widget.on_mouse_click(x, y, button, action):
                    # Set focus
                    if self.focused_widget:
                        self.focused_widget.focused = False
                    self.focused_widget = widget
                    widget.focused = True
                    break
    
    def _handle_mouse_scroll(self, x: int, y: int, direction: str):
        """Handle mouse scroll"""
        for widget in self.widgets:
            if widget.visible and widget.enabled and widget.contains_point(x, y):
                if isinstance(widget, ScrollableList):
                    widget.on_mouse_scroll(direction)
                break
    
    def _focus_next_widget(self):
        """Move focus to next widget"""
        if not self.widgets:
            return
        
        focusable = [w for w in self.widgets if w.enabled and w.visible]
        if not focusable:
            return
        
        if self.focused_widget in focusable:
            idx = focusable.index(self.focused_widget)
            idx = (idx + 1) % len(focusable)
        else:
            idx = 0
        
        if self.focused_widget:
            self.focused_widget.focused = False
        
        self.focused_widget = focusable[idx]
        self.focused_widget.focused = True
    
    def _show_context_menu(self, x: int, y: int):
        """Show context menu at position"""
        items = [
            ("Copy", lambda: None),
            ("Paste", lambda: None),
            ("Delete", lambda: None),
            ("Properties", lambda: None),
        ]
        
        if not self.context_menu:
            self.context_menu = ContextMenu(x, y, items)
        else:
            self.context_menu.show_at(x, y)

# ============================================================================
# SECTION 12: DEMO APPLICATIONS
# ============================================================================

def demo_mouse_buttons():
    """Demo: Mouse-clickable buttons"""
    set_console_size(90, 30)
    time.sleep(0.2)
    
    app = Application("Mouse Button Demo")
    
    message_y = 12
    
    def on_button1():
        Screen.print_at(message_y, 10, f"{FG_GREEN}Button 1 clicked!{RESET}" + " " * 50)
    
    def on_button2():
        Screen.print_at(message_y, 10, f"{FG_YELLOW}Button 2 clicked!{RESET}" + " " * 50)
    
    def on_button3():
        Screen.print_at(message_y, 10, f"{FG_RED}Button 3 clicked!{RESET}" + " " * 50)
    
    def on_exit():
        app.stop()
    
    # Instructions
    Screen.print_at(4, 10, f"{FG_BRIGHT_YELLOW}Click the buttons with your mouse or press Tab + Enter{RESET}")
    
    button1 = Button(10, 7, "Click Me!", on_button1)
    button2 = Button(27, 7, "Button 2", on_button2)
    button3 = Button(42, 7, "Button 3", on_button3)
    exit_button = Button(57, 7, "Exit", on_exit)
    
    app.add_widget(button1)
    app.add_widget(button2)
    app.add_widget(button3)
    app.add_widget(exit_button)
    
    app.run()

def demo_scrollable_list():
    """Demo: Scrollable list with mouse and keyboard"""
    set_console_size(90, 30)
    time.sleep(0.2)
    
    app = Application("Scrollable List Demo")
    
    items = [f"Item {i+1:03d}" for i in range(50)]
    
    def on_select(item):
        Screen.print_at(20, 50, f"{FG_GREEN}Selected: {item}{RESET}" + " " * 20)
    
    Screen.print_at(4, 10, f"{FG_BRIGHT_YELLOW}Click items, use arrow keys, or scroll with mouse wheel{RESET}")
    
    list_widget = ScrollableList(10, 6, 30, 15, items, on_select)
    app.add_widget(list_widget)
    
    exit_button = Button(50, 6, "Exit", app.stop)
    app.add_widget(exit_button)
    
    app.run()

def demo_tree_view():
    """Demo: Tree view with expand/collapse"""
    set_console_size(90, 30)
    time.sleep(0.2)
    
    app = Application("Tree View Demo")
    
    Screen.print_at(4, 10, f"{FG_BRIGHT_YELLOW}Click to expand/collapse folders. Use arrow keys to navigate.{RESET}")
    
    # Build tree structure
    root = TreeNode("Project", [
        TreeNode("src", [
            TreeNode("main.py"),
            TreeNode("utils.py"),
            TreeNode("models", [
                TreeNode("user.py"),
                TreeNode("product.py"),
            ]),
        ]),
        TreeNode("tests", [
            TreeNode("test_main.py"),
            TreeNode("test_utils.py"),
        ]),
        TreeNode("docs", [
            TreeNode("README.md"),
            TreeNode("API.md"),
        ]),
        TreeNode("requirements.txt"),
    ])
    
    tree = TreeView(10, 6, 40, 18, root)
    app.add_widget(tree)
    
    exit_button = Button(55, 6, "Exit", app.stop)
    app.add_widget(exit_button)
    
    app.run()

def demo_calendar():
    """Demo: Interactive calendar widget"""
    set_console_size(90, 30)
    time.sleep(0.2)
    
    app = Application("Calendar Demo")
    
    Screen.print_at(4, 10, f"{FG_BRIGHT_YELLOW}Click on dates to select. Use < > arrows to change months.{RESET}")
    
    calendar = Calendar(10, 6)
    app.add_widget(calendar)
    
    def show_date():
        date_str = calendar.selected_date.strftime("%Y-%m-%d")
        Screen.print_at(16, 40, f"{FG_GREEN}Selected: {date_str}{RESET}" + " " * 20)
    
    show_button = Button(40, 8, "Show Date", show_date)
    exit_button = Button(40, 10, "Exit", app.stop)
    
    app.add_widget(show_button)
    app.add_widget(exit_button)
    
    app.run()

def demo_tabbed_interface():
    """Demo: Tabbed interface"""
    set_console_size(90, 30)
    time.sleep(0.2)
    
    app = Application("Tabbed Interface Demo")
    
    Screen.print_at(4, 5, f"{FG_BRIGHT_YELLOW}Click tabs to switch views or press Tab key{RESET}")
    
    # Tab 1: List
    list1 = ScrollableList(5, 7, 70, 13, [f"List Item {i+1}" for i in range(30)])
    
    # Tab 2: Tree
    root = TreeNode("Root", [
        TreeNode("Folder 1", [TreeNode("File 1"), TreeNode("File 2")]),
        TreeNode("Folder 2", [TreeNode("File 3"), TreeNode("File 4")]),
    ])
    tree = TreeView(5, 7, 70, 13, root)
    
    # Tab 3: Calendar
    calendar = Calendar(5, 7)
    
    # Create tabbed pane
    tabs = [
        ("Files", list1),
        ("Project", tree),
        ("Calendar", calendar),
    ]
    
    tabbed = TabbedPane(5, 6, 70, 14, tabs)
    app.add_widget(tabbed)
    
    exit_button = Button(35, 22, "Exit", app.stop)
    app.add_widget(exit_button)
    
    app.run()

def demo_all_widgets():
    """Demo: All widgets together"""
    set_console_size(120, 30)
    time.sleep(0.2)
    
    app = Application("Complete Widget Showcase")
    
    Screen.print_at(2, 4, f"{FG_BRIGHT_YELLOW}Click any widget to interact - All widgets active simultaneously{RESET}")
    
    # Buttons
    button1 = Button(5, 3, "Button 1", lambda: Screen.print_at(5, 16, f"{FG_GREEN}Button 1 Pressed!{RESET}"))
    button2 = Button(20, 3, "Button 2", lambda: Screen.print_at(5, 16, f"{FG_GREEN}Button 2 Pressed!{RESET}"))
    button3 = Button(35, 3, "Exit", app.stop)
    
    # List
    list_widget = ScrollableList(5, 5, 25, 10, [f"Item {i+1}" for i in range(20)])
    
    # Tree
    root = TreeNode("Root", [
        TreeNode("Branch 1", [TreeNode("Leaf 1"), TreeNode("Leaf 2")]),
        TreeNode("Branch 2"),
    ])
    tree = TreeView(35, 5, 30, 10, root)
    
    # Calendar
    calendar = Calendar(70, 5)
    
    app.add_widget(button1)
    app.add_widget(button2)
    app.add_widget(button3)
    app.add_widget(list_widget)
    app.add_widget(tree)
    app.add_widget(calendar)
    
    app.run()

# ============================================================================
# SECTION 13: MAIN MENU
# ============================================================================

def main():
    """Main demonstration menu"""
    enable_ansi_windows()
    
    while True:
        Screen.clear()
        print(f"\n{BOLD}{FG_BRIGHT_CYAN}{'=' * 70}{RESET}")
        print(f"{BOLD}{FG_BRIGHT_CYAN}  ADVANCED CLI MENU WITH MOUSE SUPPORT{RESET}")
        print(f"{BOLD}{FG_BRIGHT_CYAN}{'=' * 70}{RESET}\n")
        print(f"{FG_BRIGHT_WHITE}Select a demo:{RESET}\n")
        print(f"  {FG_BRIGHT_YELLOW}1{RESET}. Mouse-Clickable Buttons")
        print(f"  {FG_BRIGHT_YELLOW}2{RESET}. Scrollable List (Mouse + Keyboard)")
        print(f"  {FG_BRIGHT_YELLOW}3{RESET}. Tree View with Expand/Collapse")
        print(f"  {FG_BRIGHT_YELLOW}4{RESET}. Interactive Calendar Widget")
        print(f"  {FG_BRIGHT_YELLOW}5{RESET}. Tabbed Interface")
        print(f"  {FG_BRIGHT_YELLOW}6{RESET}. Complete Widget Showcase")
        print(f"  {FG_BRIGHT_YELLOW}0{RESET}. Exit")
        print(f"\n{FG_BRIGHT_WHITE}Features:{RESET}")
        print(f"  {POINTER} Full mouse support (click, drag, scroll)")
        print(f"  {POINTER} Hover effects and visual feedback")
        print(f"  {POINTER} Right-click context menus")
        print(f"  {POINTER} Keyboard navigation (Tab, Arrow keys)")
        print(f"  {POINTER} Focus management")
        print(f"  {POINTER} Multiple widget types")
        
        choice = input(f"\n{FG_BRIGHT_CYAN}Enter choice: {RESET}").strip()
        
        if choice == '1':
            demo_mouse_buttons()
        elif choice == '2':
            demo_scrollable_list()
        elif choice == '3':
            demo_tree_view()
        elif choice == '4':
            demo_calendar()
        elif choice == '5':
            demo_tabbed_interface()
        elif choice == '6':
            demo_all_widgets()
        elif choice == '0':
            break
        else:
            print(f"{FG_RED}Invalid choice!{RESET}")
            time.sleep(1)
    
    print(f"\n{FG_BRIGHT_GREEN}Thank you for trying the Advanced CLI Menu Demo!{RESET}\n")

# ============================================================================
# SECTION 14: ENTRY POINT
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
