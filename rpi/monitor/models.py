from django.db import models

class Temperature(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	temperature = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return str(self.temperature)
