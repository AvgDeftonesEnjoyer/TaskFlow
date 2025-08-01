from django.db import models

 
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', "To Do"),
        ('in_progress', "In Progress"),
        ('done', "Done"),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.title

    
# Create your models here.
