#encoding: utf-8

from django.db import models


OPT = {'blank': True, 'null': True}


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Sponsor(TimeStampedMixin):

    GOLD_TYPE = 1
    SILVER_TYPE = 2
    BRONZE_TYPE = 3

    TYPE_CHOICES = (
        (GOLD_TYPE, u'Ouro'),
        (SILVER_TYPE, u'Prata'),
        (BRONZE_TYPE, u'Bronze'),
    )

    name = models.CharField(verbose_name=u'Nome', max_length=100)
    image = models.ImageField(verbose_name=u'Imagem', upload_to='sponsors')
    type = models.IntegerField(verbose_name=u'Tipo', choices=TYPE_CHOICES)
    link = models.URLField(verbose_name=u'Link (website)', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['type']
        verbose_name = u'Patrocinador'
        verbose_name_plural = u'Patrocinadores'
