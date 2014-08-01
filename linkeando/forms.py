# -*- coding: utf-8 *-*
__author__ = 'jenriqueps'
from django import forms
from django.forms import ModelForm
from models import *


class EnlaceForm(ModelForm):
    class Meta:
        model = Enlace
        exclude = ("votos","usuario",)