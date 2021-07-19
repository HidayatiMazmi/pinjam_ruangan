# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from order_ruangan.models import Ruangan, RuanganTerpinjam, Category


class RuanganAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'description', 'image', 'available')


class RuanganTerpinjamAdmin(admin.ModelAdmin):
    list_display = ()


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ruangan, RuanganAdmin)
admin.site.register(RuanganTerpinjam, RuanganTerpinjamAdmin)
admin.site.register(Category, CategoryAdmin)
