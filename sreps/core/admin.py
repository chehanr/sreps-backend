from django.contrib import admin

from sreps.core.models import Customer, Invoice, Product, ProductCategory, Sale

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Sale)
