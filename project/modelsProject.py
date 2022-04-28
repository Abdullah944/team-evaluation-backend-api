from tkinter import CASCADE
from django.db import models
from criteria.modelsCriteria import Criteria
from semester.modelsSemester import Semester


# ? What is the schema of the  model:

# ? Class = blueprint to make obj from it & use it else were:
class Project(models.Model):
    name = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name="project",  # ?ForeignKey =  one to many relation / CASCADE =the row will be deleted too if the ForeignKey gets deleted / related_name =specifies the name of the reverse relation from the User model back to your model.
    )
    criteria = models.ManyToManyField(
        Criteria, related_name="criteria"
    )  # ? MAny to many relations
