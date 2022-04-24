import pprint
from django.shortcuts import get_object_or_404
from api.models import Arrangements, Students, Tasks
from rest_framework import status, views
from rest_framework.response import Response
from api.serializers import ArrangementsSerializer


class WeekTaskView(views.APIView):
    queryset = Arrangements.objects.all()
    serializer_class = ArrangementsSerializer
    
    def get(self, request, student_id, *args, **kwargs):
        self.res = {'月':[], '火':[], '水':[], '木':[], '金':[], '土':[], '日':[]}
        
        student = get_object_or_404(Students, pk=student_id)
        tasks = Tasks.objects.filter(student=student)
        for task in tasks:
            arrangements = Arrangements.objects.filter(task=task)
            self.make_response(arrangements)
        
        pprint.pprint(self.res)
        return Response(self.res, status.HTTP_200_OK)

    def make_response(self, arrangements):
        for item in arrangements:
            serializer = ArrangementsSerializer(item)
            self.res[item.weekday.name].append(serializer.data)    