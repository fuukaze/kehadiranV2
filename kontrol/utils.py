import face_recognition as fr
import numpy as np
from mahasiswa.models import Mahasiswa


def is_ajax(request):
    # function untuk menerima request ajax dari script login.js
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'


def get_encoded_faces():
    # function untuk load foto semua user 
    # dan mengkodekan wajah
    
    # tarik semua data dari tabel mahasiswa di database lewat models
    qs = Mahasiswa.objects.all()

    # membuat dictionary untuk menyimpan wajah yang dikodekan wajahnya tiap user    
    encoded = {}

    for p in qs:
        # inisialisasi variabel encoding dengan none
        encoding = None

        # ambil semua foto mahasiswa
        face = fr.load_image_file(p.foto_mhs.path)

        # encode wajah
        face_encodings = fr.face_encodings(face)
        if len(face_encodings) > 0:
            encoding = face_encodings[0]
        else:
            print("Tidak ditemukan wajah pada foto")

        # Add the user's encoded face to the dictionary if encoding is not None
        if encoding is not None:
            encoded[p.nim] = encoding

    # Return the dictionary of encoded faces
    return encoded


def classify_face(img):
    # function untuk mengambil gambar sebagai input dan mengembalikan nilai wajah yang dibawa
    
    # ambil semua wajah yang dikenali dan kode wajahnya
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    # ambil wajah yang dimasukkan
    img = fr.load_image_file(img)
 
    try:
        # cari lokasi semua wajah yang dimasukkan
        face_locations = fr.face_locations(img)

        # kodekan wajah dari input gambar
        unknown_face_encodings = fr.face_encodings(img, face_locations)

        # identifikasi fajah dari input gambar
        face_names = []

        for face_encoding in unknown_face_encodings:
            # bandingkan wajah inputan yang dikodekan degan semua wajah yang dikenali
            matches = fr.compare_faces(faces_encoded, face_encoding)

            # cari wajah yang dikenali dengan kode wajah terdekat dengan wajah yang di input
            face_distances = fr.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)

            # jika wajah yang paling dikenali sesuai dengan wajah yang di input
            # berikan label pada wajah dengan nama yang dikenal dari wajah tersebut
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            else:
                name = "Unknown"

            face_names.append(name)

        # kembalikan nilai wajah pertama dengan input
        return face_names[0]
    except:
        # jika tidak ada wajah yang ditemukan pada input gambar 
        # atau terdapat eror yang dialami, kembalikan nilai false
        return False