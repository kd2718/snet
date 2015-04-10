from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from snet import views
from snet.views import AdditionalPermissionsRedirect
from snet.views import AssociateCallback


urlpatterns = patterns('',
	url(r'^accounts/callback/(?P<provider>(\w|-)+)/', AssociateCallback.as_view(), name='allaccess-callback'),
	
	url(r'^accounts/login/(?P<provider>(\w|-)+)/$', AdditionalPermissionsRedirect.as_view(), 
		    name='allaccess-login'),

    url(r'^accounts/', include('allaccess.urls')),

    url(r'^snet/', include('snet.urls', namespace='snet')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.userlogin, name='userlogin')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
