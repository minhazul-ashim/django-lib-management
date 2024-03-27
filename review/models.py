from django.db import models
from book.models import Book;
from django.contrib.auth.models import User;

# Create your models here.
class Review(models.Model) :
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review");
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length = 30);
    review = models.CharField(max_length = 150);
    createdAt = models.DateTimeField(auto_now_add = True);