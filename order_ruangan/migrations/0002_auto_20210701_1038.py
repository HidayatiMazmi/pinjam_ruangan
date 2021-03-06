# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-01 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_ruangan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuanganTerpinjam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peminjam', models.CharField(max_length=200)),
                ('tanggal_pinjam', models.DateTimeField()),
                ('tanggal_selesai', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='ruangan',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ruangan',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='ruanganterpinjam',
            name='ruangan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ruangan', to='order_ruangan.Ruangan'),
        ),
    ]
