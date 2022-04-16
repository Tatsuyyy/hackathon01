from rest_framework import serializers

class SumSerializer(serializers.Serializer):

    def sum(self, num1, num2):
        return num1 + num2