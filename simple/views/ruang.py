import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from application.models import Ruang

def index(request):
	msg = None
	if 'tambah' in request.POST:

		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)

		q = Ruang.objects.create(
				nama_ruang = request.POST['nama_ruang'],
				kapasitas = request.POST['kapasitas'],
				id_alat = '1',
				nama_alat = '1',
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

		q = Ruang.objects.filter(id = request.POST['edit']).update(
				nama_ruang = request.POST['nama_ruang'],
				kapasitas = request.POST['kapasitas'],
				id_alat = '1',
				nama_alat = '1',
				isaktif = request.POST['status']
			)
		msg = 'success'

	data = Ruang.objects.all()
	return render(request, 'admin/ruang.html', {'ruang': data, 'msg': msg})

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