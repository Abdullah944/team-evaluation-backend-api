from django.db import models


# ? What is the schema of the  model:

# ? Class = blueprint to make obj from it & use it else were:
class Criteria(models.Model):
    name = models.CharField(max_length=255)  # ? character
    weight = models.IntegerField()  # ? int
