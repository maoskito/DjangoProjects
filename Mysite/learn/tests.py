import django
from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
##settings.configure()
django.setup()
#======================
from django import template
from django.template import Template
from django.template import Context

##t = Template('{% notatag %}')
raw_template = """<p>Dear {{ person_name.1 }},</p>
...
... <p>Thanks for placing an order from {{ company }}. It's scheduled to
... ship on {{ ship_date|date:"F j, Y" }}.</p>
...
... {% if ordered_warranty %}
... <p>Your warranty information will be included in the packaging.</p>
... {% else %}
... <p>You didn't order a warranty, so you're on your own when
... the products inevitably stop working.</p>
... {% endif %}
...
... <p>Sincerely,<br />{{ company }}</p>"""
t = Template(raw_template)
import datetime
c = Context({'person_name': 'John Smith',
             'company': 'Outdoor Equipment',
             'ship_date': datetime.date(2009, 4, 2),
             'ordered_warranty': False})
c_x = Context( {'person_name': ['Markov','Bano','Maoskito']
    })
print t.render(c)
print t.render(c_x)
