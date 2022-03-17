from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def p1(request):
    return HttpResponse('This is my first project')

def p2(request):
    return HttpResponse('This is my second project')

