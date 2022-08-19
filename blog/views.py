from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post


def index(request):
    return render(request, 'index.html')


class HomeView(ListView):
    model = Post
    template_name = 'project.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


def CategoryView(request, cats):
    cats = Category.objects.get(name=cats)
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats': str(cats).capitalize, 'category_posts': category_posts})
