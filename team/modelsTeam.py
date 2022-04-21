from tkinter import CASCADE
from django.db import models
from project.modelsProject import Project

# Create your models here.
# ? what are the filed to show in the semester:
class Team(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="team")
