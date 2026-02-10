from abc import ABC, abstractmethod

# Strategy Pattern lets you define a family of algorithms, put each one in a separate class, and make them interchangeable at runtime.

# -----------------------------
# Strategy Interface
# -----------------------------
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# -----------------------------
# Concrete Strategies
# -----------------------------
class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"💳 Paid ₹{amount} using Card")


class UpiPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"📱 Paid ₹{amount} using UPI")


class WalletPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"👛 Paid ₹{amount} using Wallet")


# -----------------------------
# Context
# -----------------------------
class Checkout:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """Change strategy at runtime"""
        self._strategy = strategy

    def complete_payment(self, amount: float) -> None:
        self._strategy.pay(amount)


# -----------------------------
# Client Code (Runnable Demo)
# -----------------------------
def main():
    amount = 500

    # Pay using UPI
    checkout = Checkout(UpiPayment())
    checkout.complete_payment(amount)

    # Switch strategy at runtime
    checkout.set_strategy(CardPayment())
    checkout.complete_payment(amount)

    # Switch again
    checkout.set_strategy(WalletPayment())
    checkout.complete_payment(amount)


if __name__ == "__main__":
    main()
