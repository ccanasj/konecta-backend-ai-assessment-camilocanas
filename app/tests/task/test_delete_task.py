from models import Task
from tests.base import TestBase


class TestDeleteTask(TestBase):
    def test_delete_existing_task(self, db):
        task = Task.create(
            db, {"title": "Test task", "description": "Test description", "user_id": 1}
        )
        response = self.client.delete(f"/tasks/{task.id}", headers=self.login())

        assert response.status_code == 202
        assert response.json()["detail"] == "Task deleted"
