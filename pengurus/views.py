from django.shortcuts import render

def index(request):
    context = {
        'title': 'Login',
        'heading': 'Blog',
        'subheadin': 'silahkan masukkan username dan password anda',
        'pages': [
            ['sidepage/mahasiswa', 'Absen Mahasiswa',
                'btn btn-danger btn-block'],
            ['sidepage/dosen', 'Absen Dosen', 'btn btn-warning btn-block'],
        ],
    }
    return render(request, "pengurus/index.html", context)

def login(request):

    return render(request, "pengurus/login.html")