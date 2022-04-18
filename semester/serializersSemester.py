from rest_framework import serializers
from .modelsSemester import Semester


class SemesterViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"
