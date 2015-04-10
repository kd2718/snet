# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snet', '0004_user_bio_date_join'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_bio',
            name='ruser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=datetime.datetime(2015, 3, 31, 22, 43, 42, 769959, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
