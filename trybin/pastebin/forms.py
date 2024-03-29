from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField(label='Капча')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField(label='Капча')


class NewPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['category'].empty_label = 'Категория не выбрана'
        self.fields['privacy'].empty_label = "Установить статус приватности"
        self.fields['time_to_delete'].empty_label = "Установить время удаления"

    class Meta:
        model = NewPost
        fields = ['title', 'text', 'category', 'tags', 'privacy', 'time_to_delete', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'text': forms.Textarea(attrs={'cols': 70, 'rows': 20})
        }