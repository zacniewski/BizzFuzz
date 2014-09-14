# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import  MyUser


class MyUserForm(ModelForm):
    """
    Form of MyUser
    """
    class Meta:
        model = MyUser
        fields = ['username', 'password', 'birthday']