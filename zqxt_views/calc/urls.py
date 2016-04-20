from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'just/', views.add, name = 'just'),
]
