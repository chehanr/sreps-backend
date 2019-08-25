from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import exceptions, filters, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from sreps.api.v1.serializers.invoice import InvoiceSerializer
from sreps.api.v1.serializers.user import UserSerializer
from sreps.core.models import Invoice


class UserViewSet(mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet,):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_throttles(self):
        if self.action == 'create':
            self.throttle_scope = 'user.create'

        return super().get_throttles()

    def list(self, request):
        queryset = get_user_model().objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    @action(detail=True, methods=['GET'], name='Salesperson invoices')
    def invoices(self, request, pk=None):
        """Get invoices made by a salesperson."""

        user = get_object_or_404(self.queryset, pk=pk)

        invoices = Invoice.objects.filter(
            salesperson=user).order_by('-datetime_created')
        serializer = InvoiceSerializer(invoices, many=True)

        return Response(serializer.data)
