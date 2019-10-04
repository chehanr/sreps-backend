from rest_framework import serializers
from sreps.api.v1.serializers.customer import CustomerSerializer
from sreps.api.v1.serializers.user import UserSerializer
from sreps.core.models import Invoice, Sale


class InvoiceSerializer(serializers.ModelSerializer):
    salesperson = UserSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    products_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = (
            'id',
            'salesperson',
            'customer',
            'description',
            'other_cost',
            'tax_amount',
            'products_price',
            'total_price',
            'is_paid',
            'datetime_pay_due',
            'datetime_paid',
            'datetime_created',
        )

    def get_products_price(self, instance):
        p = 0
        sale_objs = Sale.objects.filter(invoice__id=instance.id)

        for obj in sale_objs:
            product = obj.product
            p += product.base_price - \
                (product.base_price * product.discount_amount) / 100

        return p

    def get_total_price(self, instance):
        p = self.get_products_price(instance)
        tp = p + instance.other_cost + (p * instance.tax_amount) / 100

        return tp
