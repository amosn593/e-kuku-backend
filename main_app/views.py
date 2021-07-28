from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def latestpoultry(request):
    posts = Poultry.objects.all()
    serializer = PoultrySerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def pooultrydetail(request, pk):
    post = get_object_or_404(Poultry, id=pk)
    serializer = PoultrySerializer(post, many=False)
    return Response(serializer.data)
