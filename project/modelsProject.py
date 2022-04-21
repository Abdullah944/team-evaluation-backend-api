from tkinter import CASCADE
from django.db import models
from semester.modelsSemester import Semester

# Create your models here.
# ? what are the filed to show in the semester:
class Project(models.Model):
    name = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, related_name="project"
    )
