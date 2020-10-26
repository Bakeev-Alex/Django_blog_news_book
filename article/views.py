from django.shortcuts import render, redirect
from .models import articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = articles.objects.all()
    return render(request, 'article/article_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news/')
        else:
            error = 'Ошибка в форме'

    form = ArticlesForm()
    return render(request, 'article/create.html', {'form': form,
                                                   'error': error})

class NewDetailView(DetailView):
    # с какой моделью работать
    model = articles
    # какой шаблон загружать
    template_name = 'article/detail_view.html'
    # Название ключа по которой будем передавать внутрь шаблона
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = articles
    template_name = 'article/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = articles
    success_url = '/news/'
    template_name = 'article/news_delete.html'

# Create your views here.
