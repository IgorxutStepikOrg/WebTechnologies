from django.conf.urls import url, include, patterns
from django.contrib import admin
from qa.views import

admin.autodiscover()

urlpatterns = patterns(
  url(r'^$', 'index', name='index'),
  url(r'^login/', 'login', name='login'),
  url(r'^signup/', 'signup', name='signup'),
  url(r'^question/', include('qa.urls')),
  url(r'^ask/', 'ask', name='ask'),
  url(r'^popular/', 'popular', name='popular'),
  url(r'^new/', 'new', name='new'),
  
  url(r'^admin/', admin.site.urls),
  url(r'^', include('qa.urls')),
)
