# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # my_dict = {'insert_me':"Hello I am From view.py!"}
    return render(request,'index.html',{'insert_me':"Hello I am From view.py!"})

# Create your views here.
