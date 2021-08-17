from rest_framework import serializers
from .models import Survey, Question, PossibleAnswer, ClosedSurvey


class PossibleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossibleAnswer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    possible_answer_of_question = PossibleAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    question_survey = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'


class ClosedSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosedSurvey
        fields = '__all__'
