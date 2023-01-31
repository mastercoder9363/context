from django.db import models
class Ranglar(models.Model):
    rang = models.CharField(max_length=31)
    def __str__(self) -> str:
        return self.rang

class Gul(models.Model):
    nomi = models.CharField(max_length=31)
    rangi = models.ManyToManyField(Ranglar, blank=True)
    def __str__(self) -> str:
        return self.nomi
        
class Barg(models.Model):
    turi = models.CharField(max_length=31)
    rangi = models.ManyToManyField(Ranglar, blank=True)