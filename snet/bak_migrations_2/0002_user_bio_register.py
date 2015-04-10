# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snet', '0001_squashed_0006_remove_user_bio_ruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_bio',
            name='register',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=datetime.datetime(2015, 3, 31, 23, 10, 6, 944100, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
