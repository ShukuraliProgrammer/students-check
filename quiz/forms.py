from django.forms import ModelForm
from topic.models import StudentUser
from django.contrib.auth.forms import UserCreationForm
from .models import QuesModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = StudentUser
        fields = ['username', 'password']


class AddQuestionForm(ModelForm):
    class Meta:
        model = QuesModel
        fields = '__all__'

