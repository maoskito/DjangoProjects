#-*- coding: UTF-8 -*-
##from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><b ody>It is now %s.</body></html>" % now
    return HttpResponse(html)

def plus(request, a, b):
    return HttpResponse( int(a)+int(b))

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
    t = Template(rst)
    c = Context({'person_name': u'蒲蒲'})
    
    return HttpResponse(t.render(c))
