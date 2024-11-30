from typing import Optional

from pydantic import BaseModel


class GroupInfo(BaseModel):
    id: int
    title: str
    description: Optional[str] = 'Нет описания'
    avatar_url: str
    bot_is_admin: bool = False
