# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0003_pics_is_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pics',
            name='photo',
            field=models.ImageField(upload_to=''),
            preserve_default=True,
        ),
    ]
