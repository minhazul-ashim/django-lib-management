from django.urls import path
from .views import DepositMoneyView, WithdrawMoneyView
from django.conf import settings;
from django.conf.urls.static import static;


# app_name = 'transactions'
urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    # path("report/", TransactionReportView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)