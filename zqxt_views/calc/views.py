from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def add(request):
##    a = request.GET['a']
##    b = request.GET['b']
##    c = int(a) + int(b)
##    return HttpResponse(str(c))
    
    return HttpResponse( 'Bingo' )
