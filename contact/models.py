# -*- coding:utf-8 -*-

from django.db import models
from core.models import TimeStampedMixin


class Contact(TimeStampedMixin):
    name = models.CharField(u'Nome', max_length=50)
    email = models.EmailField(u'E-Mail', max_length=254)
    body = models.TextField(u'Mensagem')

    def __unicode__(self):
        return u'Message from {0}'.format(self.name)
