from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from sreps.api.v1.serializers.invoice import InvoiceSerializer
from sreps.core.models import Invoice


class InvoiceViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,):

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
    search_fields = (
        'salesperson__name',
        'customer__name',
    )
    ordering = ('-id',)
    ordering_fields = (
        'id',
        'salesperson__id',
        'salesperson__name',
        'customer__id',
        'customer__name',
        'other_cost',
        'tax_amount',
        'is_paid',
        'datetime_pay_due',
        'datetime_paid',
        'datetime_created',
    )
    filterset_fields = (
        'salesperson__id',
        'customer__id',
        'is_paid',
    )
