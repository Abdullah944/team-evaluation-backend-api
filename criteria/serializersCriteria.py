from rest_framework import serializers
from .modelsCriteria import Criteria

# ? How the modal / scemah info shown(serializer):
class CriteriaViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = "__all__"  # ? take all the info in it.
