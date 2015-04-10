# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0003_wall'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_bio',
            name='date_join',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 20, 31, 54, 736962, tzinfo=utc), verbose_name='date joined'),
            preserve_default=False,
        ),
    ]
