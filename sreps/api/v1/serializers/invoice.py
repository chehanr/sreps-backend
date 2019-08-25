from rest_framework import serializers
from sreps.api.v1.serializers.customer import CustomerSerializer
from sreps.api.v1.serializers.user import UserSerializer
from sreps.core.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    salesperson = UserSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = (
            'id',
            'salesperson',
            'customer',
            'description',
            'other_cost',
            'tax_amount',
            'is_paid',
            'datetime_pay_due',
            'datetime_paid',
            'datetime_created',
        )
