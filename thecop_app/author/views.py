from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..logic import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    author = Author.objects.get(pk=request.session['author_id'])
    songs_total = Songs.objects.all().count()
    context = {
        "author": author,
        "songs_total": songs_total,

    }
    return render(request, 'thecop_app/author/home.html', context)


def songs(request):
    author = Author.objects.get(pk=request.session['author_id'])
    context = {
        "author": author,
        "songs": Songs.objects.all(),
        "songs_total": Songs.objects.all().count()
    }
    return render(request, 'thecop_app/author/songs.html', context)


def articles(request):
    author = Author.objects.get(pk=request.session['author_id'])
    recent_articles = Article.objects.order_by('-date_created')[:4]
    older_articles = Article.objects.order_by('date_created')[:4]
    context = {
        "author": author,
        "recent_articles": recent_articles,
        "older_articles": older_articles
    }
    return render(request, 'thecop_app/author/articles.html', context)


def login(request):
    if request.method == "POST":
        password = request.POST["password"]
        phone = request.POST["phone"]
        pk = request.POST["id"]

        try:
            author = Author.objects.get(pk=pk)

            if phone == author.phone:
                if author.password == password:
                    request.session['author_id'] = author.id
                    return redirect("author_home")
                else:
                    return HttpResponse("Fail")
            else:
                return HttpResponse("Fail")
        except ObjectDoesNotExist:
            return HttpResponse("Fail")

    return render(request, 'thecop_app/author/login.html')


def add_song(request):
    if request.method == "POST":
        lyrics = request.POST['lyrics']
        title = request.POST['title']
        author = request.POST['author']
        language = request.POST['lang']

        new_song = Songs(
            title=title,
            lyrics=lyrics,
            author=author,
            language=language
        )

        new_song.save()
        return redirect("author_songs")


def add_article(request):
    author = Author.objects.get(pk=request.session['author_id'])

    if request.method == "POST":
        body = request.POST['body']
        header = request.POST['header']
        brief = request.POST['brief']
        img = request.FILES['art_img']

        author.add_article(body=body, head=header, brief=brief, img=img)
        return redirect("author_articles")
