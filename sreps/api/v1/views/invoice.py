from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, filters, mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from sreps.api.v1.serializers.invoice import InvoiceListSerializer, InvoiceDetailSerializer, InvoiceCreateSerializer
from sreps.core.models import Invoice, Sale, Product
from django.core.exceptions import ValidationError


class InvoiceViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,):

    queryset = Invoice.objects.all()
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

    def get_serializer_class(self):
        if self.action == 'list':
            return InvoiceListSerializer
        if self.action == 'create':
            return InvoiceCreateSerializer

        return InvoiceDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = InvoiceCreateSerializer(
            context={'request': request}, data=request.data)

        if not serializer.is_valid():
            raise exceptions.ValidationError(serializer.errors)

        products = request.data.get('products')

        if not products:
            raise exceptions.ValidationError({"products": "Products cannot be empty"})

        invoice_obj = serializer.save()

        sale_objs = []
        product_errors = []

        # Validation
        for product in products:
            product_id = product.get('id')
            product_quantity = product.get('quantity')

            if not Product.objects.filter(pk=product_id).exists():
                product_errors.append({
                    product_id: 'Product doesn\'t exist'
                })
            if not product_quantity:
                product_errors.append({
                    product_id: 'Product quantity doesn\'t exist'
                })

        if product_errors:
            product_error_dict = {"products": product_errors}
            raise exceptions.ValidationError(product_error_dict)

        sales_errors = {}

        for product in products:
            product_id = product['id']
            product_quantity = product['quantity']

            product_obj = Product.objects.get(pk=product_id)

            sale_obj = None

            try:
                sale_obj = Sale(invoice=invoice_obj, product=product_obj,
                                quantity=product_quantity).save()
            except ValidationError as ve:
                sales_errors['ve'] = ve

            sale_objs.append(sale_obj)

        if sales_errors.get('ve'):
            invoice_obj.delete()
            for sale_obj in sale_objs:
                if sale_obj != None:
                    sale_obj.delete()

            return exceptions.ValidationError(sales_errors['ve'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)
