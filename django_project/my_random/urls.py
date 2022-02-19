from django.urls import path

from .views import my_random

app_name = 'my_random'

urlpatterns = [
    path('', my_random),
]
