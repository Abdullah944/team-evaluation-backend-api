from django.db import models

# Create your models here.
# ? what are the filed to show in the semester:
class Semester(models.Model):
    name = models.CharField(max_length=255)
