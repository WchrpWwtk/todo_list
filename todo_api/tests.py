from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task


class TaskAPITestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.task_data = {"title": "Task 1", "description": "Description for Task 1"}
        self.task = Task.objects.create(**self.task_data)
        self.task_url = f"/api/tasks/{self.task.id}/"

    def test_create_task(self):
        url = reverse("task-list-create")
        response = self.client.post(url, self.task_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_read_tasks(self):
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Task 1")
        self.assertEqual(response.data["description"], "Description for Task 1")

    def test_update_task(self):
        updated_data = {
            "title": "Updated Task",
            "description": "Updated Description",
            "completed": True,
        }
        response = self.client.put(self.task_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")
        self.assertEqual(self.task.description, "Updated Description")
        self.assertEqual(self.task.completed, True)

    def test_delete_task(self):
        response = self.client.delete(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_list_tasks(self):
        url = reverse("task-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_task_invalid_data_without_title(self):
        url = reverse("task-list-create")
        invalid_data = {"description": "Invalid Task Data"}
        response = self.client.post(url, invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 1)

    def test_update_task_not_found(self):
        url = reverse("task-detail", args=[999])
        response = self.client.put(url, self.task_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task_not_found(self):
        url = reverse("task-detail", args=[999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
