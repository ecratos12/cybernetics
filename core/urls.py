from django.conf.urls import include, url
from core.views import *



urlpatterns = [
    url(r'^$', home, name="index"),
    url(r'^news$', news, name="news"),
    url(r'^get_schedule$', get_schedule, name="get_schedule"),
    url(r'^study/$', study, name="study"),
    url(r'^schedule/$', schedule, name="schedule"),
    url(r'^administration-faculty/$', administration, name="administration"),
    url(r'^student-life/$', student_life, name="student_life"),
    url(r'^contacts/$', contacts, name="contacts"),
    url(r'^gallery/photo$', gallery, name="gallery"),
    url(r'^library/(?P<slug>[_0-9a-zA-Z-]+)/$', library, name='library'),
    url(r'^news/(?P<id>[0-9]+)$', new, name='new'),
    url(r'^programming-contests/(?P<id>[0-9]+)$', olimp, name='olimp'),
    url(r'^other-contests/$', olimp_other, name='olimp_other'),
    url(r'^departments/(?P<id>[0-9]+)$', departments, name='departments'),
    url(r'^degree/(?P<id>[0-9]+)$', degree, name='degree'),
    url(r'^history/personality$', personality, name='personality'),
    url(r'^(?P<slug>[_0-9a-zA-Z-]+)/$', article, name='article'),
]