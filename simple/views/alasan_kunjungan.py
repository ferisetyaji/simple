import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.files.storage import FileSystemStorage

from application.models import Alasan_kunjungan

def index(request):

	msg = None
	if 'tambah' in request.POST:

		q = Alasan_kunjungan.objects.create(
				nama_alasan = request.POST['nama_alasan'],
				isaktif = request.POST['status']
			)

		q.save
		msg = 'tambah_success'

	if 'edit' in request.POST:

		Alasan_kunjungan.objects.filter(id = request.POST['edit']).update(
				nama_alasan = request.POST['nama_alasan'],
				isaktif = request.POST['status']
			)
		msg = 'edit_success'

	data = Alasan_kunjungan.objects.all()
	return render(request, 'admin/alasan_kunjungan.html', {'alasan_kunjungan': data})

def detail(request):
	data = Alasan_kunjungan.objects.filter(id = request.POST['id']).values()[0]
	data = json.dumps(data, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")

def delete(request):
	data = None
	if request.method == 'POST':
		q_del = Alasan_kunjungan.objects.get(id = request.POST['id'])
		q_del.delete()
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")