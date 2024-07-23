from rest_framework import generics, permissions
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from posts.models import Post

from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import PostSerializer
from .throttling import LunchBreakThrottle


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_classes = (LunchBreakThrottle, AnonRateThrottle, UserRateThrottle)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    throttle_classes = (LunchBreakThrottle, AnonRateThrottle, UserRateThrottle)
