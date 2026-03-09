from abc import ABC, abstractmethod
from enum import Enum


# -------------------------
# 1. Enum: Channel Types
# -------------------------
class ChannelType(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"


# -------------------------
# 2. Sender Interface
# -------------------------
class NotificationSender(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


# -------------------------
# 3. Concrete Senders
# -------------------------
class EmailSender(NotificationSender):
    def send(self, message: str):
        print(f"[EMAIL] {message}")


class SMSSender(NotificationSender):
    def send(self, message: str):
        print(f"[SMS] {message}")


class PushSender(NotificationSender):
    def send(self, message: str):
        print(f"[PUSH] {message}")


# -------------------------
# 4. Factory Interface
# -------------------------
class NotificationFactory(ABC):

    @abstractmethod
    def create_sender(self, channel: ChannelType) -> NotificationSender:
        pass


# -------------------------
# 5. Factory Implementation
# -------------------------
class DefaultNotificationFactory(NotificationFactory):

    def create_sender(self, channel: ChannelType) -> NotificationSender:
        if channel == ChannelType.EMAIL:
            return EmailSender()
        elif channel == ChannelType.SMS:
            return SMSSender()
        elif channel == ChannelType.PUSH:
            return PushSender()
        else:
            raise ValueError("Unsupported channel type")


# -------------------------
# 6. First Class Using Factory
# -------------------------
class NotificationService:

    def __init__(self, factory: NotificationFactory):
        self.factory = factory

    def notify(self, channel: ChannelType, message: str):
        sender = self.factory.create_sender(channel)
        sender.send(message)


# -------------------------
# 7. Second Class Using Factory
# -------------------------
class AlertService:

    def __init__(self, factory: NotificationFactory):
        self.factory = factory

    def alert(self, channel: ChannelType, message: str):
        sender = self.factory.create_sender(channel)
        sender.send(f"[ALERT] {message}")


# -------------------------
# 8. Application Entry Point
# -------------------------
if __name__ == "__main__":
    factory = DefaultNotificationFactory()

    notification_service = NotificationService(factory)
    alert_service = AlertService(factory)

    notification_service.notify(ChannelType.EMAIL, "Welcome to the platform")
    notification_service.notify(ChannelType.PUSH, "You have a new message")

    alert_service.alert(ChannelType.SMS, "Server CPU usage high")
