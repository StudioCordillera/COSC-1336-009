"""
Container Components
Wrappers and structural containers for organizing UI layouts
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Menus.terminal import write, draw_box, draw_hline, ASCII, center_text, clear_line, move
from .base import Component


class Wrapper(Component):
    """Generic container with optional padding and border"""
    
    def __init__(self, row, col, width, height, padding=0, border=False):
        super().__init__(row, col, width, height)
        self.padding = padding
        self.border = border
    
    def render(self):
        """Render wrapper and children"""
        if not self.visible:
            return
        
        # Draw border if enabled
        if self.border:
            draw_box(self.row, self.col, self.width, self.height)
        
        # Render children with padding offset
        for child in self.children:
            if child.visible:
                # Adjust child position for padding
                child.row += self.padding
                child.col += self.padding
                child.render()
                # Restore original position
                child.row -= self.padding
                child.col -= self.padding


class Panel(Component):
    """Bordered container with optional title"""
    
    def __init__(self, row, col, width, height, title=""):
        super().__init__(row, col, width, height)
        self.title = title
    
    def render(self):
        """Render panel with border and title"""
        if not self.visible:
            return
        
        # Draw border
        draw_box(self.row, self.col, self.width, self.height)
        
        # Draw title if present
        if self.title:
            # Title on top border
            title_text = f" {self.title} "
            title_len = len(title_text)
            # Truncate if too long
            max_len = self.width - 4
            if title_len > max_len:
                title_text = title_text[:max_len-3] + "..."
                title_len = max_len
            if title_len < self.width:
                title_col = self.col + (self.width - title_len) // 2
                write(self.row, title_col, title_text)
        
        # Render children
        self.render_children()


class Frame(Component):
    """Titled container with decorative border"""
    
    def __init__(self, row, col, width, height, title="", subtitle=""):
        super().__init__(row, col, width, height)
        self.title = title
        self.subtitle = subtitle
    
    def render(self):
        """Render frame with title and decorative border"""
        if not self.visible:
            return
        
        # Draw double border (outer)
        draw_box(self.row, self.col, self.width, self.height)
        
        # Draw title section
        if self.title:
            # Title at top - within frame bounds
            title_row = self.row + 1
            max_title_len = self.width - 4
            title_text = self.title[:max_title_len] if len(self.title) > max_title_len else self.title
            title_col = self.col + (self.width - len(title_text)) // 2
            write(title_row, title_col, title_text)
            
            # Separator line
            draw_hline(title_row + 1, self.col + 1, self.width - 2, heavy=True)
        
        # Draw subtitle if present
        if self.subtitle:
            subtitle_row = self.row + 3 if self.title else self.row + 1
            max_subtitle_len = self.width - 4
            subtitle_text = self.subtitle[:max_subtitle_len] if len(self.subtitle) > max_subtitle_len else self.subtitle
            subtitle_col = self.col + (self.width - len(subtitle_text)) // 2
            write(subtitle_row, subtitle_col, subtitle_text)
        
        # Render children
        self.render_children()


class Section(Component):
    """Logical grouping with optional separator"""
    
    def __init__(self, row, col, width, height, label="", separator=True):
        super().__init__(row, col, width, height)
        self.label = label
        self.separator = separator
    
    def render(self):
        """Render section with label and separator"""
        if not self.visible:
            return
        
        current_row = self.row
        
        # Draw label if present
        if self.label:
            write(current_row, self.col, self.label)
            current_row += 1
        
        # Draw separator if enabled
        if self.separator:
            draw_hline(current_row, self.col, self.width)
            current_row += 1
        
        # Render children
        self.render_children()


class Dialogue(Component):
    """Modal dialogue container"""
    
    def __init__(self, row, col, width, height, title="", centered=False):
        """Initialize dialogue
        
        Args:
            row: Row position (or ignored if centered=True)
            col: Column position (or ignored if centered=True)
            width: Dialogue width (percentage or absolute)
            height: Dialogue height (percentage or absolute)
            title: Optional title text
            centered: If True, auto-center in terminal
        """
        # Calculate centered position if requested
        if centered:
            from Menus.terminal import center_box
            row, col = center_box(width, height)
        
        super().__init__(row, col, width, height)
        self.title = title
    
    def render(self):
        """Render centered dialogue box"""
        if not self.visible:
            return
        
        # Draw border
        draw_box(self.row, self.col, self.width, self.height)
        
        # Draw title if present
        if self.title:
            title_row = self.row + 1
            max_title_len = self.width - 4
            title_text = self.title[:max_title_len] if len(self.title) > max_title_len else self.title
            title_col = self.col + (self.width - len(title_text)) // 2
            write(title_row, title_col, title_text)
            # Separator under title
            draw_hline(title_row + 1, self.col + 1, self.width - 2)
        
        # Render children
        self.render_children()


class Menu(Component):
    """Navigation container with choice list"""
    
    def __init__(self, row, col, width, height, title="", prompt=""):
        super().__init__(row, col, width, height)
        self.title = title
        self.prompt = prompt
        self.choices = []
    
    def add_choice(self, text):
        """Add menu choice
        
        Args:
            text: Choice text
        """
        self.choices.append(text)
    
    def render(self):
        """Render menu with title, prompt, and choices"""
        if not self.visible:
            return
        
        # Draw border
        draw_box(self.row, self.col, self.width, self.height)
        
        current_row = self.row + 1
        
        # Draw title
        if self.title:
            max_title_len = self.width - 4
            title_text = self.title[:max_title_len] if len(self.title) > max_title_len else self.title
            title_col = self.col + (self.width - len(title_text)) // 2
            write(current_row, title_col, title_text)
            current_row += 1
            draw_hline(current_row, self.col + 1, self.width - 2, heavy=True)
            current_row += 1
        
        # Draw prompt
        if self.prompt:
            current_row += 1
            max_prompt_len = self.width - 4
            prompt_text = self.prompt[:max_prompt_len] if len(self.prompt) > max_prompt_len else self.prompt
            write(current_row, self.col + 2, prompt_text)
            current_row += 2
        
        # Draw choices
        for i, choice in enumerate(self.choices, 1):
            if current_row >= self.row + self.height - 1:
                break  # Stop if we run out of space
            
            choice_text = f"  {i}. {choice}"
            truncated = self.truncate_text(choice_text, self.width - 4)
            write(current_row, self.col + 2, truncated)
            current_row += 1
        
        # Render children
        self.render_children()
