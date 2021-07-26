from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(["GET"])
def postsview(request):
    posts = Poultry.objects.all()
    serializer = PoultrySerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def postdetailedview(request, pk):
    try:
        post = Poultry.objects.get(id=pk)
    except:
        post = "Post not found!!!"
    serializer = PoultrySerializer(post, many=False)
    return Response(serializer.data)
