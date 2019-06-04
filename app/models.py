# -*- coding: utf-8 -*-
from django.db import models

class Host(models.Model):
    ip = models.CharField(max_length=20, verbose_name='ip address')
    name = models.CharField(max_length=30, verbose_name=u'hostname')
    application = models.CharField(max_length=20, verbose_name='application')
    remark = models.TextField(max_length=50, blank=True, verbose_name='remark')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )
