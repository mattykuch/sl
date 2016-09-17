from django.db import models

class Vaccine(models.Model):
	"""A Vaccine or Device the user is inputing stock data for"""
	MEASLES = 'MEASLES'
	BCG = 'BCG'
	HPV = 'HPV'
	HEPB = 'HEPB'
	TT = 'TT'
	OPV = 'OPV'
	YELLOWFEVER = 'YELLOWFEVER'
	PCV = 'PCV'
	PENTA = 'PENTA'
	IPV = 'IPV'
	ROTA = 'ROTA'
	SYRINGE005 = 'SYRINGE005'
	SYRINGE05 = 'SYRINGE05'
	SYRINGE5 = 'SYRINGE5'
	SYRINGE2 = 'SYRINGE2'
	SB = 'SB'
	TTCARDS = 'TTCARDS'
	CHC = 'CHC'
	VCB = 'VCB'
	VACCINE_CHOICES = (
		(MEASLES, 'Measles vaccine 10 dose Vial'),
		(BCG, 'Bacillus Calmette-Guerin 20 dose Vial'),
		(HPV, 'Human Papilloma Vaccine 1 dose Vial'),
		(HEPB, 'Hepatitis .B Vaccine 10 dose Vial'),
		(TT, 'Tetanus Toxoid Vaccine 20 dose Vial'),
		(OPV, 'Oral Polio Vaccine 20 dose Vial'),
		(YELLOWFEVER, 'Yellow Fever  10 dose Vial'),
		(PCV, 'Pneumococcal Conjugate 2 dose Vial'),
		(PENTA, 'DPT-HIP B-HEB 10 Dose Vial'),
		(IPV, 'Inactivated Polio vaccine 5 dose Vial'),
		(ROTA, 'Rotavirus vaccine 1 dose Vial'),
		(SYRINGE005, 'Syringe 0.05 ml'),
		(SYRINGE05, 'Syringe 0.5 ml'),
		(SYRINGE5, 'Syringe 5 ml'),
		(SYRINGE2, 'Syringe 2 ml'),
		(SB, 'Safety Boxes'),
		(TTCARDS, 'Tetanus Toxoid Cards'),
		(CHC, 'Child Health Cards'),
		(VCB, 'Vaccine Control Books'),
		)
	vaccine_select = models.CharField(max_length=50,
									choices =VACCINE_CHOICES,
									default =MEASLES)
	date_added = models.DateTimeField(auto_now_add=True)
	

	def __unicode__(self):
		"""Return a string representation of the model."""
		return self.vaccine_select
class Entry(models.Model):
	""" Entries of stock data for specific Vaccine or Device"""
	vaccine = models.ForeignKey(Vaccine)
	stock_balance = models.IntegerField()
	stock_order = models.IntegerField()
	stock_adjustment_dvs = models.IntegerField()
	stock_adjustment_nms = models.IntegerField(default =0)


	class Meta:
		verbose_name_plural = 'entries'

	def __unicode__(self):
		"""Return a string representation of the model."""
		return "{0}, {1}, {2}, {3}".format(self.stock_balance, self.stock_order, self.stock_adjustment_dvs, self.stock_adjustment_nms)