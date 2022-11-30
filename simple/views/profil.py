import datetime

from django.shortcuts import render, redirect
from django.core import serializers
from django.core.files.storage import FileSystemStorage

from application.models import Pengguna

def index(request):

	if 'save' in request.POST:
		filename = ''

		if 'upload' in request.FILES:
			myfile = request.FILES['upload']
			
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			f = Pengguna.objects.filter(id = request.session['id']).update(foto = filename)

		if len(request.POST['password']) != 0 :
			p = Pengguna.objects.filter(id = request.session['id']).update(password = request.POST['password'])

		q = Pengguna.objects.filter(id = request.session['id']).update(
				nama_pengguna = request.POST['nama_pengguna'],
				username = request.POST['username'],
				email = request.POST['email'],
				no_telp = request.POST['telp'],
				sysupdate = datetime.datetime.now()
			)

		return redirect('profil')

	user = Pengguna.objects.filter(id = request.session['id']).values()[0]
	return render(request, 'admin/profil.html', {'user': user})