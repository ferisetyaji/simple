from django.shortcuts import render, redirect
from application.models import Pengguna

def index(request):

	msg = ''
	if request.method == 'POST':
		user = Pengguna.objects.filter(username=request.POST['username'], password=request.POST['password']).values()

		if user:
			request.session['id'] = user[0]['id']

			return redirect('dashboard')
		else:
			msg = 'alert("Username atau password salah)'

	
	return render(request, 'admin/login.html')

def logout(request):
	del request.session['id']
	return redirect('login')