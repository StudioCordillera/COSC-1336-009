class SimpleMenu:
    """Basic vertical menu with keyboard navigation"""
    
    def __init__(self, items: List[str], title: str = "Menu"):
        # Core state (-1 atomics)
        self.items = items                    # List of menu item strings
        self.title = title                    # Menu title
        self.selected_index = 0               # Currently selected item
        self.position = (0, 0)               # Screen coordinates (Coordinate)
        
        # Visual properties (styled atomics)
        self.fg_normal = '\033[37m'          # Normal text color (Color)
        self.fg_selected = '\033[30m'        # Selected text color (Color)
        self.bg_selected = '\033[47m'        # Selected background (Color)
        self.border_char = '─'               # Border character (Character)
        
        # State tracking
        self.visible = True
        self.focused = True
    
    def render(self) -> List[str]:
        """Generate menu display lines"""
        output = []
        
        # Title with border
        width = max(len(self.title), max(len(item) for item in self.items)) + 4
        output.append(f"╭{'─' * (width - 2)}╮")
        output.append(f"│ {self.title.center(width - 4)} │")
        output.append(f"├{'─' * (width - 2)}┤")
        
        # Menu items
        for i, item in enumerate(self.items):
            if i == self.selected_index:
                # Selected item (Styled Character composition)
                output.append(f"│{self.bg_selected}{self.fg_selected}▶ {item.ljust(width - 4)}\033[0m│")
            else:
                # Normal item
                output.append(f"│{self.fg_normal}  {item.ljust(width - 4)}\033[0m│")
        
        # Bottom border
        output.append(f"╰{'─' * (width - 2)}╯")
        
        return output
    
    def handle_input(self, key: str) -> Optional[int]:
        """Handle keyboard input, return selected index if enter pressed"""
        if key == 'up' and self.selected_index > 0:
            self.selected_index -= 1
        elif key == 'down' and self.selected_index < len(self.items) - 1:
            self.selected_index += 1
        elif key == 'enter':
            return self.selected_index
        return None