from django.contrib import admin
from .models import pizzaDeliveryModel

@admin.register(pizzaDeliveryModel)
class filtering(admin.ModelAdmin):
    list_display = ['id', 'flavour', 'pizza_size', 'order_status', 'quantity', 'customer', 'customer_location']
    list_filter = ['flavour', 'order_status', 'placed_at', 'delivered_at']