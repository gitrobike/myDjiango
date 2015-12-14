# -*- coding: UTF-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404

def hello(request):
    return HttpResponse("Hello, the 1st Djiango!")

def hello1(request,num):
    try:
        num = int(num)
        # return HttpResponse("测试一下汉字吧")
    except ValueError:
        raise Http404()