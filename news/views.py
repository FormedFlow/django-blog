from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def add(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Ошибка заполнения формы'

    form = ArticlesForm()
    data = {'form': form, 'error': error}
    return render(request, 'news/add.html', data)


def news_home(request):
    news = Articles.objects.all()
    data = {'news': news}
    print(news[0])
    return render(request, 'news/news_home.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/full_article.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/add.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete.html'
    success_url = '/news/'