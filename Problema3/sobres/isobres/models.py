from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Empresa(models.Model):
    nom = models.TextField(max_length=50)
    web = models.TextField(max_length=100)

    def __unicode__(self):
        return self.nom

class Sobre(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()
    concept = models.TextField(max_length=50)
    empresa = models.ForeignKey(Empresa)
    politic = models.ForeignKey(User)

    def __unicode__(self):
        return self.empresa.nom+":"+str(self.amount)+":"+self.politic.name
