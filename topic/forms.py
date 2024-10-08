from django import forms
from .models import StudentUser, Profile, ContactUs
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = StudentUser
        fields = ('last_name', 'first_name', 'surname', 'degree', 'group', 'email', 'username', 'password1', 'password2')

class ContactUsForm(forms.Form):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')
