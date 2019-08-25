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
