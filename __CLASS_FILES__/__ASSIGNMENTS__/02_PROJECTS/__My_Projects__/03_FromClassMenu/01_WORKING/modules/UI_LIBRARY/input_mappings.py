"""
Input Mappings Module
Platform-specific input handling for Windows (msvcrt/ctypes) and Linux (curses)
"""

import sys
from abc import ABC, abstractmethod
from typing import Optional, Tuple, Dict, Any

IS_WINDOWS = sys.platform == 'win32'
IS_UNIX = not IS_WINDOWS


# ═══════════════════════════════════════════════════════════════════════════
# BASE INPUT MAPPER (Abstract)
# ═══════════════════════════════════════════════════════════════════════════

class InputMapper(ABC):
    """Abstract base class for platform-specific input mapping"""
    
    @abstractmethod
    def initialize(self):
        """Initialize input system"""
        pass
    
    @abstractmethod
    def cleanup(self):
        """Cleanup and restore input system"""
        pass
    
    @abstractmethod
    def read_key(self) -> Optional[str]:
        """Read keyboard input, return key name or None"""
        pass
    
    @abstractmethod
    def has_input(self) -> bool:
        """Check if input is available (non-blocking)"""
        pass
    
    @abstractmethod
    def read_mouse_event(self) -> Optional[Dict[str, Any]]:
        """Read mouse event, return dict with event data or None"""
        pass


# ═══════════════════════════════════════════════════════════════════════════
# WINDOWS INPUT MAPPER (msvcrt + ctypes)
# ═══════════════════════════════════════════════════════════════════════════

class WindowsInputMapper(InputMapper):
    """Windows input mapper using msvcrt and ctypes Console API"""
    
    # Key code mappings (msvcrt two-byte sequences)
    KEY_CODES = {
        b'H': 'UP',
        b'P': 'DOWN',
        b'K': 'LEFT',
        b'M': 'RIGHT',
        b'G': 'HOME',
        b'O': 'END',
        b'I': 'PAGE_UP',
        b'Q': 'PAGE_DOWN',
        b'R': 'INSERT',
        b'S': 'DELETE',
        b';': 'F1',
        b'<': 'F2',
        b'=': 'F3',
        b'>': 'F4',
        b'?': 'F5',
        b'@': 'F6',
        b'A': 'F7',
        b'B': 'F8',
        b'C': 'F9',
        b'D': 'F10',
    }
    
    # Single-byte special keys
    SPECIAL_KEYS = {
        b'\r': 'ENTER',
        b'\n': 'ENTER',
        b'\x1b': 'ESC',
        b' ': 'SPACE',
        b'\t': 'TAB',
        b'\x08': 'BACKSPACE',
    }
    
    def __init__(self):
        self.kernel32 = None
        self.stdin_handle = None
        self.stdout_handle = None
        self.original_mode = None
        
    def initialize(self):
        """Initialize Windows Console API"""
        import msvcrt
        import ctypes
        from ctypes import wintypes
        
        self.msvcrt = msvcrt
        self.kernel32 = ctypes.windll.kernel32
        
        # Get handles
        self.stdin_handle = self.kernel32.GetStdHandle(-10)
        self.stdout_handle = self.kernel32.GetStdHandle(-11)
        
        # Save original mode
        self.original_mode = wintypes.DWORD()
        self.kernel32.GetConsoleMode(self.stdin_handle, ctypes.byref(self.original_mode))
        
        # Enable ANSI escape sequences
        stdout_mode = wintypes.DWORD()
        self.kernel32.GetConsoleMode(self.stdout_handle, ctypes.byref(stdout_mode))
        stdout_mode.value |= 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
        self.kernel32.SetConsoleMode(self.stdout_handle, stdout_mode.value)
        
        # Enable mouse input, disable QuickEdit
        stdin_mode = wintypes.DWORD()
        self.kernel32.GetConsoleMode(self.stdin_handle, ctypes.byref(stdin_mode))
        stdin_mode.value |= 0x0010   # ENABLE_MOUSE_INPUT
        stdin_mode.value |= 0x0080   # ENABLE_EXTENDED_FLAGS
        stdin_mode.value &= ~0x0040  # Disable ENABLE_QUICK_EDIT_MODE
        self.kernel32.SetConsoleMode(self.stdin_handle, stdin_mode.value)
        
    def cleanup(self):
        """Restore original console mode"""
        if self.kernel32 and self.stdin_handle and self.original_mode:
            self.kernel32.SetConsoleMode(self.stdin_handle, self.original_mode)
    
    def has_input(self) -> bool:
        """Check if any console input is available"""
        import ctypes
        from ctypes import wintypes
        
        # Check number of console input events
        num_events = wintypes.DWORD()
        self.kernel32.GetNumberOfConsoleInputEvents(
            self.stdin_handle,
            ctypes.byref(num_events)
        )
        return num_events.value > 0
    
    def read_key(self) -> Optional[str]:
        """Read keyboard input and map to key name"""
        import ctypes
        from ctypes import wintypes
        
        # Check for keyboard using msvcrt (faster for pure keyboard)
        if self.msvcrt.kbhit():
            key = self.msvcrt.getch()
            
            # Check for special single-byte keys
            if key in self.SPECIAL_KEYS:
                return self.SPECIAL_KEYS[key]
            
            # Check for two-byte special keys (arrows, function keys)
            if key in (b'\xe0', b'\x00'):
                if self.msvcrt.kbhit():
                    second_byte = self.msvcrt.getch()
                    return self.KEY_CODES.get(second_byte, f'UNKNOWN_{second_byte.hex()}')
                return None
            
            # Regular character
            try:
                return key.decode('utf-8')
            except UnicodeDecodeError:
                return None
        
        # Check console input for keyboard events (in case msvcrt missed it)
        class KEY_EVENT_RECORD(ctypes.Structure):
            class _CHAR_UNION(ctypes.Union):
                _fields_ = [('UnicodeChar', wintypes.WCHAR), ('AsciiChar', wintypes.CHAR)]
            
            _fields_ = [
                ('bKeyDown', wintypes.BOOL),
                ('wRepeatCount', wintypes.WORD),
                ('wVirtualKeyCode', wintypes.WORD),
                ('wVirtualScanCode', wintypes.WORD),
                ('uChar', _CHAR_UNION),
                ('dwControlKeyState', wintypes.DWORD)
            ]
        
        class INPUT_RECORD(ctypes.Structure):
            class _EVENT(ctypes.Union):
                _fields_ = [('KeyEvent', KEY_EVENT_RECORD)]
            _fields_ = [('EventType', wintypes.WORD), ('Event', _EVENT)]
        
        # Peek at console input
        input_record = INPUT_RECORD()
        events_read = wintypes.DWORD()
        
        if self.kernel32.PeekConsoleInputW(
            self.stdin_handle,
            ctypes.byref(input_record),
            1,
            ctypes.byref(events_read)
        ):
            if events_read.value > 0 and input_record.EventType == 1:  # KEY_EVENT
                # It's a keyboard event, consume it
                self.kernel32.ReadConsoleInputW(
                    self.stdin_handle,
                    ctypes.byref(input_record),
                    1,
                    ctypes.byref(events_read)
                )
                
                key_event = input_record.Event.KeyEvent
                if key_event.bKeyDown:  # Only process key press, not release
                    char = key_event.uChar.UnicodeChar
                    vk_code = key_event.wVirtualKeyCode
                    
                    # Map virtual key codes to key names
                    VK_CODES = {
                        0x0D: 'ENTER',
                        0x1B: 'ESC',
                        0x20: 'SPACE',
                        0x08: 'BACKSPACE',
                        0x09: 'TAB',
                        0x25: 'LEFT',
                        0x26: 'UP',
                        0x27: 'RIGHT',
                        0x28: 'DOWN',
                        0x21: 'PAGE_UP',
                        0x22: 'PAGE_DOWN',
                        0x23: 'END',
                        0x24: 'HOME',
                        0x2D: 'INSERT',
                        0x2E: 'DELETE',
                        0x70: 'F1',
                        0x71: 'F2',
                        0x72: 'F3',
                        0x73: 'F4',
                        0x74: 'F5',
                        0x75: 'F6',
                        0x76: 'F7',
                        0x77: 'F8',
                        0x78: 'F9',
                        0x79: 'F10',
                        0x7A: 'F11',
                        0x7B: 'F12',
                    }
                    
                    if vk_code in VK_CODES:
                        return VK_CODES[vk_code]
                    elif char and char != '\x00':
                        return char
        
        return None
    
    def read_mouse_event(self) -> Optional[Dict[str, Any]]:
        """Read mouse event from Windows Console API"""
        import ctypes
        from ctypes import wintypes
        
        # Define structures
        class COORD(ctypes.Structure):
            _fields_ = [('X', ctypes.c_short), ('Y', ctypes.c_short)]
        
        class MOUSE_EVENT_RECORD(ctypes.Structure):
            _fields_ = [
                ('dwMousePosition', COORD),
                ('dwButtonState', wintypes.DWORD),
                ('dwControlKeyState', wintypes.DWORD),
                ('dwEventFlags', wintypes.DWORD)
            ]
        
        class INPUT_RECORD(ctypes.Structure):
            class _EVENT(ctypes.Union):
                _fields_ = [('MouseEvent', MOUSE_EVENT_RECORD)]
            _fields_ = [('EventType', wintypes.WORD), ('Event', _EVENT)]
        
        # Peek at console input first to see if it's a mouse event
        input_record = INPUT_RECORD()
        events_read = wintypes.DWORD()
        
        if self.kernel32.PeekConsoleInputW(
            self.stdin_handle,
            ctypes.byref(input_record),
            1,
            ctypes.byref(events_read)
        ):
            if events_read.value > 0:
                if input_record.EventType == 2:  # MOUSE_EVENT
                    # It's a mouse event, consume it
                    self.kernel32.ReadConsoleInputW(
                        self.stdin_handle,
                        ctypes.byref(input_record),
                        1,
                        ctypes.byref(events_read)
                    )
                    
                    mouse = input_record.Event.MouseEvent
                    
                    # Convert 0-based to 1-based coordinates
                    x = mouse.dwMousePosition.X + 1
                    y = mouse.dwMousePosition.Y + 1
                    
                    # Parse button state
                    button = None
                    if mouse.dwButtonState & 0x0001:
                        button = 'LEFT'
                    elif mouse.dwButtonState & 0x0002:
                        button = 'RIGHT'
                    elif mouse.dwButtonState & 0x0004:
                        button = 'MIDDLE'
                    
                    # Parse event type
                    event_type = 'CLICK'
                    if mouse.dwEventFlags & 0x0001:
                        event_type = 'MOVE'
                    elif mouse.dwEventFlags & 0x0002:
                        event_type = 'DOUBLE_CLICK'
                    elif mouse.dwEventFlags & 0x0004:
                        event_type = 'WHEEL'
                    
                    return {
                        'x': x,
                        'y': y,
                        'button': button,
                        'event_type': event_type,
                        'raw_button_state': mouse.dwButtonState,
                        'raw_event_flags': mouse.dwEventFlags
                    }
                elif input_record.EventType == 1:  # KEY_EVENT
                    # It's a keyboard event, don't consume it here
                    # Let read_key handle it
                    return None
                else:
                    # Other event type, consume and ignore
                    self.kernel32.ReadConsoleInputW(
                        self.stdin_handle,
                        ctypes.byref(input_record),
                        1,
                        ctypes.byref(events_read)
                    )
        
        return None


# ═══════════════════════════════════════════════════════════════════════════
# LINUX/UNIX INPUT MAPPER (curses)
# ═══════════════════════════════════════════════════════════════════════════

class UnixInputMapper(InputMapper):
    """Unix/Linux input mapper using curses"""
    
    # Curses key code mappings
    KEY_NAMES = {}  # Will be populated after curses import
    
    def __init__(self, stdscr=None):
        self.stdscr = stdscr
        self.curses = None
        
    def initialize(self):
        """Initialize curses (should be called within curses.wrapper)"""
        import curses
        self.curses = curses
        
        # Populate key mappings
        self.KEY_NAMES = {
            curses.KEY_UP: 'UP',
            curses.KEY_DOWN: 'DOWN',
            curses.KEY_LEFT: 'LEFT',
            curses.KEY_RIGHT: 'RIGHT',
            curses.KEY_HOME: 'HOME',
            curses.KEY_END: 'END',
            curses.KEY_PPAGE: 'PAGE_UP',
            curses.KEY_NPAGE: 'PAGE_DOWN',
            curses.KEY_IC: 'INSERT',
            curses.KEY_DC: 'DELETE',
            curses.KEY_BACKSPACE: 'BACKSPACE',
            curses.KEY_ENTER: 'ENTER',
            ord('\n'): 'ENTER',
            ord('\r'): 'ENTER',
            27: 'ESC',
            ord(' '): 'SPACE',
            ord('\t'): 'TAB',
            curses.KEY_F1: 'F1',
            curses.KEY_F2: 'F2',
            curses.KEY_F3: 'F3',
            curses.KEY_F4: 'F4',
            curses.KEY_F5: 'F5',
            curses.KEY_F6: 'F6',
            curses.KEY_F7: 'F7',
            curses.KEY_F8: 'F8',
            curses.KEY_F9: 'F9',
            curses.KEY_F10: 'F10',
            curses.KEY_F11: 'F11',
            curses.KEY_F12: 'F12',
            curses.KEY_MOUSE: 'MOUSE',
        }
        
        if self.stdscr:
            # Setup curses
            self.curses.curs_set(0)  # Hide cursor
            self.curses.noecho()
            self.curses.cbreak()
            self.stdscr.keypad(True)
            self.stdscr.nodelay(True)  # Non-blocking
            
            # Enable colors
            if self.curses.has_colors():
                self.curses.start_color()
                self.curses.use_default_colors()
            
            # Enable mouse
            self.curses.mousemask(
                self.curses.ALL_MOUSE_EVENTS | 
                self.curses.REPORT_MOUSE_POSITION
            )
    
    def cleanup(self):
        """Cleanup curses (handled by wrapper)"""
        if self.stdscr:
            self.stdscr.keypad(False)
            self.curses.nocbreak()
            self.curses.echo()
            self.curses.curs_set(1)
    
    def set_stdscr(self, stdscr):
        """Set the curses stdscr object"""
        self.stdscr = stdscr
    
    def has_input(self) -> bool:
        """Check if input is available"""
        if not self.stdscr:
            return False
        
        key = self.stdscr.getch()
        if key != -1:
            self.curses.ungetch(key)  # Put it back
            return True
        return False
    
    def read_key(self) -> Optional[str]:
        """Read keyboard input and map to key name"""
        if not self.stdscr:
            return None
        
        key = self.stdscr.getch()
        
        if key == -1:  # No input
            return None
        
        # Check if it's a mapped key
        if key in self.KEY_NAMES:
            key_name = self.KEY_NAMES[key]
            # Skip mouse events in key reading
            if key_name == 'MOUSE':
                return None
            return key_name
        
        # Regular character
        if 32 <= key <= 126:  # Printable ASCII
            return chr(key)
        
        return None
    
    def read_mouse_event(self) -> Optional[Dict[str, Any]]:
        """Read mouse event from curses"""
        if not self.stdscr or not self.curses:
            return None
        
        key = self.stdscr.getch()
        
        if key == self.curses.KEY_MOUSE:
            try:
                _, x, y, z, bstate = self.curses.getmouse()
                
                # Parse button
                button = None
                if bstate & (self.curses.BUTTON1_PRESSED | self.curses.BUTTON1_CLICKED):
                    button = 'LEFT'
                elif bstate & (self.curses.BUTTON2_PRESSED | self.curses.BUTTON2_CLICKED):
                    button = 'MIDDLE'
                elif bstate & (self.curses.BUTTON3_PRESSED | self.curses.BUTTON3_CLICKED):
                    button = 'RIGHT'
                elif bstate & self.curses.BUTTON4_PRESSED:
                    button = 'WHEEL_UP'
                elif bstate & self.curses.BUTTON5_PRESSED:
                    button = 'WHEEL_DOWN'
                
                # Parse event type
                event_type = 'CLICK'
                if bstate & (self.curses.BUTTON1_DOUBLE_CLICKED | 
                           self.curses.BUTTON2_DOUBLE_CLICKED | 
                           self.curses.BUTTON3_DOUBLE_CLICKED):
                    event_type = 'DOUBLE_CLICK'
                elif bstate & self.curses.REPORT_MOUSE_POSITION:
                    event_type = 'MOVE'
                elif button in ('WHEEL_UP', 'WHEEL_DOWN'):
                    event_type = 'WHEEL'
                
                # Curses coordinates are already 0-based, add 1 for consistency
                return {
                    'x': x + 1,
                    'y': y + 1,
                    'button': button,
                    'event_type': event_type,
                    'raw_bstate': bstate
                }
            except self.curses.error:
                return None
        
        # Put non-mouse key back
        if key != -1:
            self.curses.ungetch(key)
        
        return None


# ═══════════════════════════════════════════════════════════════════════════
# FACTORY FUNCTION
# ═══════════════════════════════════════════════════════════════════════════

def create_input_mapper(stdscr=None) -> InputMapper:
    """
    Factory function to create appropriate input mapper for current platform
    
    Args:
        stdscr: Curses stdscr object (required for Unix)
    
    Returns:
        Platform-specific InputMapper instance
    """
    if IS_WINDOWS:
        return WindowsInputMapper()
    else:
        return UnixInputMapper(stdscr)
