from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=45)
    a_paterno = models.CharField(max_length=45, null=True)
    a_materno = models.CharField(max_length=45, null=True)
    fec_nacimiento = models.DateField(null=True)
    numero = models.IntegerField()
