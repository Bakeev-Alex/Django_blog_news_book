from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'news/post/index.html', data)

def about(request):
    return render(request, 'news/post/about.html')

def contacts(request):
    return render(request, 'news/post/contacts.html')