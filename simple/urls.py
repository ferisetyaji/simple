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

from .views import dashboard, pengunjung, kunjungan, ruang, user, group, alat, login, profil, kepuasan, alasan_kunjungan, laporan

urlpatterns = [
    path('', dashboard.index, name='dashboard'),
    path('login', login.index, name='login'),
    path('logout', login.logout, name='logout'),
    path('profil', profil.index, name='profil'),
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
    path('group/tambah', group.tambah, name='group_tambah'),
    path('group/detail', group.detail, name='group_detail'),
    path('group/edit', group.edit, name='group_edit'),
    path('group/delete', group.delete, name='group_delete'),
    path('user', user.index, name='user'),
    path('user/detail_login', user.detail_login, name='detail_login'),
    path('user/detail', user.detail, name='user_detail'),
    path('user/delete', user.delete, name='user_delete'),
    path('alat', alat.index, name='alat'),
    path('alat/tambah', alat.tambah, name='alat_tambah'),
    path('alat/edit', alat.edit, name='alat_edit'),
    path('alat/detail', alat.detail, name='alat_detail'),
    path('alat/delete', alat.delete, name='alat_delete'),
    path('kepuasan', kepuasan.index, name='kepuasan'),
    path('kepuasan/tambah', kepuasan.tambah, name='kepuasan_tambah'),
    path('kepuasan/edit', kepuasan.edit, name='kepuasan_edit'),
    path('kepuasan/detail', kepuasan.detail, name='kepuasan_detail'),
    path('kepuasan/delete', kepuasan.delete, name='kepuasan_delete'),
    path('alasan_kunjungan', alasan_kunjungan.index, name='alasan_kunjungan'),
    path('alasan_kunjungan/detail', alasan_kunjungan.detail, name='alasan_kunjungan_detail'),
    path('alasan_kunjungan/delete', alasan_kunjungan.delete, name='alasan_kunjungan_delete'),
    path('laporan/tahunan', laporan.tahunan, name='laporan_tahunan'),
    path('laporan/bulanan', laporan.bulanan, name='laporan_bulanan'),
    path('laporan/harian', laporan.harian, name='laporan_harian'),
    path('laporan/keterangan_kunjungan', laporan.keterangan_kunjungan, name='keterangan_kunjungan'),
    path('laporan/kepuasan_kunjungan', laporan.kepuasan_kunjungan, name='kepuasan_kunjungan')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)