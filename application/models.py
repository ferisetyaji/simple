from django.db import models

class Pengunjung(models.Model):
	nama_pengunjung = models.CharField(max_length=100, default=None, blank=True)
	instansi_pengunjung = models.CharField(max_length=100, default=None, blank=True)
	jabatan_pengunjung = models.CharField(max_length=100, default=None, blank=True)
	nik = models.CharField(max_length=50, default=None, blank=True)
	rfid = models.CharField(max_length=20, default=None, blank=True)
	keterangan_pengunjung = models.TextField(null=True, default=None, blank=True)
	sysinsert = models.DateTimeField(null=True, default=None, blank=True)
	sysupdate = models.DateTimeField(null=True, default=None, blank=True)

class Kunjungan(models.Model):
	id_pengunjung = models.IntegerField(null=True, default=None, blank=True)
	nama_pengunjung = models.CharField(max_length=100, default=None, blank=True)
	instansi_pengunjung = models.CharField(max_length=100, default=None, blank=True)
	id_ruang = models.IntegerField(null=True, default=None, blank=True)
	ruang = models.CharField(max_length=100, default=None, blank=True)
	waktu_kunjungan = models.DateTimeField(null=True, default=None, blank=True)
	keterangan_kunjungan = models.TextField(null=True, default=None, blank=True)
	sysinsert = models.DateTimeField(null=True, default=None, blank=True)

class Ruang(models.Model):
	nama_ruang = models.CharField(max_length=100, default=None, blank=True)
	kapasitas = models.IntegerField(null=True, default=None, blank=True)
	id_alat = models.IntegerField(null=True, default=None, blank=True)
	nama_alat = models.CharField(max_length=100, default=None, blank=True)
	foto = models.CharField(max_length=100, default=None, blank=True)
	isaktif = models.CharField(max_length=10, default=None, blank=True)

class Alat(models.Model):
	nama_alat = models.CharField(max_length=100, default=None, blank=True)
	isaktif = models.CharField(max_length=10, default=None, blank=True)

class Grup(models.Model):
	nama_group = models.CharField(max_length=100, default=None, blank=True)
	isaktif = models.CharField(max_length=10, default=None, blank=True)

class Pengguna(models.Model):
	nama_pengguna = models.CharField(max_length=100, default=None, blank=True)
	username = models.CharField(max_length=100, default=None, blank=True)
	password = models.TextField(null=True, default=None, blank=True)
	email = models.CharField(max_length=100, default=None, blank=True)
	no_telp = models.CharField(max_length=20, default=None, blank=True)
	id_group = models.IntegerField(null=True, default=None, blank=True)
	nama_group = models.CharField(max_length=100, default=None, blank=True)
	foto = models.CharField(max_length=100, default=None, blank=True)
	isaktif = models.CharField(max_length=10, default=None, blank=True)
	syscreate = models.DateTimeField(null=True, default=None, blank=True)
	sysupdate = models.DateTimeField(null=True, default=None, blank=True)