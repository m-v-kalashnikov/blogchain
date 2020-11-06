from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from auth_custom.models import User
from auth_custom.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('username',)
    permission_classes = [IsAuthenticated]


@api_view(('GET',))
def user_info(request):
    user_id = request.user.id

    user = get_object_or_404(User, id=user_id)

    return JsonResponse({
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    })
