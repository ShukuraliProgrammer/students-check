from email import message
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .forms import UserRegistrationForm
# Create your views here.
from .models import Lesson, Post
from django.views.generic import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from quiz.models import QuesModel

def registrationView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegistrationForm()
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                print(form)
                return redirect('login')

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
            print(user)

            if user is not None:
                login(request, user)
                print(username)
                print(password)
                return redirect('/')
            else:
                messages.info(request, "Sizning Username yoki Parolingiz xato")
        context = {}
        return render(request, 'login.html', context=context)


def logoutView(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homeView(request):
    lessons = Lesson.objects.all()
    posts = Post.objects.all()
    context = {
        'lessons': lessons,
        'posts': posts,
    }
    return render(request, 'home.html', context=context)


@login_required(login_url='login')
def baseView(request, pk):
    lesson = Lesson.objects.get(id=pk)

    context = {
        'lesson': lesson,
    }
    return render(request, 'base.html', context=context)


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
def lesson_detailView(request, pk):
    lesson = Lesson.objects.get(id=pk)
    print(lesson)
    context = {
        'lesson': lesson,

    }
    print(lesson.description)
    return render(request, 'maruza.html', context=context)


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
