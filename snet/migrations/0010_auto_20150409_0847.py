# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0009_user_bio_facebook_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_post',
            name='pub_date',
            field=models.DateTimeField(blank=True, verbose_name='datepublished'),
            preserve_default=True,
        ),
    ]
