# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0005_auto_20150402_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pics',
            name='photo',
            field=models.ImageField(upload_to=''),
            preserve_default=True,
        ),
    ]
