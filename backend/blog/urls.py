from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, RateOfCommentViewSet

app_name = 'blog_app'

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'rate-of-comment', RateOfCommentViewSet, basename='rate_of_comment')

urlpatterns = router.urls
