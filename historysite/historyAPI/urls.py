from django.urls import path
from .views import TestResultAPI


urlpatterns = [
    path('test_result/', TestResultAPI.as_view())
]
