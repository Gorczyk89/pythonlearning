# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=250)
    published = models.DateField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True)
