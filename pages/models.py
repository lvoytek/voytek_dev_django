from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    overview = models.CharField(max_length=4000)
    image = models.ImageField()
    tags = models.JSONField()
