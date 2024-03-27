from typing import Any
from django.views.generic import TemplateView;
from book.models import Book;
from category.models import Category;

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        category_id = self.kwargs.get('id')
        if category_id is not None:
            category = Category.objects.get(id=category_id)
            context['books'] = Book.objects.filter(category=category)
        else:
            context['books'] = Book.objects.all()

        context['categories'] = Category.objects.all()
        return context