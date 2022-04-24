from rest_framework.viewsets import ModelViewSet  # ?have all the CRUD in it.
from .modelsProject import Project
from .serializersProject import ProjectListViewSerializer, ProjectViewSerializer
from rest_framework import permissions

# ? show me all list in this form taken from Projects modal:
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()

    # ? if the request is SAFE_METHODS populate else only id(to show criteria):
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ProjectListViewSerializer  # ? populate to take all info
        else:
            return ProjectViewSerializer  # ? i want the id only to connect it
