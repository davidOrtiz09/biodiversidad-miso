# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return JsonResponse({'status': 'ok'})
