from django.urls import path

from .views import main, whoami, source_code

app_name = 'about'

urlpatterns = [
    path('', main),
    path('whoami/', whoami),
    path('source_code/', source_code),
]
