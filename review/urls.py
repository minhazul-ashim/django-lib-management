from django.contrib import admin
from django.urls import path, include;
from . import views;
from django.conf import settings;
from django.conf.urls.static import static;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.ReviewCreateView.as_view(), name="createReview")
]