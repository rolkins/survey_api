from django.contrib import admin
from .models import Profile
from survey.models import ClosedSurvey


class QuestionInstanceInline(admin.TabularInline):
    model = ClosedSurvey


@admin.register(Profile)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', )
    inlines = [QuestionInstanceInline]


