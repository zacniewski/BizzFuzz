# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bizz_fuzz_app', '0002_remove_myuser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(default=datetime.date(2014, 9, 13), verbose_name=b'Date of birth'),
            preserve_default=True,
        ),
    ]
