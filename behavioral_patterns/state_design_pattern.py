from abc import ABC, abstractmethod


# -----------------------------
# State Interface
# -----------------------------
class OrderState(ABC):

    @abstractmethod
    def next(self, order) -> None:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


# -----------------------------
# Concrete States
# -----------------------------
class CreatedState(OrderState):
    def next(self, order) -> None:
        print("💰 Payment completed")
        order.set_state(PaidState())

    def name(self) -> str:
        return "CREATED"


class PaidState(OrderState):
    def next(self, order) -> None:
        print("📦 Order shipped")
        order.set_state(ShippedState())

    def name(self) -> str:
        return "PAID"


class ShippedState(OrderState):
    def next(self, order) -> None:
        print("🚚 Order delivered")
        order.set_state(DeliveredState())

    def name(self) -> str:
        return "SHIPPED"


class DeliveredState(OrderState):
    def next(self, order) -> None:
        print("✅ Order already delivered. No further actions.")

    def name(self) -> str:
        return "DELIVERED"


# -----------------------------
# Context
# -----------------------------
class Order:
    def __init__(self):
        self._state: OrderState = CreatedState()

    def set_state(self, state: OrderState) -> None:
        self._state = state
        print(f"➡️ State changed to {self._state.name()}")

    def proceed(self) -> None:
        print(f"\nCurrent State: {self._state.name()}")
        self._state.next(self)


# -----------------------------
# Client Code
# -----------------------------
def main():
    order = Order()

    order.proceed()   # CREATED -> PAID
    order.proceed()   # PAID -> SHIPPED
    order.proceed()   # SHIPPED -> DELIVERED
    order.proceed()   # DELIVERED -> no-op


if __name__ == "__main__":
    main()
