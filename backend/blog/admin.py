from django.contrib import admin
from .models import Post, Comment, RateOfComment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'slug',
                    'was_published_recently',
                    'created_at'
                    )
    fields = ['author',
              'title',
              'picture',
              'text',
              'created_at',
              'slug',
              ]
    readonly_fields = ['created_at', 'slug']
    list_filter = ['created_at']
    search_fields = ['title', 'content']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author',
                    'post',
                    'was_published_recently',
                    'created_at'
                    )
    list_filter = ['created_at']
    fields = ['author',
              'post',
              'text',
              'created_at',
              ]
    readonly_fields = ['created_at']
    search_fields = ['post', 'text']


class RateOfCommentAdmin(admin.ModelAdmin):
    list_display = ('author',
                    'comment',
                    'opinion',
                    'created_at'
                    )
    readonly_fields = ['created_at']
    fields = ['author',
              'comment',
              'opinion',
              'created_at',
              ]
    list_filter = ['created_at']
    search_fields = ['author', 'comment']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(RateOfComment, RateOfCommentAdmin)
