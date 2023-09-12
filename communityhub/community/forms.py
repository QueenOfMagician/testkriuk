from django import forms
from .models import PesanGrup

class PesanGrupForm(forms.ModelForm):
    class Meta:
        model = PesanGrup
        fields = ["text_pesan"]