#-*- coding: UTF-8 -*-
##from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime, time
oneday = datetime.date(year=1998,month=10,day=28)
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><b ody>It is now %s.</body></html>" % now
    return HttpResponse(html)

def plus(request, a, b):
    return HttpResponse( int(a)+int(b))

def hello(request):
##    t = get_template('template_1.txt')
    
    c = {'person_name': [u'蒲蒲',u'吴猫 啊 啦啦','markov tiso',oneday],
         'hour_offset':'10',
         'next_time':'9'
         }
    return render_to_response( 'template_1.html', c)

