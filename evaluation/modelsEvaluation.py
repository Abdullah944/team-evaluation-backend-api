from django.db import models
from project.modelsProject import Project  # ? use project models
import uuid  # ? make uniq ID's

# ? What is the schema of the  model:

# ? Class = blueprint to make obj from it & use it else were:
class Evaluation(models.Model):
    # ? This will give you unique ID.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # ?CASCADE =the row will be deleted too if the ForeignKey gets deleted / related_name =specifies the name of the reverse relation from the User model back to your model.
    project = models.OneToOneField(
        Project, on_delete=models.CASCADE, related_name="linkId"
    )  # ? to make a link of a project can be shared.
    isLocked = models.BooleanField(default=False)  # ? make i lock screen modal.
