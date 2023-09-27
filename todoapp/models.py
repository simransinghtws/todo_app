from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Todo(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField(max_length=100)
    date=models.DateTimeField()
    def __str__(self):
        return self.title
    
class TodoList(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    # todo=models.ForeignKey(Todo,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.user.username
    
  
