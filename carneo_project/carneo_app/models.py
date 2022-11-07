from django.db import models

TYPE = (
    ('diesel', 'Diesel'),
    ('benzyna', 'Benzyna'),
    ('benzyna_lpg', 'Benzyna+LPG'),
    ('hybryda', 'Hybryda'),
    ('elektryczny', 'Elektryczny')
)


class Cars(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine_type = models.CharField(choices=TYPE, max_length=255)
    engine_power = models.IntegerField()
    url = models.URLField()
    ad_source = models.URLField()
    img_source = models.URLField(null=True)
