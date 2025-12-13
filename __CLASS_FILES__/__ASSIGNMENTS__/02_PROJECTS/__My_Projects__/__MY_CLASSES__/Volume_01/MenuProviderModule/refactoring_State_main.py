from __future__ import annotations
from abc import ABC, abstractmethod


class MenuContext:
    def __init__(self, state: MenuState) -> None:
        self._state = None
        self.transition_to(state)

    def transition_to(self, state: MenuState):
        self._state = state
        self._state.context = self

    def display(self):
        self._state.display()

    def handle_input(self, user_input: str):
        self._state.handle_input(user_input)


class MenuState(ABC):
    @property
    def context(self) -> MenuContext:
        return self._context

    @context.setter
    def context(self, context: MenuContext) -> None:
        self._context = context

    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def handle_input(self, user_input: str) -> None:
        pass


class MainMenu(MenuState):
    def display(self) -> None:
        print("=== MAIN MENU ===")
        print("1. Settings")

    def handle_input(self, user_input: str) -> None:
        if user_input == "1":
            self.context.transition_to(SettingsMenu())


class SettingsMenu(MenuState):
    def display(self) -> None:
        print("=== SETTINGS ===")

    def handle_input(self, user_input: str) -> None:
        if user_input == "2":
            self.context.transition_to(MainMenu())


if __name__ == "__main__":
    # 1. BOOTSTRAP
    context = MenuContext(MainMenu())
    
    # 2. DISPLAY
    context.display()
    
    # 3. USER INPUT
    context.handle_input("1")