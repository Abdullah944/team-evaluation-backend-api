from turtle import ondrag
from django.db import models
from evaluation.modelsEvaluation import Evaluation


# ? What is the schema of the  model:

# ? Class = blueprint to make obj from it & use it else were:


class Judge(models.Model):
    name = models.CharField(max_length=255)
    evaluation = models.ForeignKey(
        Evaluation,
        on_delete=models.CASCADE,
        related_name="judge",  # ?ForeignKey =  one to many relation / CASCADE =the row will be deleted too if the ForeignKey gets deleted / related_name =specifies the name of the reverse relation from the User model back to your model.
    )
    grade = models.JSONField(null=True, blank=True)
