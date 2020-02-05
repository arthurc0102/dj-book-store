from rest_framework import serializers

from books.serializers import BookSerializer

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('creator',)
