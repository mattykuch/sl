"""Defines URL patterns for sls."""

from django.conf.urls import url

from . import views

urlpatterns = [
	# Home page
	url(r'^$', views.index, name='index'),

	# Show all vaccines
	url(r'^vaccines/$', views.vaccines, name='vaccines'),

	# Detail page for a single vaccine
	url(r'^vaccines/(?P<vaccine_id>\d+)/$', views.vaccine, name='vaccine'),

	# Page for adding a new vaccine
	url(r'^new_vaccine/$', views.new_vaccine, name='new_vaccine'),

	# Page for adding a new entry
	url(r'^new_entry/(?P<vaccine_id>\d+)/$', views.new_entry, name='new_entry'),
]