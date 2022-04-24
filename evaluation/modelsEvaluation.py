from django.db import models
from project.modelsProject import Project  # ? use project models
import uuid  # ? make uniq ID's


class Evaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.OneToOneField(
        Project, on_delete=models.CASCADE, related_name="linkId"
    )  # ? to make a link of a project can be shared.
    isLocked = models.BooleanField(default=False)  # ? make i lock screen modal.
