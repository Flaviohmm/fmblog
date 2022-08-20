import django_filters

from .models import Post, Category

class CategoryFilter(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = ['category', 'title', 'summary']
