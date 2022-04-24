from django.shortcuts import get_object_or_404
from rest_framework import views, status
from rest_framework.response import Response
from api.models import Students, Tasks, Arrangements, Weekdays
from api.serializers import TaskSerializer
from api.serializers import ArrangementsSerializer


class ArrangementsUpdateView(views.APIView):
    """arrangementsの一部更新view"""
    
    def patch(self, request, task_id, *args, **kwargs):
        """
        done_per_dayの更新用  
        params = {
            "weekday": int ,
            "done_per_day":int
        }  
        weekday:
            1:月曜 ~ 7:日曜
        """
        day = get_object_or_404(Weekdays, pk=request.data['weekday'])
        task = get_object_or_404(Tasks, pk=task_id)
        arrangement = Arrangements.objects.get(weekday=day, task=task)
        serializer = ArrangementsSerializer(
            arrangement, data={'done_per_day': request.data['done_per_day']}, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
        
