from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('pentadmin/', include('thecop_app.pentAdmin.urls')),
    path('nationaladmin/', include('thecop_app.nationalAdmin.urls')),
    path('area_admin/', include('thecop_app.areaAdmin.urls')),
    path('districtadmin/', include('thecop_app.districtAdmin.urls')),
    path('localadmin/', include('thecop_app.localAdmin.urls')),
    path('member/', include('thecop_app.member.urls')),
]
