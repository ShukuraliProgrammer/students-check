from django.urls import path
from . import views
app_name = "quiz"
urlpatterns = [
    path('result', views.testView, name='result'),
    path('addques', views.addQuestionView, name='addQuestion'),
    path('<int:pk>/test/', views.testView, name='test'),
    # path('export_pdf', views.export_pdf, name='export_pdf'),


]
