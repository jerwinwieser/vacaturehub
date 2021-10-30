from django.db import models


class Vacancy(models.Model):
	title = models.CharField(max_length=30)
	body = models.CharField(max_length=1000)

	def __str__(self):
		return self.title
