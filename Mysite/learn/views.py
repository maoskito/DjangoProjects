from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def time_plus(request, a, b):
    return HttpResponse( int(a)+int(b))

def file_download(request):
    filename = r'E:\MyCode\DjangoProjects\Mysite\test\testdownloadfile.txt'
    f = open(filename)
    data = f.read()
    f.close()

##    response = HttpResponse(data,content_type='application/octet-stream')
    response = HttpResponse(data,content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

