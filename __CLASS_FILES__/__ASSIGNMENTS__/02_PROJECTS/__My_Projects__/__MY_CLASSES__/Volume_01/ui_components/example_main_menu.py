"""
Main Menu Example
Recreates MenuNav Standard Catalog Item #1 using UI components
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Menus.terminal import clear, hide_cursor, show_cursor, move, get_height, margin
from ui_components import *


def build_main_menu():
    """Build main menu using UI components
    
    From catalog:
    {main_menu:{
        type: FORK,
        fork:{
            1: item_registration,
            2: view_collection, 
            3: settings,
            4: exit_app
        },
        design:{
            1: menu_wrapper:{
                1.1: title,
                1.2: choice_menu_wrapper:{
                    1.2.1: prompt,
                    1.2.2: choices_wrapper:{
                        1.2.2.1: choice_object
                    }
                }
            }
        }
    }}
    """
    clear()
    hide_cursor()
    
    # Calculate responsive layout with margins
    content_row, content_col, content_width, content_height = margin(0.15, 0.15, 0.15, 0.15)
    
    # 1: menu_wrapper (Frame)
    menu_wrapper = Frame(
        content_row, 
        content_col, 
        content_width, 
        content_height,
        title="MAIN MENU",
        subtitle="Content Management System"
    )
    menu_wrapper.render()
    
    # 1.1: title (already in frame)
    
    # 1.2: choice_menu_wrapper (Section)
    choice_section_row = content_row + 5
    choice_section = Section(
        choice_section_row,
        content_col + 3,
        content_width - 6,
        content_height - 8,
        label="Please select an option",
        separator=True
    )
    choice_section.render()
    
    # 1.2.1: prompt (handled by section label)
    
    # 1.2.2: choices_wrapper with choice_objects
    choices_start_row = choice_section_row + 3
    
    # Individual choice objects
    choice1 = ChoiceObject(choices_start_row, content_col + 6, content_width - 12, 1, "REGISTER NEW ITEM")
    choice1.render()
    
    choice2 = ChoiceObject(choices_start_row + 2, content_col + 6, content_width - 12, 2, "VIEW COLLECTION")
    choice2.set_state(Component.STATE_ACTIVE)  # Highlight this one
    choice2.render()
    
    choice3 = ChoiceObject(choices_start_row + 4, content_col + 6, content_width - 12, 3, "SETTINGS")
    choice3.render()
    
    choice4 = ChoiceObject(choices_start_row + 6, content_col + 6, content_width - 12, 4, "EXIT")
    choice4.render()
    
    # Status bar at bottom
    status = StatusBar(0.98, "Ready | Use arrow keys to navigate, Enter to select")
    status.render()
    
    # Move cursor to bottom
    move(get_height(), 1)
    show_cursor()


if __name__ == "__main__":
    try:
        build_main_menu()
        input("\nPress Enter to exit...")
        clear()
    finally:
        show_cursor()
