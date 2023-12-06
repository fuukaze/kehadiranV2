from django.urls import path
from . import views

urlpatterns = [
    path('mahasiswa/', views.mahasiswa, name='mahasiswa'),
    path('pengurus/', views.pengurus, name='pengurus'),
    path('verif_login/', views.admin_verif_login, name='verif_login'),
    path('mahasiswa/classify/', views.find_user_view, name='classify'),
    path('halaman_mahasiswa/',views.halaman_mhs, name="halaman_mahasiswa")
]
