# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151106_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='downvotes_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='upvotes_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
