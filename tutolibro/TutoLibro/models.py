from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
# Create your models here.
