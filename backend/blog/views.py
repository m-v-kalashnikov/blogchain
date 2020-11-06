from django.core.exceptions import ObjectDoesNotExist
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Post, Comment, RateOfComment
from .permisions import AdminOrAuthorCanEdit, AdminOrPostAuthorOrCommentAuthorCanDelete
from .serializers import PostSerializer, CommentSerializer, RateOfCommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('slug',)
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
        serializer.save(author=self.request.user, post=Post.objects.get(id=self.request.data['post_id']))


class RateOfCommentViewSet(viewsets.ModelViewSet):
    queryset = RateOfComment.objects.all()
    serializer_class = RateOfCommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('comment__id',)
    permission_classes = [IsAuthenticatedOrReadOnly,
                          AdminOrAuthorCanEdit
                          ]

    def perform_create(self, serializer):
        try:
            rate_of_comment = RateOfComment.objects.get(author=self.request.user,
                                                        comment_id=self.request.data['comment']
                                                        )
            rate_of_comment.opinion = self.request.data['opinion']
            rate_of_comment.save()
            return Response(serializer.data)
        except ObjectDoesNotExist:
            serializer.save(author=self.request.user)
