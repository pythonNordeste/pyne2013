from django.conf.urls import patterns, url

urlpatterns = patterns('courses.views',
    url(r'^$', 'course_list', name='course-list'),
)
