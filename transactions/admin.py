from django.contrib import admin
from .models import Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'transaction_type']
    
    def save_model(self, request, obj, form, change):
        obj.account.balance += obj.amount
        obj.account.save()
        super().save_model(request, obj, form, change)