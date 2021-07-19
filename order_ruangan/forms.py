from django import forms
from .models import Ruangan, RuanganTerpinjam


# creating a form
class RuanganForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Ruangan

        # specify fields to be used
        fields = [
            "name",
            "alias",
            "description",
            "image",
            "available",
            "categories"
        ]


class OrderRuanganForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = RuanganTerpinjam

        # specify fields to be used
        fields = [
            "ruangan",
            "user",
            "tanggal_pinjam",
            "tanggal_selesai",
        ]
