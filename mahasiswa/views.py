from django.shortcuts import render

# Create your views here.
def index(request):
   #  context = {
   #      'title': 'HomePage',
   #      'heading': 'Main Page',
   #      'subheading': 'jurnal kelas terbuka',
   #      'nav': [
   #          ['/', 'HOMEPAGE'],
   #      ],
   #      'kehadiran': [
   #          ['form/mahasiswa/', 'Mahasiswa'],
   #          ['form/', 'Admin']
   #      ],
   #  }
    return render(request, 'mahasiswa/index.html')
