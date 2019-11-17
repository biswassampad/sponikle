from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from core import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(url))
]
