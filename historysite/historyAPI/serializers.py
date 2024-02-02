from rest_framework import serializers
from historyApp.models import *


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ('user', 'test', 'date', 'score')
