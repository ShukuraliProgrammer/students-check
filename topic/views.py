from email import message
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Lesson, Post, StudentUser, AboutProject, UsefulLink, ControlWork, Glossary
from django.views.generic import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from quiz.models import QuesModel, ResultModel


def registrationView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegistrationForm()
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, f"{user} muvaffaqqiyatli yaratildi.")
                return redirect('login')
            else:
                messages.error(request, form.errors)
        context = {
            'form': form,
        }
        return render(request, 'registration.html', context=context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Sizning Username yoki Parolingiz xato")
        context = {}
        return render(request, 'login.html', context=context)


def logoutView(request):
    logout(request)
    return redirect('login')


def homeView(request):
    lessons = Lesson.objects.all()
    posts = Post.objects.all()
    about_project = AboutProject.objects.last()
    students_count = StudentUser.objects.count()
    useful_links = UsefulLink.objects.all()
    context = {
        'lessons': lessons,
        'posts': posts,
        "about_project": about_project,
        "students_count": students_count,
        "useful_links": useful_links
    }
    return render(request, 'home.html', context=context)


# @login_required(login_url='login')
# def baseView(request, pk):
#     lesson = Lesson.objects.get(id=pk)
#
#     context = {
#         'lesson': lesson,
#     }
#     return render(request, 'base.html', context=context)


@login_required(login_url='login')
def videoView(request, pk):
    video = Lesson.objects.get(id=pk)
    tests = QuesModel.objects.get(id=pk)
    context = {
        'videos': video,
        'test': tests,
    }
    return render(request, 'video.html', context=context)


@login_required(login_url='login')
def lesson_detailView(request, lesson_order):
    context = {}
    if lesson_order == 1:
        lesson = Lesson.objects.get(order=lesson_order)
    else:
        last_test_result = ResultModel.objects.filter(user=request.user, lesson__order=(lesson_order - 1)).first()
        if last_test_result is None:
            lesson1 = Lesson.objects.filter(resultmodel__score__gte=60, resultmodel__user=request.user).order_by(
                '-order').first()
            if lesson1:
                o_l = lesson1.order
                lesson = Lesson.objects.get(order=o_l + 1)
            else:
                lesson = Lesson.objects.get(order=1)
        elif last_test_result.score > 60:
            lesson = Lesson.objects.get(order=lesson_order)
        else:
            lesson = Lesson.objects.get(order=(lesson_order - 1))
        # context = {}
        # if request.user.is_authenticated:
        #     if pk > 1:
        #         quiz = QuesModel.objects.get(id=pk - 1)
        #     else:
        #         quiz = QuesModel.objects.get(id=pk)
        #     lesson = Lesson.objects.get(id=pk)
        #     user = StudentUser.objects.get(id=request.user.id)
        #     print(user)
        #     lesson_r = lesson.id
        #     print(lesson_r)
        #     results = ResultModel.objects.filter(user_result=user.id, test_result=quiz.id).first()
        #
        #     percent1 = results.percent
        #

    context['lesson'] = lesson
    return render(request, 'maruza1.html', context)


@login_required(login_url='login')
def all_lecture(request):
    lectures = Lesson.objects.all()
    context = {
        'lectures': lectures,
    }
    return render(request, 'all_lecture.html', context=context)


@login_required(login_url='login')
def all_videos(request):
    videos = Lesson.objects.all()

    context = {
        'videos': videos,

    }
    return render(request, 'all_videos.html', context=context)


# def lecture(request):
#     context = {
#
#     }
#     return render(request, 'maruza1.html', context=context)


class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'news.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        latest_news = Post.objects.all().order_by("-created")[:5]
        context['latest_news'] = latest_news
        return context


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        latest_news = Post.objects.all().order_by("-created")[:5]
        context['latest_news'] = latest_news
        return context


@login_required(login_url='login')
def about_project(request):
    about_pro = AboutProject.objects.last()
    context = {
        "about_pro": about_pro,
    }
    return render(request, "about_project.html", context=context)


class ControlWorksView(LoginRequiredMixin, ListView):
    model = ControlWork
    template_name = 'nazoratlar.html'
    context_object_name = 'works'
    ordering = ('title', )
    def get_queryset(self):
        query_param = self.request.GET.get('q')
        if query_param == "JN":
            return ControlWork.objects.filter(type=ControlWork.WorkType.JN).order_by('title')
        elif query_param == 'ON':
            return ControlWork.objects.filter(type=ControlWork.WorkType.ON).order_by('title')
        elif query_param == 'YN':
            return ControlWork.objects.filter(type=ControlWork.WorkType.YN).order_by('title')
        return ControlWork.objects.all().order_by('title')


class GlossaryListView(ListView):
    model = Glossary
    template_name = 'glossariy.html'
    context_object_name = 'glossary'
    ordering = ('title', )