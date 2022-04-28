from tkinter import CASCADE
from django.db import models
from project.modelsProject import Project


# ? What is the schema of the  model:

# ? Class = blueprint to make obj from it & use it else were:
class Team(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="team"
    )  # ?ForeignKey =  one to many relation / CASCADE =the row will be deleted too if the ForeignKey gets deleted / related_name =specifies the name of the reverse relation from the User model back to your model.
