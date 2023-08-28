from django.shortcuts import render


def index(request):
    return render(request, 'thecop_app/index.html')


def about_leaders(request):
    return render(request, 'thecop_app/about_leaders.html')
