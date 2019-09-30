from django.urls import path

from rest_framework.routers import DefaultRouter
from sreps.api.v1.views.customer import CustomerViewSet
from sreps.api.v1.views.invoice import InvoiceViewSet
from sreps.api.v1.views.me import MeView
from sreps.api.v1.views.product import ProductViewSet
from sreps.api.v1.views.product_category import ProductCategoryViewSet
from sreps.api.v1.views.sale import SaleViewSet
from sreps.api.v1.views.user import UserViewSet

app_name = 'api-v1'

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
]

router = DefaultRouter()
router.register(r'user', UserViewSet, base_name='user')
router.register(r'customer', CustomerViewSet, base_name='customer')
router.register(r'product', ProductViewSet, base_name='product')
router.register(r'product-category', ProductCategoryViewSet, base_name='product-category')
router.register(r'sale', SaleViewSet, base_name='sale')
router.register(r'invoice', InvoiceViewSet, base_name='invoice')

urlpatterns.extend(router.urls)
