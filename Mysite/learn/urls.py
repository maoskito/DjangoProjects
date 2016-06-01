from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^time/$', views.current_datetime),
    url(r'^(\d{1,3})\+(\d{1,3})$', views.plus),
##    url(r'^download/file_download$', views.file_download),
    url(r'^hello$', views.hello),
]
