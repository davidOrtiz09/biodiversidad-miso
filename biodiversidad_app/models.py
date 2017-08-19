# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Comment(models.Model):
    email= models.CharField(max_length=150)
    comment = models.CharField(max_length=1000, blank=True)

