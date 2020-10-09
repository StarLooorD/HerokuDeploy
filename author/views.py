from .models import Author
from rest_framework import viewsets
from .serializers import AuthorSerializer
from rest_framework.permissions import IsAdminUser


# Views for Django REST API
class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminUser, )
