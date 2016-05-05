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

def hello(request):
    rst = '''
<html>
<head><title>Ordering notice</title></head>

<body>

<h1>Ordering notice</h1>

<p>Dear {{ person_name }},</p>

<p>Thanks for placing an order from {{ company }}. It's scheduled to
ship on {{ ship_date|date:"F j, Y" }}.</p>

<p>Here are the items you've ordered:</p>

<ul>
{% for item in item_list %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

{% if ordered_warranty %}
    <p>Your warranty information will be included in the packaging.</p>
{% else %}
    <p>You didn't order a warranty, so you're on your own when
    the products inevitably stop working.</p>
{% endif %}

<p>Sincerely,<br />{{ company }}</p>

</body>
</html>
'''
    return HttpResponse(rst)

def view_1(request):
    pass
