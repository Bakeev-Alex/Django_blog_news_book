from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update-detail'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete-detail'),
]