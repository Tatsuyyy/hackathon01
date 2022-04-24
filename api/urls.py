from django.urls import path, include
from rest_framework import routers
from api.views import TaskViewSet, StudentViewSet, TeacherViewSet, StudentTaskView, WeekTaskView, ArrangementsUpdateView, ArrangementsUpdateTodayView

router = routers.SimpleRouter()
router.register('tasks', TaskViewSet)
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
    path('tasks/filter/student/<student_id>/', StudentTaskView.as_view()),
    path('tasks/filter/week/<student_id>/', WeekTaskView.as_view()),
    path('arrangements/update/done/<task_id>/', ArrangementsUpdateView.as_view()),
    path('arrangements/update/done/today/<task_id>/', ArrangementsUpdateTodayView.as_view()),
]