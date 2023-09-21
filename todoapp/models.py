from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Todo(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField(max_length=100)
    date=models.DateTimeField()
    def __str__(self):
        return self.title
    
  
