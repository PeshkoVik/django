from django.shortcuts import render
from django.http import HttpResponse
from .models import News
# Create your views here.

from .models import News

def index(request):
  news = News.objects.all()
  return render(request, 'news/index.html', {'news': news, 'title':'List of news'})
