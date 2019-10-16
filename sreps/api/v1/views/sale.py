from django_filters.rest_framework import DjangoFilterBackend  # pylint:disable=unresolved-import
from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action, renderer_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from sreps.api.v1.serializers.sale import SaleSerializer
from sreps.api.v1.renderers.sale import SaleCsvRenderer
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

    @action(detail=False, methods=['GET'], name='Export', renderer_classes=[SaleCsvRenderer])
    def export(self, request, pk=None):
        """Get CSV export for sales."""

        sale_objs = Sale.objects.all()
        content = [
            {
                'id': sale_obj.pk,
                'quantity': sale_obj.quantity,
                'datetime-created': sale_obj.datetime_created,
                'invoice-id': sale_obj.invoice.pk,
                'invoice-description': sale_obj.invoice.description,
                'invoice-other-cost': sale_obj.invoice.other_cost,
                'invoice-tax-amount': sale_obj.invoice.tax_amount,
                'invoice-is-paid': sale_obj.invoice.is_paid,
                'invoice-datetime-pay-due': sale_obj.invoice.datetime_pay_due,
                'invoice-datetime-paid': sale_obj.invoice.datetime_paid,
                'invoice-datetime-created': sale_obj.invoice.datetime_created,
                'invoice-salesperson-id': sale_obj.invoice.salesperson.pk,
                'invoice-salesperson-username': sale_obj.invoice.salesperson.username,
                'invoice-customer-id': sale_obj.invoice.customer.pk,
                'invoice-customer-name': sale_obj.invoice.customer.name,
                'product-id': sale_obj.product.pk,
                'product-name': sale_obj.product.name,
                'product-category': sale_obj.product.category,
                'product-lst': sale_obj.product.low_stock_threshold,
                'product-base-price': sale_obj.product.base_price,
                'product-discount-amount': sale_obj.product.discount_amount,
                'product-datetime-created': sale_obj.product.datetime_created,
            }
            for sale_obj in sale_objs
        ]

        return Response(content)
