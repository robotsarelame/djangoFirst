from django.conf.urls import patterns, url

urlpatterns = patterns('phonebook.views',
	url(r'^$', 'list'),
	url(r'^person/(?P<person_id>\d+)/$', 'detail'),
	url(r'^person/new', 'new'),
	url(r'^person/add', 'add'),
	url(r'^person/edit/(?P<person_id>\d+)/$', 'edit'),
	url(r'^person/edit/update/(?P<person_id>\d+)/$', 'update'),
	url(r'^person/delete/(?P<person_id>\d+)/$', 'delete'),
)
