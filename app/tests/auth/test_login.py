from tests.base import TestBase
from models import User


class TestLoginUser(TestBase):
    def test_valid_username_and_password(self, db):
        User.create(db, {"username": "test_user", "password": "test_password"})

        response = self.client.post(
            "/login", json={"username": "test_user", "password": "test_password"}
        )

        assert response.status_code == 200
        assert "access_token" in response.json()
