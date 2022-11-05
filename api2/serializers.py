from rest_framework import serializers
from .models import pizzaDeliveryModel

class pizzaDeliverySerializers(serializers.ModelSerializer):
    order_status = serializers.HiddenField(default = 'PENDING')
    # pizza_size = serializers.CharField(max_length=30)
    quantity = serializers.IntegerField()
    flavour = serializers.CharField(max_length=30)
    customer_location = serializers.CharField(max_length=30)

    class Meta:
        model = pizzaDeliveryModel
        fields = ['order_status', 'pizza_size', 'quantity', 'flavour','customer_location']

class pizzaDeliveryUpdateStatusSerializers(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length=30)

    class Meta:
        model = pizzaDeliveryModel
        fields = ['order_status']