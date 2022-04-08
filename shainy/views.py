from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status, generics
from .models import PostModel, ResponseModel

class AddPostView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = serializers.PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)

class PostsListView(generics.ListAPIView):
    queryset = PostModel.objects.all().order_by('date_pub')
    serializer_class = serializers.ShowPostSerializer

class SendResponse(APIView):
    def post(self, request, post_id):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if not PostModel.objects.filter(id=post_id):
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = PostModel.objects.get(id=post_id)
        #if post.user == request.user:
            #return Response({'error':'you try to send response yourself'})
        ResponseModel.objects.create(post=post, user1=request.user, post_author=post.user)
        return Response(status=status.HTTP_201_CREATED)

class MyResponsesView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        responses = ResponseModel.objects.filter(post_author=request.user)
        serializer = serializers.ResponseSerializer(responses, many=True)
        return Response({"responses": serializer.data})

class MatchReponseView(APIView):
    def get(self, request, resp_id):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if not ResponseModel.objects.filter(id=resp_id):
            return Response(status=status.HTTP_404_NOT_FOUND)
        response = ResponseModel.objects.get(id=resp_id)
        email = response.user1.email
        response.delete()
        return Response({'user_email': email})
