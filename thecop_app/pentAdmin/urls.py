from django.urls import path, include
from . import views

urlpatterns = [
    path("signup", views.signup, name="copAdmin_signup"),
    path("home", views.home, name="copAdmin_home"),
    path("nations", views.nations, name="copAdmin_nations"),
    path("admins", views.admins, name="copAdmin_admins"),
    path("members", views.members, name="copAdmin_members"),
    path("login", views.login, name="copAdmin_login"),
    path("addnation", views.add_nation, name="copAdmin_add_nation"),
    path("addnationadmin", views.add_nation_admin, name="copAdmin_add_nation_admin"),
]
