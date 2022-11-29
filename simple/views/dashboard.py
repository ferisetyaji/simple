import datetime

from django.shortcuts import render, redirect

from application.models import Pengunjung

def index(request):
	
	jan = 0
	feb = 0
	mar = 0
	apr = 0
	mei = 0
	jun = 0
	jul = 0
	ags = 0
	sep = 0
	okt = 0
	nov = 0
	des = 0

	data = Pengunjung.objects.all();
	for item in data:
		tgl = item.sysinsert
		bulan = tgl.month
		jan += 1 if tgl == 1 else 0
		feb += 1 if tgl == 2 else 0
		mar += 1 if tgl == 3 else 0
		apr += 1 if tgl == 4 else 0
		mei += 1 if tgl == 5 else 0
		jun += 1 if tgl == 6 else 0
		jul += 1 if tgl == 7 else 0
		ags += 1 if tgl == 8 else 0
		sep += 1 if tgl == 9 else 0
		okt += 1 if tgl == 10 else 0
		nov += 1 if tgl == 11 else 0
		des += 1 if tgl == 12 else 0


	return render(request, 'admin/dashboard.html')