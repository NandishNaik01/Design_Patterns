from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


# 1. Enum for channels
class Channel(Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"


# 2. DTOs (Data Transfer Objects)

@dataclass
class SMSContextDTO:
    phone: str


@dataclass
class EmailContextDTO:
    email: str
    subject: str = "No Subject"


# 3. Target Interface
class NotificationService(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


# 4. Adaptees (incompatible vendor APIs)

class SMSVendorAPI:
    def send_sms(self, phone: str, text: str):
        print(f"[SMS] Sent to {phone}: {text}")


class EmailVendorAPI:
    def send_email(self, email: str, subject: str, body: str):
        print(f"[EMAIL] To {email} | Subject: {subject} | Body: {body}")


# 5. Adapters (consume DTOs)

class SMSAdapter(NotificationService):

    def __init__(self, context: SMSContextDTO):
        self.vendor = SMSVendorAPI()
        self.context = context

    def send(self, message: str):
        self.vendor.send_sms(
            self.context.phone,
            message
        )


class EmailAdapter(NotificationService):

    def __init__(self, context: EmailContextDTO):
        self.vendor = EmailVendorAPI()
        self.context = context

    def send(self, message: str):
        self.vendor.send_email(
            self.context.email,
            self.context.subject,
            message
        )


# 6. Factory
class NotificationFactory:

    @staticmethod
    def create(channel: Channel, context) -> NotificationService:

        if channel == Channel.SMS and isinstance(context, SMSContextDTO):
            return SMSAdapter(context)

        if channel == Channel.EMAIL and isinstance(context, EmailContextDTO):
            return EmailAdapter(context)

        raise ValueError("Invalid channel or context DTO")


# 7. Client
def main():
    sms_context = SMSContextDTO(phone="9999999999")
    sms = NotificationFactory.create(Channel.SMS, sms_context)
    sms.send("Your OTP is 1234")

    print("-" * 40)

    email_context = EmailContextDTO(
        email="user@example.com",
        subject="Welcome"
    )
    email = NotificationFactory.create(Channel.EMAIL, email_context)
    email.send("Thanks for signing up!")


if __name__ == "__main__":
    main()
