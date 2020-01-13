from django.db import models

#Main Model
class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self):
        return self.title


