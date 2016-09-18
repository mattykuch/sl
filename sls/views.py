from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Vaccine, Entry
from .forms import VaccineForm, EntryForm

def index(request):
	"""The homepage for stocklog(sl)"""
	return render(request, 'sls/index.html')

@login_required(login_url='/users/login/')
def vaccines(request):
	"""Show all vaccines."""
	vaccines = Vaccine.objects.filter(owner=request.user).order_by('date_added')
	context = {'vaccines': vaccines}
	return render(request, 'sls/vaccines.html', context)

@login_required(login_url='/users/login/')
def vaccine(request, vaccine_id):
	"""Show a single vaccine and all its entries."""
	vaccine = Vaccine.objects.get(id=vaccine_id)
	# Make sure the vaccine belongs to the current user
	if vaccine.owner != request.user:
		raise Http404

	entries = vaccine.entry_set.order_by('id')
	context = { 'vaccine': vaccine, 'entries': entries}
	return render(request, 'sls/vaccine.html', context)

@login_required(login_url='/users/login/')
def new_vaccine(request):
	"""Add a new vaccine."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = VaccineForm()
	else:
		# POST data submitted; process data.
		form = VaccineForm(request.POST)
		if form.is_valid():
			new_vaccine = form.save(commit=False)
			new_vaccine.owner = request.user
			new_vaccine.save()
			return HttpResponseRedirect(reverse('sls:vaccines'))

	context = {'form': form}
	return render(request, 'sls/new_vaccine.html', context)

@login_required(login_url='/users/login/')
def new_entry(request, vaccine_id):
	""" Add a new entry for a particular vaccine."""
	vaccine = Vaccine.objects.get(id=vaccine_id)

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = EntryForm()

	else:
		# POST data submitted; process data.
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.vaccine = vaccine
			new_entry.save()
			return HttpResponseRedirect(reverse('sls:vaccine', args=[vaccine_id]))

	context = {'vaccine': vaccine, 'form': form}
	return render(request, 'sls/new_entry.html', context)

@login_required(login_url='/users/login/')
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id=entry_id)
	vaccine = entry.vaccine
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry
		form = EntryForm(instance=entry)
	else:
		# POST data submitted;process data.
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('sls:vaccine', args=[vaccine.id]))
	context = {'entry': entry, 'vaccine': vaccine, 'form': form}
	return render(request, 'sls/edit_entry.html', context)