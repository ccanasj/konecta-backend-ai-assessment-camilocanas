from tests.base import TestBase


class TestRegisterUser(TestBase):
    def test_register_new_user_successfully(self, db):
        test_user = {
            "username": "testuser",
            "password": "testpassword",
        }

        response = self.client.post("/register", json=test_user)
        assert response.status_code == 200
        assert "access_token" in response.json()

