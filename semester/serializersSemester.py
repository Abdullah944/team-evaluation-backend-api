from rest_framework import serializers

from project.serializersProject import ProjectViewSerializer
from .modelsSemester import Semester

# ? How the modal / scemah info shown(serializer):
class SemesterViewSerializer(serializers.ModelSerializer):
    project = ProjectViewSerializer(
        many=True, read_only=True
    )  # ?read_only = unchangeable / many= True = you tell drf that queryset contains mutiple items (a list of items).

    class Meta:
        model = Semester
        fields = "__all__"
