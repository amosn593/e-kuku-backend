from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.http.response import Http404


@api_view(["GET"])
def latestpoultry(request):
    posts = Poultry.objects.all()
    serializer = PoultrySerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def poultrydetail(request, pk):
    post = get_object_or_404(Poultry, id=pk)
    serializer = PoultrySerializer(post, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def poultryeggs(request):
    try:
        post = Poultry.objects.filter(category=1)
    except:
        raise Http404
    serializer = PoultrySerializer(post, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def poultrychicks(request):
    try:
        post = Poultry.objects.filter(category=2)
    except:
        raise Http404
    serializer = PoultrySerializer(post, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def poultrychicken(request):
    try:
        post = Poultry.objects.filter(category=3)
    except:
        raise Http404
    serializer = PoultrySerializer(post, many=True)
    return Response(serializer.data)
