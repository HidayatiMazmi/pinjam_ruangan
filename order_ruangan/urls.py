from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_ruangan, name="index_ruangan"),
    url(r'^(?P<id>[0-9]+)$', views.detail_ruangan, name="detail_ruangan"),
    url(r'^<category>/$', views.category_ruangan, name="category_ruangan"),
    url(r'^<ruangan_terpinjam>/$', views.ruangan_terpinjam, name="ruangan_terpinjam"),
    url(r'^<order>/$', views.order_ruangan, name="order_ruangan"),
]
