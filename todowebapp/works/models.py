from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title= models.CharField(max_length=100)
    created_date= models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

class Todo(models.Model):
    title= models.CharField(max_length=100,null=True)
    description= models.TextField()
    status= models.BooleanField(default=False)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    project= models.ForeignKey(Project, related_name="todos", on_delete=models.CASCADE)
