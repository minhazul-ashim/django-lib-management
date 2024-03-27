from django import forms
from .models import Transaction
from django import forms
from accounts.models import UserAccount

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit=True):
        self.instance.account = self.account
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 500
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'Minimum Deposit Amount is ${min_deposit_amount} '
            )

        return amount


class WithdrawForm(TransactionForm):

    def clean_amount(self):
        account = self.account
        balance = account.balance
        amount = self.cleaned_data.get('amount')

        if amount > balance:
            raise forms.ValidationError(
                f'You have insufficient balance in your account.'
            )

        return amount



# class TransactionForm(forms.Form):
#     account_number = forms.CharField(label='Account Number')
#     amount = forms.DecimalField(label='Amount')
    
#     def clean(self):
#         cleaned_data = super().clean()
#         account_number = cleaned_data.get('account_number')
#         amount = cleaned_data.get('amount')
#         user_account = UserBankAccount.objects.filter(account_no=account_number).first()
#         if user_account == None:
#             raise forms.ValidationError("Account not found!!")
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({
                
#                 'class' : (
#                     'appearance-none block w-full bg-gray-200 '
#                     'text-gray-700 border border-gray-200 rounded '
#                     'py-3 px-4 leading-tight focus:outline-none '
#                     'focus:bg-white focus:border-gray-500'
#                 ) 
#             })