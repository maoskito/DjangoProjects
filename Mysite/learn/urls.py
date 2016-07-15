from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^time/$', views.current_datetime),
##    url(r'^download/file_download$', views.file_download),
    url(r'^hello$', views.hello),
    url(r'^search$', views.search),
    url(r'^contact$', views.contact),
##    url(r'^search$', views.search),
]
