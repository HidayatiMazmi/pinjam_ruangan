# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-03 04:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_ruangan', '0003_auto_20210702_0801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruanganterpinjam',
            name='peminjam',
        ),
    ]