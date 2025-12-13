"""
State Design Pattern

Intent: Lets an object alter its behavior when its internal state changes. It
appears as if the object changed its class.

===============================================================================
MENU ORCHESTRATION APPLICATION
===============================================================================

This pattern is ideal for menu orchestration systems with the following features:

REQUIREMENTS MET:
✅ Orchestrate menu state across navigation flows (linear and intertwined)
✅ Support ID-only menu navigation
✅ Handle fork menus (main menu with multiple paths)
✅ Support CMS-style menus (dynamic repository wrappers)
✅ Compatible with factory pattern for menu creation
✅ Support dynamically populated menus from shared variables

MENU-SPECIFIC ADAPTATIONS:

1. CONTEXT AS MENU ORCHESTRATOR
   The Context class acts as your central menu manager:
   
   class MenuContext:
       def __init__(self, initial_menu_state: MenuState):
           self.menu_factory = MenuFactory()
           self.history = []  # Navigation history for back button
           self.shared_state = {}  # Shared data across menus
           self.transition_to(initial_menu_state)
       
       def transition_to(self, state: MenuState):
           self.history.append(self._state) if self._state else None
           self._state = state
           self._state.context = self
       
       def go_back(self):
           if self.history:
               self._state = self.history.pop()

2. MENU STATES WITH NAVIGATION CONTROL
   Each menu becomes a concrete state with back-references:
   
   class MainMenuState(MenuState):
       def display(self):
           print("1. Settings")
           print("2. Employee Manager")
       
       def handle_input(self, choice):
           if choice == "1":
               self.context.transition_to(SettingsMenuState())
           elif choice == "2":
               self.context.transition_to(EmployeeManagerState())

3. FACTORY PATTERN INTEGRATION
   Your factory can create and configure menu states dynamically:
   
   class MenuFactory:
       @staticmethod
       def create_menu(menu_id: str, shared_data: dict):
           if menu_id == "MAIN":
               return MainMenuState(shared_data)
           elif menu_id == "SETTINGS":
               return SettingsMenuState(shared_data)
           # Factory dynamically builds menus from shared variables

4. ID-ONLY NAVIGATION
   Navigate using menu IDs through the factory:
   
   class MenuState(ABC):
       def navigate_to_id(self, menu_id: str):
           new_state = self.context.menu_factory.create_menu(menu_id)
           self.context.transition_to(new_state)

5. CMS/DYNAMIC REPOSITORY SUPPORT
   For employee manager or CMS-style menus:
   
   class EmployeeManagerState(MenuState):
       def __init__(self, employee_repository):
           self.repository = employee_repository
       
       def display(self):
           employees = self.repository.get_all()
           for idx, emp in enumerate(employees):
               print(f"{idx}. {emp.name}")

NAVIGATION FLOWS SUPPORTED:
- Linear flows: State A → State B → State C
- Intertwined flows: States can transition to any other state via context
- Fork menus: States can branch to multiple different states
- Back navigation: States maintain history through context

PATTERN STRENGTHS:
- Flexibility: States can transition to any other state
- Extensibility: Easy to add new menu states without modifying existing ones
- Maintainability: Each menu's behavior is encapsulated in its own class
- Testability: States can be tested independently
- Factory Integration: Natural fit with menu factory model

Decision Date: 2025-12-12
Source: behavioral/refactoring_State_main.py
===============================================================================
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class MenuContext:
    """
    The MenuContext acts as the central menu orchestrator. It maintains the current
    menu state, navigation history, and shared data across all menus.
    
    RESPONSIBILITIES:
    - Maintains current menu state and navigation history
    - Provides transition_to() for state changes
    - Supports go_back() functionality via history stack
    - Holds shared_state dictionary for data passing between menus
    - Delegates display and input handling to current menu state
    
    USAGE:
        menu_ctx = MenuContext(MainMenuState())
        menu_ctx.display_current_menu()  # Shows current menu
        menu_ctx.handle_user_input("1")  # Processes user choice
        menu_ctx.go_back()  # Returns to previous menu
    """

    _state = None
    """
    A reference to the current menu state.
    """

    def __init__(self, state: MenuState, menu_factory=None) -> None:
        self.history = []  # Navigation history for back functionality
        self.shared_state = {}  # Shared data across menus
        self.menu_factory = menu_factory  # Optional factory for ID-based navigation
        self.transition_to(state)

    def transition_to(self, state: MenuState):
        """
        Navigate to a new menu state. Automatically maintains history.
        """
        if self._state is not None:
            self.history.append(self._state)
        
        print(f"[Navigation] → {type(state).__name__}")
        self._state = state
        self._state.context = self

    def go_back(self):
        """
        Return to the previous menu state in history.
        """
        if self.history:
            self._state = self.history.pop()
            print(f"[Navigation] ← Back to {type(self._state).__name__}")
        else:
            print("[Navigation] No previous menu in history")

    def navigate_by_id(self, menu_id: str):
        """
        Navigate to a menu using its ID (requires menu_factory).
        """
        if self.menu_factory:
            new_state = self.menu_factory.create_menu(menu_id, self.shared_state)
            self.transition_to(new_state)
        else:
            raise RuntimeError("MenuFactory not configured for ID-based navigation")

    """
    The MenuContext delegates display and input handling to the current menu state.
    """

    def display_current_menu(self):
        """Display the current menu."""
        self._state.display()

    def handle_user_input(self, user_input: str):
        """Process user input through the current menu state."""
        self._state.handle_input(user_input)


class MenuState(ABC):
    """
    The base MenuState class represents a single menu screen. All concrete menu
    states must implement display() and handle_input() methods.
    
    RESPONSIBILITIES:
    - Display menu options and content
    - Handle user input and navigate to other menus
    - Access shared data via self.context.shared_state
    - Trigger state transitions via self.context.transition_to()
    
    NAVIGATION PATTERNS:
        # Direct state transition
        self.context.transition_to(SettingsMenuState())
        
        # ID-based navigation (requires factory)
        self.context.navigate_by_id("SETTINGS")
        
        # Back navigation
        self.context.go_back()
        
        # Pass data between menus
        self.context.shared_state['selected_item'] = item
    
    CONCRETE IMPLEMENTATION EXAMPLES:
        - MainMenuState: Entry point with navigation options
        - SettingsMenuState: Configuration options
        - EmployeeManagerState: CMS-style with dynamic data
        - DetailViewState: Show item details
        - EditFormState: Handle data input and validation
    """

    @property
    def context(self) -> MenuContext:
        return self._context

    @context.setter
    def context(self, context: MenuContext) -> None:
        self._context = context

    @abstractmethod
    def display(self) -> None:
        """Display the menu options and content."""
        pass

    @abstractmethod
    def handle_input(self, user_input: str) -> None:
        """Process user input and perform navigation or actions."""
        pass


"""
Concrete Menu States implement specific menu screens.

Key Menu Pattern:
1. Each State = One Menu Screen
2. display() = Show menu options and content
3. handle_input() = Process user choice and navigate
4. self.context.transition_to() = Navigate to another menu
5. self.context.shared_state = Pass data between menus
6. self.context.go_back() = Return to previous menu
"""


class MainMenuState(MenuState):
    """The main entry menu with navigation to sub-menus."""
    
    def display(self) -> None:
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. Settings")
        print("2. Employee Manager")
        print("3. Exit")
        print("b. Go Back")
        print("="*50)

    def handle_input(self, user_input: str) -> None:
        if user_input == "1":
            self.context.transition_to(SettingsMenuState())
        elif user_input == "2":
            # Pass shared data to next menu
            self.context.shared_state['from_menu'] = 'main'
            self.context.transition_to(EmployeeManagerState())
        elif user_input == "3":
            print("[System] Exiting application...")
        elif user_input.lower() == "b":
            self.context.go_back()
        else:
            print("[Error] Invalid choice. Please try again.")


class SettingsMenuState(MenuState):
    """Settings menu demonstrating back navigation and state transitions."""
    
    def display(self) -> None:
        print("\n" + "="*50)
        print("SETTINGS MENU")
        print("="*50)
        print("1. Display Settings")
        print("2. User Preferences")
        print("3. Return to Main Menu")
        print("b. Go Back")
        print("="*50)

    def handle_input(self, user_input: str) -> None:
        if user_input == "1":
            print("[Settings] Display settings configured.")
        elif user_input == "2":
            print("[Settings] User preferences saved.")
        elif user_input == "3":
            self.context.transition_to(MainMenuState())
        elif user_input.lower() == "b":
            self.context.go_back()
        else:
            print("[Error] Invalid choice. Please try again.")


class EmployeeManagerState(MenuState):
    """CMS-style menu demonstrating dynamic content and shared state."""
    
    def __init__(self, employee_repository=None):
        # Simulate a repository - in production, inject actual repository
        self.repository = employee_repository or self._get_mock_repository()
    
    def _get_mock_repository(self):
        """Mock repository for demonstration."""
        class MockRepository:
            def get_all(self):
                return [
                    type('Employee', (), {'name': 'Alice Johnson', 'id': 1}),
                    type('Employee', (), {'name': 'Bob Smith', 'id': 2}),
                    type('Employee', (), {'name': 'Carol Williams', 'id': 3}),
                ]
        return MockRepository()
    
    def display(self) -> None:
        print("\n" + "="*50)
        print("EMPLOYEE MANAGER")
        print("="*50)
        
        # Check shared state for context
        from_menu = self.context.shared_state.get('from_menu', 'unknown')
        print(f"[Info] Navigated from: {from_menu}")
        
        # Dynamically populate from repository
        employees = self.repository.get_all()
        for idx, emp in enumerate(employees, 1):
            print(f"{idx}. {emp.name} (ID: {emp.id})")
        
        print("m. Return to Main Menu")
        print("b. Go Back")
        print("="*50)

    def handle_input(self, user_input: str) -> None:
        if user_input.lower() == "m":
            self.context.transition_to(MainMenuState())
        elif user_input.lower() == "b":
            self.context.go_back()
        elif user_input.isdigit():
            employee_id = int(user_input)
            employees = self.repository.get_all()
            if 1 <= employee_id <= len(employees):
                selected = employees[employee_id - 1]
                print(f"[Action] Selected employee: {selected.name}")
                # Store selection in shared state
                self.context.shared_state['selected_employee'] = selected
            else:
                print("[Error] Invalid employee ID.")
        else:
            print("[Error] Invalid choice. Please try again.")


#if __name__ == "__main__":


"""
    MENU ORCHESTRATION DEMONSTRATION
    
    This example demonstrates the State Pattern adapted for menu systems:
    - MenuContext orchestrates navigation between menu states
    - Each MenuState represents a distinct menu screen
    - Navigation history enables back functionality
    - Shared state allows data passing between menus
    - Dynamic content from repositories (CMS-style)
 
    KEY FEATURES DEMONSTRATED:
    ✓ State transitions (Main → Settings → Main → Employee Manager)
    ✓ Back navigation using history stack
    ✓ Shared state for data passing between menus
    ✓ Dynamic content from mock repository
    ✓ Clean separation of menu logic into states
    ✓ Extensible architecture for adding new menus
    
    TO EXTEND:
    1. Add more MenuState subclasses for new menus
    2. Integrate MenuFactory for ID-based navigation
    3. Add real repositories for CMS functionality
    4. Implement validation and error handling
    5. Add menu state serialization for session management
    """
    