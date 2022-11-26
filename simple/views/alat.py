import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from application.models import Alat

def index(request):
	data = Alat.objects.all()
	return render(request, 'admin/alat.html', {'alat': data})

def tambah(request):
	data = None
	if request.method == 'POST':
		q = Alat.objects.create(
				nama_alat = request.POST['nama_alat'],
				isaktif = request.POST['status']
			)
		q.save

		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def detail(request):
	data = Alat.objects.filter(id = request.POST['id']).values()[0]
	data = json.dumps(data, indent=4, sort_keys=True, default=str)
	return HttpResponse(data, content_type="text/json-comment-filtered")

def edit(request):
	data = None
	if request.method == 'POST':
		Alat.objects.filter(id = request.POST['id']).update(
				nama_alat = request.POST['nama_alat'],
				isaktif = request.POST['status']
			)
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")

def delete(request):
	data = None
	if request.method == 'POST':
		q_del = Alat.objects.get(id = request.POST['id'])
		q_del.delete()
		data = '{"respon":"success"}'

	return HttpResponse(data, content_type="text/json-comment-filtered")