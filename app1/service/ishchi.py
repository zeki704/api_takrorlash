from django.db import models


class Ishchi(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    oylik = models.CharField(max_length=128)
    yoshi = models.DateField()
    jinsi = models.BooleanField(default="Erkak")

    def __str__(self):
        return self.first_name

