from abc import ABC, abstractmethod
import time


# 1. Common Interface (what your system talks to)
class ThirdPartyUserService(ABC):

    @abstractmethod
    def fetch_users(self) -> list[str]:
        pass


# 2. Real Subjects (actual third-party APIs)

class OktaAPI:
    def fetch_okta_users(self) -> list[str]:
        print("Calling Okta REST API...")
        time.sleep(1)
        return ["okta_user_1", "okta_user_2"]


class WorkdayAPI:
    def get_workers(self) -> list[str]:
        print("Calling Workday REST API...")
        time.sleep(1)
        return ["workday_user_a", "workday_user_b"]


# 3. Proxies (adapt + control access)

class OktaProxy(ThirdPartyUserService):

    def __init__(self):
        self._okta_api: OktaAPI | None = None

    def fetch_users(self) -> list[str]:
        if self._okta_api is None:
            print("Initializing Okta API client...")
            self._okta_api = OktaAPI()

        print("Fetching users via OktaProxy")
        return self._okta_api.fetch_okta_users()


class WorkdayProxy(ThirdPartyUserService):

    def __init__(self):
        self._workday_api: WorkdayAPI | None = None

    def fetch_users(self) -> list[str]:
        print("Initializing Workday API client...")
        api = WorkdayAPI()
        print("Fetching users via WorkdayProxy")
        return api.get_workers()


# 4. Facade-like wrapper (optional but nice)
class ThirdParty:
    def __init__(self):
        self.okta = OktaProxy()
        self.workday = WorkdayProxy()


# 5. Client
def main():
    thirdparty = ThirdParty()

    print("\n--- OKTA USERS ---")
    users = thirdparty.okta.fetch_users()
    print(users)

    print("\n--- WORKDAY USERS ---")
    users = thirdparty.workday.fetch_users()
    print(users)


if __name__ == "__main__":
    main()
