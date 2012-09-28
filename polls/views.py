from django.shortcuts import render_to_response
from django.template import Context, loader
from polls.models import Poll
from django.http import HttpResponse

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	#hardoced view commented out
	#output = ', '.join([p.question for p in latest_poll_list])
	#here goes new 'zen' view using templates
	template = loader.get_template('polls/index.html')
	context = Context({
		'latest_poll_list':latest_poll_list,
	})
	#return HttpResponse(template.render(context))
	#and even simplier below:
	return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
	
def detail(request, poll_id):
	try:
		p = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render_to_response('polls/detail.html', {'poll': p})

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)
	
def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)
	