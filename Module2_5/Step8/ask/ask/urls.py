from django.conf.urls import url, include
from django.contrib import admin

from qa.views import index, popular, question

admin.autodiscover()

urlpatterns = [
    url(r'^$', index),
    url(r'^login/.*$', 'qa.views.test'),
    url(r'^signup/.*$', 'qa.views.test'),
    url(r'^question/\d+/$', question),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'^popular/.*$', popular),
    url(r'^new/.*$', 'qa.views.test')
]
