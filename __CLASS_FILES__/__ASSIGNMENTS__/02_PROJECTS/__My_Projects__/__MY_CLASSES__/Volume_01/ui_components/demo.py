"""
UI Components Demo
Showcases all 31 components with various states and layouts
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Menus.terminal import clear, hide_cursor, show_cursor, move, get_height, write, draw_box, ASCII  # noqa: F401
from ui_components import (
    Component, Wrapper, Panel, Frame, Section, Menu, Dialogue,
    Header, Label, Prompt, Message, List, Tree, Preview,
    InputField, Button, TextField, Dropdown, TextArea, Selector,
    Checkbox, Toggle, Breadcrumb, NavigationControls, NavigationButtons,
    Pagination, Tabs, ChoiceObject, ParamField, CheckboxList,
    DirectoryTree, StatusBar
)


# Grid Layout Helper
class GridLayout:
    """Helper class for creating grid-based layouts"""
    
    def __init__(self, rows, cols, margin=2, padding=1):
        self.rows = rows
        self.cols = cols
        self.margin = margin
        self.padding = padding
        
        # Calculate total available space
        self.total_width = 78  # Terminal width
        self.total_height = 35  # Terminal height
        
        # Calculate cell dimensions
        self.cell_width = (self.total_width - (margin * 2) - (cols - 1) * padding) // cols
        self.cell_height = (self.total_height - (margin * 2) - (rows - 1) * padding) // rows
    
    def get_cell(self, row, col):
        """Get the position and size of a grid cell
        Returns: (y, x, width, height)
        """
        x = self.margin + col * (self.cell_width + self.padding)
        y = self.margin + row * (self.cell_height + self.padding)
        return (y, x, self.cell_width, self.cell_height)
    
    def draw_grid(self):
        """Draw the entire grid structure"""
        for row in range(self.rows):
            for col in range(self.cols):
                y, x, w, h = self.get_cell(row, col)
                draw_box(y, x, w, h)
    
    def get_inner_bounds(self, row, col, margin=1):
        """Get inner bounds of a cell with margin
        Returns: (y, x, width, height)
        """
        y, x, w, h = self.get_cell(row, col)
        return (y + margin, x + margin, w - (2 * margin), h - (2 * margin))


def demo_containers():
    """Demo: Container components using grid layout"""
    clear()
    hide_cursor()
    
    # Create 3x2 grid layout
    grid = GridLayout(rows=3, cols=2, margin=2, padding=2)
    
    # Draw grid structure
    grid.draw_grid()
    
    # Title at top
    write(1, 3, "=== CONTAINER COMPONENTS (3x2 Grid) ===")
    
    # [0,0] Wrapper
    y, x, w, h = grid.get_inner_bounds(0, 0)
    write(y, x, "WRAPPER")
    wrapper = Wrapper(y+1, x+1, w-4, h-3, padding=1, border=True)
    wrapper.render()
    write(y+2, x+3, "Wrapped content")
    
    # [0,1] Panel
    y, x, w, h = grid.get_inner_bounds(0, 1)
    write(y, x, "PANEL")
    panel = Panel(y+1, x+1, w-4, h-3, title="Panel Example")
    panel.render()
    write(y+3, x+3, "Panel content")
    
    # [1,0] Frame
    y, x, w, h = grid.get_inner_bounds(1, 0)
    write(y, x, "FRAME")
    frame = Frame(y+1, x+1, w-4, h-3, title="Frame Title", subtitle="Subtitle")
    frame.render()
    
    # [1,1] Section
    y, x, w, h = grid.get_inner_bounds(1, 1)
    write(y, x, "SECTION")
    section = Section(y+1, x+1, w-4, h-3, label="Section Label", separator=True)
    section.render()
    write(y+3, x+3, "Section content")
    
    # [2,0] Menu
    y, x, w, h = grid.get_inner_bounds(2, 0)
    write(y, x, "MENU")
    menu = Menu(y+1, x+1, w-4, h-3, title="MAIN MENU", prompt="Select:")
    menu.add_choice("Register")
    menu.add_choice("View")
    menu.add_choice("Settings")
    menu.render()
    
    # [2,1] Dialogue
    y, x, w, h = grid.get_inner_bounds(2, 1)
    write(y, x, "DIALOGUE")
    dialogue = Dialogue(y+2, x+3, w-8, h-4, title="Dialog Box")
    dialogue.render()
    write(y+4, x+6, "Modal example")
    
    move(get_height(), 1)
    show_cursor()
    input("\nPress Enter to continue...")


def demo_display():
    """Demo: Display components using grid layout"""
    clear()
    hide_cursor()
    
    # Create 4x2 grid layout
    grid = GridLayout(rows=4, cols=2, margin=2, padding=2)
    
    # Draw grid structure
    grid.draw_grid()
    
    # Title at top
    write(1, 3, "=== DISPLAY COMPONENTS (4x2 Grid) ===")
    
    # [0,0-1] Header (spans 2 columns)
    y, x, w, h = grid.get_cell(0, 0)
    _, x2, w2, _ = grid.get_cell(0, 1)
    full_width = (x2 + w2) - x
    write(y+1, x+2, "HEADER")
    header = Header(y+2, x+3, full_width-6, "This is a Header", underline=True)
    header.render()
    
    # [1,0] Labels & Prompt
    y, x, w, h = grid.get_inner_bounds(1, 0)
    write(y, x, "LABELS & PROMPT")
    label1 = Label(y+1, x+1, w-4, "Left-aligned", align="left")
    label1.render()
    label2 = Label(y+2, x+1, w-4, "Centered", align="center")
    label2.render()
    label3 = Label(y+3, x+1, w-4, "Right", align="right")
    label3.render()
    prompt = Prompt(y+5, x+1, w-4, "This is a prompt")
    prompt.render()
    
    # [1,1] Messages
    y, x, w, h = grid.get_inner_bounds(1, 1)
    write(y, x, "MESSAGES")
    msg_info = Message(y+2, x+1, w-4, "Info message", style=Message.STYLE_INFO)
    msg_info.render()
    msg_warning = Message(y+5, x+1, w-4, "Warning!", style=Message.STYLE_WARNING)
    msg_warning.render()
    
    # [2,0] List
    y, x, w, h = grid.get_inner_bounds(2, 0)
    write(y, x, "LIST")
    item_list = List(y+1, x+1, w-4, h-3, numbered=True)
    item_list.add_item("First item")
    item_list.add_item("Second item")
    item_list.add_item("Third item")
    item_list.render()
    
    # [2,1] Tree
    y, x, w, h = grid.get_inner_bounds(2, 1)
    write(y, x, "TREE")
    tree = Tree(y+1, x+1, w-4, h-3, indent=2)
    tree.add_node("Root", level=0)
    tree.add_node("Child 1", level=1)
    tree.add_node("Child 2", level=1)
    tree.add_node("Grandchild", level=2)
    tree.render()
    
    # [3,0-1] Preview (spans 2 columns)
    y, x, w, h = grid.get_cell(3, 0)
    _, x2, w2, _ = grid.get_cell(3, 1)
    full_width = (x2 + w2) - x
    write(y+1, x+2, "PREVIEW")
    preview = Preview(y+2, x+3, full_width-8, h-4, title="Content Preview")
    preview.set_lines([
        "Line 1 of content",
        "Line 2 of content",
        "Line 3 with more text"
    ])
    preview.render()
    
    move(get_height(), 1)
    show_cursor()
    input("\nPress Enter to continue...")


def demo_input():
    """Demo: Input components using grid layout"""
    clear()
    hide_cursor()
    
    # Create 5x2 grid layout
    grid = GridLayout(rows=5, cols=2, margin=2, padding=2)
    
    # Draw grid structure
    grid.draw_grid()
    
    # Title at top
    write(1, 3, "=== INPUT COMPONENTS (5x2 Grid) ===")
    
    # [0,0] Input Fields
    y, x, w, h = grid.get_inner_bounds(0, 0)
    write(y, x, "INPUT FIELDS")
    input_field = InputField(y+1, x+1, w-4, placeholder="Enter text...")
    input_field.render()
    input_focused = InputField(y+3, x+1, w-4, placeholder="Focused")
    input_focused.set_state(Component.STATE_FOCUSED)
    input_focused.set_value("Some text")
    input_focused.render()
    
    # [0,1] Buttons
    y, x, w, h = grid.get_inner_bounds(0, 1)
    write(y, x, "BUTTONS")
    btn_normal = Button(y+1, x+2, w-6, "Normal")
    btn_normal.render()
    btn_active = Button(y+3, x+2, w-6, "Active")
    btn_active.set_state(Component.STATE_ACTIVE)
    btn_active.render()
    
    # [1,0] Text Fields
    y, x, w, h = grid.get_inner_bounds(1, 0)
    write(y, x, "TEXT FIELDS")
    text_field = TextField(y+1, x+1, w-4, label="Username", required=True)
    text_field.render()
    text_field_filled = TextField(y+3, x+1, w-4, label="Email", required=True)
    text_field_filled.set_value("user@example.com")
    text_field_filled.render()
    
    # [1,1] Dropdown
    y, x, w, h = grid.get_inner_bounds(1, 1)
    write(y, x, "DROPDOWN")
    dropdown = Dropdown(y+1, x+2, w-6, label="Theme", options=["Light", "Dark", "Auto"])
    dropdown.render()
    
    # [2,0] Text Area
    y, x, w, h = grid.get_inner_bounds(2, 0)
    write(y, x, "TEXT AREA")
    text_area = TextArea(y+1, x+1, w-4, h-3)
    text_area.set_lines([
        "Multi-line text",
        "area component",
        "with lines"
    ])
    text_area.render()
    
    # [2,1] Selector
    y, x, w, h = grid.get_inner_bounds(2, 1)
    write(y, x, "SELECTOR")
    selector = Selector(y+1, x+2, w-6, options=["Option A", "Option B", "Option C"])
    selector.render()
    
    # [3,0] Checkboxes
    y, x, w, h = grid.get_inner_bounds(3, 0)
    write(y, x, "CHECKBOXES")
    checkbox1 = Checkbox(y+1, x+1, "Enable notifications", checked=False)
    checkbox1.render()
    checkbox2 = Checkbox(y+2, x+1, "Remember me", checked=True)
    checkbox2.render()
    checkbox3 = Checkbox(y+3, x+1, "Focused option", checked=False)
    checkbox3.set_state(Component.STATE_FOCUSED)
    checkbox3.render()
    
    # [3,1] Toggles
    y, x, w, h = grid.get_inner_bounds(3, 1)
    write(y, x, "TOGGLES")
    toggle1 = Toggle(y+1, x+1, "Dark Mode", enabled=False)
    toggle1.render()
    toggle2 = Toggle(y+2, x+1, "Auto-save", enabled=True)
    toggle2.render()
    toggle3 = Toggle(y+3, x+1, "Focused toggle", enabled=True)
    toggle3.set_state(Component.STATE_FOCUSED)
    toggle3.render()
    
    # [4,0-1] Button disabled (spans 2 columns)
    y, x, w, h = grid.get_cell(4, 0)
    _, x2, w2, _ = grid.get_cell(4, 1)
    full_width = (x2 + w2) - x
    btn_disabled = Button(y+2, x + (full_width // 2) - 10, 20, "Disabled Button")
    btn_disabled.set_state(Component.STATE_DISABLED)
    btn_disabled.render()
    
    move(get_height(), 1)
    show_cursor()
    input("\nPress Enter to continue...")


def demo_navigation():
    """Demo: Navigation components using grid layout"""
    clear()
    hide_cursor()
    
    # Create 4x1 grid layout (4 rows, 1 column)
    grid = GridLayout(rows=4, cols=1, margin=2, padding=2)
    
    # Draw grid structure
    grid.draw_grid()
    
    # Title at top
    write(1, 3, "=== NAVIGATION COMPONENTS (4x1 Grid) ===")
    
    # [0,0] Breadcrumb
    y, x, w, h = grid.get_inner_bounds(0, 0)
    write(y, x, "BREADCRUMB")
    breadcrumb = Breadcrumb(y+1, x+1, w-4, path=["Home", "Documents", "Projects", "MyApp"])
    breadcrumb.render()
    
    # [1,0] Navigation Controls & Buttons
    y, x, w, h = grid.get_inner_bounds(1, 0)
    write(y, x, "NAVIGATION CONTROLS & BUTTONS")
    nav_controls = NavigationControls(y+1, x+2)
    nav_controls.render()
    
    nav_buttons = NavigationButtons(y+1, x+30, buttons=["Save", "Cancel", "Help"])
    nav_buttons.select_button(0)
    nav_buttons.render()
    
    # [2,0] Pagination
    y, x, w, h = grid.get_inner_bounds(2, 0)
    write(y, x, "PAGINATION")
    pagination = Pagination(y+1, x+2, total_pages=10, current_page=5)
    pagination.render()
    
    # [3,0] Tabs
    y, x, w, h = grid.get_inner_bounds(3, 0)
    write(y, x, "TABS")
    tabs = Tabs(y+1, x+2, w-6, tabs=["Overview", "Details", "Settings", "About"])
    tabs.set_active(1)
    tabs.render()
    
    move(get_height(), 1)
    show_cursor()
    input("\nPress Enter to continue...")


def demo_specialized():
    """Demo: Specialized components using grid layout"""
    clear()
    hide_cursor()
    
    # Create 4x2 grid layout
    grid = GridLayout(rows=4, cols=2, margin=2, padding=2)
    
    # Draw grid structure
    grid.draw_grid()
    
    # Title at top
    write(1, 3, "=== SPECIALIZED COMPONENTS (4x2 Grid) ===")
    
    # [0,0] ChoiceObject
    y, x, w, h = grid.get_inner_bounds(0, 0)
    write(y, x, "CHOICE OBJECTS")
    choice1 = ChoiceObject(y+1, x+1, w-4, 1, "Register New Item")
    choice1.render()
    choice2 = ChoiceObject(y+2, x+1, w-4, 2, "View Collection")
    choice2.set_state(Component.STATE_ACTIVE)
    choice2.render()
    choice3 = ChoiceObject(y+3, x+1, w-4, 3, "Settings")
    choice3.render()
    
    # [0,1] ParamField
    y, x, w, h = grid.get_inner_bounds(0, 1)
    write(y, x, "PARAMETER FIELDS")
    param1 = ParamField(y+1, x+1, w-4, "Item Name", value="MyItem")
    param1.render()
    param2 = ParamField(y+3, x+1, w-4, "Category")
    param2.set_state(Component.STATE_FOCUSED)
    param2.render()
    
    # [1,0] CheckboxList
    y, x, w, h = grid.get_inner_bounds(1, 0)
    write(y, x, "CHECKBOX LIST")
    checkbox_list = CheckboxList(y+1, x+1, w-4, h-3, items=[
        "Item Alpha",
        "Item Beta",
        "Item Gamma",
        "Item Delta",
        "Item Epsilon"
    ])
    checkbox_list.toggle_item(1)
    checkbox_list.toggle_item(3)
    checkbox_list.focused_index = 2
    checkbox_list.set_state(Component.STATE_FOCUSED)
    checkbox_list.render()
    
    # [1,1] DirectoryTree
    y, x, w, h = grid.get_inner_bounds(1, 1)
    write(y, x, "DIRECTORY TREE")
    dir_tree = DirectoryTree(y+1, x+1, w-4, h-3)
    dir_tree.add_entry("Documents", indent_level=0, is_dir=True)
    dir_tree.add_entry("file1.txt", indent_level=1, is_dir=False)
    dir_tree.add_entry("file2.txt", indent_level=1, is_dir=False)
    dir_tree.add_entry("Projects", indent_level=0, is_dir=True)
    dir_tree.add_entry("project_a", indent_level=1, is_dir=True)
    dir_tree.add_entry("README.md", indent_level=2, is_dir=False)
    dir_tree.set_selected(3)
    dir_tree.render()
    
    # [2,0-1] Status Bar (spans 2 columns)
    y, x, w, h = grid.get_cell(2, 0)
    _, x2, w2, _ = grid.get_cell(2, 1)
    full_width = (x2 + w2) - x
    write(y+1, x+2, "STATUS BAR")
    status_bar = StatusBar(0.95, text="Ready | Components: 31 | Status: Demo Mode")
    status_bar.render()
    
    # [3,0-1] Empty space for status info
    y, x, w, h = grid.get_cell(3, 0)
    write(y+2, x+20, "Grid Layout System - 4 rows x 2 columns")
    
    move(get_height() - 2, 1)
    show_cursor()
    input("\nPress Enter to continue...")


def demo_all():
    """Run all demos"""
    hide_cursor()
    
    try:
        demo_containers()
        demo_display()
        demo_input()
        demo_navigation()
        demo_specialized()
        
        clear()
        print("\n=== DEMO COMPLETE ===")
        print("\nAll 31 components demonstrated!")
        print("\nComponent Summary:")
        print("  - 6 Container components")
        print("  - 8 Display components")
        print("  - 8 Input components")
        print("  - 5 Navigation components")
        print("  - 5 Specialized components")
        print("\nTotal: 32 components (including base Component class)")
        
    finally:
        show_cursor()


if __name__ == "__main__":
    demo_all()
