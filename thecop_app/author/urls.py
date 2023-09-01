from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="author_home"),
    path("songs", views.songs, name="author_songs"),
    path("articles", views.articles, name="author_articles"),
    path("login", views.login, name="author_login"),
    path("add_song", views.add_song, name="author_add_song"),
    path("add_article", views.add_article, name="author_add_article"),
]
