from rest_framework import serializers
from criteria.serializersCriteria import CriteriaViewSerializer
from .modelsProject import Project
from team.serializersTeam import TeamViewSerializer
from evaluation.serializersEvaluation import EvaluationSerializer

# ? populate:
class ProjectListViewSerializer(serializers.ModelSerializer):
    team = TeamViewSerializer(
        many=True, read_only=True
    )  # ? show obj by obj and not changable.
    criteria = CriteriaViewSerializer(
        many=True,
    )
    linkId = EvaluationSerializer(read_only=True)  # ? link for the projects

    class Meta:
        model = Project
        fields = "__all__"


# ? give me only id: when you don't mention the criteria it comes with id by default:
class ProjectViewSerializer(serializers.ModelSerializer):
    team = TeamViewSerializer(
        many=True, read_only=True
    )  # ? show obj by obj and not changable.

    class Meta:
        model = Project
        fields = "__all__"
