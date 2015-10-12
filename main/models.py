from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    abbrev = models.CharField(max_length=255, null=True, blank=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class StateCapital(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    # state = models.ForeignKey('main.State', null=True, blank=True)
    state = models.OneToOneField('main.State', null=True, blank=True)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    state = models.ForeignKey('main.State', null=True, blank=True)
# class Meta:
#
    def __unicode__(self):
        return self.name

