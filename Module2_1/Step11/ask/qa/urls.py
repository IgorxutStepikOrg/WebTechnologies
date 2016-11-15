from django.conf.urls import url
from django.contrib import admin

from qa.views import test

admin.autodiscover()

urlpatterns = [
    url(r"^(?P<num>\d+)/$", test),
]
