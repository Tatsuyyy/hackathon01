from rest_framework import serializers
from api.models import Arrangements

class ArrangementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arrangements
        fields = '__all__'
