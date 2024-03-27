from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView;
from . import forms;
from book.models import Book;
from django.contrib.auth.models import User;

class ReviewCreateView(CreateView):
    template_name = 'bookDetail.html'
    form_class = forms.ReviewForm
    success_url = reverse_lazy("homePage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get('id')
        book = Book.objects.get(id=book_id)
        context['book'] = book
        context['user'] = self.request.user
        
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.get_context_data().get('book')
        return super().form_valid(form)