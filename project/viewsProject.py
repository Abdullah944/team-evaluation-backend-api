from rest_framework.viewsets import ModelViewSet  # ?have all the CRUD in it.
from .modelsProject import Project
from .serializersProject import ProjectViewSerializer

# Create your views here.

# ? show me all list in this form taken from Projects modal:
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectViewSerializer
