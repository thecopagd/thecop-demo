from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.home, name="areaAdmin_home"),
    path("login", views.login, name="areaAdmin_login"),
    path("add_district", views.add_district, name="areaAdmin_add_district"),
    path("add_districtadmin", views.add_district_admin, name="areaAdmin_add_district_admin"),
    path("add_announcement", views.add_announcement, name="areaAdmin_add_announcement"),
    path("add_event", views.add_event, name="areaAdmin_add_event"),
]
