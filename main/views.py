from django.shortcuts import render, redirect
from news.models import Articles
from .forms import CreateAccount
from django.contrib import messages

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
        else:
            messages.error(request, 'Ошибка при регистрации')
    data = {'form': form}
    return render(request, 'main/register.html', data)


