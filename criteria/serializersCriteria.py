from rest_framework import serializers
from .modelsCriteria import Criteria


class CriteriaViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = "__all__"
