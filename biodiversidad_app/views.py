# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from django.shortcuts import render


class Index(View):
    def get(self, request):
        return render(request, 'biodeversidad_app/index.html', {})
