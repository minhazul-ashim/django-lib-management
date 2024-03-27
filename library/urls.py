from django.contrib import admin
from django.urls import path, include;
from . import views;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name="homePage"),
    path('accounts/', include('accounts.urls')),
    path('transactions/', include('transactions.urls'))
]
