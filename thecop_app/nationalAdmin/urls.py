from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="nationalAdmin_home"),
    path("login", views.login, name="nationalAdmin_login"),
    path("addarea", views.add_area, name="nationalAdmin_add_area"),
    path("addareaadmin", views.add_area_admin, name="nationalAdmin_add_area_admin"),
    path("add_announcement", views.add_announcement, name="nationalAdmin_add_announcement"),
    path("add_event", views.add_event, name="nationalAdmin_add_event")
]
