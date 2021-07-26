
from django.urls import path
from .views import *

urlpatterns = [
    path('', postsview, name="postsview"),
    path('postdetails/<int:pk>', postdetailedview, name="postdetails"),

]
