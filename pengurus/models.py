from django.db import models
from django.contrib.auth.models import User
from mahasiswa.models import Mahasiswa

# models admin
class Pengurus(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    fakultas_pengurus = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile ({self.nama}) Fakultas ({self.fakultas_pengurus})"

# models kehadiran mahasiswa mahasiswa
class Kehadiran(models.Model):
   mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, blank=True, null=True)
   nim = models.CharField(max_length=100, null=True)
   nama = models.CharField(max_length=100, null=True)
   jurusan = models.CharField(max_length=50, null=True)
   foto_hadir = models.ImageField(upload_to="KehadiranMahasiswa")
   lokasi = models.CharField(max_length=255, blank=True, null=True) 
   jam_hadir = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f"{self.nama} ({self.nim})"