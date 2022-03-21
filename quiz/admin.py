from django.contrib import admin
from .models import QuesModel


# Register your models here.
@admin.register(QuesModel)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('topic','question', 'op1', 'op2', 'op3', 'op4')
    list_filter = ('topic', 'question')
