from rest_framework import serializers
from criteria.serializersCriteria import CriteriaViewSerializer
from .modelsProject import Project
from team.serializersTeam import TeamViewSerializer
from evaluation.serializersEvaluation import EvaluationSerializer

# ? How the modal / scemah info shown(serializer):
# ? populate(give me all project):
class ProjectListViewSerializer(serializers.ModelSerializer):
    team = TeamViewSerializer(
        many=True, read_only=True
    )  # ? show obj by obj and not changable.  / read_only = unchangeable / many= True = you tell drf that queryset contains mutiple items (a list of items).
    criteria = CriteriaViewSerializer(
        many=True,
    )
    linkId = EvaluationSerializer(read_only=True)  # ? link for the projects

    class Meta:
        model = Project
        fields = "__all__"


# ? give me only (id): because when you don't mention the criteria it comes with id by default:
class ProjectViewSerializer(serializers.ModelSerializer):
    team = TeamViewSerializer(
        many=True, read_only=True
    )  # ? show obj by obj and not changable.

    class Meta:
        model = Project
        fields = "__all__"
