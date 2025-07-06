from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskFrontendTestCase(TestCase):
    def SetUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            status='todo',
            priority=1
        )   
    
    def test_task_list_view(self):
        url = reverse('task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        
    def test_task_create_view(self):
        url = reverse('task_create')
        data = {
            'title':'New Task',
            'description':'New Task Description',
            'status':'todo',
            'priority': 2
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())
        
    def test_task_update_view(self):
        url = reverse('task_update', args=[self.task.id])
        data = {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'status': 'done',
            'priority': 3
        }
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title,'Updated Task')
        
    def test_task_delete_view(self):
        url = reverse('task_delete', args=[self.task.id])
        
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
        
        
        