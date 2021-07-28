
from django.urls import path
from .views import *

urlpatterns = [
    path('latestpoultry/', latestpoultry, name="postsview"),
    path('pooultrydetail/<int:pk>', pooultrydetail, name="postdetails"),

]
