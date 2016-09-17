from django import forms

from .models import Vaccine

class VaccineForm(forms.ModelForm):
	class Meta:
		model = Vaccine
		fields = ['vaccine_select']
		labels = {'vaccine_select': ''}