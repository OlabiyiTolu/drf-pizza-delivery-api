from django.urls import path
from .views import pizzaView, pizzaIdView, pizzaUpdateOrderStatusView, pizzaUserOrderView, pizzaUserOrderDetailView

urlpatterns = [
    path('orders/', pizzaView.as_view(), name='orders'),
    path('order/<int:order_id>/', pizzaIdView.as_view(),name='order'),
    path('update-status/<int:order_id>/', pizzaUpdateOrderStatusView.as_view(),name='update'),
    path('user-orders/<int:user_id>/orders', pizzaUserOrderView.as_view(),name='users_orders'),
    path('user-order/<int:user_id>/order/<int:order_id>/', pizzaUserOrderDetailView.as_view(),name='user_order_detail'),
]
