from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Mahasiswa(models.Model):
   class Gender(models.TextChoices):
      COWOK = "LK", _("Laki-Laki")
      CEWEK = "PR", _("Perempuan")

   nama = models.CharField(max_length=100)
   nim = models.CharField(max_length=15)
   alamat = models.TextField()
   foto_mhs = models.ImageField(upload_to='ProfileMahasiswa')
   jenis_kelamin = models.CharField(
      max_length=2, choices=Gender.choices
      )
   jurusan = models.CharField(max_length=50)
   email = models.EmailField()

   def __str__(self):
      return "{} ({})".format(self.nama,self.nim)