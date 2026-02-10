from abc import ABC, abstractmethod


# -----------------------------
# Handler Interface
# -----------------------------
class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request: dict) -> None:
        pass


# -----------------------------
# Concrete Handlers
# -----------------------------
class AuthenticationHandler(Handler):
    def handle(self, request: dict) -> None:
        if not request.get("authenticated"):
            print("❌ Authentication failed")
            return

        print("✅ Authentication passed")
        if self.next_handler:
            self.next_handler.handle(request)


class AuthorizationHandler(Handler):
    def handle(self, request: dict) -> None:
        if not request.get("is_admin"):
            print("❌ Authorization failed")
            return

        print("✅ Authorization passed")
        if self.next_handler:
            self.next_handler.handle(request)


class ValidationHandler(Handler):
    def handle(self, request: dict) -> None:
        if not request.get("data"):
            print("❌ Validation failed")
            return

        print("✅ Validation passed")
        if self.next_handler:
            self.next_handler.handle(request)


class BusinessLogicHandler(Handler):
    def handle(self, request: dict) -> None:
        print("🎯 Business logic executed successfully")


# -----------------------------
# Client Code
# -----------------------------
def main():
    # Build the chain
    chain = AuthenticationHandler(
        AuthorizationHandler(
            ValidationHandler(
                BusinessLogicHandler()
            )
        )
    )

    print("\n--- Request 1: All good ---")
    request1 = {
        "authenticated": True,
        "is_admin": True,
        "data": "important payload"
    }
    chain.handle(request1)

    print("\n--- Request 2: Auth fails ---")
    request2 = {
        "authenticated": False,
        "is_admin": True,
        "data": "important payload"
    }
    chain.handle(request2)


if __name__ == "__main__":
    main()
