from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="localAdmin_home"),
    path("members", views.members, name="localAdmin_members"),
    # -------------------------------------------------------------------------------------------------------- #
    path("announcements", views.announcements, name="localAdmin_announcement"),
    path("add_announcement", views.add_announcement, name="localAdmin_add_announcement"),
    path("delete_announcement/<str:id>", views.delete_announcement, name="localAdmin_delete_announcement"),
    # -------------------------------------------------------------------------------------------------------- #
    path("login", views.login, name="localAdmin_login"),
    path("addmember", views.add_member, name="localAdmin_add_member"),
    path("add_event", views.add_event, name="localAdmin_add_event"),
]
