
from django.urls import path
from .views import *

urlpatterns = [
    path('latestpoultry/', latestpoultry, name="latestpoultry"),
    path('pooultrydetail/<int:pk>', poultrydetail, name="pooultrydetail"),
    path('poultryeggs/', poultryeggs, name="poultryeggs"),
    path('poultrychicks/', poultrychicks, name="poultrychicks"),
    path('poultrychicken/', poultrychicken, name="poultrychicken"),
    path('poultryfeed/', poultryfeed, name="poultryfeed"),
]
