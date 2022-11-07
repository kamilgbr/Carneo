from django.db import models

TYPE = (
    ('diesel', 'Diesel'),
    ('benzyna', 'Benzyna'),
    ('benzyna_lpg', 'Benzyna+LPG'),
    ('hybryda', 'Hybryda'),
    ('elektryczny', 'Elektryczny')
)

AD_SOURCE = (
    ('otomoto', 'Otomoto.pl'),
    ('autocentrum', 'AutoCentrum.pl')
)


class Cars(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engine_type = models.CharField(choices=TYPE, max_length=255)
    engine_power = models.IntegerField()
    url = models.URLField()
    ad_source = models.CharField(choices=AD_SOURCE, max_length=255)
    img_source = models.URLField(null=True, blank=True)
