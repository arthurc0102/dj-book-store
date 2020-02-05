from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django_filters import rest_framework as filters

from utils.permissions import IsAdminUserOrReadOnly

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('is_online',)
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
