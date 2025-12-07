"""
Base Component Class
Foundation for all UI components with responsive layout and state management
"""

import sys
import os

# Add parent directory to path for terminal import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Menus.terminal import get_width, get_height, pct


class Component:
    """Base class for all UI components
    
    Provides:
    - Responsive positioning (percentages or absolute)
    - State management
    - Child component hierarchy
    - Boundary validation
    """
    
    # Standard component states
    STATE_IDLE = "IDLE"
    STATE_ACTIVE = "ACTIVE"
    STATE_FOCUSED = "FOCUSED"
    STATE_DISABLED = "DISABLED"
    
    def __init__(self, row, col, width, height):
        """Initialize component with position and dimensions
        
        Args:
            row: Row position (1-based int OR 0.0-1.0 percentage)
            col: Column position (1-based int OR 0.0-1.0 percentage)
            width: Width (int OR 0.0-1.0 percentage)
            height: Height (int OR 0.0-1.0 percentage)
        """
        # Convert percentages to absolute positions
        self.row = self._to_absolute(row, of_width=False)
        self.col = self._to_absolute(col, of_width=True)
        self.width = self._to_absolute(width, of_width=True)
        self.height = self._to_absolute(height, of_width=False)
        
        # Validate bounds
        self._validate_bounds()
        
        # Component state
        self.state = self.STATE_IDLE
        self.visible = True
        
        # Child components
        self.children = []
        
        # Content
        self.content = ""
    
    def _to_absolute(self, value, of_width=True):
        """Convert percentage to absolute value
        
        Args:
            value: Percentage (0.0-1.0) OR integer
            of_width: True for width, False for height
            
        Returns:
            Absolute integer value
        """
        if isinstance(value, float) and 0 <= value <= 1:
            return pct(value, of_width=of_width)
        return int(value)
    
    def _validate_bounds(self):
        """Ensure component stays within terminal bounds"""
        max_width = get_width()
        max_height = get_height()
        
        # Clamp position
        self.row = max(1, min(self.row, max_height))
        self.col = max(1, min(self.col, max_width))
        
        # Clamp dimensions
        self.width = max(1, min(self.width, max_width - self.col + 1))
        self.height = max(1, min(self.height, max_height - self.row + 1))
    
    def render(self):
        """Draw component at current position
        
        Override this method in subclasses
        """
        raise NotImplementedError(f"{self.__class__.__name__} must implement render()")
    
    def set_state(self, state):
        """Update component state
        
        Args:
            state: One of STATE_IDLE, STATE_ACTIVE, STATE_FOCUSED, STATE_DISABLED
        """
        self.state = state
    
    def set_visible(self, visible):
        """Set component visibility
        
        Args:
            visible: Boolean visibility flag
        """
        self.visible = visible
    
    def add_child(self, child):
        """Add nested component
        
        Args:
            child: Component instance
        """
        self.children.append(child)
    
    def render_children(self):
        """Render all child components"""
        for child in self.children:
            if child.visible:
                child.render()
    
    def set_content(self, content):
        """Set component content
        
        Args:
            content: String content to display
        """
        self.content = str(content)
    
    def truncate_text(self, text, max_length, suffix="..."):
        """Truncate text with ellipsis if too long
        
        Args:
            text: Text to truncate
            max_length: Maximum length
            suffix: Ellipsis string (default: "...")
            
        Returns:
            Truncated string
        """
        if len(text) <= max_length:
            return text
        return text[:max_length - len(suffix)] + suffix
    
    def get_bounds(self):
        """Get component boundaries
        
        Returns:
            Tuple of (row, col, width, height)
        """
        return (self.row, self.col, self.width, self.height)
    
    def is_inside(self, row, col):
        """Check if position is inside component
        
        Args:
            row: Row to check
            col: Column to check
            
        Returns:
            Boolean
        """
        return (self.row <= row < self.row + self.height and
                self.col <= col < self.col + self.width)
