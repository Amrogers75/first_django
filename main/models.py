from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
# Create your models here.


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True)
    

class State(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    abbrev = models.CharField(max_length=255, null=True, blank=True)
    capital = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    # pop = models.CharField(max_length=255, null=True, blank=True)
    state_map = models.ImageField(upload_to='state_map', null=True, blank=True)
    upvotes = models.ManyToManyField('main.UserProfile', related_name='up_votes')
    downvotes = models.ManyToManyField('main.UserProfile', related_name='down_votes')

    upvotes_count = models.IntegerField(default=0, null=True, blank=False)
    downvotes_count = models.IntegerField(default=0, null=True, blank=False)
    
    votes = models.IntegerField(default=0, null=True, blank=False)
    
    def total_votes(self):
        total_votes = self.upvotes_count - self.downvotes_count
        return total_votes
    
    def __unicode__(self):
        return self.name


def recount_up(sender, instance, **kwargs):
    print "upvotes_count:%s , upvotes.count: %s" % (instance.upvotes_count, instance.upvotes.count())
    instance.upvotes_count = instance.upvotes.count()
    instance.save()

    instance.votes = instance.upvotes_count - instance.downvotes_count

    instance.save()

m2m_changed.connect(recount_up, sender=State.upvotes.through)


def recount_down(sender, instance, **kwargs):
    print "downvotes_count:%s , downvotes.count: %s" % (instance.downvotes_count, instance.downvotes.count())
    instance.downvotes_count = instance.downvotes.count()
    instance.save()

    instance.votes = instance.upvotes_count - instance.downvotes_count

    instance.save()

    print "downvotes_count:%s , downvotes.count: %s, votes: %s" % (instance.downvotes_count, instance.downvotes.count(), instance.votes)

m2m_changed.connect(recount_down, sender=State.downvotes.through)


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
    name = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    state = models.ForeignKey('main.State', null=True, blank=True)
# class Meta:
#

    def __unicode__(self):
        return self.name

