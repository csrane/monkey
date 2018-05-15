#do.views.py
from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    #nunbers = "1/2/213/214/315/425"
    result = sum(map(lambda s : int(s or 0) , numbers.split('/')))
    return HttpResponse(result)
 