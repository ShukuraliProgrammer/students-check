import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import QuesModel, ResultModel
from .forms import AddQuestionForm
from django.shortcuts import redirect
from topic.models import Lesson, StudentUser


def testView(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            questions = QuesModel.objects.filter(topic=pk)
            score = 0
            wrong = 0
            correct = 0
            total = 0
            for q in questions:
                total += 1
                if q.ans == request.POST.get(q.question):
                    score += 10
                    correct += 1
                else:
                    wrong += 1
            if total != 0:
                percent = score / (total * 10) * 100
            else:
                percent = 0
                total = 0
                score = 0

            if percent >= 60:
                if pk != 15:
                    lesson = Lesson.objects.get(id=pk + 1)
                else:
                    lesson = Lesson.objects.get(id=15)
            else:
                lesson = Lesson.objects.get(id=pk)
            user1 = StudentUser.objects.get(id=request.user.id)
            test_lesson = Lesson.objects.get(id=pk)
            result1 = ResultModel.objects.filter(user=user1,lesson=test_lesson).first()
            if result1:
                result1.delete()
            r = ResultModel.objects.create(
                    user=user1,
                    lesson=test_lesson,
                    result=total,
                    score=percent,
               )
            context = {
                'lesson': lesson,
                'score': score,
                'correct': correct,
                'wrong': wrong,
                'percent': percent,
                'total': total,
                'time': request.POST.get('timer'),
            }
            return render(request, 'result.html', context=context)
        else:
            questions = QuesModel.objects.filter(topic=pk)
            context = {
                'questions': questions,
            }
            return render(request, 'quiz.html', context=context)


def addQuestionView(request):
    if request.user.is_staff:
        form = AddQuestionForm()
        if request.method == "POST":
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'addQuestion.html', context=context)
    else:
        return redirect('test')

# def export_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=Expenses' + \
#                                       str(datetime.datetime.now()) + '.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#     html_string = render_to_string(
#         'expenses/pdf_output.html', {'expenses': [], 'total': 0}
#     )
#
#     html = HTML(string=html_string)
#
#     result = html.write_pdf()
#
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output.open(output.name, 'rb')
#         response.write(output.read())
#     return response
