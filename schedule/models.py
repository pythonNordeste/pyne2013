#coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_(u'Nome'), max_length=200)
    short_bio = models.TextField(_(u'Biografia'))
    email = models.EmailField(_(u'E-mail'))
    twitter_profile = models.CharField(
        _(u'Twitter'),
        max_length=100,
        blank=True
    )

    def get_twitter_url(self):
        return 'http://twitter.com/{0}'.format(self.twitter_profile)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Palestrante'


class Slot(models.Model):
    TRACK_CHOICES = (
        ('core', _(u'Python Core')),
        ('web', _(u'Python Web')),
        ('enterprise', _(u'Gestão e Enterprise')),
        ('mobility', _(u'Mobilidade, Networking e Multimídia')),
        ('frameworks', _(u'Frameworks Python')),
        ('science', _(u'Science')),
    )
    TYPE_CHOICES = (
        ('talk', 'Palestra'),
        ('others', 'Outros'),
    )
    speaker = models.ForeignKey(
        Speaker,
        related_name='talks',
        null=True,
        blank=True
    )
    title = models.CharField(_(u'Título'), max_length=300)
    time = models.DateTimeField(_(u'Data e Hora'))
    abstract = models.TextField(_(u'Resumo'), null=True, blank=True)
    type = models.CharField(_(u'Tipo'), max_length=10, choices=TYPE_CHOICES)
    track = models.CharField(
        _(u'Trilha'),
        max_length=20,
        choices=TRACK_CHOICES,
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return u'{0} - {1}'.format(self.time, self.title)


class Reference(models.Model):
    talk = models.ForeignKey(Slot, related_name='references')
    url = models.CharField(_(u'URL'), max_length=300)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.talk.title, self.url)

    class Meta:
        verbose_name = u'Referências'
