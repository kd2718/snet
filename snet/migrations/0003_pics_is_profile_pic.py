# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0002_pics'),
    ]

    operations = [
        migrations.AddField(
            model_name='pics',
            name='is_profile_pic',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
