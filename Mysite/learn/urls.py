from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus(\d{1,3})$', views.time_plus),

]
