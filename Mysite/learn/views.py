from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><b ody>It is now %s.</body></html>" % now
    return HttpResponse(html)

def plus(request, a, b):
    return HttpResponse( int(a)+int(b))

def file_download(request):
    filename_01 = r'E:\MyCode\DjangoProjects\Mysite\test\test_file_01.txt'
    f = open(filename_01)
    data = f.read()
    f.close()

    filename_02 = r'E:\MyCode\DjangoProjects\Mysite\test\test_file_02.txt'
    f_02 = open(filename_02)
    data_02 = f_02.read()
    f_02.close()
##    response = HttpResponse(data,content_type='application/octet-stream')
    response = HttpResponse(data,content_type='application/vnd.ms-txt')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename_01
    
    response_02 = HttpResponse(data_02,content_type='application/vnd.ms-txt')
    response_02['Content-Disposition'] = 'attachment; filename=%s' % filename_02
    return response_02

def download_list():
    pass

