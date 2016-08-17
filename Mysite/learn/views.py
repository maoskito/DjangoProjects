#-*- coding: UTF-8 -*-
##from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

from learn.models import Book

import datetime, time
oneday = datetime.date(year=1998,month=10,day=28)
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

import code
def hello(request):
    meta_list = request.META
    print "=================================="
    for key in meta_list:
        try:
            meta_list[key] = meta_list[key].decode('gbk')
        except AttributeError:
            pass
      
    c = Context({'meta_list':meta_list})
    
    return render_to_response('meta.html',c)

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        query = request.GET['q']
        if query:
            has_query = True
            if len(query) > 5:
                errors.append('查询内容过长')
                return render_to_response('search_form.html', { 'errors':errors})
            books = Book.objects.filter( title__icontains = query)
            return render_to_response('search_results.html', {'books':books, 'query':query})
        else:
            errors.append('未输入查询内容')
            return render_to_response('search_form.html', {'errors':errors})
    else:
        return render_to_response('search_form.html', {'errors':errors})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',
        {'errors': errors})
    
