from rest_framework import serializers
from sreps.core.models import ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'name',
            'datetime_created',
        )


class ProductCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'name',
            'description',
            'datetime_created',
        )
