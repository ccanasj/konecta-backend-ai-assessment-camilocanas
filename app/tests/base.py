from fastapi.testclient import TestClient
from main import app


class TestBase:
    client = TestClient(app)

    def login(self) -> dict[str, str]:
        response = self.client.post(
            "/login", json={"username": "User tester", "password": "123456789"}
        )

        headers = {"Authorization": f"Bearer {response.json()['access_token']}"}
        return headers
