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
]