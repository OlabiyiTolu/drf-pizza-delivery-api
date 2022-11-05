from random import choices
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class pizzaDeliveryModel(models.Model):
    PIZZA_SIZE = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA LARGE', 'extra large'),
        )
    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN TRANSIT', 'in transit'),
        ('DELIVERED', 'delivered'),
    )

    order_status = models.CharField(max_length=30, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    pizza_size = models.CharField(max_length=30, choices=PIZZA_SIZE, default=PIZZA_SIZE[0][0])
    quantity = models.IntegerField()
    flavour = models.CharField(max_length=30)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_location = models.CharField(max_length=30)
    placed_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order place by {self.customer} at {self.placed_at} to be delivered to {self.customer_location}'