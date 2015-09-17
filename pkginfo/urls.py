from django.conf.urls import patterns, include, url

urlpatterns = patterns('pkginfo.views',
	url(r'^index/*$', 'index'),
	url(r'^confirm/*$', 'confirm'),
	url(r'^$', 'index'),
	#url(r'^(?P<pkginfo_name>[^/]+)/(?P<item_name>[^/]+)/$', 'test_index'),
	#url(r'^(?P<pkginfo_name>[^/]+)/edit/$', 'edit'),
)