from rest_framework import filters
from api.models import Tasks

class TaskFilter(filters.FilterSet):
    class Meta:
        model = Tasks
        fields = '__all__'
        
    