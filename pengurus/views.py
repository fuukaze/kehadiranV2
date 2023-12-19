from django.shortcuts import render
from .models import Kehadiran
from mahasiswa.models import Mahasiswa

def index(request):
    context = {
        'title': 'Admin | Beranda',
        'type' : 'Beranda',
        'heading': 'Blog',
        'subheadin': 'silahkan masukkan username dan password anda',
        'nav': ['Pengurus','Beranda'],
    }
    return render(request, "pengurus/pages/beranda.html", context)

def dataMahasiswa(request):
    mhs = Mahasiswa.objects.all()
    context = {
        'title': 'Admin | Mahasiswa',
        'heading': 'Blog',
        'subheadin': 'silahkan masukkan username dan password anda',
        'nav': ['Pengurus','Mahasiswa'],
        'tabel_mhs': mhs,
    }
    return render(request, "pengurus/pages/data-mahasiswa.html", context)

def dataKehadiran(request):
    hadir = Kehadiran.objects.all()
    context = {
        'title': 'Admin | Kehadiran',
        'heading': 'Blog',
        'subheadin': 'silahkan masukkan username dan password anda',
        'nav': ['Pengurus','Kehadiran'],
        'tabel_kehadiran': hadir,
    }
    return render(request, "pengurus/pages/data-kehadiran.html", context)