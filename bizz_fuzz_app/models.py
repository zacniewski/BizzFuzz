# -*- coding: utf-8 -*-
from random import randint
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse


def generate_random_number():
    return randint(1, 100)


class MyUser(AbstractUser):
    birthday = models.DateField('Birthday', default=date.today())
    random_number = models.IntegerField('Random', max_length=3, default=generate_random_number)

    class Meta:
        verbose_name = u'My user'
        verbose_name_plural = u'My users'
        app_label = 'bizz_fuzz_app'

    def get_absolute_url(self):
        return reverse('myuser-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        if self.first_name:
            return u'{} {}'.format(self.first_name, self.last_name)
        else:
            return u'{}'.format(self.username)