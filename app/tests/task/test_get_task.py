from models import Task
from tests.base import TestBase


class TestGetTask(TestBase):
    def test_get_existing_task(self, db):
        task = Task.create(
            db, {"title": "Test task", "description": "Test description", "user_id": 1}
        )
        response = self.client.get(f"/tasks/{task.id}", headers=self.login())
        assert response.status_code == 200
        assert response.json()["title"] == "Test task"
        assert response.json()["description"] == "Test description"
