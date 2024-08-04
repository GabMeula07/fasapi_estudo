from http import HTTPStatus

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


def test_read_user(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "testeUserName",
                "email": "test@test.com",
                "id": 1,
            }
        ]
    }


def test_get_one_user(client):
    response = client.get("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "testeUserName",
        "email": "test@test.com",
        "id": 1,
    }


def test_update_user(client):
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


def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Usuário deletado com sucesso!"}


def test_update_return_user_not_found(client):
    response = client.put("/users/99")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body"],
                "msg": "Field required",
                "input": None,
            }
        ]
    }


def test_delete_return_user_not_found(client):
    response = client.delete("/users/0")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_get_return_user_not_found(client):
    response = client.get("/users/0")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
