from django.db import models
from topic.models import Lesson
from topic.models import StudentUser


class QuesModel(models.Model):
    topic = models.ForeignKey(Lesson, on_delete=models.SET_NULL, related_name='topic', null=True)
    question = models.CharField('Savol', max_length=200, null=True)
    op1 = models.CharField('A javob', max_length=200, null=True)
    op2 = models.CharField('B javob', max_length=200, null=True)
    op3 = models.CharField('C javob', max_length=200, null=True)
    op4 = models.CharField('D javob', max_length=200, null=True)
    ans = models.CharField('Haqiqiy javob', max_length=200, null=True)

    def __str__(self):
        return str(self.topic.number)

    def get_name(self):
        return self.topic.title


def get_number(value):
    if value <= 15:
        return value
    else:
        raise ValueError("0 va 15 oralig'idagi son kiriting.")


class ResultModel(models.Model):
    user = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name='user')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    result = models.IntegerField(validators=[get_number])
    score = models.FloatField()
