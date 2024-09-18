from .fixtures.test_client import test_client


def test_get_all(test_client):
    response = test_client.get("/todo/todos")
    print(response)
    assert response.status_code == 200
