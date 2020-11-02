from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, Comment, RateOfComment
from .permisions import AdminOrAuthorCanEdit, AdminOrPostAuthorOrCommentAuthorCanDelete
from .serializers import PostSerializer, CommentSerializer, RateOfCommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          AdminOrAuthorCanEdit
                          ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          AdminOrPostAuthorOrCommentAuthorCanDelete
                          ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RateOfCommentViewSet(viewsets.ModelViewSet):
    queryset = RateOfComment.objects.all()
    serializer_class = RateOfCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          AdminOrAuthorCanEdit
                          ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
