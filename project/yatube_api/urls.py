from django.contrib import admin
from django.urls import include, path

from yatube_api.schema import schema

urlpatterns = [
    path('', schema),
    path('', include('api.urls')),
]
