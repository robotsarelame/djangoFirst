from django.conf.urls import patterns, url

urlpatterns = patterns('phonebook.views',
	url(r'^$', 'list'),
	url(r'^person/(?P<person_id>\d+)/$', 'detail'),
)
