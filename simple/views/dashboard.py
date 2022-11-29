import datetime

from django.shortcuts import render, redirect

from application.models import Pengunjung, Ruang, Kunjungan

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

	_kunjungan = []

	data_pengunjung = Pengunjung.objects.all();
	for dp_item in data_pengunjung:

		jml_kp = Kunjungan.objects.filter(id_pengunjung=dp_item['id']).count()
		_kunjungan.append({
				'nama':dp_item['nama_pengunjung'],
				'jml':jml_kp
			})

		tgl = dp_item.sysinsert
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


	data_ruang = Ruang.objects.all()
	_ruang = []
	for dr_item in data_ruang:
		jml_kunjungan_ruang = Kunjungan.filter(id_ruang = dr_item['id']).count()
		sp = ',' if _ruang != [] else ''
		_ruang.append({
				'nama':dr_item['nama_ruang'],
				'jml':jml_kunjungan_ruang,
				'sp':sp
			});


	return render(request, 'admin/dashboard.html', {
			'jan':jan,
			'feb':feb,
			'mar':mar,
			'apr':apr,
			'mei':mei,
			'jun':jun,
			'jul':jul,
			'ags':ags,
			'sep':sep,
			'okt':okt,
			'nov':nov,
			'des':des,
			'ruang':_ruang,
			'kunjungan':_kunjungan
		})