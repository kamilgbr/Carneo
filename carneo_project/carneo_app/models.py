from django.db import models


class Cars(models.Model):
    brand = models.CharField(max_length=255)
    model = models.TextField()
    engine_type = models.CharField(max_length=255)
    engine_power = models.IntegerField()
    url = models.URLField()
    ad_source = models.TextField()