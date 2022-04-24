from tkinter import CASCADE
from django.db import models
from criteria.modelsCriteria import Criteria
from semester.modelsSemester import Semester

# ? what are the filed to show in the project:
class Project(models.Model):
    name = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, related_name="project"
    )
    criteria = models.ManyToManyField(Criteria, related_name="criteria")
