# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from location_field.models.plain import PlainLocationField


class CustomEvent(models.Model):
    lugar = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    class Meta():
        abstract = True
# Create your models here.
