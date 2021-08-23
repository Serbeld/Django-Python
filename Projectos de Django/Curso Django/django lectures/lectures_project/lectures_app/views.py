# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    my_dict = {'insert_content':"Hello I'm from Lectures App"}
    return render(request,'lectures_app/index.html',context=my_dict)