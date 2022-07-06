from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    overview = models.CharField(max_length=4000)
    image = models.ImageField(upload_to="project-images")
    tags = models.JSONField()
    priority = models.IntegerField(default=200)

    def __str__(self):
        return self.title

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        elif self.priority == other.priority:
            return self.title < other.title

        return False


class SkillCategory(models.Model):
    title = models.CharField(max_length=120)
    priority = models.IntegerField(default=200)

    def __str__(self):
        return self.title

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        elif self.priority == other.priority:
            return self.title < other.title

        return False


class Skill(models.Model):
    title = models.CharField(max_length=120)
    tag = models.CharField(max_length=120)
    category = models.ForeignKey('SkillCategory', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="skill-images")

    def __str__(self):
        return self.title

    def __lt__(self, other):
        return self.title < other.title
