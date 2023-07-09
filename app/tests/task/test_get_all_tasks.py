from models import Task
from tests.base import TestBase


class TestGetAllTasks(TestBase):
    def test_get_existing_task(self, db):
        Task.bulk(
            db,
            [
                {
                    "title": "Test task 1",
                    "description": "Test description 1",
                    "user_id": 1,
                },
                {
                    "title": "Test task 2",
                    "description": "Test description 2",
                    "user_id": 1,
                },
                {
                    "title": "Test task 3",
                    "description": "Test description 3",
                    "user_id": 1,
                },
            ],
        )
        response = self.client.get("/tasks", headers=self.login())
        assert response.status_code == 200

        assert response.json()[0]["title"] == "Test task 1"
        assert response.json()[0]["description"] == "Test description 1"

        assert response.json()[1]["title"] == "Test task 2"
        assert response.json()[1]["description"] == "Test description 2"

        assert response.json()[2]["title"] == "Test task 3"
        assert response.json()[2]["description"] == "Test description 3"
