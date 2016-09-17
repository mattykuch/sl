from django import forms

from .models import Vaccine, Entry

class VaccineForm(forms.ModelForm):
	class Meta:
		model = Vaccine
		fields = ['vaccine_select']
		labels = {'vaccine_select': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['stock_balance',
				  'stock_order',
				  'stock_adjustment_dvs',
				  'stock_adjustment_nms',	
					]
		labels = {'stock_balance': 'Stock Balance ',
				  'stock_order': 'Stock Order ',
				  'stock_adjustment_dvs':'Stock Adjustment (DVS) ',
				  'stock_adjustment_nms':'Stock Adjustment (NMS) ',	
					}
		widgets = {'stock_balance': forms.NumberInput(),
				  'stock_order': forms.NumberInput(),
				  'stock_adjustment_dvs':forms.NumberInput(),
				  'stock_adjustment_nms':forms.NumberInput(),	
					}