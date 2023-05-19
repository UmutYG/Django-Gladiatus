from django.db import models


class OyuncuBilgi(models.Model):
    kullanici = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    gecirilenGun = models.TextField()
    moneyUsed = models.IntegerField()
    kayitGunu = models.DateTimeField(auto_now_add=True)


class karakter(models.Model):
    kullanici = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    Power = models.IntegerField()
    Beceri = models.IntegerField()
    Ceviklik = models.IntegerField()
    Dayaniklilik = models.IntegerField()
    Karizma = models.IntegerField()
    Zeka = models.IntegerField()
    Hasar = models.IntegerField()


# Create your models here.
