from rest_framework import generics
from historyApp.models import *
from .serializers import TestResultSerializer


class TestResultAPI(generics.ListAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
