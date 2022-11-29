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

	kunjungan = []

	data_pengunjung = Pengunjung.objects.all()
	for dp_item in data_pengunjung:

		jml_kp = Kunjungan.objects.filter(id_pengunjung=dp_item.id).count()
		kunjungan.append({
				'nama':dp_item.nama_pengunjung,
				'nik': dp_item.nik,
				'jabatan': dp_item.jabatan_pengunjung,
				'instansi': dp_item.instansi_pengunjung,
				'jml':jml_kp
			})

		tgl = dp_item.sysinsert
		bulan = tgl.month
		jan += 1 if bulan == 1 else 0
		feb += 1 if bulan == 2 else 0
		mar += 1 if bulan == 3 else 0
		apr += 1 if bulan == 4 else 0
		mei += 1 if bulan == 5 else 0
		jun += 1 if bulan == 6 else 0
		jul += 1 if bulan == 7 else 0
		ags += 1 if bulan == 8 else 0
		sep += 1 if bulan == 9 else 0
		okt += 1 if bulan == 10 else 0
		nov += 1 if bulan == 11 else 0
		des += 1 if bulan == 12 else 0


	data_ruang = Ruang.objects.all()
	ruang = []
	for dr_item in data_ruang:
		jml_kunjungan_ruang = Kunjungan.objects.filter(id_ruang = dr_item.id).count()
		sp = ',' if ruang != [] else ''
		ruang.append({
				'nama':dr_item.nama_ruang,
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
			'ruang':ruang,
			'kunjungan':kunjungan
		})