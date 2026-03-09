from abc import ABC, abstractmethod


# Bridge separates what you do (abstraction) from how you do it (implementation), so both can change independently.

# ------------------------------
# IMPLEMENTATION HIERARCHY
# (HOW the message is sent)
# ------------------------------
class MessageSender(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class EmailSender(MessageSender):

    def send(self, message: str):
        print(f"[EMAIL] {message}")


class SMSSender(MessageSender):

    def send(self, message: str):
        print(f"[SMS] {message}")


# ------------------------------
# ABSTRACTION HIERARCHY
# (WHAT type of message it is)
# ------------------------------
class Notification(ABC):

    def __init__(self, sender: MessageSender):
        self.sender = sender  # <-- THE BRIDGE

    @abstractmethod
    def notify(self, message: str):
        pass


class Alert(Notification):

    def notify(self, message: str):
        self.sender.send(f"ALERT: {message}")


class Reminder(Notification):

    def notify(self, message: str):
        self.sender.send(f"REMINDER: {message}")


# ------------------------------
# CLIENT
# ------------------------------
def main():
    email_sender = EmailSender()
    sms_sender = SMSSender()

    alert_email = Alert(email_sender)
    alert_sms = Alert(sms_sender)

    reminder_email = Reminder(email_sender)
    reminder_sms = Reminder(sms_sender)

    alert_email.notify("Server is down")
    alert_sms.notify("High CPU usage")

    reminder_email.notify("Meeting at 10 AM")
    reminder_sms.notify("Submit timesheet")


if __name__ == "__main__":
    main()
