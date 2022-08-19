from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('projects', views.HomeView.as_view(), name="project"),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name="article-detail"),
    path('category/<str:cats>', views.CategoryView, name="category"),
    path('list/', views.PaginatorView, name="list"),
]