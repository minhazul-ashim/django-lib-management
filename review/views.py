from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView;
from . import forms;

# Create your views here.
class ReviewCreateView(CreateView) :
    template_name = '../book/templates/bookDetail.html';
    form_class = forms.ReviewForm;
    success_url = reverse_lazy("homePage")