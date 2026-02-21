from django.shortcuts import render
from rest_framework.views import APIView

from blog.serializers import *


# Create your views here.

class PostAPIView(APIView):
    serializer_class = PostSerializer
    http_method_names = ['get', 'post']

class LikesAPIView(APIView):
    serializer_class = LikesSerializer
    http_method_names = ['get', 'put', 'post']

class CommentAPIView(APIView):
    serializers_class = CommentsSerializer
    http_method_names = ['get', 'put', 'post']

