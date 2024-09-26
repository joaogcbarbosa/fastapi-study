from .fixtures import test_client, db_session, test_user


def test_login_for_access_token(test_client, test_user):
  response = test_client.post("/auth/token", data=test_user)
  assert response.status_code == 200
  token = response.json()["access_token"]
  assert token is not None
  return token


def test_get_all(test_client):
    response = test_client.get("/todo/todos")
    print(response)
    assert response.status_code == 200
