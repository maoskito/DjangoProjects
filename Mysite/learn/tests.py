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
class SilentAssertionError(AssertionError):
    silent_variable_failure = True

class PersonClass3(object):
    
    def first_name(self):
        raise SilentAssertionError, "foo"
    def delete(self):
        print 'delete!'
    delete.alters_data = True

t = Template('''
{% for athlete in athlete_list %}
    <p>{{ athlete }}</p>
    {{forloop.first}}
{% empty %}
    <p>There are no athletes. Only computer programmers.</p>
{% endfor %}
''')


c = { 'athlete_list':['','test_1','test_2','test_3']}
print t.render(Context(c))
