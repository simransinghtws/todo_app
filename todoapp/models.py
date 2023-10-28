from django.db import models
import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()
class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=100)
    date=models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.title
  
    def get_absolute_url(self):
        return reverse("home")
    
