# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from order_ruangan.models import Ruangan, RuanganTerpinjam, Category

from django.shortcuts import redirect, render


def index_ruangan(request):
    ruangan = Ruangan.objects.all().order_by('-created_on')
    context = {
        "ruangan": ruangan,
    }
    return render(request, "index_ruangan.html", context)


def ruangan_terpinjam(request):
    ruangan_terpinjam = RuanganTerpinjam.objects.all().order_by('-created_on')
    context = {
        "ruangan_terpinjam": ruangan_terpinjam,
    }
    return render(request, "index_ruangan_terpinjam.html", context)


def category_ruangan(request, category):
    ruangan = Ruangan.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "ruangan": ruangan
    }
    return render(request, "category_ruangan.html", context)


def detail_ruangan(request, pk):
    ruangan = Ruangan.objects.get(pk=pk)
    context = {
        'ruangan': ruangan
    }
    return render(request, 'detail_ruangan.html', context)


def order_ruangan(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            author=request.user.username,
            body=form.cleaned_data["body"],
            post=post
        )
        comment.save()
        redirect("index_ruangan")
    context = {
        'form': form
    }
    return render(request, "order_ruangan.html", context)
