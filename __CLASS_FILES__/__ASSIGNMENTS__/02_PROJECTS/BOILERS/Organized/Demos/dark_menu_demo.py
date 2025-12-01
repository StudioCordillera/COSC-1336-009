"""
DARK THEME MENU WITH BLUE HIGHLIGHTS
=====================================
Deep dark primary background with muted secondary and blue accent highlights
"""

import sys
import os

# Enable ANSI on Windows
if sys.platform == 'win32':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# ============================================================================
# COLOR PALETTE DEFINITION
# ============================================================================

# Primary Colors (Deep Dark Theme - 20% Less Contrast)
BG_DARK_PRIMARY = '\033[48;2;28;28;34m'      # Slightly raised dark blue-gray #1C1C22
BG_DARK_SECONDARY = '\033[48;2;35;35;42m'    # Closer to primary #23232A
BG_DARK_TERTIARY = '\033[48;2;42;42;52m'     # Subtle elevation #2A2A34

# Text Colors
FG_TEXT_PRIMARY = '\033[38;2;220;220;230m'   # Light gray text #DCDCE6
FG_TEXT_SECONDARY = '\033[38;2;160;160;175m' # Muted gray text #A0A0AF
FG_TEXT_DIM = '\033[38;2;100;100;115m'       # Dimmed text #646473

# Blue Highlight Colors
FG_BLUE_BRIGHT = '\033[38;2;100;180;255m'    # Bright blue #64B4FF
FG_BLUE_MEDIUM = '\033[38;2;70;140;220m'     # Medium blue #468CDC
FG_BLUE_ACCENT = '\033[38;2;50;120;200m'     # Accent blue #3278C8

BG_BLUE_HIGHLIGHT = '\033[48;2;40;80;140m'   # Blue highlight bg #28508C
BG_BLUE_SUBTLE = '\033[48;2;30;50;80m'       # Subtle blue bg #1E3250

# Muted Highlight (Secondary Accent)
FG_MUTED_HIGHLIGHT = '\033[38;2;180;160;140m' # Warm muted #B4A08C
BG_MUTED_HIGHLIGHT = '\033[48;2;60;55;50m'    # Muted bg #3C3732

# Status Colors
FG_SUCCESS = '\033[38;2;100;200;130m'        # Muted green #64C882
FG_WARNING = '\033[38;2;220;180;100m'        # Muted yellow #DCB464
FG_ERROR = '\033[38;2;220;100;100m'          # Muted red #DC6464

# Borders & Dividers
FG_BORDER = '\033[38;2;60;60;75m'            # Subtle border #3C3C4B
FG_BORDER_BRIGHT = '\033[38;2;80;80;100m'    # Brighter border #505064

# Reset
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# ============================================================================
# MENU COMPONENTS
# ============================================================================

def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_header():
    """Draw the menu header"""
    print(f"{BG_DARK_PRIMARY}{FG_TEXT_PRIMARY}")
    print(f"  ╔══════════════════════════════════════════════════════════╗")
    print(f"  ║{BG_DARK_SECONDARY}                                                          {BG_DARK_PRIMARY}║")
    print(f"  ║{BG_DARK_SECONDARY}  {FG_BLUE_BRIGHT}{BOLD}    APPLICATION MENU - DARK THEME DEMO    {RESET}{BG_DARK_SECONDARY}            {BG_DARK_PRIMARY}║")
    print(f"  ║{BG_DARK_SECONDARY}                                                          {BG_DARK_PRIMARY}║")
    print(f"  ╚══════════════════════════════════════════════════════════╝")
    print(RESET)

def draw_menu_item(number, label, selected=False, status=None):
    """Draw a single menu item"""
    if selected:
        # Selected item with blue highlight
        bg = BG_BLUE_HIGHLIGHT
        fg_num = FG_BLUE_BRIGHT + BOLD
        fg_text = FG_TEXT_PRIMARY + BOLD
        marker = "▶"
    else:
        # Normal item
        bg = BG_DARK_SECONDARY
        fg_num = FG_BLUE_MEDIUM
        fg_text = FG_TEXT_PRIMARY
        marker = " "
    
    # Status indicator
    status_text = ""
    if status == "new":
        status_text = f" {FG_BLUE_BRIGHT}[NEW]{RESET}{bg}"
    elif status == "active":
        status_text = f" {FG_SUCCESS}[ACTIVE]{RESET}{bg}"
    elif status == "disabled":
        status_text = f" {FG_TEXT_DIM}[DISABLED]{RESET}{bg}"
    
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}│{RESET} {bg}{marker} {fg_num}[{number}]{RESET}{bg} {fg_text}{label}{status_text}{' ' * (45 - len(label) - len(status_text))} {BG_DARK_PRIMARY}{FG_BORDER}│{RESET}")

def draw_divider():
    """Draw a divider line"""
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}├{'─' * 58}┤{RESET}")

def draw_footer():
    """Draw the menu footer"""
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}╰{'─' * 58}╯{RESET}")
    print()
    print(f"{BG_DARK_TERTIARY}{FG_TEXT_SECONDARY}  Press number key to select  │  {FG_BLUE_MEDIUM}[Q]{FG_TEXT_SECONDARY} Quit  │  {FG_BLUE_MEDIUM}[H]{FG_TEXT_SECONDARY} Help  {RESET}")
    print()

def draw_info_panel():
    """Draw an information panel"""
    print(f"{BG_DARK_SECONDARY}{FG_TEXT_PRIMARY}  ")
    print(f"  {FG_BORDER_BRIGHT}╭{'─' * 56}╮{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}{FG_BLUE_BRIGHT}{BOLD}  COLOR PALETTE PREVIEW{RESET}{BG_DARK_TERTIARY}{' ' * 33}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}├{'─' * 56}┤{RESET}")
    
    # Color swatches
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}  {FG_TEXT_SECONDARY}Primary Dark:   {BG_DARK_PRIMARY}{'  ' * 10}{RESET}{BG_DARK_TERTIARY}  #121218{' ' * 7}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}  {FG_TEXT_SECONDARY}Secondary Dark: {BG_DARK_SECONDARY}{'  ' * 10}{RESET}{BG_DARK_TERTIARY}  #1C1C24{' ' * 7}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}  {FG_TEXT_SECONDARY}Blue Highlight: {BG_BLUE_HIGHLIGHT}{'  ' * 10}{RESET}{BG_DARK_TERTIARY}  #28508C{' ' * 7}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}  {FG_TEXT_SECONDARY}Muted Accent:   {BG_MUTED_HIGHLIGHT}{'  ' * 10}{RESET}{BG_DARK_TERTIARY}  #3C3732{' ' * 7}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}{' ' * 56}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}  {FG_TEXT_SECONDARY}Text Colors:{' ' * 43}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}  {FG_TEXT_PRIMARY}Primary Text  {FG_TEXT_SECONDARY}Secondary Text  {FG_TEXT_DIM}Dimmed Text{RESET}{BG_DARK_TERTIARY}{' ' * 9}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}  {FG_BLUE_BRIGHT}Bright Blue   {FG_BLUE_MEDIUM}Medium Blue   {FG_BLUE_ACCENT}Accent Blue{RESET}{BG_DARK_TERTIARY}{' ' * 9}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}{' ' * 56}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}  {FG_TEXT_SECONDARY}Status:{RESET}{BG_DARK_TERTIARY} {FG_SUCCESS}● Success{RESET}{BG_DARK_TERTIARY}  {FG_WARNING}● Warning{RESET}{BG_DARK_TERTIARY}  {FG_ERROR}● Error{RESET}{BG_DARK_TERTIARY}{' ' * 15}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}╰{'─' * 56}╯{RESET}")
    print()

def draw_complete_menu():
    """Draw the complete menu demonstration"""
    clear_screen()
    
    # Set background color for entire screen
    print(f"{BG_DARK_PRIMARY}{FG_TEXT_PRIMARY}")
    print()
    
    # Header
    draw_header()
    
    # Main menu section
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}╭{'─' * 58}╮{RESET}")
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}│{RESET}{BG_DARK_SECONDARY}{FG_TEXT_SECONDARY}  MAIN MENU{' ' * 47}{BG_DARK_PRIMARY}{FG_BORDER}│{RESET}")
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}├{'─' * 58}┤{RESET}")
    
    # Menu items
    draw_menu_item("1", "Dashboard Overview", selected=True, status="active")
    draw_menu_item("2", "Data Analysis", status="new")
    draw_menu_item("3", "Reports & Statistics")
    draw_menu_item("4", "User Management")
    draw_menu_item("5", "System Settings")
    
    draw_divider()
    
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}│{RESET}{BG_DARK_SECONDARY}{FG_TEXT_SECONDARY}  TOOLS{' ' * 51}{BG_DARK_PRIMARY}{FG_BORDER}│{RESET}")
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}├{'─' * 58}┤{RESET}")
    
    draw_menu_item("6", "Import Data")
    draw_menu_item("7", "Export Results")
    draw_menu_item("8", "Backup & Restore", status="disabled")
    
    draw_divider()
    
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}│{RESET}{BG_DARK_SECONDARY}{FG_TEXT_SECONDARY}  HELP & INFO{' ' * 45}{BG_DARK_PRIMARY}{FG_BORDER}│{RESET}")
    print(f"{BG_DARK_PRIMARY}  {FG_BORDER}├{'─' * 58}┤{RESET}")
    
    draw_menu_item("9", "Documentation")
    draw_menu_item("0", "About")
    
    # Footer
    draw_footer()
    
    # Info panel
    draw_info_panel()
    
    # Status bar at bottom
    print(f"{BG_DARK_TERTIARY}{FG_TEXT_DIM}  System Status: {FG_SUCCESS}● Online{RESET}{BG_DARK_TERTIARY}{FG_TEXT_DIM}  │  Users: {FG_BLUE_BRIGHT}247{RESET}{BG_DARK_TERTIARY}{FG_TEXT_DIM}  │  Version: {FG_MUTED_HIGHLIGHT}2.1.0{RESET}{BG_DARK_TERTIARY}{' ' * 8}{RESET}")
    print(RESET)

# ============================================================================
# ADDITIONAL DEMOS
# ============================================================================

def draw_card_demo():
    """Draw card-style components"""
    print(f"\n{BG_DARK_PRIMARY}  {FG_BLUE_BRIGHT}{BOLD}CARD COMPONENTS DEMO{RESET}\n")
    
    # Card 1
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}╭{'─' * 28}╮{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}{FG_BLUE_BRIGHT}{BOLD}  Active Projects{RESET}{BG_DARK_TERTIARY}{' ' * 13}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}├{'─' * 28}┤{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}{FG_TEXT_PRIMARY}  Total: {FG_BLUE_BRIGHT}{BOLD}42{RESET}{BG_DARK_TERTIARY}{' ' * 16}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}{FG_TEXT_SECONDARY}  Completed: {FG_SUCCESS}28{RESET}{BG_DARK_TERTIARY}{' ' * 10}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}│{RESET}{BG_DARK_TERTIARY}{FG_TEXT_SECONDARY}  In Progress: {FG_WARNING}14{RESET}{BG_DARK_TERTIARY}{' ' * 8}{BG_DARK_SECONDARY}{FG_BORDER_BRIGHT}│{RESET}")
    print(f"{BG_DARK_SECONDARY}  {FG_BORDER_BRIGHT}╰{'─' * 28}╯{RESET}")
    
    print()

def draw_progress_demo():
    """Draw progress bars"""
    print(f"\n{BG_DARK_PRIMARY}  {FG_BLUE_BRIGHT}{BOLD}PROGRESS INDICATORS{RESET}\n")
    
    print(f"{BG_DARK_SECONDARY}  {FG_TEXT_PRIMARY}Loading Data:{RESET}")
    print(f"{BG_DARK_TERTIARY}  [{BG_BLUE_HIGHLIGHT}{'█' * 20}{BG_DARK_TERTIARY}{'░' * 10}{BG_DARK_TERTIARY}] {FG_BLUE_BRIGHT}67%{RESET}")
    print()
    
    print(f"{BG_DARK_SECONDARY}  {FG_TEXT_PRIMARY}Processing:{RESET}")
    print(f"{BG_DARK_TERTIARY}  [{BG_BLUE_HIGHLIGHT}{'█' * 15}{BG_DARK_TERTIARY}{'░' * 15}{BG_DARK_TERTIARY}] {FG_BLUE_BRIGHT}50%{RESET}")
    print()
    
    print(f"{BG_DARK_SECONDARY}  {FG_TEXT_PRIMARY}Upload:{RESET}")
    print(f"{BG_DARK_TERTIARY}  [{BG_BLUE_HIGHLIGHT}{'█' * 30}{BG_DARK_TERTIARY}] {FG_SUCCESS}100%{RESET}")
    print()

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    draw_complete_menu()
    
    # Optional: Show additional demos
    print(f"\n{BG_DARK_PRIMARY}{FG_BORDER}{'═' * 62}{RESET}\n")
    draw_card_demo()
    draw_progress_demo()
    
    print(f"{BG_DARK_PRIMARY}{FG_TEXT_DIM}  Press any key to exit...{RESET}")
    print()
