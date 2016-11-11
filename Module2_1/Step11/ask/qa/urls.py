from django.conf.urls import patterns, url
from qa.views import *

urlpatterns = patterns(
  url(r'^$', 'index', name='index'),
  url(r'^login/', 'login', name='login'),
  url(r'^signup/', 'signup', name='signup'),
  url(r'^question/(?P<slug>\w+)/', 'question', name='question'),
  url(r'^ask/', 'ask', name='ask'),
  url(r'^popular/', 'popular', name='popular'),
  url(r'^new/', 'new', name='new'),
)
