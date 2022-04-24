from rest_framework import serializers
from api.models import Arrangements, Tasks


class ArrangementsSerializer(serializers.ModelSerializer):
    task_name = serializers.SerializerMethodField() 
    task_content = serializers.SerializerMethodField() 
    task_required_time = serializers.SerializerMethodField() 

    def get_task_name(self, obj):
        print(obj)
        task = Tasks.objects.get(pk=obj.task.id)
        return task.name
    
    def get_task_content(self, obj):
        task = Tasks.objects.get(pk=obj.task.id)
        return task.content
    
    def get_task_required_time(self, obj):
        task = Tasks.objects.get(pk=obj.task.id)
        return task.required_time
    
    
    class Meta:
        model = Arrangements
        fields = ('task', 'required_per_day','done_per_day','weekday',
                    'task_name', 'task_content', 'task_required_time')
