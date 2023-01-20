import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from application.models import Pengunjung, Kunjungan, Ruang, Kepuasan

def unique(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    data = []
    for x in unique_list:
        data.append(x)

    return data

def tahunan(request):
	tahun = []
	select_tahun = None

	data = Kunjungan.objects.all()

	for item in data:
		tahun_item = item.waktu_kunjungan
		tahun.append(tahun_item.year)

	if 'cari' in request.POST:
		select_tahun = request.POST['tahun']
		data = Kunjungan.objects.filter(waktu_kunjungan__startswith=(request.POST['tahun']))

	tahun = unique(tahun)

	return render(request, 'admin/laporan.html', {
		'kunjungan': data,
		'tahun' : tahun,
		'select_tahun': select_tahun
		})

def bulanan(request):
	tahun = []
	bulan = []
	select_tahun = None
	select_bulan = None

	data = Kunjungan.objects.all()

	for item in data:
		print(item.waktu_kunjungan)
		tahun_item = item.waktu_kunjungan
		tahun.append(tahun_item.year)
		data_bulan = {
			'nama':tahun_item.strftime("%b"),
			'bulan':tahun_item.strftime("%m")
		}
		bulan.append(data_bulan)
		#bulan.append(tahun_item.strftime("%m"))

	if 'cari' in request.POST:
		select_tahun = request.POST['tahun']
		select_bulan =  request.POST['bulan']
		print(select_bulan+'. '+select_tahun)
		if len(select_tahun) != 0 and len(select_bulan) != 0:
			data = Kunjungan.objects.filter(waktu_kunjungan__contains=(select_tahun+'-'+select_bulan))
		else:
			if len(select_tahun) != 0:
				data = Kunjungan.objects.filter(waktu_kunjungan__startswith=(request.POST['tahun']))
			if len(select_bulan) != 0:
				data = Kunjungan.objects.filter(waktu_kunjungan__startswith=(request.POST['bulan']))

	tahun = unique(tahun)
	bulan = unique(bulan)

	return render(request, 'admin/laporan_bulanan.html', {
		'kunjungan': data,
		'tahun' : tahun,
		'bulan' : bulan,
		'select_tahun' : select_tahun,
		'select_bulan' : select_bulan
		})

def harian(request):
	data = Kunjungan.objects.all()

	start_date = None
	end_date = None

	if 'cari' in request.POST:
		start_date = request.POST['dari']
		end_date = request.POST['ke']
		if start_date != '' and end_date != '':
			data = Kunjungan.objects.filter(waktu_kunjungan__range=(start_date, end_date))

	return render(request, 'admin/laporan_harian.html', {
		'kunjungan': data,
		'dari': start_date,
		'ke': end_date,
		})

def keterangan_kunjungan(request):
	ket = []
	select_ket = None
	start_date = None
	end_date = None

	data = Kunjungan.objects.all()

	for item in data:
		ket.append(item.keterangan_kunjungan)

	if 'cari' in request.POST:
		start_date = request.POST['dari']
		end_date = request.POST['ke']
		select_ket = request.POST['ket']

		if start_date != '' and end_date != '':
			if select_ket != '':
				data = Kunjungan.objects.filter(waktu_kunjungan__range=(start_date, end_date), keterangan_kunjungan__startswith=(request.POST['ket']))
			else:
				data = Kunjungan.objects.filter(waktu_kunjungan__range=(start_date, end_date))
		else:
			if request.POST['ket'] != '':
				select_ket = request.POST['ket']
				data = Kunjungan.objects.filter(keterangan_kunjungan__startswith=(request.POST['ket']))

	ket = unique(ket)

	return render(request, 'admin/laporan_keterangan.html', {
		'kunjungan': data,
		'ket' : ket,
		'dari': start_date,
		'ke': end_date,
		'select_ket' : select_ket
		})

def kepuasan_kunjungan(request):
	ket = []
	select_kep = None
	start_date = None
	end_date = None

	data = Kunjungan.objects.all()

	for item in data:
		ket.append(item.kepuasan)

	if 'cari' in request.POST:
		start_date = request.POST['dari']
		end_date = request.POST['ke']
		select_kep = request.POST['kep']

		if start_date != '' and end_date != '':
			if request.POST['kep'] != '':
				data = Kunjungan.objects.filter(waktu_kunjungan__range=(start_date, end_date), kepuasan__startswith=(request.POST['kep']))
			else:
				data = Kunjungan.objects.filter(waktu_kunjungan__range=(start_date, end_date))
		else:
			if request.POST['kep'] != '':
				data = Kunjungan.objects.filter(kepuasan__startswith=(request.POST['kep']))

	ket = unique(ket)

	return render(request, 'admin/laporan_kepuasan.html', {
		'kunjungan': data,
		'ket' : ket,
		'dari': start_date,
		'ke': end_date,
		'select_ket' : select_kep
		})
