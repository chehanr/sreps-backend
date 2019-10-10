from rest_framework import serializers
from sreps.api.v1.serializers.product_category import (ProductCategoryDetailSerializer,
                                                       ProductCategorySerializer)
from sreps.core.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'name',
            'stock_quantity',
            'low_stock_threshold',
            'base_price',
            'discount_amount',
            'price',
            'is_available',
            'datetime_created',
        )

    def get_price(self, instance):
        return instance.base_price - (instance.base_price * instance.discount_amount) / 100


class ProductDetailSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'name',
            'description',
            'stock_quantity',
            'low_stock_threshold',
            'base_price',
            'discount_amount',
            'price',
            'is_available',
            'datetime_expire',
            'datetime_created',
        )

    def to_representation(self, instance):
        """ 
        Overide the representation to support POST 
        requests with foreign key assignments.
        """

        data = super().to_representation(instance)

        if data['category']:
            data['category'] = ProductCategoryDetailSerializer(
                ProductCategory.objects.get(pk=data['category'])).data

        return data

    def get_price(self, instance):
        return instance.base_price - (instance.base_price * instance.discount_amount) / 100
