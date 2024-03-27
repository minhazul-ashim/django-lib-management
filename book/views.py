from django.shortcuts import render, redirect
from .models import Book;
from django.views.generic import DetailView
from review.forms import ReviewForm
from review.models import Review
from accounts.models import UserAccount;
from borrow.models import Borrow;
from book.models import Book;
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator

class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'pk'
    template_name = 'bookDetail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        context['reviews'] = Review.objects.filter(book=context['book'])
        context['canReview'] = False
        if self.request.user.is_authenticated:
            try:
                borrow = Borrow.objects.get(book=context['book'], user=self.request.user)
                context['canReview'] = True
            except Borrow.DoesNotExist:
                pass
        return context


@method_decorator(require_POST, name='dispatch')
class BorrowBook(DetailView):
    model = Book

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        user = UserAccount.objects.get(user=request.user)
        user.balance -= book.price
        user.save()
        borrow = Borrow.objects.create(user=request.user, book=book)
        return redirect('profile', pk=book.pk)