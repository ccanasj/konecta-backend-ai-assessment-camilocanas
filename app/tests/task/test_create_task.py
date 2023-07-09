from tests.base import TestBase


class TestCreateTask(TestBase):
    def test_create_existing_task(self, db):
        response = self.client.post(
            "/tasks",
            headers=self.login(),
            json={"title": "Test task", "description": "Test description"},
        )

        assert response.status_code == 201
        assert response.json()["title"] == "Test task"
        assert response.json()["description"] == "Test description"
