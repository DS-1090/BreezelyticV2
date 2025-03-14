
from django.contrib import admin
from django.urls import path
from .views import  fetchLocData, sendtoApp, fetchrecords, sendCurrentAQI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fetchLocData/', fetchLocData, name="fetchLocData"),
    path('sendtoApp/', sendtoApp),
    path('fetchrecords/', fetchrecords),
    path('sendCurrentAQI/', sendCurrentAQI)
]
