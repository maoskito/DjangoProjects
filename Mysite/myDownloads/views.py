from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import StreamingHttpResponse
import datetime, os

def file_iterator(file_name, chunk_size=512):
    with open(file_name,'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
def file_download(request, filename):
    print "#######begin to download"
    folder = r'E:\MyCode\DjangoProjects\Mysite\test'
    print '==========>'+request.META['REMOTE_ADDR']
    
##    response = HttpResponse(data,content_type='application/octet-stream')
    response = StreamingHttpResponse(file_iterator(os.path.join( folder, filename)))
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response['Content-Type'] = 'application/octet-stream'
    print "#######end to download"
    return response






