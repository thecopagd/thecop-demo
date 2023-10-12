from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="member_home"),
    path("login", views.login, name="member_login"),
    path("headlines", views.headlines, name="member_headlines"),
    path("me", views.me, name="member_me"),
]

