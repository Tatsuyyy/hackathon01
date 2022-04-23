from django.urls import path, include
from rest_framework import routers
from api.views import TaskViewSet, StudentViewSet, TeacherViewSet

router = routers.SimpleRouter()
router.register('tasks', TaskViewSet)
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)

app_name = 'api'
urlpatterns = [
    path('/', include(router.urls))
]