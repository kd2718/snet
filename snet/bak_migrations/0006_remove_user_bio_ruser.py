# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0005_user_bio_ruser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_bio',
            name='ruser',
        ),
    ]
