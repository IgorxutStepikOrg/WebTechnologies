from django.conf.urls import url
from django.contrib import admin

urlpatterns = [url(r'^admin/', include(admin.site.urls)), url(r'^', include('qa.urls', namespace='qa')),]
