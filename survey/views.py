from .models import Survey, Question, PossibleAnswer, ClosedSurvey
from .serializers import SurveySerializer, QuestionSerializer, PossibleAnswerSerializer, ClosedSurveySerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status


class SurveyList(APIView):
    def get(self, request, format=None):
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerViewSet(APIView):
    def post(self, request):
        current_user = request.user
        answers_by_user = request.data["answers"]
        survey = Survey.objects.get(pk=request.data["survey"])

        right_answer = []
        wrong_answer = []

        if len(answers_by_user) < len(survey.question_survey.all()):
            return JsonResponse({"error": "Вы ответили не на все вопросы!"})
        else:
            for ua in answers_by_user:
                answer = survey.question_survey.filter(id=ua['id'],
                                                       possible_answer_of_question=ua['answer'],
                                                       possible_answer_of_question__is_correct=True)
                if answer:
                    right_answer.append(answer)
                else:
                    wrong_answer.append(not answer)

            percent = len(right_answer) / len(survey.question_survey.all()) * 100

            print(len(right_answer))
            print(len(wrong_answer))
            print(percent)

            right_answer = str(len(right_answer))
            wrong_answer = str(len(wrong_answer))

            closed_survey = ClosedSurvey.objects.create(survey=survey, profile=current_user.profile,
                                                        right_answer=right_answer,
                                                        wrong_answer=wrong_answer, percent=str(percent) + '%')

            serializer = ClosedSurveySerializer(closed_survey, many=False)
            return Response(serializer.data)
