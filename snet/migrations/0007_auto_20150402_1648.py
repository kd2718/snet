# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0006_auto_20150402_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pics',
            name='photo',
            field=models.ImageField(default='welcome.jpg', upload_to=''),
            preserve_default=True,
        ),
    ]
