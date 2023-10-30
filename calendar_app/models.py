from django.db import models

# Create your models here.

CHOICE = (('primary','完了'),('warning','着手'),('danger','未着手'),('dark','期限切れ'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
        )
    duedate = models.DateField()
    
    
    def __str__(self):
        return self.title