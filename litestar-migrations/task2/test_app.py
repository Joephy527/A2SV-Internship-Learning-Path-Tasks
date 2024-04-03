from litestar.status_codes import HTTP_200_OK
from litestar.testing import TestClient
from app import app

client = TestClient(app)


def test_read_litestar_hello_world() -> None:
    with client:
        response = client.get("/")

        assert response.status_code == HTTP_200_OK
        assert response.text == "Hello, World!"
