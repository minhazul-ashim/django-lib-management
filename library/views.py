from typing import Any
from django.views.generic import TemplateView;
from book.models import Book;
from category.models import Category;

class HomePageView(TemplateView) :
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['categories'] = Category.objects.all()
        return context