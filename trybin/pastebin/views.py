from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from pastebin.forms import RegisterUserForm, LoginUserForm, ContactForm, NewPostForm
from pastebin.utils import DataMixin

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'FAQ', 'url_name': 'faq'},
]


def home(request):
    context = {
        'title': 'Новая версия Pastebin',
        'menu': menu
    }
    return render(request, 'pastebin/home.html', context=context)


class Home(DataMixin, CreateView):
    form_class = NewPostForm
    template_name = 'pastebin/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='pastebin')
        return dict(list(context.items()) + list(c_def.items()))


class ContactView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'pastebin/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def faq(request):
    return HttpResponse('faq')


def about(request):
    return HttpResponse('about')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'pastebin/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'pastebin/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

# Create your views here.
