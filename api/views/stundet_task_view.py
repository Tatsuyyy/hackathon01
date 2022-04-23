from django.shortcuts import get_object_or_404
from rest_framework import views, status
from api.models import Students, Tasks
from api.serializers import TaskSerializer
from rest_framework.response import Response

class StudentTaskView(views.APIView):
    """
    student_idで指定したstudentに登録されているtaskを全件取得する
    """
        
    def get(self, request, student_id, *args, **kwargs):
        student = get_object_or_404(Students, pk=student_id)
        tasks = Tasks.objects.filter(student=student)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)