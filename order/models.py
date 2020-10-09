from django.db import models
from django.utils import timezone
from book.models import Book
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(null=True)
    plated_end_at = models.DateTimeField(default=(timezone.now()+timedelta(days=15)))
