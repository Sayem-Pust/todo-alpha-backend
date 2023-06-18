from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    dir = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title

