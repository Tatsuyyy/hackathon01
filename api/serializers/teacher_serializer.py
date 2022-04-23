from rest_framework import serializers
from api.models import Teachers

class TeacherSerializer(serializers.ModelSerializer):
    """
    Students用シリアライザ
    """
    
    class Meta:
        model = Teachers
        fields = '__all__'
        
    def validate_name(self, name):
        if len(name) > 101:
            raise serializers.ValidationError("名前は50文字以内にしてください。")
        return name