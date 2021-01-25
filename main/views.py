from django.shortcuts import render, redirect
from news.models import Articles
from .forms import CreateAccount
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    count = Articles.objects.count()
    data = {'count': count}
    return render(request, 'main/about.html', data)

def register(request):
    form = CreateAccount()
    if request.method == 'POST':
        form = CreateAccount(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно зарегистрирован!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка при регистрации')
    data = {'form': form}
    return render(request, 'main/register.html', data)

def login_user(request):
    form = CreateAccount()
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверный логин или пароль')
    data = {'form': form}
    return render(request, 'main/login.html', data)

def logout_user(request):
    logout(request)
    return redirect('login')

