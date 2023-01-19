# Generated by Django 4.1.3 on 2023-01-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_alat', models.CharField(blank=True, default=None, max_length=100)),
                ('isaktif', models.CharField(blank=True, default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Grup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_group', models.CharField(blank=True, default=None, max_length=100)),
                ('isaktif', models.CharField(blank=True, default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kepuasan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('gambar', models.CharField(max_length=100)),
                ('isaktif', models.CharField(blank=True, default=None, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kunjungan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pengunjung', models.IntegerField(blank=True, default=None, null=True)),
                ('nama_pengunjung', models.CharField(blank=True, default=None, max_length=100)),
                ('instansi_pengunjung', models.CharField(blank=True, default=None, max_length=100)),
                ('id_ruang', models.IntegerField(blank=True, default=None, null=True)),
                ('ruang', models.CharField(blank=True, default=None, max_length=100)),
                ('waktu_kunjungan', models.DateTimeField(blank=True, default=None, null=True)),
                ('keterangan_kunjungan', models.TextField(blank=True, default=None, null=True)),
                ('status', models.CharField(blank=True, default=None, max_length=10)),
                ('id_kepuasan', models.IntegerField()),
                ('kepuasan', models.CharField(max_length=100)),
                ('sysinsert', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pengguna', models.CharField(blank=True, default=None, max_length=100)),
                ('username', models.CharField(blank=True, default=None, max_length=100)),
                ('password', models.TextField(blank=True, default=None, null=True)),
                ('email', models.CharField(blank=True, default=None, max_length=100)),
                ('no_telp', models.CharField(blank=True, default=None, max_length=20)),
                ('id_group', models.IntegerField(blank=True, default=None, null=True)),
                ('nama_group', models.CharField(blank=True, default=None, max_length=100)),
                ('foto', models.CharField(blank=True, default=None, max_length=100)),
                ('isaktif', models.CharField(blank=True, default=None, max_length=10)),
                ('syscreate', models.DateTimeField(blank=True, default=None, null=True)),
                ('sysupdate', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pengunjung', models.CharField(blank=True, default=None, max_length=100)),
                ('instansi_pengunjung', models.CharField(blank=True, default=None, max_length=100)),
                ('jabatan_pengunjung', models.CharField(blank=True, default=None, max_length=100)),
                ('nik', models.CharField(blank=True, default=None, max_length=50)),
                ('rfid', models.CharField(blank=True, default=None, max_length=20)),
                ('keterangan_pengunjung', models.TextField(blank=True, default=None, null=True)),
                ('sysinsert', models.DateTimeField(blank=True, default=None, null=True)),
                ('sysupdate', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ruang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_ruang', models.CharField(blank=True, default=None, max_length=100)),
                ('kapasitas', models.IntegerField(blank=True, default=None, null=True)),
                ('id_alat', models.IntegerField(blank=True, default=None, null=True)),
                ('nama_alat', models.CharField(blank=True, default=None, max_length=100)),
                ('foto', models.CharField(blank=True, default=None, max_length=100)),
                ('isaktif', models.CharField(blank=True, default=None, max_length=10)),
            ],
        ),
    ]
