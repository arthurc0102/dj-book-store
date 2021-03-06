from rest_framework.viewsets import ModelViewSet

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
