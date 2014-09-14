# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bizz_fuzz_app.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bizz_fuzz_app', '0003_myuser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='random_number',
            field=models.IntegerField(default=bizz_fuzz_app.models.generate_random_number, max_length=3, verbose_name=b'Random'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(default=datetime.date(2014, 9, 14), verbose_name=b'Birthday'),
        ),
    ]
