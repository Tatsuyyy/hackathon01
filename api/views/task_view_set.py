from rest_framework import viewsets
from api.models import Tasks
from api.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """tasksモデルのCRUD用クラス"""
    
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer