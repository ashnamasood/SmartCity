from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.FloatField()
    lon = models.FloatField()
    country = models.CharField(max_length=50, default='IN')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"