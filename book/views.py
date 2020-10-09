from .models import Book
from rest_framework import viewsets, permissions
from .serializers import BookSerializer, TerseBookSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner


# View for Django REST API
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated)
