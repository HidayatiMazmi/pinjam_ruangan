# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ruangan(models.Model):

    # fields of the model
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=100,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.FilePathField(path="/img")
    available = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='ruangan')

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name

class RuanganTerpinjam(models.Model):
    ruangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE, related_name='ruangan')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    peminjam = models.CharField(max_length=200)
    tanggal_pinjam = models.DateTimeField()
    tanggal_selesai = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ruangan