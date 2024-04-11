from django.contrib import admin
from django.urls import path, include

from apps.landing.views import show_landing_view

urlpatterns = [
    path('', show_landing_view)
]
