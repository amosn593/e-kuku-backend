
from django.urls import path
from .views import *

urlpatterns = [
    path('latestpoultry/', latestpoultry, name="latestpoultry"),
    path('poultrydetail/<str:pk>', poultrydetail, name="poultrydetail"),
    path('poultryview/<str:pk>', poultryview, name="poultryview"),
    path('poultryeggs/', poultryeggs, name="poultryeggs"),
    path('poultrychicks/', poultrychicks, name="poultrychicks"),
    path('poultrychicken/', poultrychicken, name="poultrychicken"),
    path('poultryfeed/', poultryfeed, name="poultryfeed"),
]
