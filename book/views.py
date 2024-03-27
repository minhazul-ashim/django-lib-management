from django.shortcuts import render
from . import models;
from django.views.generic import DetailView
from review.forms import ReviewForm
from review.models import Review
# Create your views here.
class BookDetailView(DetailView) :
    model = models.Book;
    pk_url_kwarg = 'pk';
    template_name = 'bookDetail.html';
    context_object_name = 'book';

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm
        context['reviews'] = Review.objects.all();
        return context;