from django_filters.rest_framework import DjangoFilterBackend # pylint:disable=unresolved-import
from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from sreps.api.v1.serializers.sale import SaleSerializer
from sreps.core.models import Sale


class SaleViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,):

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
    search_fields = ('product__name',)
    ordering = ('-id',)
    ordering_fields = (
        'id',
        'invoice__id',
        'product__id',
        'product__name',
        'quantity',
        'datetime_created',
    )
    filterset_fields = (
        'invoice__id',
        'product__id',
    )
