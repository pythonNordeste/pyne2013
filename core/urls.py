#encoding: utf-8

from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from core.views import IndexView, CallForPapersView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^callforpapers$', CallForPapersView.as_view(), name='call_for_papers'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)