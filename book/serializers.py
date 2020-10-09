from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Book
        fields = '__all__'


class TerseBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'description')
