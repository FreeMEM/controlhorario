from django.conf import settings
from django.utils import timezone 
# from django.contrib.auth import get_user_model

from django.db import models

# Create your models here.


class Company(models.Model):
	name = models.CharField(max_length=200,unique=True)
	user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING )

	def __str__(self):
		cadena= "{0} - administrador: {1}"
		return cadena.format(self.name, self.user)

class Employee(models.Model):
	name = models.CharField(max_length=200)
	company = models.ForeignKey('Company', on_delete=models.DO_NOTHING, blank=False, null=False)
	email = models.EmailField(max_length=254)
	user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING )

	def __str__(self):
		cadena= "Nombre: {0} - Empresa: {1}  Comentario: {2}"
		return cadena.format(self.name, self.company.name, self.email, self.user)

class Track(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	employee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, blank=False, null=False)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		cadena= "Entrada: {0} - Salida: {1}"
		return cadena.format(self.start, self.end)
	
	

