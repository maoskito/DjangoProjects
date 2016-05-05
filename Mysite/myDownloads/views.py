from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import StreamingHttpResponse
import datetime, os

##def file_download(request, filename):
##    folder = r'E:\MyCode\DjangoProjects\Mysite\test'
##    print '==========>'+filename
##    f = open(os.path.join( folder, filename))
##    data = f.read()
##    f.close()
####    response = HttpResponse(data,content_type='application/octet-stream')
##    response = HttpResponse(data,content_type='application/vnd.ms-txt')
##    response['Content-Disposition'] = 'attachment; filename=%s' % filename
##
##    return response

def file_iterator(file_name, chunk_size=512):
    with open(file_name,'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
def file_download(request, filename):
    folder = r'E:\MyCode\DjangoProjects\Mysite\test'
    print '==========>'+filename
    
##    response = HttpResponse(data,content_type='application/octet-stream')
    response = StreamingHttpResponse(file_iterator(os.path.join( folder, filename)))
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response['Content-Type'] = 'application/octet-stream'
    return response






