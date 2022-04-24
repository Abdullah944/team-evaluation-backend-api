from rest_framework import serializers

from judge.modelsJudge import Judge
from .modelsEvaluation import Evaluation  # ? from the model grab the class.
from judge.serializersJudge import JudgeSerializer


class EvaluationSerializer(serializers.ModelSerializer):
    Judge = JudgeSerializer(many=True, read_only=True)

    class Meta:
        model = Evaluation
        fields = "__all__"
