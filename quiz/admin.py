from django.contrib import admin
from .models import QuesModel, ResultModel
from topic.models import Lesson



@admin.register(QuesModel)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['topic', 'question', 'op1', 'op2', 'op3', 'op4']
    list_filter = ('topic', 'question')



@admin.register(ResultModel)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'result', 'score']


