from django.shortcuts import render

from .models import Vaccine

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