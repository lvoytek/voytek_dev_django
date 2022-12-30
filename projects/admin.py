from django.contrib import admin
from .models import Project, SkillCategory, Skill

# Register your models here.
admin.site.register(Project)
admin.site.register(SkillCategory)
admin.site.register(Skill)
