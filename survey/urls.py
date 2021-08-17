from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from survey import views

urlpatterns = [
    path('surveys/', views.SurveyList.as_view()),
    path('answer/', views.AnswerViewSet.as_view()),
]