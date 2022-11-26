import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from application.models import Pengunjung, Kunjungan

def index(request):

	data_pengunjung = Pengunjung.objects.all()
	return render(request, 'admin/pengunjung.html', {'pengunjung': data_pengunjung})

def tambah(request):
	data = None
	if request.method == 'POST':
		q = Pengunjung.objects.create(
				nama_pengunjung = request.POST['nama'],
				instansi_pengunjung = request.POST['instansi'],
				jabatan_pengunjung = request.POST['jabatan'],
				nik = request.POST['no_ktp'],
				rfid = request.POST['kode_rfid'],
				keterangan_pengunjung = request.POST['keterangan'],
				sysinsert = datetime.datetime.now()
			)
		q.save

		p_data = Pengunjung.objects.filter(rfid = request.POST['kode_rfid']).values()[0]

		k = Kunjungan.objects.create(
				id_pengunjung = p_data['id'],
				nama_pengunjung = request.POST['nama'],
				instansi_pengunjung = request.POST['instansi'],
				id_ruang = 1,
				ruang = 'ruang 1',
				waktu_kunjungan = datetime.datetime.now(),
				keterangan_kunjungan = request.POST['keterangan'],
				sysinsert = datetime.datetime.now()
			)
		k.save

		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def data_pengunjung(request):
	data = Pengunjung.objects.filter(id = request.POST['id']).values()[0]
	data = json.dumps(data, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")

def edit(request):
	data = None
	if request.method == 'POST':
		Pengunjung.objects.filter(id = request.POST['id']).update(
				nama_pengunjung = request.POST['nama'],
				instansi_pengunjung = request.POST['instansi'],
				jabatan_pengunjung = request.POST['jabatan'],
				nik = request.POST['no_ktp'],
				rfid = request.POST['kode_rfid'],
				keterangan_pengunjung = request.POST['keterangan'],
				sysupdate = datetime.datetime.now()
			)
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def delete(request):
	data = None
	if request.method == 'POST':
		q_del = Pengunjung.objects.get(id = request.POST['id'])
		q_del.delete()
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")
