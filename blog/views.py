from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def project(request):
    return render(request, 'project.html')

def description(request):
    return render(request, 'description.html')