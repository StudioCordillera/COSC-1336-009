"""
Input Components
Interactive elements for user input and actions
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Menus.terminal import write, draw_box, ASCII, center_text
from .base import Component


class InputField(Component):
    """Generic single-line input"""
    
    def __init__(self, row, col, width, placeholder=""):
        super().__init__(row, col, width, 1)
        self.placeholder = placeholder
        self.value = ""
    
    def set_value(self, value):
        """Set input value"""
        self.value = str(value)
    
    def render(self):
        """Render input field"""
        if not self.visible:
            return
        
        # Determine display text
        display_text = self.value if self.value else self.placeholder
        
        # Add cursor if focused
        if self.state == self.STATE_FOCUSED:
            display_text = f"{display_text}_"
        
        # Truncate and display
        truncated = self.truncate_text(display_text, self.width - 2)
        
        # Draw field box
        field_text = f"[{truncated:<{self.width-2}}]"
        write(self.row, self.col, field_text)


class TextField(Component):
    """Single-line text with validation"""
    
    def __init__(self, row, col, width, label="", placeholder="", required=False):
        super().__init__(row, col, width, 1)
        self.label = label
        self.placeholder = placeholder
        self.required = required
        self.value = ""
        self.valid = True
    
    def set_value(self, value):
        """Set and validate value"""
        self.value = str(value)
        self.valid = not (self.required and not self.value)
    
    def render(self):
        """Render text field with label"""
        if not self.visible:
            return
        
        # Draw label if present
        if self.label:
            label_text = f"{self.label}: "
            write(self.row, self.col, label_text)
            field_col = self.col + len(label_text)
            field_width = self.width - len(label_text)
        else:
            field_col = self.col
            field_width = self.width
        
        # Draw field
        display_text = self.value if self.value else self.placeholder
        if self.state == self.STATE_FOCUSED:
            display_text = f"{display_text}_"
        
        truncated = self.truncate_text(display_text, field_width - 2)
        
        # Style based on validation
        bracket_left = "[" if self.valid else "<"
        bracket_right = "]" if self.valid else ">"
        
        field_text = f"{bracket_left}{truncated:<{field_width-2}}{bracket_right}"
        write(self.row, field_col, field_text)


class TextArea(Component):
    """Multi-line text input"""
    
    def __init__(self, row, col, width, height):
        super().__init__(row, col, width, height)
        self.lines = []
        self.max_lines = height - 2  # Account for borders
    
    def add_line(self, line):
        """Add line to text area"""
        if len(self.lines) < self.max_lines:
            self.lines.append(line)
    
    def set_lines(self, lines):
        """Set all lines"""
        self.lines = lines[:self.max_lines]
    
    def render(self):
        """Render multi-line text area"""
        if not self.visible:
            return
        
        # Draw border
        draw_box(self.row, self.col, self.width, self.height)
        
        # Draw lines
        current_row = self.row + 1
        for line in self.lines:
            if current_row >= self.row + self.height - 1:
                break
            
            truncated = self.truncate_text(line, self.width - 4)
            write(current_row, self.col + 2, truncated)
            current_row += 1
        
        # Draw cursor if focused
        if self.state == self.STATE_FOCUSED:
            write(current_row, self.col + 2, "_")


class Button(Component):
    """Action trigger (normal/highlighted)"""
    
    def __init__(self, row, col, width, text):
        super().__init__(row, col, width, 3)
        self.text = text
    
    def render(self):
        """Render button with state-based styling"""
        if not self.visible:
            return
        
        if self.state == self.STATE_DISABLED:
            # Disabled button (dim)
            border = ASCII.HLINE * self.width
            write(self.row, self.col, border)
            center_text(self.row + 1, f"[{self.text}]")
            write(self.row + 2, self.col, border)
        
        elif self.state == self.STATE_ACTIVE or self.state == self.STATE_FOCUSED:
            # Active/Focused button (highlighted)
            draw_box(self.row, self.col, self.width, self.height)
            center_text(self.row + 1, f"> {self.text} <")
        
        else:
            # Normal button
            border = ASCII.HLINE * self.width
            write(self.row, self.col, border)
            center_text(self.row + 1, self.text)
            write(self.row + 2, self.col, border)


class Checkbox(Component):
    """Boolean toggle with visual state"""
    
    def __init__(self, row, col, label="", checked=False):
        super().__init__(row, col, len(label) + 5, 1)
        self.label = label
        self.checked = checked
    
    def toggle(self):
        """Toggle checked state"""
        self.checked = not self.checked
    
    def render(self):
        """Render checkbox"""
        if not self.visible:
            return
        
        # Checkbox character
        box_char = "[X]" if self.checked else "[ ]"
        
        # Add focus indicator
        if self.state == self.STATE_FOCUSED:
            box_char = f">{box_char}"
        else:
            box_char = f" {box_char}"
        
        # Full text
        checkbox_text = f"{box_char} {self.label}"
        write(self.row, self.col, checkbox_text)


class Toggle(Component):
    """Binary switch (ON/OFF)"""
    
    def __init__(self, row, col, label="", enabled=False):
        super().__init__(row, col, len(label) + 12, 1)
        self.label = label
        self.enabled = enabled
    
    def toggle(self):
        """Toggle enabled state"""
        self.enabled = not self.enabled
    
    def render(self):
        """Render toggle switch"""
        if not self.visible:
            return
        
        # Switch visualization
        if self.enabled:
            switch = "[===|  ]"  # ON position
            status = "ON"
        else:
            switch = "[  |===]"  # OFF position
            status = "OFF"
        
        # Full text
        toggle_text = f"{self.label}: {switch} {status}"
        write(self.row, self.col, toggle_text)


class Dropdown(Component):
    """List selector (collapsed/expanded)"""
    
    def __init__(self, row, col, width, label="", options=None):
        super().__init__(row, col, width, 1)
        self.label = label
        self.options = options if options else []
        self.selected_index = 0
        self.expanded = False
    
    def set_selected(self, index):
        """Set selected option"""
        if 0 <= index < len(self.options):
            self.selected_index = index
    
    def render(self):
        """Render dropdown"""
        if not self.visible:
            return
        
        # Calculate heights
        if self.expanded:
            self.height = min(len(self.options) + 2, 10)  # Max 10 items
        else:
            self.height = 1
        
        # Draw label
        if self.label:
            write(self.row, self.col, f"{self.label}:")
            field_col = self.col + len(self.label) + 2
            field_width = self.width - len(self.label) - 2
        else:
            field_col = self.col
            field_width = self.width
        
        if self.expanded:
            # Draw expanded list
            current_row = self.row
            for i, option in enumerate(self.options[:8]):  # Limit display
                if current_row >= self.row + self.height:
                    break
                
                prefix = "> " if i == self.selected_index else "  "
                option_text = f"{prefix}{option}"
                truncated = self.truncate_text(option_text, field_width)
                write(current_row, field_col, truncated)
                current_row += 1
        else:
            # Draw collapsed (show selected)
            selected_text = self.options[self.selected_index] if self.options else ""
            arrow = ASCII.DOWN if self.state == self.STATE_FOCUSED else ASCII.RIGHT
            dropdown_text = f"[{selected_text}] {arrow}"
            truncated = self.truncate_text(dropdown_text, field_width)
            write(self.row, field_col, truncated)


class Selector(Component):
    """Choice picker (arrow navigation)"""
    
    def __init__(self, row, col, width, options=None):
        super().__init__(row, col, width, 1)
        self.options = options if options else []
        self.selected_index = 0
    
    def next_option(self):
        """Move to next option"""
        self.selected_index = (self.selected_index + 1) % len(self.options)
    
    def prev_option(self):
        """Move to previous option"""
        self.selected_index = (self.selected_index - 1) % len(self.options)
    
    def render(self):
        """Render selector with arrow navigation"""
        if not self.visible or not self.options:
            return
        
        selected_text = self.options[self.selected_index]
        selector_text = f"< {selected_text} >"
        
        # Center the selector
        padding = (self.width - len(selector_text)) // 2
        write(self.row, self.col + padding, selector_text)
