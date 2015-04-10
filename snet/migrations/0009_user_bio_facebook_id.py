# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0008_sub_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_bio',
            name='facebook_id',
            field=models.CharField(blank=True, null=True, max_length=255, default=None),
            preserve_default=True,
        ),
    ]
