from datetime import datetime, timedelta

from _zoneinfo import ZoneInfo
from jwt import encode
from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 30


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data_claims: dict):
    to_encode = data_claims.copy()

    # adiciona 30 minutos baseado no horario atual
    expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE
    )

    to_encode.update({"exp": expire})

    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
