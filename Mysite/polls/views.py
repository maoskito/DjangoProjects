from django.shortcuts import render
#
import inspect, sys
# Create your views here.
from django.http import HttpResponse


def index(request,test):
    return HttpResponse("Hello, world. You're at the polls index."+test)

def Page_2(request,test):
    name = sys._getframe().f_code.co_name
    return HttpResponse(name)

def add( request, test):
    return HttpResponse('nothing')

def hello(request):
    return HttpResponse("this is content for view.hello")
