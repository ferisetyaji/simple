"""simple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from .views import dashboard, pengunjung, kunjungan, ruang, user, group, alat

urlpatterns = [
    path('', dashboard.index, name='dashboard'),
    path('pengunjung', pengunjung.index, name='pengunjung'),
    path('pengunjung/tambah', pengunjung.tambah, name='pengunjung_tambah'),
    path('pengunjung/data_pengunjung', pengunjung.data_pengunjung, name='data_pengunjung'),
    path('pengunjung/edit', pengunjung.edit, name='pengunjung_edit'),
    path('pengunjung/delete', pengunjung.delete, name='pengunjung_delete'),
    path('kunjungan', kunjungan.index, name='kunjungan'),
    path('kunjungan/detail', kunjungan.detail, name='kunjungan_detail'),
    path('kunjungan/delete', kunjungan.delete, name='kunjungan_delete'),
    path('ruang', ruang.index, name='ruang'),
    path('ruang/detail', ruang.detail, name='ruang_detail'),
    path('ruang/delete', ruang.delete, name='ruang_delete'),
    path('user', user.index, name='user'),
    path('group', group.index, name='group'),
    path('user', user.index, name='user'),
    path('alat', alat.index, name='alat'),
    path('alat/edit', alat.edit, name='alat_edit'),
    path('alat/detail', alat.detail, name='alat_detail'),
    path('alat/delete', alat.delete, name='alat_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)