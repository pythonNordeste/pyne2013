# -*- coding: utf-8 -*-

from django.db import models

from core.models import TimeStampedMixin, OPT


class Hotel(TimeStampedMixin):
    TYPES = (
        (u'hostel', u'Hostel'),
        (u'hotel', u'Hotel'),
        (u'inn', u'Pousada'),
    )

    name = models.CharField(verbose_name=u'Nome', max_length=100)
    description = models.TextField(blank=True)
    address = models.CharField(verbose_name=u'Endereço', max_length=100)
    phone = models.CharField(
        verbose_name=u'Telefone', max_length=12, help_text=u'Somente números',
    )
    bus_description = models.TextField(
        verbose_name=u'Descrição de onibus', blank=True,
    )
    link = models.URLField(verbose_name=u'Link (website)', blank=True)

    hotel_type = models.CharField(
        verbose_name=u'Tipo', max_length=20, choices=TYPES,
    )

    def __unicode__(self):
        return self.name

    def get_type(self):
        return dict(self.TYPES)[self.hotel_type]


class Bedroom(models.Model):
    hotel = models.ForeignKey('hotels.Hotel')

    price = models.DecimalField(
        verbose_name=u'Preço', max_digits=10, decimal_places=2,
    )
    air_con = models.BooleanField(
        verbose_name=u'Ar condicionado', default=False,
    )
    max_people = models.PositiveIntegerField(**OPT)
    min_people = models.PositiveIntegerField(**OPT)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.price, self.max_people)


class TaxiRoute(models.Model):
    hotel = models.ForeignKey('hotels.Hotel')

    fr = models.CharField(verbose_name=u'De:', max_length=30)
    to = models.CharField(verbose_name=u'Para:', max_length=30)

    flag_1 = models.DecimalField(
        verbose_name=u'Bandeira 1', max_digits=10, decimal_places=2,
    )
    flag_2 = models.DecimalField(
        verbose_name=u'Bandeira 2', max_digits=10, decimal_places=2,
    )

    def __unicode__(self):
        return u'De: {0} para: {1}'.format(self.fr, self.to)
