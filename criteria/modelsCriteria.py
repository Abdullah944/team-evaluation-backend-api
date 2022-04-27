from django.db import models


# ? what are the filed to show in the Criteria:
class Criteria(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
