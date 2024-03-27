from pydantic import BaseModel


class PublicUser(BaseModel):
    name: str


class SignInUser(PublicUser):
    password: str


class PrivateUser(PublicUser):
    hash: str
