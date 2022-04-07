from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, ShowPostSerializer
from rest_framework import status, generics
from .models import PostModel

class AddPostView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)

class PostsListView(generics.ListAPIView):
    queryset = PostModel.objects.all().order_by('date_pub')
    serializer_class = ShowPostSerializer
