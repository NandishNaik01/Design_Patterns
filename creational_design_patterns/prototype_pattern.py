import copy
from abc import ABC, abstractmethod


# ==================================================
# 1. PROTOTYPE INTERFACE
# ==================================================

class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


# ==================================================
# 2. CONCRETE PROTOTYPE
# ==================================================

class UserProfile(Prototype):
    def __init__(self, role, permissions, preferences):
        self.role = role
        self.permissions = permissions
        self.preferences = preferences

    def clone(self):
        # Deep copy to avoid shared references
        return copy.deepcopy(self)

    def __str__(self):
        return (
            f"UserProfile(role={self.role}, "
            f"permissions={self.permissions}, "
            f"preferences={self.preferences})"
        )


# ==================================================
# 3. APPLICATION ENTRY POINT
# ==================================================

if __name__ == "__main__":

    # Create a prototype (heavy object)
    base_user = UserProfile(
        role="USER",
        permissions=["read", "comment"],
        preferences={"theme": "light", "lang": "en"}
    )

    # Clone for new users
    user_1 = base_user.clone()
    user_1.preferences["theme"] = "dark"

    user_2 = base_user.clone()
    user_2.permissions.append("upload")

    print("Base User:", base_user)
    print("User 1:", user_1)
    print("User 2:", user_2)
