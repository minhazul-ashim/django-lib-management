from django.urls import path
from . import views;
urlpatterns = [
    path('<int:pk>/', views.BookDetailView.as_view(), name='detailPage'),
]