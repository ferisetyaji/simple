import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from application.models import Pengunjung, Kunjungan, Ruang


def index(request):
	start_date = None
	end_date = None
	s_ruang = None

	data = Kunjungan.objects.all()

	if 'cari' in request.POST:
		start_date = request.POST['dari']
		end_date = request.POST['ke']

		if start_date != '' and end_date != '':
			if len(request.POST['ruang']) != 0:
				s_ruang = request.POST['ruang']
				data = Kunjungan.objects.filter(waktu_kunjungan__range=(start_date, end_date), id_ruang=s_ruang)
			else:
				data = Kunjungan.objects.filter(waktu_kunjungan__range=(start_date, end_date))
		else:
			if len(request.POST['ruang']) != 0:
				s_ruang = request.POST['ruang']
				data = Kunjungan.objects.filter(id_ruang=s_ruang)

		

	ruang = Ruang.objects.all()

	return render(request, 'admin/kunjungan.html', {
		'kunjungan': data,
		'dari': start_date,
		'ke': end_date,
		'ruang': ruang,
		's_ruang': s_ruang
		})

def detail(request):
	_kunjungan = Kunjungan.objects.filter(id = request.POST['id']).values()[0]
	_pengunjung = Pengunjung.objects.filter(id = _kunjungan['id_pengunjung']).values()[0]

	data = {
		'kunjungan': _kunjungan,
		'pengunjung': _pengunjung
	}

	data = json.dumps(data, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")

def delete(request):
	data = None
	if request.method == 'POST':
		q_del = Kunjungan.objects.get(id = request.POST['id'])
		q_del.delete()
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")