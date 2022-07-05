from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    overview = models.CharField(max_length=4000)
    image = models.ImageField(upload_to="project-images")
    tags = models.JSONField()

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=120)
    tag = models.CharField(max_length=120)
    category = SkillCategory()
    image = models.ImageField(upload_to="skill-images")

    def __str__(self):
        return self.title
