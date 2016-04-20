from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Page_2,{'test':'the page_2'}),
    url(r'^next$', views.index,{'test':'this is test info'}),
    url(r'^add$',views.add,),
    url(r'^hello ', views.hello)

]
