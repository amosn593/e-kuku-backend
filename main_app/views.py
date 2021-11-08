from rest_framework import status, permissions
from rest_framework_simplejwt import authentication
from PIL import Image
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from accounts.models import UserAccount
from main_app.models import *
from main_app.serializers import *
from django.shortcuts import get_object_or_404
from django.http import Http404


@api_view(["GET"])
def latestpoultry(request):
    try:
        posts = Poultry.objects.all()
        serializer = PoultrySerializer(posts, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def poultrysearch(request, search):
    try:
        posts = Poultry.objects.filter(
            title__icontains=search) | Poultry.objects.filter(
            category__name__icontains=search)
        serializer = PoultrySerializer(posts, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def mypoultry(request):
    try:
        posts = Poultry.objects.filter(seller=request.user)
        serializer = PoultrySerializer(posts, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def poultrycreate(request):
    parser_classes = (MultiPartParser, FormParser)
    serializer = PoultryCreateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(seller=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def mypoultrydelete(request, pk):
    try:
        post = Poultry.objects.get(seller=request.user, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def poultrydetail(request, pk):
    try:
        post = Poultry.objects.get(pk=pk)
        serializer = PoultrySerializer(post, many=False)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def poultryview(request, pk):
    try:
        post = Poultry.objects.get(pk=pk)
        current_views = post.views
        post.views = current_views + 1
        post.save(update_fields=["views"])
        return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def poultryeggs(request):
    try:
        post = Poultry.objects.filter(category__name__icontains="eggs")
        serializer = PoultrySerializer(post, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def poultrychicken(request):
    try:
        post = Poultry.objects.filter(category__name__icontains="Chicken")
        serializer = PoultrySerializer(post, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def poultrychicks(request):
    try:
        post = Poultry.objects.filter(category__name__icontains="Chicks")
        serializer = PoultrySerializer(post, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def poultryfeed(request):
    try:
        post = Poultry.objects.filter(category__name__icontains="Feeds")
        serializer = PoultrySerializer(post, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def poultrystructure(request):
    try:
        post = Poultry.objects.filter(
            category__name__icontains="Poultry Facilities")
        serializer = PoultrySerializer(post, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def getcounty(request):
    try:
        counties = County.objects.all()
        counties = CountySerializer(counties, many=True)
        return Response(counties.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def getsubcounty(request, pk):
    try:
        subcounties = Subcounty.objects.filter(county=pk)
        subcounties = SubcountySerializer(subcounties, many=True)
        return Response(subcounties.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def getcategory(request):
    try:
        categories = Category.objects.all()
        categories = CategorySerializer(categories, many=True)
        return Response(categories.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
