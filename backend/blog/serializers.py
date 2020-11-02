from rest_framework import serializers

from auth_custom.models import User
from blog.models import Post, Comment, RateOfComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name'
                  ]


class CommentForPost(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id',
                  'author',
                  'text',
                  'positive',
                  'negative',
                  'was_published_recently',
                  'created_at'
                  ]


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentForPost(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['id',
                  'slug',
                  'title',
                  'author',
                  'comments',
                  'picture',
                  'text',
                  'was_published_recently',
                  'created_at'
                  ]


class PostForCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id',
                  'slug',
                  'title',
                  'author',
                  'picture',
                  'text',
                  'was_published_recently',
                  'created_at'
                  ]


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = PostForCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id',
                  'author',
                  'post',
                  'text',
                  'was_published_recently',
                  'created_at'
                  ]


class RateOfCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = RateOfComment
        fields = ['id',
                  'author',
                  'comment',
                  'opinion',
                  'created_at'
                  ]
