from django.urls import path
from .views import DepositMoneyView
from django.conf import settings;
from django.conf.urls.static import static;


# app_name = 'transactions'
urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)