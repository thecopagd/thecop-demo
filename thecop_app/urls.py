from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
          path("", views.index, name="index"),
          path("songs", views.songs, name="songs"),
          path("about/leaders", views.about_leaders, name="about_leaders"),
          path('pentadmin/', include('thecop_app.pentAdmin.urls')),
          path('nationaladmin/', include('thecop_app.nationalAdmin.urls')),
          path('area_admin/', include('thecop_app.areaAdmin.urls')),
          path('districtadmin/', include('thecop_app.districtAdmin.urls')),
          path('localadmin/', include('thecop_app.localAdmin.urls')),
          path('member/', include('thecop_app.member.urls')),
          path('author/', include('thecop_app.author.urls')),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
