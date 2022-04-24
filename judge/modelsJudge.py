from turtle import ondrag
from django.db import models
from evaluation.modelsEvaluation import Evaluation


class Judge(models.Model):
    name = models.CharField(max_length=255)
    evaluation = models.ForeignKey(
        Evaluation, on_delete=models.CASCADE, related_name="judge"
    )
    grade = models.JSONField(null=True, blank=True)
