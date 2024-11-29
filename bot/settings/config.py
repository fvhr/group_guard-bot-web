from dataclasses import dataclass, field

from environs import Env

env = Env()
env.read_env()


@dataclass
class Settings:
    BOT_TOKEN: str = field(default_factory=lambda: env('BOT_TOKEN'))
    ADMIN_TG_UUID: int = field(default_factory=lambda: env('ADMIN_TG_UUID'))
