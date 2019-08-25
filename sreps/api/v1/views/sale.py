from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from sreps.api.v1.serializers.sale import SaleSerializer
from sreps.core.models import Sale


class SaleViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,):

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (IsAdminUser,)
