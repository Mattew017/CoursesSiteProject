from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Course


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label="Пароль",
                                widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Повтор пароля",
                                widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': "form-control"}))


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
