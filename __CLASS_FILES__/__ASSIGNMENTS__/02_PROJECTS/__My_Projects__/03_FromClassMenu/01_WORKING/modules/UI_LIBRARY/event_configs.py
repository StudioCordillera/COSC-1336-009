"""
Event Interaction Configs Module
Platform-specific event handling configurations for Windows and Linux
"""

import sys
from typing import Dict, Callable, Any, Optional
from dataclasses import dataclass, field

IS_WINDOWS = sys.platform == 'win32'
IS_UNIX = not IS_WINDOWS


# ═══════════════════════════════════════════════════════════════════════════
# EVENT DATA CLASSES
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class KeyEvent:
    """Standardized keyboard event"""
    key: str
    modifiers: list = field(default_factory=list)  # ['ctrl', 'shift', 'alt']
    raw_code: Any = None
    platform: str = 'unknown'


@dataclass
class MouseEvent:
    """Standardized mouse event"""
    x: int
    y: int
    button: Optional[str] = None  # 'LEFT', 'RIGHT', 'MIDDLE', 'WHEEL_UP', 'WHEEL_DOWN'
    event_type: str = 'CLICK'  # 'CLICK', 'DOUBLE_CLICK', 'MOVE', 'WHEEL'
    modifiers: list = field(default_factory=list)
    raw_data: Any = None
    platform: str = 'unknown'


# ═══════════════════════════════════════════════════════════════════════════
# BASE EVENT CONFIG
# ═══════════════════════════════════════════════════════════════════════════

class EventConfig:
    """Base event configuration with handler mappings"""
    
    def __init__(self):
        self.key_handlers: Dict[str, Callable] = {}
        self.mouse_handlers: Dict[str, Callable] = {}
        self.default_key_handler: Optional[Callable] = None
        self.default_mouse_handler: Optional[Callable] = None
        
    def register_key_handler(self, key: str, handler: Callable):
        """Register a handler for a specific key"""
        self.key_handlers[key] = handler
    
    def register_mouse_handler(self, event_type: str, handler: Callable):
        """Register a handler for a specific mouse event type"""
        self.mouse_handlers[event_type] = handler
    
    def set_default_key_handler(self, handler: Callable):
        """Set default handler for unregistered keys"""
        self.default_key_handler = handler
    
    def set_default_mouse_handler(self, handler: Callable):
        """Set default handler for unregistered mouse events"""
        self.default_mouse_handler = handler
    
    def handle_key_event(self, event: KeyEvent) -> bool:
        """
        Process keyboard event
        Returns True if event was handled, False otherwise
        """
        handler = self.key_handlers.get(event.key, self.default_key_handler)
        if handler:
            handler(event)
            return True
        return False
    
    def handle_mouse_event(self, event: MouseEvent) -> bool:
        """
        Process mouse event
        Returns True if event was handled, False otherwise
        """
        handler = self.mouse_handlers.get(event.event_type, self.default_mouse_handler)
        if handler:
            handler(event)
            return True
        return False


# ═══════════════════════════════════════════════════════════════════════════
# WINDOWS EVENT CONFIG
# ═══════════════════════════════════════════════════════════════════════════

class WindowsEventConfig(EventConfig):
    """Windows-specific event configuration with Console API details"""
    
    # Console mode flags
    ENABLE_PROCESSED_INPUT = 0x0001
    ENABLE_LINE_INPUT = 0x0002
    ENABLE_ECHO_INPUT = 0x0004
    ENABLE_WINDOW_INPUT = 0x0008
    ENABLE_MOUSE_INPUT = 0x0010
    ENABLE_INSERT_MODE = 0x0020
    ENABLE_QUICK_EDIT_MODE = 0x0040
    ENABLE_EXTENDED_FLAGS = 0x0080
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004  # Output mode
    
    # Mouse button states
    FROM_LEFT_1ST_BUTTON_PRESSED = 0x0001
    RIGHTMOST_BUTTON_PRESSED = 0x0002
    FROM_LEFT_2ND_BUTTON_PRESSED = 0x0004
    
    # Mouse event flags
    MOUSE_MOVED = 0x0001
    DOUBLE_CLICK = 0x0002
    MOUSE_WHEELED = 0x0004
    MOUSE_HWHEELED = 0x0008
    
    def __init__(self):
        super().__init__()
        self.console_mode_config = {
            'mouse_enabled': True,
            'quickedit_disabled': True,
            'ansi_enabled': True,
            'echo_enabled': False,
        }
    
    def get_recommended_input_mode(self) -> int:
        """Get recommended console input mode flags"""
        mode = 0
        if self.console_mode_config['mouse_enabled']:
            mode |= self.ENABLE_MOUSE_INPUT
            mode |= self.ENABLE_EXTENDED_FLAGS
        if not self.console_mode_config['quickedit_disabled']:
            mode |= self.ENABLE_QUICK_EDIT_MODE
        return mode
    
    def get_recommended_output_mode(self) -> int:
        """Get recommended console output mode flags"""
        mode = 0
        if self.console_mode_config['ansi_enabled']:
            mode |= self.ENABLE_VIRTUAL_TERMINAL_PROCESSING
        return mode
    
    def configure_console_mode(self, **kwargs):
        """Update console mode configuration"""
        self.console_mode_config.update(kwargs)
    
    def parse_mouse_button(self, button_state: int) -> Optional[str]:
        """Parse Windows button state to button name"""
        if button_state & self.FROM_LEFT_1ST_BUTTON_PRESSED:
            return 'LEFT'
        elif button_state & self.RIGHTMOST_BUTTON_PRESSED:
            return 'RIGHT'
        elif button_state & self.FROM_LEFT_2ND_BUTTON_PRESSED:
            return 'MIDDLE'
        return None
    
    def parse_event_type(self, event_flags: int) -> str:
        """Parse Windows event flags to event type"""
        if event_flags & self.MOUSE_MOVED:
            return 'MOVE'
        elif event_flags & self.DOUBLE_CLICK:
            return 'DOUBLE_CLICK'
        elif event_flags & self.MOUSE_WHEELED:
            return 'WHEEL'
        return 'CLICK'


# ═══════════════════════════════════════════════════════════════════════════
# UNIX/LINUX EVENT CONFIG
# ═══════════════════════════════════════════════════════════════════════════

class UnixEventConfig(EventConfig):
    """Unix/Linux-specific event configuration with curses details"""
    
    def __init__(self):
        super().__init__()
        self.curses_config = {
            'colors_enabled': True,
            'mouse_enabled': True,
            'keypad_enabled': True,
            'echo_enabled': False,
            'cursor_visible': False,
            'nodelay': True,  # Non-blocking input
        }
        
        # Mouse mask configuration
        self.mouse_mask_config = {
            'button1_click': True,
            'button1_double': True,
            'button2_click': True,
            'button3_click': True,
            'scroll_wheel': True,
            'mouse_movement': True,
        }
    
    def get_mouse_mask(self) -> int:
        """
        Get curses mouse mask based on configuration
        Requires curses module to be imported
        """
        try:
            import curses
            mask = 0
            
            if self.mouse_mask_config['button1_click']:
                mask |= curses.BUTTON1_CLICKED | curses.BUTTON1_PRESSED | curses.BUTTON1_RELEASED
            if self.mouse_mask_config['button1_double']:
                mask |= curses.BUTTON1_DOUBLE_CLICKED
            if self.mouse_mask_config['button2_click']:
                mask |= curses.BUTTON2_CLICKED | curses.BUTTON2_PRESSED | curses.BUTTON2_RELEASED
            if self.mouse_mask_config['button3_click']:
                mask |= curses.BUTTON3_CLICKED | curses.BUTTON3_PRESSED | curses.BUTTON3_RELEASED
            if self.mouse_mask_config['scroll_wheel']:
                mask |= curses.BUTTON4_PRESSED | curses.BUTTON5_PRESSED
            if self.mouse_mask_config['mouse_movement']:
                mask |= curses.REPORT_MOUSE_POSITION
            
            return mask
        except ImportError:
            return 0
    
    def configure_curses(self, **kwargs):
        """Update curses configuration"""
        self.curses_config.update(kwargs)
    
    def configure_mouse_mask(self, **kwargs):
        """Update mouse mask configuration"""
        self.mouse_mask_config.update(kwargs)
    
    def parse_mouse_button(self, bstate: int) -> Optional[str]:
        """Parse curses button state to button name"""
        try:
            import curses
            
            if bstate & (curses.BUTTON1_PRESSED | curses.BUTTON1_CLICKED):
                return 'LEFT'
            elif bstate & (curses.BUTTON2_PRESSED | curses.BUTTON2_CLICKED):
                return 'MIDDLE'
            elif bstate & (curses.BUTTON3_PRESSED | curses.BUTTON3_CLICKED):
                return 'RIGHT'
            elif bstate & curses.BUTTON4_PRESSED:
                return 'WHEEL_UP'
            elif bstate & curses.BUTTON5_PRESSED:
                return 'WHEEL_DOWN'
        except ImportError:
            pass
        
        return None
    
    def parse_event_type(self, bstate: int) -> str:
        """Parse curses button state to event type"""
        try:
            import curses
            
            if bstate & (curses.BUTTON1_DOUBLE_CLICKED | 
                        curses.BUTTON2_DOUBLE_CLICKED | 
                        curses.BUTTON3_DOUBLE_CLICKED):
                return 'DOUBLE_CLICK'
            elif bstate & curses.REPORT_MOUSE_POSITION:
                return 'MOVE'
            elif bstate & (curses.BUTTON4_PRESSED | curses.BUTTON5_PRESSED):
                return 'WHEEL'
        except ImportError:
            pass
        
        return 'CLICK'


# ═══════════════════════════════════════════════════════════════════════════
# UNIFIED EVENT MANAGER
# ═══════════════════════════════════════════════════════════════════════════

class EventManager:
    """Unified event manager that uses platform-specific configs"""
    
    def __init__(self):
        if IS_WINDOWS:
            self.config = WindowsEventConfig()
        else:
            self.config = UnixEventConfig()
        
        self.platform = 'windows' if IS_WINDOWS else 'unix'
    
    def register_key_handler(self, key: str, handler: Callable):
        """Register keyboard event handler"""
        self.config.register_key_handler(key, handler)
    
    def register_mouse_handler(self, event_type: str, handler: Callable):
        """Register mouse event handler"""
        self.config.register_mouse_handler(event_type, handler)
    
    def process_key(self, key: str, modifiers: list = None, raw_code: Any = None) -> bool:
        """Process keyboard input"""
        event = KeyEvent(
            key=key,
            modifiers=modifiers or [],
            raw_code=raw_code,
            platform=self.platform
        )
        return self.config.handle_key_event(event)
    
    def process_mouse(self, x: int, y: int, button: str = None, 
                     event_type: str = 'CLICK', modifiers: list = None,
                     raw_data: Any = None) -> bool:
        """Process mouse event"""
        event = MouseEvent(
            x=x,
            y=y,
            button=button,
            event_type=event_type,
            modifiers=modifiers or [],
            raw_data=raw_data,
            platform=self.platform
        )
        return self.config.handle_mouse_event(event)
    
    def get_config(self):
        """Get platform-specific event config"""
        return self.config


# ═══════════════════════════════════════════════════════════════════════════
# FACTORY FUNCTION
# ═══════════════════════════════════════════════════════════════════════════

def create_event_config() -> EventConfig:
    """
    Factory function to create appropriate event config for current platform
    
    Returns:
        Platform-specific EventConfig instance
    """
    if IS_WINDOWS:
        return WindowsEventConfig()
    else:
        return UnixEventConfig()
