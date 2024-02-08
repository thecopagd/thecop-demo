from django.shortcuts import render
from .models import *


def index(request):
    recent_articles = Article.objects.order_by('-date_created')[:4]
    context = {
        'locals_total': LocalAssembly.objects.all().count(),
        'members_total': Member.objects.all().count(),
        "recent_articles": recent_articles
    }
    return render(request, 'thecop_app/index.html', context)


def songs(request):
    return render(request, 'thecop_app/songs.html')

def about_leaders(request):
    return render(request, 'thecop_app/about_leaders.html')


def gallery(request):
    return render(request, 'thecop_app/gallery.html')


def find_church(request):
    return render(request, 'thecop_app/find_church.html')
