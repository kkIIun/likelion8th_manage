from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import wordcount.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="home"),
    url(r'^wordcount/', include(wordcount.urls)),
    url(r'^accounts/', include('allauth.urls')),
]

