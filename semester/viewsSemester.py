from rest_framework.viewsets import ModelViewSet  # ?have all the CRUD in it.
from .modelsSemester import Semester
from .serializersSemester import SemesterViewSerializer

# Create your views here.

# ? show me all list in this form taken from Semesters modal:
class SemesterViewSet(ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterViewSerializer
