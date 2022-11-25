import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from application.models import Pengunjung, Kunjungan


def index(request):
	start_date = None
	end_date = None
	if 'dari' in request.POST and 'ke' in request.POST:
		start_date = request.POST['dari']
		end_date = request.POST['ke']
		data = Kunjungan.objects.filter(waktu_kunjungan__range=(start_date, end_date))
	else:
		data = Kunjungan.objects.all()
	
	return render(request, 'admin/kunjungan.html', {
		'kunjungan': data,
		'dari': start_date,
		'ke': end_date
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