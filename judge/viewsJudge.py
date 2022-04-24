from rest_framework.viewsets import ModelViewSet
from .modelsJudge import Judge
from .serializersJudge import JudgeSerializer, JudgeCreateSerializer


class JudgeViewSet(ModelViewSet):
    queryset = Judge.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return JudgeCreateSerializer
        return JudgeSerializer
