"""
UI_LIBRARY Package
Cross-platform CLI menu and UI components with standardized configurations
"""

from .input_mappings import (
    InputMapper,
    WindowsInputMapper,
    UnixInputMapper,
    create_input_mapper
)

from .event_configs import (
    KeyEvent,
    MouseEvent,
    EventConfig,
    WindowsEventConfig,
    UnixEventConfig,
    EventManager,
    create_event_config
)

from .ascii_config import (
    ASCIIChars,
    ANSIEscapes,
    ThemeConfig,
    UIElementConfig,
    ASCIIConfigLoader
)

__all__ = [
    # Input Mappings
    'InputMapper',
    'WindowsInputMapper',
    'UnixInputMapper',
    'create_input_mapper',
    
    # Event Configs
    'KeyEvent',
    'MouseEvent',
    'EventConfig',
    'WindowsEventConfig',
    'UnixEventConfig',
    'EventManager',
    'create_event_config',
    
    # ASCII Config
    'ASCIIChars',
    'ANSIEscapes',
    'ThemeConfig',
    'UIElementConfig',
    'ASCIIConfigLoader',
]

__version__ = '1.0.0'
