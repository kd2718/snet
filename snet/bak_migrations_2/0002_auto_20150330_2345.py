# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_bio',
            name='age',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
