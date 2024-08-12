from jwt import decode

from fast_curso.segurity import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data_claims = {"sub": "test@test.com"}
    result = create_access_token(data_claims)

    decoded = decode(result, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded["sub"] == data_claims["sub"]
    assert decoded["exp"]
