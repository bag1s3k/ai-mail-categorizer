from pydantic import BaseModel


class EnvConfig(BaseModel):
    """Validate env config"""

    IMAP_SERVER: str
    USER_EMAIL: str
    EMAIL_PASS: str
    PORT: int = 993


class AppConfig(BaseModel):
    """Validate app config file"""
    ...
