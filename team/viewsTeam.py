from rest_framework.viewsets import ModelViewSet  # ?have all the CRUD in it.
from .modelsTeam import Team
from .serializersTeam import TeamViewSerializer

# Create your views here.

# ? show me all list in this form taken from Teams modal:
class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamViewSerializer
