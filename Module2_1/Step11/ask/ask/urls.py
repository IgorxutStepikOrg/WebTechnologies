from django.conf.urls import url, include, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
  url(r'^admin/', include(admin.site.urls)),
  url(r'^', include('qa.urls')),
)
