from django.conf.urls import url
from KvitokApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^kvitok/$', views.kvitok_base, name='kvitok_base'),
    url(r'^kvitok/add/$', views.kvitok_add, name='kvitok-add'),
    url(r'^(?P<kvitok_id>\d+)/$', views.kvitok_detail, name='kvitok-detail'),


]
