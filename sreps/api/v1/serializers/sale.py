from rest_framework import serializers
from sreps.api.v1.serializers.invoice import InvoiceSerializer
from sreps.api.v1.serializers.product import ProductSerializer
from sreps.core.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Sale
        fields = (
            'id',
            'invoice',
            'product',
            'quantity',
        )
