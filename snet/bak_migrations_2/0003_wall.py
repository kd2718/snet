# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0002_auto_20150330_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wall',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('status', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(to='snet.User_Bio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
