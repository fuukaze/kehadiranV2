from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from kontrol import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('form/', include("form.urls")),
    path('mahasiswa/', include("mahasiswa.urls")),
    path('pengurus/', include("pengurus.urls")),
    # path('classify/', views.find_user_view),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

