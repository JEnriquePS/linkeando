# -*- coding: utf-8 *-*

from django import forms
from django.forms import ModelForm
from models import Enlace


class EnlaceForm(ModelForm):
    class Meta:
        model = Enlace
        exclude = ("votos","usuario",)