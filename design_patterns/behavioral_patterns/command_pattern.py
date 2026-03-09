from abc import ABC, abstractmethod


# -----------------------------
# Command Interface
# -----------------------------
class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


# -----------------------------
# Receiver
# -----------------------------
class Light:
    def turn_on(self) -> None:
        print("💡 Light turned ON")

    def turn_off(self) -> None:
        print("🌑 Light turned OFF")


# -----------------------------
# Concrete Commands
# -----------------------------
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()

    def undo(self) -> None:
        self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()

    def undo(self) -> None:
        self.light.turn_on()


# -----------------------------
# Invoker
# -----------------------------
class RemoteControl:
    def __init__(self):
        self._history: list[Command] = []

    def press_button(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def press_undo(self) -> None:
        if not self._history:
            print("⚠️ Nothing to undo")
            return
        last_command = self._history.pop()
        last_command.undo()


# -----------------------------
# Client Code
# -----------------------------
def main():
    light = Light()
    remote = RemoteControl()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    print("\n--- Turn ON ---")
    remote.press_button(light_on)

    print("\n--- Turn OFF ---")
    remote.press_button(light_off)

    print("\n--- Undo last action ---")
    remote.press_undo()

    print("\n--- Undo again ---")
    remote.press_undo()


if __name__ == "__main__":
    main()
