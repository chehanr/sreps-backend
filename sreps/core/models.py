from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Customer(models.Model):
    """
    Customer model.
    """

    name = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    address = models.TextField(
        blank=True,
        null=True
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        if self.name:
            return f'{self.pk}, {self.name}'

        return self.pk


class Invoice(models.Model):
    """
    Invoice model.
    """

    salesperson = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    other_cost = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0)]
    )
    tax_amount = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0)]
    )
    is_paid = models.BooleanField(
        default=False
    )
    datetime_pay_due = models.DateTimeField(
        blank=True,
        null=True
    )
    datetime_paid = models.DateTimeField(
        blank=True,
        null=True
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Invoice")
        verbose_name_plural = _("Invoices")

    def __str__(self):
        if self.datetime_created:
            return f'{self.pk}, CREATED: {self.datetime_created}'

        return self.pk


class ProductCategory(models.Model):
    """
    ProductCategory model.
    """

    name = models.CharField(
        max_length=128,
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product model.
    """

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    stock_quantity = models.PositiveSmallIntegerField(
        default=0
    )
    base_price = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0)]
    )
    discount_amount = models.FloatField(
        default=0,
        validators=[MinValueValidator(0.0)]
    )
    is_available = models.BooleanField(
        default=True
    )
    datetime_expire = models.DateTimeField(
        blank=True,
        null=True
    )
    datetime_created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f'{self.pk}, {self.name}'


class Sale(models.Model):
    """
    Sale model.
    """

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.PositiveSmallIntegerField(
        default=0
    )

    class Meta:
        verbose_name = _("Sale")
        verbose_name_plural = _("Sales")

    def __str__(self):
        if self.product:
            return f'{self.pk}, PRODUCT: {self.product}, QTY: {self.quantity}'

        return self.pk
