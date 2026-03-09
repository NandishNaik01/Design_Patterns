from abc import ABC, abstractmethod


# 1. Target interface (what our app expects)
class NotificationService(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


# 2. Adaptee (third-party / legacy code we cannot change)
class SMSVendorAPI:

    def send_sms(self, phone_number: str, text: str):
        print(f"SMS sent to {phone_number}: {text}")


# 3. Adapter (bridges Target and Adaptee)
class SMSAdapter(NotificationService):

    def __init__(self, sms_vendor: SMSVendorAPI, phone_number: str):
        self.sms_vendor = sms_vendor
        self.phone_number = phone_number

    def send(self, message: str):
        # Translate expected interface → vendor interface
        self.sms_vendor.send_sms(self.phone_number, message)


# 4. Client code
def main():
    # Client depends only on NotificationService
    notification: NotificationService = SMSAdapter(
        SMSVendorAPI(),
        "9999999999"
    )

    notification.send("Your OTP is 1234")


if __name__ == "__main__":
    main()
