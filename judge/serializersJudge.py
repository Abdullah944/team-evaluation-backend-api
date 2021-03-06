from rest_framework import serializers
from .modelsJudge import Judge

# ? How the modal / scemah info shown(serializer):

# ? CREATE:
class JudgeCreateSerializer(serializers.ModelSerializer):
    grade = serializers.ReadOnlyField()

    class Meta:
        model = Judge
        fields = "__all__"

    def create(self, validated_data):
        defCriteria = []
        for criteria in validated_data["evaluation"].project.criteria.all():
            defCriteria.append(
                {
                    "criteria_id": criteria.id,
                    "criteria_name": criteria.name,
                    "criteria_weight": criteria.weight,
                    "grade": 0,
                }
            )
        teams = []
        for team in validated_data["evaluation"].project.team.all():
            teams.append(
                {"team_id": team.id, "team_name": team.name, "grade": defCriteria}
            )
        validated_data["grade"] = teams
        return super().create(validated_data)

    # ? SHOW:


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = "__all__"
