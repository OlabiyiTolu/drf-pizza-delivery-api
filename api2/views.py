from .serializers import pizzaDeliverySerializers, pizzaDeliveryUpdateStatusSerializers
from .models import User, pizzaDeliveryModel
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import get_object_or_404 #as _get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework_simplejwt.views import TokenBlacklistView,TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework import viewsets

User = get_user_model()

class pizzaView(generics.ListAPIView, generics.CreateAPIView): 
    serializer_class = pizzaDeliverySerializers
    queryset = pizzaDeliveryModel.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Get all orders', operation_description="welcome")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create an order")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class pizzaIdView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = pizzaDeliverySerializers
    queryset = pizzaDeliveryModel.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Get the details of an order by its ID')
    def get(self, request, order_id):
        pizza = get_object_or_404(pizzaDeliveryModel, pk=order_id)
        serializer = self.serializer_class(instance=pizza)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary='Update an order by its ID')
    def put(self, request, order_id):
        order = get_object_or_404(pizzaDeliveryModel, pk=order_id)
        serializer = self.serializer_class(instance=order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Delete an order by its ID')
    def delete(self, request, order_id):
        pizza = get_object_or_404(pizzaDeliveryModel, pk=order_id)
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class pizzaUpdateOrderStatusView(generics.GenericAPIView):
    serializer_class = pizzaDeliveryUpdateStatusSerializers
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary='Update the status of an order')
    def put(self, request, order_id):
        order = get_object_or_404(pizzaDeliveryModel, pk=order_id)
        serializer = self.serializer_class(instance=order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class pizzaUserOrderView(mixins.RetrieveModelMixin, generics.ListAPIView, generics.GenericAPIView):
    serializer_class = pizzaDeliverySerializers
    queryset = pizzaDeliveryModel.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary='Get all order(s) by a specific user')
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        pizza = pizzaDeliveryModel.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=pizza, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class pizzaUserOrderDetailView(generics.GenericAPIView):
    serializer_class = pizzaDeliverySerializers
    queryset = pizzaDeliveryModel.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary='Get the detail of an order by a specific user')
    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        pizza = pizzaDeliveryModel.objects.all().filter(customer=user).filter(pk=order_id)
        serializer = self.serializer_class(instance=pizza, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)