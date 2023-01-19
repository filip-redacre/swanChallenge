class Config(object):
    """Default system config."""

    TESTING = False
    DEBUG = False
    DB_HOST = "localhost"
    DB_PORT = 5432
    DB_TABLE = "swan"
    DB_USER = "swan-user"
    DB_PASS = "Swan2023!"  # TODO Hash plaintext password using something like bcrypt

    @property
    def DATABASE_URI(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_TABLE}"


class DevelopmentConfig(Config):
    """Enable debug mode"""

    DEBUG = True


class ProductionConfig(Config):
    """Uses production database server."""

    DB_HOST = "1.2.3.4"


class TestConfig(Config):
    """Uses test database server."""

    TESTING = True
    DEBUG = True
    DB_HOST = "4.3.2.1"
