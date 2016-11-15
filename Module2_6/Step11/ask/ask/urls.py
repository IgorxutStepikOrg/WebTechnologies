from django.conf.urls import url, include
from django.contrib import admin

from qa.views import index, popular, test, ask

admin.autodiscover()

urlpatterns = [
    url(r'^$', index),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', ask),
    url(r'^popular/', popular),
    url(r'^new/', test)
]
