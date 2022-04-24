from rest_framework.viewsets import ModelViewSet  # ?have all the CRUD in it.
from .modelsCriteria import Criteria
from .serializersCriteria import CriteriaViewSerializer


# ? show me all list in this form taken from Criteria modal:
class CriteriaViewSet(ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaViewSerializer
