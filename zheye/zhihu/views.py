from django.shortcuts import render
from django.http import HttpResponse
import datetime, time


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def current_time(request):
    now = datetime.datetime.now()
    html = '谢谢，The time now is %s.' % (now.strftime('%Y-%m-%d %H:%M:%S'))
    return HttpResponse(html)
