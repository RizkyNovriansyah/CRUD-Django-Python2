from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Weather (models.Model):
    ext_id = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    lar = models.CharField(max_length=100)
    weather_state = models.CharField(max_length=100)

    # def __unicode__(self):
    #     return self.nama

class Divisi (models.Model):
    nama = models.CharField(max_length=100)
    keterangan =models.TextField(blank=True)

    # def __unicode__(self):
    #     return self.nama

class Jabatan (models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True)

    # def __unicode__(self):
    #     return self.nama

class Karyawan (models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('pria', 'Pria'),
        ('wanita', 'Wanita'),
    )

    JENIS_KARYAWAN_CHOICES = (
        ('magang', 'Magang'),
        ('kontrak', 'Kontrak'),
        ('tetap', 'Tetap'),
    )

    nama = models.CharField(max_length=100)
    alamat = models.TextField(blank=True)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)
    jenis_karyawan = models.CharField(max_length=10, choices=JENIS_KARYAWAN_CHOICES)
    no_telepon = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    no_rekening = models.CharField(max_length=100)
    pemilik_rekening = models.CharField(max_length=100)
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE,)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE,)

    # def __unicode__(self):
    #     return self.nama

class Akun (models.Model):
    JENIS_AKUN_CHOICES = (
        ('karyawan', 'Karyawan'),
        ('admin', 'Administrator'),
    )

    akun = models.ForeignKey(User, on_delete=models.CASCADE,)
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE,)
    jenis_akun = models.CharField(max_length=20, choices=JENIS_AKUN_CHOICES)

    # def __unicode__(self):
    #     return self.karyawan.nama
