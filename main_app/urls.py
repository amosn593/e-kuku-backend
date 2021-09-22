from django.urls import path
from . import views

urlpatterns = [
    path('latestpoultry/', views.latestpoultry, name="latestpoultry"),
    path('mypoultry/', views.mypoultry, name="mypoultry"),
    path('poultrycreate/', views.poultrycreate, name="poultrycreate"),
    path('poultrydetail/<str:pk>', views.poultrydetail, name="poultrydetail"),
    path('poultryview/<str:pk>', views.poultryview, name="poultryview"),
    path('poultryeggs/', views.poultryeggs, name="poultryeggs"),
    path('poultrychicks/', views.poultrychicks, name="poultrychicks"),
    path('poultrychicken/', views.poultrychicken, name="poultrychicken"),
    path('poultryfeed/', views.poultryfeed, name="poultryfeed"),
    path('getcounty/', views.getcounty, name="getcounty"),
    path('getsubcounty/<str:pk>', views.getsubcounty, name="getsubcounty"),
    path('getcategory/', views.getcategory, name="getcategory"),
]
