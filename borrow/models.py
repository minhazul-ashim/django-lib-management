from django.db import models
from django.contrib.auth.models import User;
from book.models import Book;

# Create your models here.
class Borrow(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrows");
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrow_books");
    createdAt = models.DateTimeField(auto_now_add = True);
    is_returned = models.BooleanField(default=False)