"""
UI Components - MenuNav Standard Implementation
Phase 1: Minimal working versions with good formatting and robust rendering

Exports all UI components for easy import:
    from ui_components import Panel, Button, List, etc.
"""

from .base import Component
from .containers import Wrapper, Panel, Frame, Section, Dialogue, Menu
from .display import Header, Title, Label, Prompt, Message, List, Tree, Preview
from .input import InputField, TextField, TextArea, Button, Checkbox, Toggle, Dropdown, Selector
from .navigation import Breadcrumb, NavigationControls, NavigationButtons, Pagination, Tabs
from .specialized import ChoiceObject, ParamField, CheckboxList, DirectoryTree, StatusBar

__all__ = [
    # Base
    'Component',
    
    # Containers
    'Wrapper', 'Panel', 'Frame', 'Section', 'Dialogue', 'Menu',
    
    # Display
    'Header', 'Title', 'Label', 'Prompt', 'Message', 'List', 'Tree', 'Preview',
    
    # Input
    'InputField', 'TextField', 'TextArea', 'Button', 'Checkbox', 'Toggle', 'Dropdown', 'Selector',
    
    # Navigation
    'Breadcrumb', 'NavigationControls', 'NavigationButtons', 'Pagination', 'Tabs',
    
    # Specialized
    'ChoiceObject', 'ParamField', 'CheckboxList', 'DirectoryTree', 'StatusBar'
]

__version__ = "1.0.0"
