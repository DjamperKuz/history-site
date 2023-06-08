from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=1)
    text = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Topic, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
    score = models.CharField(max_length=255)
