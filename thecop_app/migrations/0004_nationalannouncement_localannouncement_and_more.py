# Generated by Django 4.1.7 on 2023-06-09 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thecop_app', '0003_alter_member_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='NationalAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brief', models.TextField()),
                ('cover', models.ImageField(upload_to='national/announcements')),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thecop_app.nation')),
            ],
        ),
        migrations.CreateModel(
            name='LocalAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brief', models.TextField()),
                ('cover', models.ImageField(upload_to='local/announcements')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thecop_app.localassembly')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brief', models.TextField()),
                ('cover', models.ImageField(upload_to='district/announcements')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thecop_app.district')),
            ],
        ),
        migrations.CreateModel(
            name='AreaAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brief', models.TextField()),
                ('cover', models.ImageField(upload_to='area/announcements')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thecop_app.area')),
            ],
        ),
    ]
