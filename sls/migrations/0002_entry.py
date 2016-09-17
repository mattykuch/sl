# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_balance', models.IntegerField()),
                ('stock_order', models.IntegerField()),
                ('stock_adjustment_dvs', models.IntegerField()),
                ('stock_adjustment_nms', models.IntegerField(default=0)),
                ('vaccine', models.ForeignKey(to='sls.Vaccine')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
