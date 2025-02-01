from django import forms
from .models import Kullanici  # Kullanici modelini import et
from .models import Part
from django.db import models


class KullaniciKayitForm(forms.ModelForm):
    class Meta:
        model = Kullanici
        fields = ['username', 'password', 'email', 'takim']

    password = forms.CharField(widget=forms.PasswordInput)

class KullaniciGirisForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


#-----------görevler
class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'team', 'airplane']

#-------------------------

