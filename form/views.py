from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import LoginForm
from kontrol.utils import is_ajax, classify_face
from pengurus.models import Kehadiran
from mahasiswa.models import Mahasiswa
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile

# Create your views here.

def pengurus(request):
    # function untuk halaman login pengurus
    context = {
        'title': 'Login',
        'heading': 'Blog',
        'subheadin': 'silahkan masukkan username dan password anda',
        'pages': [
            ['mahasiswa/', 'Absen Mahasiswa',
                'btn btn-danger btn-block'],
            ['sidepage/dosen', 'Absen Dosen', 'btn btn-warning btn-block'],
        ],
    }
    return render(request, "form/pengurus.html", context)


def mahasiswa(request):
    # function untuk halaman login mahasiswa
    context = {
        'title': 'Mahasiswa',
        'pesan': 'Silahkan masukkan foto dan NIM kalian',
        'heading': [
            ['', 'Login Mahasiswa'],
        ],
        'data': 'A11.xxxx.xxxxx',
    }
    return render(request, "form/mahasiswa.html", context)

def admin_verif_login(request):
    # function untuk verifikasi login pengurus
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/pengurus/')
        else:
            messages.error(request, 'Invalid login details')
    return render(request, 'form/pengurus.html', {'form': LoginForm})

def admin_logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out!!')
    return redirect('pengurus')

# def halaman_mhs(request):
#     app2_url = '/mahasiswa/'  # Adjust the URL as needed
#     return redirect(app2_url)

# def find_user_view(request):
#     # function untuk mencari mahasiswa apakah hadir atau tidak
#     if is_ajax(request):
#         # jika menerima paket dari kode program ajax akan menjalankan kode program

#         # terima data yang dikirim ajax
#         photo = request.POST.get('foto_hadir') #ambil nilai request foto_hadir dari tipe POST
#         latitude = float(request.POST.get('latitude'))
#         longitude = float(request.POST.get('longitude'))
#         _, str_img = photo.split(';base64') #pecah file sebelum ;base64 supaya str_img berisi kode gambar dalam format base64

#         # print(photo)
#         decoded_file = base64.b64decode(str_img)
#         # print(decoded_file)

#         x = Kehadiran()
#         x.foto_hadir.save('upload.jpg', ContentFile(decoded_file))
#         x.lokasi = f"{latitude},{longitude}"
#         x.save()

#         res = classify_face(x.foto_hadir.path)
#         if res:
#             user_exists = Mahasiswa.objects.filter(nim=res).exists()
#             if user_exists:
#                 mhs = Mahasiswa.objects.get(nim=res)
#                 x.nama = mhs.nama
#                 x.nim = mhs.nim
#                 x.jurusan = mhs.jurusan
#                 x.mahasiswa = mhs
#                 x.save()

#                 login(request, None)

#                 return JsonResponse({'success': True, 'redirect_url': '/mahasiswa/'})
            
#         # return redirect('mahasiswa/')
#         return JsonResponse({'success': False})
#     return redirect('mahasiswa/')
        
def find_user_view(request):
    # Function to check if the request is an AJAX request
    if is_ajax(request) and request.method == 'POST':
        try:
            # Terima data yang dikirim ajax
            photo = request.POST.get('foto_hadir')
            latitude = float(request.POST.get('latitude'))
            longitude = float(request.POST.get('longitude'))
            _, str_img = photo.split(';base64')

            decoded_file = base64.b64decode(str_img)

            x = Kehadiran()
            x.foto_hadir.save('upload.jpg', ContentFile(decoded_file))
            x.lokasi = f"{latitude},{longitude}"
            x.save()

            res = classify_face(x.foto_hadir.path)
            if res:
                user_exists = Mahasiswa.objects.filter(nim=res).exists()
                if user_exists:
                    mhs = Mahasiswa.objects.get(nim=res)
                    x.nama = mhs.nama
                    x.nim = mhs.nim
                    x.jurusan = mhs.jurusan
                    x.mahasiswa = mhs
                    x.save()

                    login(request, None)

                    return JsonResponse({'success': True, 'redirect_url': '/mahasiswa/'})
        except ValueError:
            # Handle the case where latitude or longitude cannot be converted to float
            return JsonResponse({'success': False, 'error': 'Invalid latitude or longitude'})
        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'success': False, 'error': str(e)})
        
        return JsonResponse({'success': False, 'error': 'Classification failed'})
    else:
        # If the request is not an AJAX POST request, redirect to 'mahasiswa/' URL
        return redirect('mahasiswa/')