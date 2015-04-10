# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [('snet', '0001_initial'), ('snet', '0002_auto_20150330_2345'), ('snet', '0003_wall'), ('snet', '0004_user_bio_date_join'), ('snet', '0005_user_bio_ruser'), ('snet', '0006_remove_user_bio_ruser')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Bio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(default=0)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='F')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(to='snet.User_Bio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user_bio',
            name='date_join',
            field=models.DateTimeField(verbose_name='date joined', default=datetime.datetime(2015, 3, 31, 20, 31, 54, 736962, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
