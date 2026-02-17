from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Article
from .models import News
class ArticleListView(ListView):
  model = Article
  template_name = 'index.html'


class ArticleDetailView(DetailView):
  model = Article
  template_name = 'detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['news_list'] = News.objects.all()[:5]#получение всех данных из таблицы
    return context

def contacts(request):
  return render(request, 'contacts.html')