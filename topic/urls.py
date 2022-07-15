from unicodedata import name
from django.urls import path
from django.urls import reverse
from . import views
urlpatterns = [
    path('login', views.loginView, name='login'),
    path('registration', views.registrationView, name='registration'),
    path('logout/', views.logoutView, name='logout'),
    
    path('', views.homeView, name='home'),

    path('lesson/<int:lesson_order>/maruza', views.lesson_detailView, name='lesson_lecture'),
    path('all_lecture', views.all_lecture, name='all_lecture'),
    path('all_videos', views.all_videos, name='all_videos'),
    path('video', views.videoView, name='video'),
    path('glassariy/', views.glassariyView, name='glassariy'),
    path('nazorat/', views.nazoratView, name='nazorat'),
    path('adabiyotlar/', views.adabiyotView, name='adabiyot'),
    path('shahsiy-topshiriqlar/', views.privatetaskView, name='private-task'),
    path('news', views.newsView, name='news'),
    path('lesson/<int:pk>/video', views.videoView, name='lesson_video'),
    path('news/<int:pk>/', views.newsdetailView, name='news-detail'),

    
]