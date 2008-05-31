from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^admin/', include('django.contrib.admin.urls')),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Sites/lbb/site_media/'}),
	(r'^$', 'book.views.index'),
	(r'^test/$', 'book.views.test'),
)
