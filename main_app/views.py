from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
# @api_view["GET"]
def index(request):
    return Response("Hello world")