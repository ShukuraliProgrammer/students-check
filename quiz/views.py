import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import QuesModel
from .forms import AddQuestionForm
from django.shortcuts import redirect

# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
# from django.db.models import Sum
# import datetime


# Create your views here.

def testView(request,pk):
    if request.user.is_authenticated:

        if request.method == "POST":
            questions = QuesModel.objects.filter(topic=pk)
            print(questions)
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

            percent = score / (total * 10) * 100
            context = {
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
