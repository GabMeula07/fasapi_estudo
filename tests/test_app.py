from http import HTTPStatus

from fast_curso.schemas import UserPublic

# toda vez que uma função de teste recever


""" 
def test_read_root_deve_retornar_ok():
    client = TestClient(app)  # arrange (organização)
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert json.loads(response.text)["message"] == "olá, mundo!"
 """


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "testeUserName",
            "email": "test@test.com",
            "password": "password",
        },
    )
    # Valida o userPublic
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "testeUserName",
        "email": "test@test.com",
        "id": 1,
    }


def test_create_user_err_exist_username(client, user):
    response = client.post(
        "/users/",
        json={
            "username": "gabriel",
            "email": "gabrielqieismeula@test.com",
            "password": "fldkf;asjklsajfl;asdf",
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Username already exits"}


def test_create_user_err_exist_email(client, user):
    response = client.post(
        "/users/",
        json={
            "username": "gdsadads",
            "email": "gabriel@gabi.com",
            "password": "fldkf;asjklsajfl;asdf",
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Email already exits"}


def test_read_user(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": []}


def test_read_user_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": [user_schema]}


def test_get_one_user(client, user):
    response = client.get("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "gabriel",
        "id": 1,
        "email": "gabriel@gabi.com",
    }


def test_update_user(client, user):
    response = client.put(
        "/users/1",
        json={
            "username": "BoB",
            "email": "test@test.com",
            "password": "password",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "BoB",
        "email": "test@test.com",
        "id": 1,
    }


def test_delete_user(client, user):
    response = client.delete("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}


def test_update_return_user_not_found(client):
    response = client.put(
        "/users/99",
        json={
            "username": "BoB",
            "email": "test@test.com",
            "password": "password",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_return_user_not_found(client, user):
    response = client.delete("/users/9999999")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_get_return_user_not_found(client, user):
    response = client.get("/users/0")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
