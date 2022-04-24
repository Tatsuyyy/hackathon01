from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models import Students, Tasks, Arrangements, Weekdays
from api.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """tasksモデルのCRUD用クラス"""
    
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.insert_task(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
        
    def insert_task(self, data):
        """送信されたtaskを保存し、6等分してArrangementsに保存"""
        
        student_obj = get_object_or_404(Students, pk=data['student'])
        task_obj = Tasks(
            name=data['name'],
            content=data['content'],
            required_time=data['required_time'],
            is_done=data['is_done'],
            student=student_obj,
            )
        task_obj.save()
        days = self.get_days()
        self.split_task(days, task_obj)
        
        
    def split_task(self, days, task_obj):
        """
        日レベルに分割
        
        params
        ------
        days: list(int)
            1:月曜 ~ 7:日曜 に対応する値のlist
            含まれる値に対応した曜日に分割してtaskをArrangementsテーブルに格納
        
        task_obj: models.Tasks
            taskのobj
        """
        for day in days:
            if day < 8 and day > 0:
                weekday_obj = self.get_weekday_obj(day)
                arrangements_obj = Arrangements(
                    task=task_obj,
                    weekday=weekday_obj,
                    required_per_day=(task_obj.required_time/ len(days)),
                    done_per_day=0
                )
                arrangements_obj.save(force_insert=True)
            else:
                continue
        
    def get_days(self):
        return [1, 2, 3, 4, 5, 6]
        
    def get_weekday_obj(self, day):
        """
        指定されたdayのweekday_objを取得
        params
        ------
        
        day: int
            1:月曜 ~ 7:日曜   
        """
        if day < 8 and day > 0:
            weekday_obj = Weekdays.objects.get(pk=day)
            return weekday_obj
        else:
            return False