from pydantic import BaseModel, ConfigDict, EmailStr

# Contrato do que será recebido e enviado em todos os casos


class Message(BaseModel):
    message: str


class Token(BaseModel):
    access_token: str
    token_type: str  # Como ela vai usar este token?


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]
