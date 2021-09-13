from rest_framework import status, authentication, permissions
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
    posts = Poultry.objects.all()
    serializer = PoultrySerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def poultrycreate(request):
    print(request.user)
    parser_classes = (MultiPartParser, FormParser)
    serializer = PoultryCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(seller=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # print('error', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def poultrydetail(request, pk):
    post = get_object_or_404(Poultry, id=pk)
    serializer = PoultrySerializer(post, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def poultryview(request, pk):
    post = get_object_or_404(Poultry, id=pk)
    current_views = post.views
    post.views = current_views + 1
    post.save(update_fields=["views"])
    return Response("Updated successfully!!!")


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
        post = Poultry.objects.filter(category=3)
    except:
        raise Http404
    serializer = PoultrySerializer(post, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def poultrychicken(request):
    try:
        post = Poultry.objects.filter(category=2)
    except:
        raise Http404
    serializer = PoultrySerializer(post, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def poultryfeed(request):
    try:
        post = Poultry.objects.filter(category=4)
    except:
        raise Http404
    serializer = PoultrySerializer(post, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getcounty(request):
    try:
        counties = County.objects.all()
    except:
        raise http404
    counties = CountySerializer(counties, many=True)
    return Response(counties.data)


@api_view(["GET"])
def getsubcounty(request, pk):
    try:
        subcounties = Subcounty.objects.filter(county=pk)
    except:
        raise http404
    subcounties = SubcountySerializer(subcounties, many=True)
    return Response(subcounties.data)


@api_view(["GET"])
def getcategory(request):
    try:
        categories = Category.objects.all()
    except:
        raise http404
    categories = CategorySerializer(categories, many=True)
    return Response(categories.data)


@api_view(["GET"])
def testget(request):
    tests = Testmodel.objects.all()
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def testget(request):
    parser_classes = (MultiPartParser, FormParser)
    if request.method == 'GET':
        snippets = Testmodel.objects.all()
        serializer = TestSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('error', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
