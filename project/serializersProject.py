from rest_framework import serializers
from .modelsProject import Project
from team.serializersTeam import TeamViewSerializer


class ProjectViewSerializer(serializers.ModelSerializer):
    team = TeamViewSerializer(
        many=True, read_only=True
    )  # ? show obj by obj and not changable

    class Meta:
        model = Project
        fields = "__all__"
