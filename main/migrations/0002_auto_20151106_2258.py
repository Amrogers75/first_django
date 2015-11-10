# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='downvotes_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='upvotes_count',
        ),
    ]
