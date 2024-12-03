from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import PostCreateSerializer, PostSerializer, PostUpdateSerializer

from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return PostUpdateSerializer
        return PostSerializer

    def update(self, request, *args, **kwargs):
        response = {"detail": 'Method "PUT" not allowed.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
