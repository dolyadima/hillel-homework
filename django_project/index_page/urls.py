from django.urls import path

from .views import index_page

app_name = 'index_page'

urlpatterns = [
    path('', index_page),
]
