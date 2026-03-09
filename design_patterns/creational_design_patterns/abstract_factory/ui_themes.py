from abc import ABC, abstractmethod


# ==================================================
# 1. ABSTRACT PRODUCTS (Interfaces)
# ==================================================

class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class TextBox(ABC):
    @abstractmethod
    def render(self):
        pass


# ==================================================
# 2. CONCRETE PRODUCTS (Light Theme)
# ==================================================

class LightButton(Button):
    def render(self):
        print("Rendering LIGHT button")


class LightTextBox(TextBox):
    def render(self):
        print("Rendering LIGHT textbox")


# ==================================================
# 3. CONCRETE PRODUCTS (Dark Theme)
# ==================================================

class DarkButton(Button):
    def render(self):
        print("Rendering DARK button")


class DarkTextBox(TextBox):
    def render(self):
        print("Rendering DARK textbox")


# ==================================================
# 4. ABSTRACT FACTORY
# ==================================================

class UIFactory(ABC):
    """
    Abstract Factory defines methods for creating
    a family of related objects.
    """

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass


# ==================================================
# 5. CONCRETE FACTORIES (Families)
# ==================================================

class LightThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_textbox(self) -> TextBox:
        return LightTextBox()


class DarkThemeFactory(UIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_textbox(self) -> TextBox:
        return DarkTextBox()


# ==================================================
# 6. CLIENT CODE (Theme-agnostic)
# ==================================================

class ApplicationUI:
    """
    Client code depends only on the abstract factory
    and abstract products.
    """

    def __init__(self, factory: UIFactory):
        self.factory = factory

    def render(self):
        button = self.factory.create_button()
        textbox = self.factory.create_textbox()

        button.render()
        textbox.render()


# ==================================================
# 7. APPLICATION ENTRY POINT
# ==================================================

if __name__ == "__main__":

    print("---- Using LIGHT theme ----")
    light_factory = LightThemeFactory()
    light_ui = ApplicationUI(light_factory)
    light_ui.render()

    print("\n---- Using DARK theme ----")
    dark_factory = DarkThemeFactory()
    dark_ui = ApplicationUI(dark_factory)
    dark_ui.render()
