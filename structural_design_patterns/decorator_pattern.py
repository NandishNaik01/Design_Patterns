from abc import ABC, abstractmethod


# Decorator pattern allows behavior to be added to objects dynamically by wrapping them in decorator classes that implement the same interface

# ------------------------------
# COMPONENT
# ------------------------------
class Notification(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


# ------------------------------
# CONCRETE COMPONENT
# ------------------------------
class BasicNotification(Notification):

    def send(self, message: str):
        print(f"Sending notification: {message}")


# ------------------------------
# DECORATOR (base)
# ------------------------------
class NotificationDecorator(Notification):

    def __init__(self, notification: Notification):
        self._notification = notification

    def send(self, message: str):
        self._notification.send(message)


# ------------------------------
# CONCRETE DECORATORS
# ------------------------------
class LoggingDecorator(NotificationDecorator):

    def send(self, message: str):
        print("[LOG] Notification sending started")
        super().send(message)
        print("[LOG] Notification sending completed")


class EncryptionDecorator(NotificationDecorator):

    def send(self, message: str):
        encrypted = f"ENCRYPTED({message})"
        super().send(encrypted)


class RetryDecorator(NotificationDecorator):

    def send(self, message: str):
        print("[RETRY] Attempt 1")
        super().send(message)


# ------------------------------
# CLIENT
# ------------------------------
def main():
    notification = BasicNotification()

    # Add features dynamically
    notification = LoggingDecorator(notification)
    notification = EncryptionDecorator(notification)
    notification = RetryDecorator(notification)

    notification.send("Your OTP is 1234")


if __name__ == "__main__":
    main()
