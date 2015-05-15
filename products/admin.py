from django.contrib import admin
from products.models import Product, RequestProduct

class RequestProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'added', 'completed']

admin.site.register(Product)
admin.site.register(RequestProduct, RequestProductAdmin)

