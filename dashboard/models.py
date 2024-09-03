from django.db import models

# Create your models here.
class Pelatihan(models.Model):
    nama = models.CharField(null=False, max_length=(100))
    author = models.CharField(null=False, max_length=(100))
    rating = models.IntegerField(null=False)
    harga = models.DecimalField(null=False, max_digits=9, decimal_places=2)
    kategori = models.CharField(null=False, max_length=(20))