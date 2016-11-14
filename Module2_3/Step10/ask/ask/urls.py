from django.conf.urls import url, include

from qa.views import test


urlpatterns = [
    url(r'^$', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/', include("qa.urls")),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test)
]
