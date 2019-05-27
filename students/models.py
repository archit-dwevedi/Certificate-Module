from django.db import models

# Create your models here.


class student(models.Model):
	name=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	branch=models.CharField(max_length=250)
	sent=models.BooleanField(default=False)


	def __str__(self):
		return self.name
