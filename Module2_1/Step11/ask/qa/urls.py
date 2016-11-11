from django.conf.urls import patterns, url
from qa.views import *

urlpatterns = patterns(
  url(r'^(?P<num>\d+)/$', question),
)
