from rest_framework import serializers
from .modelsTeam import Team

# ? How the modal / scemah info shown(serializer):
class TeamViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
