from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import *


# Create your views here.

class PostAPIView(APIView):
    serializer_class = PostSerializer
    http_method_names = ['get', 'post']
    def get(self, request, id:int|None=None):
        if id is None or id == 0:
            return Response({'message': 'This is a message'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            post = Post.objects.get(id=id)
            serializer = self.serializer_class(post)
            return Response(serializer.data, status=status.HTTP_200_OK)

class LikesAPIView(APIView):
    serializer_class = LikesSerializer
    http_method_names = ['get', 'put', 'post']

class CommentAPIView(APIView):
    serializers_class = CommentsSerializer
    http_method_names = ['get', 'put', 'post']

def blog_page(request):
    return render(request, 'blog/index.html')

