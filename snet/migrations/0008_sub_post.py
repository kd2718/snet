# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snet', '0007_auto_20150402_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='datepublished')),
                ('parent_post', models.ForeignKey(to='snet.Post')),
                ('poster', models.ForeignKey(to='snet.User_Bio')),
                ('wall', models.ForeignKey(to='snet.Wall')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
