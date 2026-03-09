# ==================================================
# 1. PRODUCT: ServerConfig
# ==================================================

class ServerConfig:
    def __init__(self):
        self.host = None
        self.port = None
        self.protocol = None
        self.timeout = None
        self.retries = None
        self.ssl_enabled = None

    def __str__(self):
        return (
            f"ServerConfig(host={self.host}, port={self.port}, "
            f"protocol={self.protocol}, timeout={self.timeout}, "
            f"retries={self.retries}, ssl={self.ssl_enabled})"
        )


# ==================================================
# 2. BUILDER
# ==================================================

class ServerConfigBuilder:
    def __init__(self):
        self.config = ServerConfig()

    def set_host(self, host):
        self.config.host = host
        return self

    def set_port(self, port):
        self.config.port = port
        return self

    def set_protocol(self, protocol):
        self.config.protocol = protocol
        return self

    def set_timeout(self, timeout):
        self.config.timeout = timeout
        return self

    def set_retries(self, retries):
        self.config.retries = retries
        return self

    def enable_ssl(self):
        self.config.ssl_enabled = True
        return self

    def build(self):
        return self.config


# ==================================================
# 3. APPLICATION ENTRY POINT
# ==================================================

if __name__ == "__main__":

    # Build config step by step
    config = (
        ServerConfigBuilder()
        .set_host("localhost")
        .set_port(8080)
        .set_protocol("https")
        .set_timeout(30)
        .set_retries(3)
        .enable_ssl()
        .build()
    )

    print(config)
