from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="nationalAdmin_home"),
    path("announcement", views.announcement, name="nationalAdmin_announcement"),
    path("delete_announcement/<str:id>", views.delete_announcement, name="nationalAdmin_delete_announcement"),
    path("areas", views.areas, name="nationalAdmin_areas"),
    path("admins", views.admins, name="nationalAdmin_admins"),
    path("members", views.members, name="nationalAdmin_members"),
    path("login", views.login, name="nationalAdmin_login"),
    path("addarea", views.add_area, name="nationalAdmin_add_area"),
    path("addareaadmin", views.add_area_admin, name="nationalAdmin_add_area_admin"),
    path("add_announcement", views.add_announcement, name="nationalAdmin_add_announcement"),
    path("add_event", views.add_event, name="nationalAdmin_add_event"),
    path("add_author", views.add_author, name="nationalAdmin_add_author"),
]
