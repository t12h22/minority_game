from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=50)
