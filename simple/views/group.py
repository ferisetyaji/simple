import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from application.models import Grup

def index(request):
	data = Grup.objects.all()
	return render(request, 'admin/group.html', {'group': data})

def tambah(request):
	data = None
	if request.method == 'POST':
		q = Grup.objects.create(
				nama_group = request.POST['nama_group'],
				isaktif = request.POST['status']
			)
		q.save

		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def detail(request):
	data = Grup.objects.filter(id = request.POST['id']).values()[0]
	data = json.dumps(data, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")

def edit(request):
	data = None
	if request.method == 'POST':
		Grup.objects.filter(id = request.POST['id']).update(
				nama_group = request.POST['nama_group'],
				isaktif = request.POST['status']
			)
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def delete(request):
	data = None
	if request.method == 'POST':
		q_del = Grup.objects.get(id = request.POST['id'])
		q_del.delete()
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")