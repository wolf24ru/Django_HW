from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly, IsAdminUserOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_class = AdvertisementFilter
    filterset_fields = ['created_at', 'updated_at', 'status', 'creator']
    ordering_fields = ['created_at', 'updated_at', 'status']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly | IsAdminUserOrReadOnly]

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated(), IsOwnerOrReadOnly(), IsAdminUserOrReadOnly()]
    #     return []
