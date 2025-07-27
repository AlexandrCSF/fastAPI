from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    database_url: str

@dataclass
class JWTAuthConfig:
    access_token_lifetime: int
    refresh_token_lifetime: int

@dataclass
class Config:
    JWTAuthConfig: JWTAuthConfig
    DatabaseConfig: DatabaseConfig
    SECRET_KEY: str
    debug: bool


env = Env()
env.read_env()
config = Config(
    JWTAuthConfig=JWTAuthConfig(access_token_lifetime=3600,refresh_token_lifetime=36000),
    DatabaseConfig=DatabaseConfig(database_url=env("DATABASE_URL")),
    SECRET_KEY=env("SECRET_KEY"),
    debug=env.bool("DEBUG", default=False),
)
