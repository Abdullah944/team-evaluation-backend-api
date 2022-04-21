from rest_framework import serializers

from project.serializersProject import ProjectViewSerializer
from .modelsSemester import Semester


class SemesterViewSerializer(serializers.ModelSerializer):
    project = ProjectViewSerializer(many=True, read_only=True)

    class Meta:
        model = Semester
        fields = "__all__"
