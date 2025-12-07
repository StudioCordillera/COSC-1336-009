"""
Navigation Components
Path display and navigation controls
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Menus.terminal import write, ASCII
from .base import Component


class Breadcrumb(Component):
    """Path display with separators"""
    
    def __init__(self, row, col, width, path=None, separator=">"):
        super().__init__(row, col, width, 1)
        self.path = path if path else []
        self.separator = separator
    
    def set_path(self, path):
        """Set breadcrumb path
        
        Args:
            path: List of path segments
        """
        self.path = path
    
    def render(self):
        """Render breadcrumb path"""
        if not self.visible:
            return
        
        # Build path string
        path_str = f" {self.separator} ".join(self.path)
        truncated = self.truncate_text(path_str, self.width)
        
        write(self.row, self.col, truncated)


class NavigationControls(Component):
    """Movement button group"""
    
    def __init__(self, row, col):
        super().__init__(row, col, 20, 3)
        self.can_go_back = True
        self.can_go_forward = True
        self.can_go_up = True
    
    def render(self):
        """Render navigation controls"""
        if not self.visible:
            return
        
        # Back button
        back_text = f"[{ASCII.LEFT} Back]" if self.can_go_back else f"[{ASCII.LEFT} Back]"
        write(self.row, self.col, back_text)
        
        # Forward button
        fwd_text = f"[Fwd {ASCII.RIGHT}]" if self.can_go_forward else f"[Fwd {ASCII.RIGHT}]"
        write(self.row, self.col + 10, fwd_text)
        
        # Up button
        up_text = f"[{ASCII.UP} Up]" if self.can_go_up else f"[{ASCII.UP} Up]"
        write(self.row + 2, self.col + 5, up_text)


class NavigationButtons(Component):
    """Action button set"""
    
    def __init__(self, row, col, buttons=None):
        """Initialize navigation buttons
        
        Args:
            row, col: Position
            buttons: List of button labels
        """
        super().__init__(row, col, 40, 1)
        self.buttons = buttons if buttons else ["OK", "Cancel"]
        self.selected_index = 0
    
    def select_button(self, index):
        """Select button by index"""
        if 0 <= index < len(self.buttons):
            self.selected_index = index
    
    def render(self):
        """Render button set"""
        if not self.visible:
            return
        
        current_col = self.col
        
        for i, button in enumerate(self.buttons):
            if i == self.selected_index:
                button_text = f"[{button}]"
            else:
                button_text = f" {button} "
            
            write(self.row, current_col, button_text)
            current_col += len(button_text) + 2


class Pagination(Component):
    """Page control (prev/next/numbers)"""
    
    def __init__(self, row, col, total_pages=1, current_page=1):
        super().__init__(row, col, 30, 1)
        self.total_pages = total_pages
        self.current_page = current_page
    
    def set_page(self, page):
        """Set current page"""
        self.current_page = max(1, min(page, self.total_pages))
    
    def next_page(self):
        """Go to next page"""
        if self.current_page < self.total_pages:
            self.current_page += 1
    
    def prev_page(self):
        """Go to previous page"""
        if self.current_page > 1:
            self.current_page -= 1
    
    def render(self):
        """Render pagination controls"""
        if not self.visible:
            return
        
        # Prev button
        prev_text = f"[{ASCII.LEFT}]" if self.current_page > 1 else f" {ASCII.LEFT} "
        write(self.row, self.col, prev_text)
        
        # Page numbers
        page_text = f" Page {self.current_page} of {self.total_pages} "
        write(self.row, self.col + 4, page_text)
        
        # Next button
        next_text = f"[{ASCII.RIGHT}]" if self.current_page < self.total_pages else f" {ASCII.RIGHT} "
        write(self.row, self.col + 4 + len(page_text), next_text)


class Tabs(Component):
    """View switcher with active indicator"""
    
    def __init__(self, row, col, width, tabs=None):
        """Initialize tabs
        
        Args:
            row, col: Position
            width: Total width
            tabs: List of tab labels
        """
        super().__init__(row, col, width, 2)
        self.tabs = tabs if tabs else ["Tab 1", "Tab 2", "Tab 3"]
        self.active_index = 0
    
    def set_active(self, index):
        """Set active tab"""
        if 0 <= index < len(self.tabs):
            self.active_index = index
    
    def render(self):
        """Render tabs with active indicator"""
        if not self.visible:
            return
        
        # Calculate tab widths
        tab_width = self.width // len(self.tabs)
        
        current_col = self.col
        
        for i, tab in enumerate(self.tabs):
            is_active = (i == self.active_index)
            
            # Tab text
            tab_text = tab.center(tab_width)
            if is_active:
                # Active tab
                write(self.row, current_col, tab_text)
                # Underline
                write(self.row + 1, current_col, ASCII.HLINE_HEAVY * tab_width)
            else:
                # Inactive tab
                write(self.row, current_col, tab_text)
                write(self.row + 1, current_col, ASCII.HLINE * tab_width)
            
            current_col += tab_width
