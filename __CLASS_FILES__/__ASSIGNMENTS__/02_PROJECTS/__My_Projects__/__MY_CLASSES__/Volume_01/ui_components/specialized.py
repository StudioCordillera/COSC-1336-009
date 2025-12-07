"""
Specialized Components
Complex components for specific use cases
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Menus.terminal import write, draw_box, ASCII
from .base import Component


class ChoiceObject(Component):
    """Menu item (number + text + arrow)"""
    
    def __init__(self, row, col, width, number, text):
        super().__init__(row, col, width, 1)
        self.number = number
        self.text = text
    
    def render(self):
        """Render choice object"""
        if not self.visible:
            return
        
        # Build choice text
        if self.state == self.STATE_ACTIVE or self.state == self.STATE_FOCUSED:
            choice_text = f"{ASCII.RIGHT} {self.number}. {self.text}"
        else:
            choice_text = f"  {self.number}. {self.text}"
        
        truncated = self.truncate_text(choice_text, self.width)
        write(self.row, self.col, truncated)


class ParamField(Component):
    """Labeled input pair"""
    
    def __init__(self, row, col, width, label, value=""):
        super().__init__(row, col, width, 1)
        self.label = label
        self.value = value
    
    def set_value(self, value):
        """Set field value"""
        self.value = str(value)
    
    def render(self):
        """Render parameter field"""
        if not self.visible:
            return
        
        # Calculate label and field widths
        label_width = len(self.label) + 2
        field_width = self.width - label_width
        
        # Draw label
        write(self.row, self.col, f"{self.label}: ")
        
        # Draw field
        field_col = self.col + label_width
        display_value = self.value if self.value else "..."
        
        if self.state == self.STATE_FOCUSED:
            display_value = f"{display_value}_"
        
        truncated = self.truncate_text(display_value, field_width - 2)
        field_text = f"[{truncated:<{field_width-2}}]"
        write(self.row, field_col, field_text)


class CheckboxList(Component):
    """Multi-select list"""
    
    def __init__(self, row, col, width, height, items=None):
        super().__init__(row, col, width, height)
        self.items = items if items else []
        self.checked = set()  # Set of checked indices
        self.focused_index = 0
    
    def add_item(self, item):
        """Add item to list"""
        self.items.append(item)
    
    def toggle_item(self, index):
        """Toggle item checked state"""
        if 0 <= index < len(self.items):
            if index in self.checked:
                self.checked.remove(index)
            else:
                self.checked.add(index)
    
    def is_checked(self, index):
        """Check if item is checked"""
        return index in self.checked
    
    def render(self):
        """Render checkbox list"""
        if not self.visible:
            return
        
        current_row = self.row
        
        for i, item in enumerate(self.items):
            if current_row >= self.row + self.height:
                break
            
            # Checkbox
            box = "[X]" if self.is_checked(i) else "[ ]"
            
            # Focus indicator
            if i == self.focused_index and self.state == self.STATE_FOCUSED:
                prefix = ">"
            else:
                prefix = " "
            
            # Full item text
            item_text = f"{prefix} {box} {item}"
            truncated = self.truncate_text(item_text, self.width)
            write(current_row, self.col, truncated)
            
            current_row += 1


class DirectoryTree(Component):
    """File browser display"""
    
    def __init__(self, row, col, width, height):
        super().__init__(row, col, width, height)
        self.entries = []  # List of (indent_level, name, is_dir) tuples
        self.selected_index = 0
    
    def add_entry(self, name, indent_level=0, is_dir=False):
        """Add directory entry
        
        Args:
            name: Entry name
            indent_level: Indentation level
            is_dir: True if directory, False if file
        """
        self.entries.append((indent_level, name, is_dir))
    
    def set_selected(self, index):
        """Set selected entry"""
        if 0 <= index < len(self.entries):
            self.selected_index = index
    
    def render(self):
        """Render directory tree"""
        if not self.visible:
            return
        
        # Draw border
        draw_box(self.row, self.col, self.width, self.height)
        
        current_row = self.row + 1
        
        for i, (level, name, is_dir) in enumerate(self.entries):
            if current_row >= self.row + self.height - 1:
                break
            
            # Indent
            indent = "  " * level
            
            # Icon
            icon = f"[{ASCII.CORNER}]" if is_dir else f" {ASCII.HLINE} "
            
            # Selection indicator
            if i == self.selected_index:
                prefix = ASCII.RIGHT
            else:
                prefix = " "
            
            # Full entry text
            entry_text = f"{prefix}{indent}{icon} {name}"
            truncated = self.truncate_text(entry_text, self.width - 4)
            write(current_row, self.col + 2, truncated)
            
            current_row += 1


class StatusBar(Component):
    """Bottom info bar"""
    
    def __init__(self, width, text="Ready"):
        """Initialize status bar at bottom of terminal
        
        Args:
            width: Bar width (percentage or absolute)
            text: Status text
        """
        from Menus.terminal import get_height
        
        # Position at bottom
        row = get_height()
        super().__init__(row, 1, width, 1)
        self.text = text
    
    def set_text(self, text):
        """Update status text"""
        self.text = text
    
    def render(self):
        """Render status bar"""
        if not self.visible:
            return
        
        # Background bar
        bar = ASCII.HLINE_HEAVY * self.width
        write(self.row, self.col, bar)
        
        # Status text (left-aligned)
        truncated = self.truncate_text(f" {self.text}", self.width - 2)
        write(self.row, self.col, truncated)
