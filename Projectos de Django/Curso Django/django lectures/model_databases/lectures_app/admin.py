# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from lectures_app.models import AccesRecord,Topic,Webpage

# Register your models here.
admin.site.register(AccesRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

