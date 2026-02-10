from abc import ABC, abstractmethod


# -----------------------------
# Observer Interface
# -----------------------------
class Observer(ABC):

    @abstractmethod
    def update(self, order_id: int, status: str) -> None:
        pass


# -----------------------------
# Subject
# -----------------------------
class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.status = "CREATED"
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def _notify(self) -> None:
        for observer in self._observers:
            observer.update(self.order_id, self.status)

    def update_status(self, status: str) -> None:
        self.status = status
        self._notify()


# -----------------------------
# Concrete Observers
# -----------------------------
class EmailNotification(Observer):
    def update(self, order_id: int, status: str) -> None:
        print(f"📧 Email: Order {order_id} is now {status}")


class SmsNotification(Observer):
    def update(self, order_id: int, status: str) -> None:
        print(f"📱 SMS: Order {order_id} is now {status}")


class AuditLogger(Observer):
    def update(self, order_id: int, status: str) -> None:
        print(f"📝 Audit Log: Order {order_id} changed to {status}")


# -----------------------------
# Client Code
# -----------------------------
def main():
    order = Order(order_id=101)

    email = EmailNotification()
    sms = SmsNotification()
    audit = AuditLogger()

    # Subscribe observers
    order.attach(email)
    order.attach(sms)
    order.attach(audit)

    print("\n--- Order Placed ---")
    order.update_status("PLACED")

    print("\n--- Order Shipped ---")
    order.update_status("SHIPPED")

    print("\n--- Remove SMS notifications ---")
    order.detach(sms)

    print("\n--- Order Delivered ---")
    order.update_status("DELIVERED")


if __name__ == "__main__":
    main()
