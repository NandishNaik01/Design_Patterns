# -------------------------
# Singleton: AppConfig
# -------------------------
class AppConfig:
    """
    This class represents application-wide configuration.
    Only ONE instance of this class will ever exist.
    """

    _instance = None
    _initialized = False

    def __new__(cls, env: str):
        # __new__ controls object creation
        if cls._instance is None:
            print("Creating AppConfig instance")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, env: str):
        # __init__ runs every time AppConfig() is called
        # So we guard initialization
        if not self._initialized:
            print("Initializing AppConfig")
            self.env = env
            self.service_urls = {
                "auth": "https://auth.service",
                "data": "https://data.service"
            }
            self._initialized = True


# -------------------------
# Classes Using AppConfig
# -------------------------
class Server:
    def start(self):
        config = AppConfig("prod")
        print(f"Server running in {config.env}")
        print("Server URLs:", config.service_urls)


class Worker:
    def run(self):
        config = AppConfig("dev")  # ignored
        print(f"Worker running in {config.env}")
        print("Worker URLs:", config.service_urls)


# -------------------------
# Application Entry Point
# -------------------------
if __name__ == "__main__":
    server = Server()
    server.start()

    print("-" * 40)

    worker = Worker()
    worker.run()

    print("-" * 40)

    # Proving it's the SAME object
    config_a = AppConfig("test")
    config_b = AppConfig("stage")

    print("Same object?", config_a is config_b)
