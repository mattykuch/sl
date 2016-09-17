from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Vaccine
from .forms import VaccineForm, EntryForm

def index(request):
	"""The homepage for stocklog(sl)"""
	return render(request, 'sls/index.html')

def vaccines(request):
	"""Show all vaccines."""
	vaccines = Vaccine.objects.order_by('date_added')
	context = {'vaccines': vaccines}
	return render(request, 'sls/vaccines.html', context)

def vaccine(request, vaccine_id):
	"""Show a single vaccine and all its entries."""
	vaccine = Vaccine.objects.get(id=vaccine_id)
	entries = vaccine.entry_set.order_by('id')
	context = { 'vaccine': vaccine, 'entries': entries}
	return render(request, 'sls/vaccine.html', context)

def new_vaccine(request):
	"""Add a new vaccine."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = VaccineForm()
	else:
		# POST data submitted; process data.
		form = VaccineForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('sls:vaccines'))

	context = {'form': form}
	return render(request, 'sls/new_vaccine.html', context)

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