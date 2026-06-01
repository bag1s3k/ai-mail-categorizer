from dotenv import dotenv_values
from tomllib import load

from .help import EnvConfig, AppConfig


env_config = EnvConfig(**dotenv_values(".env"))

with open("config.toml", "rb") as f:
    app_config = AppConfig(**load(f))
