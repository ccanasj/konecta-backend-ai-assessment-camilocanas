from models import Task
from tests.base import TestBase


class TestUpdateTask(TestBase):
    def test_update_existing_task(self, db):
        task = Task.create(
            db, {"title": "Test task", "description": "Test description", "user_id": 1}
        )
        response = self.client.put(
            f"/tasks/{task.id}",
            headers=self.login(),
            json={"title": "Updated task", "description": "Updated description"},
        )

        assert response.status_code == 202
        assert response.json()["title"] == "Updated task"
        assert response.json()["description"] == "Updated description"
