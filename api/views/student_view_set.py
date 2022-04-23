from rest_framework import viewsets
from api.models import Students
from api.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """studentsモデルのCRUD用クラス"""
    
    queryset = Students.objects.all()
    serializer_class = StudentSerializer