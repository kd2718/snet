# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0004_auto_20150402_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pics',
            name='is_profile_pic',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pics',
            name='photo',
            field=models.ImageField(default='welcome.jpg', upload_to=''),
            preserve_default=True,
        ),
    ]
