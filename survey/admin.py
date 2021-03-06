from django.contrib import admin
from .models import Survey, PossibleAnswer, Question

admin.site.register(PossibleAnswer)


class QuestionInstanceInline(admin.TabularInline):
    model = Question


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'pub_date', )
    inlines = [QuestionInstanceInline]