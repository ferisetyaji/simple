import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.files.storage import FileSystemStorage

from application.models import Kepuasan

def index(request):

	msg = None
	if 'tambah' in request.POST:
		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)

		q = Kepuasan.objects.create(
				nama = request.POST['nama_kepuasan'],
				gambar = filename,
				isaktif = request.POST['status']
			)
		print(request.POST['status'])
		q.save
		msg = 'tambah_success'

	if 'edit' in request.POST:
		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			f = Pengguna.objects.filter(id = request.POST['edit']).update(gambar = filename)

		Kepuasan.objects.filter(id = request.POST['edit']).update(
				nama = request.POST['nama_kepuasan'],
				isaktif = request.POST['status']
			)
		msg = 'edit_success'

	data = Kepuasan.objects.all()
	return render(request, 'admin/kepuasan.html', {'kepuasan': data})

def tambah(request):
	data = None
	if request.method == 'POST':

		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)

		q = Kepuasan.objects.create(
				nama = request.POST['nama_kepuasan'],
				gambar = filename,
				isaktif = request.POST['status']
			)
		q.save

		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def detail(request):
	data = Kepuasan.objects.filter(id = request.POST['id']).values()[0]
	data = json.dumps(data, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")

def edit(request):
	data = None
	if request.method == 'POST':

		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			f = Pengguna.objects.filter(id = request.POST['id']).update(gambar = filename)

		Kepuasan.objects.filter(id = request.POST['id']).update(
				nama = request.POST['nama_kepuasan'],
				isaktif = request.POST['status']
			)
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def delete(request):
	data = None
	if request.method == 'POST':
		q_del = Kepuasan.objects.get(id = request.POST['id'])
		q_del.delete()
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")