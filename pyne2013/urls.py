from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^talk/', include('schedule.urls')),
    url(r'^hoteis/', include('hotels.urls')),
    url('^pages/', include('django.contrib.flatpages.urls')),
)
