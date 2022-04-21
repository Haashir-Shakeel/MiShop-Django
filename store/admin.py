from django.contrib import admin
from store.models import Customer,Order,OrderItem,ShippingAddress,Product
# Register your models here.

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Product)


