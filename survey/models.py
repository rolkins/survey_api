from django.db import models
from users.models import Profile
from django.http import JsonResponse


class Survey(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='question_survey')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PossibleAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='possible_answer_of_question')
    title = models.CharField(max_length=120)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ClosedSurvey(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, blank=True, null=True)
    right_answer = models.IntegerField()
    wrong_answer = models.IntegerField()
    percent = models.CharField(max_length=20)