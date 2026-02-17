from django.contrib import admin

# Register your models here.

from .models import Article, News
admin.site.register(Article)
admin.site.register(News)