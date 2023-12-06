from django.shortcuts import render
from django.contrib.auth import login
from django.http import JsonResponse
# from .utils import is_ajax, classify_face
import base64
from django.core.files.base import ContentFile
from pengurus.models import Pengurus, Kehadiran
from mahasiswa.models import Mahasiswa
# method view


def index(request):
    context = {
        'title': 'HomePage',
        'heading': 'Main Page',
        'subheading': 'jurnal kelas terbuka',
        'nav': [
            ['/', 'HOMEPAGE'],
        ],
        'kehadiran': [
            ['form/mahasiswa/', 'Mahasiswa'],
            ['form/pengurus/', 'Admin']
        ],
    }
    return render(request, 'base.html', context)

# def find_user_view(request):
#     # function untuk mencari mahasiswa apakah hadir atau tidak

#     if is_ajax(request):
#         # jika menerima paket dari kode program ajax akan menjalankan kode program

#         # terima data yang dikirim ajax
#         photo = request.POST.get('foto_kehadiran') #ambil nilai request foto_hadir dari tipe POST
#         _, str_img = photo.split(';base64') #pecah file sebelum ;base64 supaya str_img berisi kode gambar dalam format base64

#         # print(photo)
#         decoded_file = base64.b64decode(str_img)
#         print(decoded_file)

#         x = Kehadiran()
#         nama = x.nama
#         x.foto_hadir.save('upload.jpg', ContentFile(decoded_file))
#         x.save()

#         res = classify_face(x.foto_hadir.path)
#         if res:
#             user_exists = Mahasiswa.objects.filter(nama=res).exists()
#             if user_exists:
#                 mhs = Mahasiswa.objects.get(nama=res)
#                 x.mahasiswa = mhs
#                 x.save()

#                 login(request, mhs)
#                 return JsonResponse({'success': True})
#         return JsonResponse({'success': False})
    