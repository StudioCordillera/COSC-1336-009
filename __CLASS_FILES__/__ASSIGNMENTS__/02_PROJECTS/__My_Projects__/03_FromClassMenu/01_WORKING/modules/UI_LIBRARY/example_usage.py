"""
Example Usage: UI_LIBRARY Components
Demonstrates how to use the segmented classes for cross-platform CLI applications
"""

import sys
import time

# Import UI_LIBRARY components
from input_mappings import create_input_mapper
from event_configs import EventManager, KeyEvent, MouseEvent
from ascii_config import ASCIIConfigLoader


# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE 1: Basic Input Mapping
# ═══════════════════════════════════════════════════════════════════════════

def example_input_mapping():
    """Example: Platform-agnostic input handling"""
    
    print("Example 1: Input Mapping")
    print("Press arrow keys, ESC to quit\n")
    
    # Create appropriate input mapper for platform
    input_mapper = create_input_mapper()
    input_mapper.initialize()
    
    try:
        running = True
        while running:
            # Check for keyboard input
            if input_mapper.has_input():
                key = input_mapper.read_key()
                if key:
                    print(f"Key pressed: {key}")
                    if key == 'ESC':
                        running = False
            
            time.sleep(0.05)  # Small delay to reduce CPU
    
    finally:
        input_mapper.cleanup()
        print("\nCleanup complete")


# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE 2: Event Manager with Handlers
# ═══════════════════════════════════════════════════════════════════════════

def example_event_manager():
    """Example: Using EventManager to handle input events"""
    
    print("Example 2: Event Manager")
    print("Press UP/DOWN, ENTER to select, ESC to quit\n")
    
    # Create event manager
    event_manager = EventManager()
    
    # State
    selected = 0
    items = ["Option 1", "Option 2", "Option 3", "Exit"]
    
    # Define handlers
    def handle_up(event: KeyEvent):
        nonlocal selected
        selected = (selected - 1) % len(items)
        print(f"Selected: {items[selected]}")
    
    def handle_down(event: KeyEvent):
        nonlocal selected
        selected = (selected + 1) % len(items)
        print(f"Selected: {items[selected]}")
    
    def handle_enter(event: KeyEvent):
        print(f"\n✓ Activated: {items[selected]}\n")
    
    # Register handlers
    event_manager.register_key_handler('UP', handle_up)
    event_manager.register_key_handler('DOWN', handle_down)
    event_manager.register_key_handler('ENTER', handle_enter)
    
    # Create input mapper
    input_mapper = create_input_mapper()
    input_mapper.initialize()
    
    try:
        print(f"Selected: {items[selected]}")
        running = True
        
        while running:
            if input_mapper.has_input():
                key = input_mapper.read_key()
                if key:
                    if key == 'ESC':
                        running = False
                    else:
                        # Process through event manager
                        event_manager.process_key(key)
            
            time.sleep(0.05)
    
    finally:
        input_mapper.cleanup()
        print("\nCleanup complete")


# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE 3: ASCII Config for UI Elements
# ═══════════════════════════════════════════════════════════════════════════

def example_ascii_config():
    """Example: Using ASCII config for styled UI elements"""
    
    print("Example 3: ASCII Configuration")
    print("-" * 50)
    
    # Load configuration (dark theme with Unicode)
    config = ASCIIConfigLoader(theme_name="dark", use_unicode=True)
    ui = config.get_ui_config()
    chars = config.chars
    ansi = config.ansi
    
    # Print cursor control
    print(f"{ansi.CLEAR_SCREEN}{ansi.cursor_pos(1, 1)}", end='')
    
    # Draw a styled box
    print(ui.draw_box(5, 3, 50, 10, style="double", title="Menu System"))
    
    # Draw menu items
    menu_items = [
        ("Start Application", "normal"),
        ("Settings", "highlight"),
        ("Help", "normal"),
        ("Exit", "error")
    ]
    
    for i, (text, style) in enumerate(menu_items):
        y = 5 + i
        styled_text = ui.style_text(f"  {chars.POINTER_RIGHT} {text}", style)
        print(f"{ansi.cursor_pos(y, 7)}{styled_text}", end='')
    
    # Status line
    status = ui.style_text(f"{chars.CHECK_MARK} Ready", "success")
    print(f"{ansi.cursor_pos(11, 7)}{status}", end='')
    
    # Footer
    print(f"{ansi.cursor_pos(15, 1)}", end='')
    print(f"\nPress Ctrl+C to exit\n")
    
    try:
        input()  # Wait for user
    except KeyboardInterrupt:
        pass
    
    # Cleanup
    print(f"{ansi.CLEAR_SCREEN}{ansi.cursor_pos(1, 1)}", end='')
    print("Example complete\n")


# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE 4: Complete Integration - Mouse + Keyboard + Styled UI
# ═══════════════════════════════════════════════════════════════════════════

def example_complete_integration():
    """Example: Full integration of all components"""
    
    print("Example 4: Complete Integration")
    print("Use arrow keys or mouse to navigate, ENTER/Click to select\n")
    
    # Setup components
    config = ASCIIConfigLoader(theme_name="dark", use_unicode=True)
    ui = config.get_ui_config()
    ansi = config.ansi
    chars = config.chars
    
    event_manager = EventManager()
    input_mapper = create_input_mapper()
    input_mapper.initialize()
    
    # State
    items = ["🚀 Start", "⚙️ Settings", "📊 Stats", "❌ Exit"]
    selected = 0
    needs_render = True
    
    def render():
        """Render the UI"""
        print(f"{ansi.CLEAR_SCREEN}{ansi.cursor_pos(1, 1)}", end='')
        print(ui.draw_box(2, 2, 40, len(items) + 4, style="single", title="Main Menu"))
        
        for i, item in enumerate(items):
            y = 4 + i
            if i == selected:
                text = ui.style_text(f" {chars.POINTER_RIGHT} {item}", "highlight")
            else:
                text = ui.style_text(f"   {item}", "normal")
            print(f"{ansi.cursor_pos(y, 4)}{text}", end='')
        
        print(f"{ansi.cursor_pos(len(items) + 8, 1)}", end='')
        print("↑↓: Navigate | Enter: Select | ESC: Quit\n")
    
    # Event handlers
    def handle_up(event):
        nonlocal selected, needs_render
        selected = (selected - 1) % len(items)
        needs_render = True
    
    def handle_down(event):
        nonlocal selected, needs_render
        selected = (selected + 1) % len(items)
        needs_render = True
    
    def handle_select(event):
        print(f"\n{ui.style_text(f'{chars.CHECK_MARK} Selected: {items[selected]}', 'success')}\n")
        time.sleep(1)
    
    def handle_mouse_click(event: MouseEvent):
        nonlocal selected, needs_render
        # Simple click detection (4-7 are menu item rows)
        if 4 <= event.y <= 7:
            item_index = event.y - 4
            if 0 <= item_index < len(items):
                selected = item_index
                needs_render = True
                handle_select(event)
    
    # Register handlers
    event_manager.register_key_handler('UP', handle_up)
    event_manager.register_key_handler('DOWN', handle_down)
    event_manager.register_key_handler('ENTER', handle_select)
    event_manager.register_mouse_handler('CLICK', handle_mouse_click)
    
    # Main loop
    try:
        running = True
        
        while running:
            if needs_render:
                render()
                needs_render = False
            
            # Check keyboard
            if input_mapper.has_input():
                key = input_mapper.read_key()
                if key:
                    if key == 'ESC':
                        running = False
                    else:
                        event_manager.process_key(key)
            
            # Check mouse
            mouse_event = input_mapper.read_mouse_event()
            if mouse_event:
                if mouse_event['event_type'] == 'CLICK' and mouse_event['button']:
                    event_manager.process_mouse(
                        x=mouse_event['x'],
                        y=mouse_event['y'],
                        button=mouse_event['button'],
                        event_type=mouse_event['event_type']
                    )
            
            time.sleep(0.05)
    
    except KeyboardInterrupt:
        pass
    
    finally:
        input_mapper.cleanup()
        print(f"{ansi.CLEAR_SCREEN}{ansi.cursor_pos(1, 1)}", end='')
        print("Example complete\n")


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Run examples"""
    
    examples = {
        '1': ("Basic Input Mapping", example_input_mapping),
        '2': ("Event Manager", example_event_manager),
        '3': ("ASCII Config UI", example_ascii_config),
        '4': ("Complete Integration", example_complete_integration),
    }
    
    print("=" * 60)
    print("UI_LIBRARY Examples")
    print("=" * 60)
    print("\nAvailable examples:")
    for key, (name, _) in examples.items():
        print(f"  {key}. {name}")
    print()
    
    choice = input("Select example (1-4, or 'all'): ").strip()
    
    if choice == 'all':
        for key in sorted(examples.keys()):
            name, func = examples[key]
            print(f"\n{'=' * 60}")
            print(f"Running: {name}")
            print('=' * 60)
            func()
            input("\nPress Enter to continue...")
    elif choice in examples:
        name, func = examples[choice]
        func()
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()
