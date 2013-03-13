from django.conf.urls import patterns, url

from core.views import IndexView, CallForPapersView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^callforpapers$', CallForPapersView.as_view(), name='call_for_papers'),
)
