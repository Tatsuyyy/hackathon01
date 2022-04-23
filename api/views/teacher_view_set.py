from rest_framework import viewsets
from api.models import Teachers
from api.serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    """TeachersモデルのCRUD用クラス"""
    
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer