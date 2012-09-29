from django.db import models

class Person(models.Model):

	name = models.CharField(max_length = 100)
	phone = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 75)

	def __unicode__(self):
		return self.name