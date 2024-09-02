from fastapi.testclient import TestClient
from todo.main import app


test_client = TestClient(app=app, base_url="https://0.0.0.0:3000")


def test_get_all():
    response = test_client.get("/todo/todos")
    print(response)
    assert response.status_code == 200
