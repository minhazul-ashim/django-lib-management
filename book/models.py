from django.db import models
from category.models import Category;
from django.contrib.auth.models import User;

# Create your models here.
class Book(models.Model) :
    title = models.CharField(max_length=25);
    description = models.CharField(max_length=500);
    image = models.ImageField(upload_to='uploads/media/', blank=True, null=True);
    price = models.DecimalField(decimal_places=2, max_digits=12);
    category=models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)