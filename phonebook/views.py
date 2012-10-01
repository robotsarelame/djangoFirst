from django.shortcuts import render_to_response, get_object_or_404
from phonebook.models import Person
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

def list(request):
    contact_list = Person.objects.all().order_by('name')
    paginator = Paginator(contact_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('phonebook/contacts_list.html', {"contacts": contacts})
	
def detail(request, person_id):
	p = get_object_or_404(Person, pk=person_id)
	return render_to_response('phonebook/detail.html', {'person': p}, context_instance=RequestContext(request))
	
def new(request):
	return render_to_response('phonebook/contact_add_edit_form.html', {'action': 'add', 'button': 'Add'}, context_instance=RequestContext(request))
	
def add(request):
	person_name = request.POST.get("person_name")
	person_phone = request.POST.get("person_phone")
	person_email = request.POST.get("person_email")
	p = Person(name = person_name, phone = person_phone, email = person_email)
	p.save()
	return HttpResponseRedirect(reverse('phonebook.views.list'))

def edit(request, person_id):
	#p = Person.objects.get(pk=person_id)
	return render_to_response('phonebook/contact_add_edit_form.html', {'action': 'index.html', 'button': 'Update'}, context_instance=RequestContext(request))

def update(request, person_id):
	p = get_object_or_404(Person, pk=person_id)
	p.name = request.POST.get("person_name")
	p.phone = request.POST.get("person_phone")
	p.email = request.POST.get("person_email")
	p.save()
	return HttpResponseRedirect(reverse('phonebook.views.detail', args=(p.id,)))
	
def delete(request, person_id):
	Person.objects.get(pk=person_id).delete()
	return HttpResponseRedirect(reverse('phonebook.views.list'))
