#encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'certificates.views',
    url(r'^download/', 'download', name='download_certificate')
)
