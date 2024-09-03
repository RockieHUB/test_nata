from django.db import models
from pendaftaran.models import Akun
from dashboard.models import Pelatihan

# Create your models here.
class Enrollment(models.Model):
    akun = models.ForeignKey(Akun, on_delete=models.CASCADE)
    pelatihan = models.ForeignKey(Pelatihan, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('akun', 'pelatihan')