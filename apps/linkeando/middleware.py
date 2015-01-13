# -*- coding: utf-8 *-*

from django.shortcuts import redirect
from random import choice
pais = ['Colombia', 'Peru', 'Panama', 'Mexico']


def de_donde_vengo(request):
    return choice(pais)


class PaisMiddleware():
    def process_request(self, request):
        pais = de_donde_vengo(request)
        if pais == "Mexico":
            return redirect('https://mejorandola.la')
