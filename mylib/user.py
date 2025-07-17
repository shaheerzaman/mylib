from __future__ import annotations
from typing import ClassVar
from pydantic import EmailStr

from mylib.base import BaseAPIModel


class User(BaseAPIModel[User]):
    name: str
    email: EmailStr

    _resource_path: ClassVar[str] = "users"
