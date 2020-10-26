from django.db import models
from django.utils import timezone

# Create your models here.

class articles(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField('Заголовок', max_length=150)
    anons = models.CharField('Анонс', max_length=250)
    body = models.TextField('Статья')
    date = models.DateTimeField("Дата публикации", default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # Показывает title как текст, а не objects(1)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-date',)

    def get_absolute_url(self):
        return f'/news/{self.id}'


