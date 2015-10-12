# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='name',
        ),
    ]
