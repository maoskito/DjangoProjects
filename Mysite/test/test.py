# -*- coding:UTF-8 -*-

import sqlite3
import MySQLdb

import urllib

urllib.urlretrieve(#r'http://web.topfreeweb.net:8000/index.php/downapp/localdown?aid=34',
                    r'http://192.168.171.217:8000/learn/download/file_download',
                   r'E:\MyCode\DjangoProjects\Mysite\learn\aaa.txt'
                   )

print"END"
