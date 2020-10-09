from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer


class OrderAPI(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated, )
