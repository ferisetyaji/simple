import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from application.models import Ruang, Alat

def index(request):
	msg = None
	if 'tambah' in request.POST:

		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)

		alat = Alat.objects.filter(id = request.POST['alat']).values()[0]
		q = Ruang.objects.create(
				nama_ruang = request.POST['nama_ruang'],
				kapasitas = request.POST['kapasitas'],
				id_alat = alat['id'],
				nama_alat = alat['nama_alat'],
				foto = filename,
				isaktif = request.POST['status']
			)

		q.save
		msg = 'success'

	if 'edit' in request.POST:

		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			print(myfile)
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			f = Ruang.objects.filter(id = request.POST['edit']).update(foto = filename)

		alat = Alat.objects.filter(id = request.POST['alat']).values()[0]
		q = Ruang.objects.filter(id = request.POST['edit']).update(
				nama_ruang = request.POST['nama_ruang'],
				kapasitas = request.POST['kapasitas'],
				id_alat = alat['id'],
				nama_alat = alat['nama_alat'],
				isaktif = request.POST['status']
			)
		msg = 'success'

	data = Ruang.objects.all()
	alat = 	Alat.objects.filter(isaktif='Aktif').values()
	return render(request, 'admin/ruang.html', {'ruang': data, 'alat':alat, 'msg': msg})

def detail(request):
	data = Ruang.objects.filter(id = request.POST['id']).values()[0]
	data = json.dumps(data, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")

def delete(request):
	data = None
	if request.method == 'POST':
		q_del = Ruang.objects.get(id = request.POST['id'])
		q_del.delete()
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")