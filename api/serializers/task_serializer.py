from rest_framework import serializers
from api.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    """
    Task用シリアライザ
    """
    
    class Meta:
        model = Tasks
        fields = '__all__'
        
    def validate_required_time(self, required_time):
        # タスク時間のバリデーション
        if required_time > 10081:
            raise serializers.ValidationError("1タスクは1週間に収まるサイズにしてください。")
        return required_time

    def validate_name(self, name):
        if len(name) > 101:
            raise serializers.ValidationError("タスク名は100文字以内にしてください。")
        return name