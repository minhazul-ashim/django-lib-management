from django.shortcuts import render
from django.views.generic import ListView;
from . import models;

# Create your views here.
class ListBorrows(ListView) :
    template_name = '../authservice/templates/profile.html';
    model = models.Borrow;
    context_object_name = 'orders'

def createBorrow(request) :
    pass;