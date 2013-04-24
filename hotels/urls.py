from django.conf.urls import patterns, url

urlpatterns = patterns('hotels.views',
    url(r'^$', 'hotel_list', name='hotel-list'),
)
