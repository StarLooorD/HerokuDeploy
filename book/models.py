from django.db import models
from django.contrib.auth import get_user_model
from author.models import Author

User = get_user_model()


class Book(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    count = models.IntegerField(blank=True, default=10)
    authors = models.ManyToManyField(Author, related_name='books')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
