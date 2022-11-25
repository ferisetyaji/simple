# Generated by Django 4.1.2 on 2022-11-24 15:19

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
                ('nama_alat', models.CharField(max_length=100)),
                ('isaktif', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Grup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_group', models.CharField(max_length=100)),
                ('isaktif', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kunjungan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pengunjung', models.IntegerField()),
                ('nama_pengunjung', models.CharField(max_length=100)),
                ('instansi_pengunjung', models.CharField(max_length=100)),
                ('id_ruang', models.IntegerField()),
                ('ruang', models.CharField(max_length=100)),
                ('waktu_kunjungan', models.DateTimeField()),
                ('keterangan_kunjungan', models.TextField()),
                ('sysinsert', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pengguna', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('no_telp', models.CharField(max_length=20)),
                ('id_group', models.IntegerField()),
                ('nama_group', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=100)),
                ('isaktif', models.CharField(max_length=10)),
                ('syscreate', models.DateTimeField()),
                ('sysupdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pengunjung', models.CharField(max_length=100)),
                ('instansi_pengunjung', models.CharField(max_length=100)),
                ('jabatan_pengunjung', models.CharField(max_length=100)),
                ('nik', models.CharField(max_length=50)),
                ('rfid', models.CharField(max_length=20)),
                ('keterangan_pengunjung', models.TextField()),
                ('sysinsert', models.DateTimeField()),
                ('sysupdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ruang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_ruang', models.CharField(max_length=100)),
                ('kapasitas', models.IntegerField()),
                ('id_alat', models.IntegerField()),
                ('nama_alat', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=100)),
                ('isaktif', models.CharField(max_length=10)),
            ],
        ),
    ]