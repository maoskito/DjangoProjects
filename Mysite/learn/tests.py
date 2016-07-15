import os
import django
from django.test import TestCase
from django.conf import settings
import mysite
from learn import myapp_defaults

os.environ.setdefault('DJANGO_SETTINGS_MODULE','learn.myapp_defaults')
django.setup()
#
from learn.models import Publisher

##print Publisher.objects.all()[0]
print Publisher.objects.filter(name__contains='A')


