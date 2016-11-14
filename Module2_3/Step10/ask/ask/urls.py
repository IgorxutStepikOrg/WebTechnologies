from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', 'qa.views.test'),
    url(r'^login/', 'qa.views.test'),
    url(r'^signup/', 'qa.views.test'),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', 'qa.views.test'),
    url(r'^popular/', 'qa.views.test'),
    url(r'^new/', 'qa.views.test')
]
