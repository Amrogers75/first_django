# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('county', models.CharField(max_length=255, null=True, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('zip_code', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('abbrev', models.CharField(max_length=255, null=True, blank=True)),
                ('capital', models.CharField(max_length=255, null=True, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('pop', models.IntegerField(null=True, blank=True)),
                ('state_map', models.ImageField(null=True, upload_to=b'state_map', blank=True)),
                ('upvotes_count', models.IntegerField(default=0, null=True)),
                ('downvotes_count', models.IntegerField(default=0, null=True)),
                ('votes', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateCapital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('pop', models.IntegerField(null=True, blank=True)),
                ('state', models.OneToOneField(null=True, blank=True, to='main.State')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=255, null=True, blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='downvotes',
            field=models.ManyToManyField(related_name='down_votes', to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='state',
            name='upvotes',
            field=models.ManyToManyField(related_name='up_votes', to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(blank=True, to='main.State', null=True),
        ),
    ]
