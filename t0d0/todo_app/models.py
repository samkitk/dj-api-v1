from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=512)
    status = models.BooleanField()
    
    def __str__(self):
        return self.title