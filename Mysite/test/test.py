# -*- coding:UTF-8 -*-

import sqlite3
import MySQLdb

import urllib
from django.conf import settings
from django import template

t = template.Template('My name is {{ name }}.')
##c = template.Context({'name': 'Adrian'})
##print t.render(c)
##
##c = template.Context({'name': 'Fred'})
##print t.render(c)

