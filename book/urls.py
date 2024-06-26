from django.urls import path
from . import views;
from django.conf import settings;
from django.conf.urls.static import static;

urlpatterns = [
    path('<int:pk>/', views.BookDetailView.as_view(), name='detailPage'),
    path('book/borrow/<int:pk>/', views.BorrowBook.as_view(), name='borrowBook'),
    path('book/return/<int:pk>/', views.ReturnBook.as_view(), name='bookReturn'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)