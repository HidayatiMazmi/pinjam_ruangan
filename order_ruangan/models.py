# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ruangan(models.Model):

    # fields of the model
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='ruangan')

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name