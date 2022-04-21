from rest_framework import serializers
from .modelsTeam import Team


class TeamViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
