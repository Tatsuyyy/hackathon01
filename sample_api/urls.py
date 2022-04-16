from django.urls import path

from sample_api.views import IndexView, SimpleView, SumView

from . import views


app_name = 'sample_api'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('hello', SimpleView.as_view(), name='hello'),
    path('sum', SumView.as_view(), name='sum'),
]