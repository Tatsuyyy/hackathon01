import datetime
from django.shortcuts import get_object_or_404
from rest_framework import views, status
from rest_framework.response import Response
from api.models import Students, Tasks, Arrangements, Weekdays
from api.serializers import TaskSerializer
from api.serializers import ArrangementsSerializer


class ArrangementsUpdateTodayView(views.APIView):
    """arrangementsの一部更新view"""
    
    def patch(self, request, task_id, *args, **kwargs):
        """
        task_idで指定したtaskの今日分のdone_per_dayを更新する 
        
        params = {
            "done_per_day":int
        }  
        """
        day_id = datetime.date.today().weekday()+1
        day = get_object_or_404(Weekdays, pk=day_id)
        task = get_object_or_404(Tasks, pk=task_id)
        arrangement = Arrangements.objects.get(weekday=day, task=task)
        serializer = ArrangementsSerializer(
            arrangement, data={'done_per_day': request.data['done_per_day']}, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
        
