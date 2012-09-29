from django.conf.urls import patterns, url

urlpatterns = patterns('polls.views',
	url(r'^$', 'index'),
	url(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
	url(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
	url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
)
