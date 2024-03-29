from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="districtAdmin_home"),
    path("locals", views.locals, name="districtAdmin_locals"),
    path("admins", views.admins, name="districtAdmin_admins"),
    path("members", views.members, name="districtAdmin_members"),
    path("login", views.login, name="districtAdmin_login"),
    path("addlocal", views.add_local, name="districtAdmin_add_local"),
    path("addlocaladmin", views.add_local_admin, name="districtAdmin_add_local_admin"),
    path("add_announcement", views.add_announcement, name="districtAdmin_add_announcement"),
    path("add_event", views.add_event, name="districtAdmin_add_event"),
]
