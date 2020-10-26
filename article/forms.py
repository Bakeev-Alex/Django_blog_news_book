from .models import articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = articles
        fields = ['title', 'anons', 'body', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Анонс статьи'
            }),
            'body': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Текст статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': "form-control",
                'type': "datetime-local",
                'placeholder': 'Дата публикации'
            }),
        }