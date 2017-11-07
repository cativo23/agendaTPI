# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from schedule.models import EventRelation

admin.site.register(EventRelation, admin.ModelAdmin)
