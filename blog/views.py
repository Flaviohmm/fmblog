from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import CategoryFilter


def index(request):
    return render(request, 'index.html')


class HomeView(ListView):
    model = Post
    template_name = 'project.html'
    ordering = ['-post_date']
    context_object_name = 'users'
    paginate_by = 2
    queryset = Post.objects.get_queryset().order_by('id')


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


# def CategoryView(request, cats):
#     cats = Category.objects.get(name=cats)
#     category_posts = Post.objects.filter(category=cats)
#     return render(request, 'category.html', {'cats': str(cats).capitalize, 'category_posts': category_posts})


def PaginatorView(request):
    post_list = Post.objects.get_queryset().order_by('id')

    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
   
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', { 'users': users, 'post_list': post_list })


def show_all_categories_page(request, cats):
    context = {}
    cats = Category.objects.get(name=cats)

    filtered_categories = CategoryFilter(
        request.GET,
        queryset=Post.objects.filter(category=cats)
    )

    context['filtered_categories'] = filtered_categories.qs

    paginated_filtered_categories = Paginator(filtered_categories.qs, 2)
    page_number = request.GET.get('page')
    category_page_obj = paginated_filtered_categories.get_page(page_number)

    context['category_page_obj'] = category_page_obj

    return render(request, 'show_all_categories_page.html', context=context)
