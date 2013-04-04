from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^(?P<talk_id>\d+)/$', 'schedule.views.talk', name='talk'),
)
