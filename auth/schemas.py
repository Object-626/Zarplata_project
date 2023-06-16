
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    email: str
    password: str


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
