import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.files.storage import FileSystemStorage

from application.models import Pengguna, Grup

def index(request):

	msg = None
	if 'tambah' in request.POST:

		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)

		group = Grup.objects.filter(id = request.POST['group']).values()[0]
		q = Pengguna.objects.create(
				nama_pengguna = request.POST['nama'],
				username = request.POST['username'],
				password = request.POST['password'],
				email = request.POST['email'],
				no_telp = request.POST['no_telp'],
				id_group = group['id'],
				nama_group = group['nama_group'],
				foto = filename,
				isaktif = request.POST['status'],
				syscreate = datetime.datetime.now()
			)

		q.save
		msg = 'success'

	if 'edit' in request.POST:

		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			f = Pengguna.objects.filter(id = request.POST['edit']).update(foto = filename)

		if len(request.POST['password']) != 0:
			p = Pengguna.objects.filter(id = request.POST['edit']).update(password = request.POST['password'])

		group = Grup.objects.filter(id = request.POST['group']).values()[0]
		q = Pengguna.objects.filter(id = request.POST['edit']).update(
				nama_pengguna = request.POST['nama'],
				username = request.POST['username'],
				password = request.POST['password'],
				email = request.POST['email'],
				no_telp = request.POST['no_telp'],
				id_group = group['id'],
				nama_group = group['nama_group'],
				isaktif = request.POST['status'],
				sysupdate = datetime.datetime.now()
			)

		msg = 'success'

	data = Pengguna.objects.all()
	grup = 	Grup.objects.filter(isaktif='Aktif').values()
	return render(request, 'admin/user.html', {'user': data, 'grup':grup, 'msg': msg})

def detail(request):
	data = Pengguna.objects.filter(id = request.POST['id']).values()[0]
	data = json.dumps(data, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")

def delete(request):
	data = None
	if request.method == 'POST':
		q_del = Pengguna.objects.get(id = request.POST['id'])
		q_del.delete()
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def detail_login(request):
	if 'id' in request.session:
		cs = Pengguna.objects.filter(id = request.session['id']).values()[0]
		data = json.dumps(cs, indent=4, sort_keys=True, default=str)
	else:
		data = '{"msg":"faild"}';

	return HttpResponse(data, content_type="text/json-comment-filtered")