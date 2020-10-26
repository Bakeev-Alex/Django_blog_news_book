from django.contrib import admin
from .models import articles


@admin.register(articles)
class ArticAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status')

# Register your models here.
