from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^poll/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]