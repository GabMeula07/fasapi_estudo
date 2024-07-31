import json
from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_curso.app import app


def test_read_root_deve_retornar_ok():
    client = TestClient(app)  # arrange (organização)
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert json.loads(response.text)["message"] == "olá, mundo!"
