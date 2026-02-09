# Facade Pattern – Single Runnable Example


# ------------------------------
# Subsystems (complex internals)
# ------------------------------
class AuthService:
    def authenticate(self):
        print("Authenticating request")


class UserService:
    def create_user(self, name: str):
        print(f"Creating user: {name}")
        return {"id": 1, "name": name}


class PermissionService:
    def assign_default_permissions(self, user_id: int):
        print(f"Assigning permissions to user {user_id}")


class AuditService:
    def log(self, message: str):
        print(f"Audit log: {message}")


class NotificationService:
    def send_welcome_email(self, user_name: str):
        print(f"Sending welcome email to {user_name}")


# ------------------------------
# Facade
# ------------------------------
class UserOnboardingFacade:

    def __init__(self):
        self.auth = AuthService()
        self.user_service = UserService()
        self.permission_service = PermissionService()
        self.audit = AuditService()
        self.notification = NotificationService()

    def onboard_user(self, name: str):
        self.auth.authenticate()

        user = self.user_service.create_user(name)

        self.permission_service.assign_default_permissions(user["id"])

        self.audit.log(f"User {user['id']} created")

        self.notification.send_welcome_email(user["name"])


# ------------------------------
# Client
# ------------------------------
def main():
    onboarding = UserOnboardingFacade()

    onboarding.onboard_user("Alice")


if __name__ == "__main__":
    main()
