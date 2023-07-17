from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="localAdmin_home"),
    path("login", views.login, name="localAdmin_login"),
    path("addmember", views.add_member, name="localAdmin_add_member"),
    path("add_announcement", views.add_announcement, name="localAdmin_add_announcement"),
    path("add_event", views.add_event, name="localAdmin_add_event"),
]
