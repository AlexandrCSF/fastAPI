from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    database_url: str


@dataclass
class Config:
    DatabaseConfig: DatabaseConfig
    secret_key: str
    debug: bool


env = Env()
env.read_env()
config = Config(
    DatabaseConfig=DatabaseConfig(database_url=env("DATABASE_URL")),
    secret_key=env("SECRET_KEY"),
    debug=env.bool("DEBUG", default=False),
)
