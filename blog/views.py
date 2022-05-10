from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def index(request):
    return render(request, 'index.html')


class HomeView(ListView):
    model = Post
    template_name = 'project.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'