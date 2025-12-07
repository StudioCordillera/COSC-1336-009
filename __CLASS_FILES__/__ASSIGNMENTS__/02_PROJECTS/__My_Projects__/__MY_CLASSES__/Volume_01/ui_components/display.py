"""
Display Components
Text and information display elements
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Menus.terminal import write, draw_hline, center_text, ASCII
from .base import Component


class Header(Component):
    """Styled section heading"""
    
    def __init__(self, row, col, width, text, underline=True):
        super().__init__(row, col, width, 2 if underline else 1)
        self.text = text
        self.underline = underline
    
    def render(self):
        """Render header with optional underline"""
        if not self.visible:
            return
        
        # Center text
        center_text(self.row, self.text)
        
        # Draw underline
        if self.underline:
            draw_hline(self.row + 1, self.col, self.width, heavy=True)


class Title(Component):
    """Primary label (large text)"""
    
    def __init__(self, row, col, width, text, centered=True):
        super().__init__(row, col, width, 1)
        self.text = text
        self.centered = centered
    
    def render(self):
        """Render title text"""
        if not self.visible:
            return
        
        if self.centered:
            center_text(self.row, self.text)
        else:
            truncated = self.truncate_text(self.text, self.width)
            write(self.row, self.col, truncated)


class Label(Component):
    """Standard text display"""
    
    def __init__(self, row, col, width, text, align="left"):
        super().__init__(row, col, width, 1)
        self.text = text
        self.align = align  # left, center, right
    
    def render(self):
        """Render label text"""
        if not self.visible:
            return
        
        truncated = self.truncate_text(self.text, self.width)
        
        if self.align == "center":
            padding = (self.width - len(truncated)) // 2
            write(self.row, self.col + padding, truncated)
        elif self.align == "right":
            padding = self.width - len(truncated)
            write(self.row, self.col + padding, truncated)
        else:  # left
            write(self.row, self.col, truncated)


class Prompt(Component):
    """User instruction with icon/marker"""
    
    def __init__(self, row, col, width, text, marker=None):
        super().__init__(row, col, width, 1)
        self.text = text
        self.marker = marker if marker else ASCII.RIGHT
    
    def render(self):
        """Render prompt with marker"""
        if not self.visible:
            return
        
        prompt_text = f"{self.marker} {self.text}"
        truncated = self.truncate_text(prompt_text, self.width)
        write(self.row, self.col, truncated)


class Message(Component):
    """Notification text with style (info/warning/error)"""
    
    STYLE_INFO = "info"
    STYLE_WARNING = "warning"
    STYLE_ERROR = "error"
    STYLE_SUCCESS = "success"
    
    def __init__(self, row, col, width, text, style=STYLE_INFO):
        super().__init__(row, col, width, 3)  # 3 rows for border
        self.text = text
        self.style = style
    
    def _get_prefix(self):
        """Get prefix based on style"""
        prefixes = {
            self.STYLE_INFO: "[i]",
            self.STYLE_WARNING: "[!]",
            self.STYLE_ERROR: "[X]",
            self.STYLE_SUCCESS: "[✓]"
        }
        return prefixes.get(self.style, "[*]")
    
    def render(self):
        """Render message with style indicator"""
        if not self.visible:
            return
        
        # Top border
        write(self.row, self.col, ASCII.HLINE * self.width)
        
        # Message with prefix
        prefix = self._get_prefix()
        message_text = f"{prefix} {self.text}"
        truncated = self.truncate_text(message_text, self.width - 2)
        write(self.row + 1, self.col + 1, truncated)
        
        # Bottom border
        write(self.row + 2, self.col, ASCII.HLINE * self.width)


class List(Component):
    """Ordered item display (numbered/bulleted)"""
    
    def __init__(self, row, col, width, height, items=None, numbered=True):
        super().__init__(row, col, width, height)
        self.items = items if items else []
        self.numbered = numbered
    
    def add_item(self, item):
        """Add item to list"""
        self.items.append(item)
    
    def render(self):
        """Render list items"""
        if not self.visible:
            return
        
        current_row = self.row
        
        for i, item in enumerate(self.items):
            if current_row >= self.row + self.height:
                break  # Stop if we run out of space
            
            if self.numbered:
                item_text = f"{i + 1}. {item}"
            else:
                item_text = f"{ASCII.BULLET} {item}"
            
            truncated = self.truncate_text(item_text, self.width)
            write(current_row, self.col, truncated)
            current_row += 1


class Tree(Component):
    """Hierarchical display with indent"""
    
    def __init__(self, row, col, width, height, indent=2):
        super().__init__(row, col, width, height)
        self.nodes = []  # List of (level, text) tuples
        self.indent = indent
    
    def add_node(self, text, level=0):
        """Add node at specified level
        
        Args:
            text: Node text
            level: Indentation level (0 = root)
        """
        self.nodes.append((level, text))
    
    def render(self):
        """Render tree with indentation"""
        if not self.visible:
            return
        
        current_row = self.row
        
        for level, text in self.nodes:
            if current_row >= self.row + self.height:
                break
            
            indent_str = " " * (level * self.indent)
            prefix = f"{ASCII.VLINE}{ASCII.HLINE} " if level > 0 else ""
            node_text = f"{indent_str}{prefix}{text}"
            
            truncated = self.truncate_text(node_text, self.width)
            write(current_row, self.col, truncated)
            current_row += 1


class Preview(Component):
    """Content preview area"""
    
    def __init__(self, row, col, width, height, title="Preview"):
        super().__init__(row, col, width, height)
        self.title = title
        self.lines = []
    
    def set_lines(self, lines):
        """Set preview content lines
        
        Args:
            lines: List of text lines
        """
        self.lines = lines
    
    def render(self):
        """Render preview box with content"""
        if not self.visible:
            return
        
        # Top border with title
        border = ASCII.CORNER + ASCII.HLINE * (self.width - 2) + ASCII.CORNER
        write(self.row, self.col, border)
        
        # Title
        if self.title:
            title_text = f" {self.title} "
            title_col = self.col + (self.width - len(title_text)) // 2
            write(self.row, title_col, title_text)
        
        # Content lines
        current_row = self.row + 1
        for line in self.lines:
            if current_row >= self.row + self.height - 1:
                break
            
            truncated = self.truncate_text(line, self.width - 4)
            write(current_row, self.col + 1, ASCII.VLINE)
            write(current_row, self.col + 2, truncated)
            write(current_row, self.col + self.width - 1, ASCII.VLINE)
            current_row += 1
        
        # Bottom border
        write(self.row + self.height - 1, self.col, border)
