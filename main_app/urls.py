from django.urls import path
from . import views

urlpatterns = [
    path('latestpoultry/', views.latestpoultry, name="latestpoultry"),
    path('poultrysearch/<str:search>', views.poultrysearch, name="poultrysearch"),
    path('mypoultry/', views.mypoultry, name="mypoultry"),
    path('mypoultrydelete/<str:pk>', views.mypoultrydelete, name="mypoultrydelete"),
    path('poultrycreate/', views.poultrycreate, name="poultrycreate"),
    path('poultrydetail/<str:pk>', views.poultrydetail, name="poultrydetail"),
    path('poultryview/<str:pk>', views.poultryview, name="poultryview"),
    path('poultryeggs/', views.poultryeggs, name="poultryeggs"),
    path('poultrychicks/', views.poultrychicks, name="poultrychicks"),
    path('poultrychicken/', views.poultrychicken, name="poultrychicken"),
    path('poultryfeed/', views.poultryfeed, name="poultryfeed"),
    path('poultrystructure/', views.poultrystructure, name="poultrystructure"),
    path('getcounty/', views.getcounty, name="getcounty"),
    path('getsubcounty/<str:pk>', views.getsubcounty, name="getsubcounty"),
    path('getcategory/', views.getcategory, name="getcategory"),
]
