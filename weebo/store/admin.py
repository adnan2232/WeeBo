from django.contrib import admin
from .models import *


admin.site.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock')
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product','order','quantity')

admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(ShippingAddress)

class OrderedAdmin(admin.ModelAdmin):
    list_display = ('customer','order','datetime','orderstatus','address')
admin.site.register(Ordered,OrderedAdmin)