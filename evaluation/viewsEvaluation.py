from rest_framework.viewsets import ModelViewSet
from .serializersEvaluation import EvaluationSerializer
from .modelsEvaluation import Evaluation


class Evaluation(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
