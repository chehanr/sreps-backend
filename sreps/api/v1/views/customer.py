from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from sreps.api.v1.serializers.customer import CustomerSerializer
from sreps.api.v1.serializers.invoice import InvoiceSerializer
from sreps.core.models import Customer, Invoice


class CustomerViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAdminUser,)

    @action(detail=True, methods=['GET'], name='Customer invoices')
    def invoices(self, request, pk=None):
        """Get invoices made by a customer."""

        customer = get_object_or_404(self.queryset, pk=pk)

        invoices = Invoice.objects.filter(
            customer=customer).order_by('-datetime_created')
        serializer = InvoiceSerializer(invoices, many=True)

        return Response(serializer.data)
