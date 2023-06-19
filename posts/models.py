from django.db import models
import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    dir = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Directory(models.Model):
    dir = models.CharField(max_length=255)

    def __str__(self):
        return self.dir
