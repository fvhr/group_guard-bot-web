from dataclasses import dataclass, field

from environs import Env

env = Env()
env.read_env()


@dataclass
class Settings:
    BOT_TOKEN: str = field(default_factory=lambda: env('BOT_TOKEN'))
    ADMIN_TG_UUID: int = field(default_factory=lambda: env('ADMIN_TG_UUID'))
    BASE_AVATAR_PATH: str = field(
        default_factory=lambda: env('BASE_AVATAR_PATH'),
    )
    BASE_API_TG_URL: str = field(
        default_factory=lambda: env('BASE_API_TG_URL'),
    )
    BASE_API_BACKEND_URL: str = field(
        default_factory=lambda: env('BASE_API_BACKEND_URL'),
    )
