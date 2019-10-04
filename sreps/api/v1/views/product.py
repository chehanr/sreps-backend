from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from sreps.api.v1.serializers.product import (ProductDetailSerializer,
                                              ProductSerializer)
from sreps.core.models import Product


class ProductViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,):

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
    search_fields = ('name',)
    ordering = ('-id',)
    ordering_fields = (
        'id',
        'name',
        'category__id',
        'category__name',
        'stock_quantity',
        'base_price',
        'discount_amount',
        'is_available',
        'datetime_created',
    )
    filterset_fields = (
        'category__id',
        'is_available',
    )
    permission_classes_by_action = {
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'partial_update': [IsAdminUser],
        'destroy': [IsAdminUser],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer

        return ProductDetailSerializer
