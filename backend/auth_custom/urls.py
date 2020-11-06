from allauth.account.views import email_verification_sent
from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter

from auth_custom.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls

urlpatterns += [
    path('confirm-email/', email_verification_sent, name='account_email_verification_sent'),
    re_path(r'^auth/', include('rest_auth.urls')),
    re_path(r'^auth/registration/', include('rest_auth.registration.urls')),
]
