from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('projects', views.project, name="project"),
    path('projects/description', views.description, name="description"),
]
