#simeple urls for my social network app-- KD

from django.conf.urls import patterns
from django.conf.urls import url
from snet import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), # change this to login page
    
    #/snet/USERNAME/wall/
    url(r'^(?P<user_name>\w+)/wall$', views.profile, name='profile'),
    
    url(r'^login', views.userlogin, name = 'userlogin'),
    
    url(r'^(?P<user_name>\w+)/list/$', views.upload_file, name='list'),
    
    url(r'^(?P<user_name>\w+)/update/(?P<photo_id>\d+)$',
    	views.photo_update, name='photo_update'),
    
    #url(r'^(?P<user_name>\w+)/search/(?P<search_str>\w+)',
    url(r'^(?P<user_name>\w+)/search/(?P<search_str>.+)',
    	views.search_index, name='search_index'),
    
    url(r'^(?P<user_name>\w+)/(?P<post_pk>\d+)/(?P<box_id>\d+)',
    	views.subpost, name='subpost'),
    
    url(r'^facelogin', views.facelogin, name='facelogin'),
    
    #url(r'^faceregister/(?P<f_id>\d+)/', 
    #	views.faceregister, name='faceregister'),
)
