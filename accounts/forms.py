from django.contrib.auth.forms import UserCreationForm;
from django.contrib.auth.models import User;
from django import forms;
from accounts.models import UserAccount;

class UserRegisterForm(UserCreationForm) :
    class Meta :
        model = User;
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',];

    def save(self, commit=True) :
        user = super().save(commit=False);
        if commit == True :
            user.save();

            UserAccount.objects.create(
                user = user
            )



# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance:
#             try:
#                 user_account = self.instance.account
#             except UserAccount.DoesNotExist:
#                 user_account = None
#                 user_address = None

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()

#             user_account, created = UserAccount.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
#             user_address, created = UserAccount.objects.get_or_create(user=user) 

#             user_account.account_type = self.cleaned_data['account_type']
#             user_account.gender = self.cleaned_data['gender']
#             user_account.birth_date = self.cleaned_data['birth_date']
#             user_account.save()

#             user_address.street_address = self.cleaned_data['street_address']
#             user_address.city = self.cleaned_data['city']
#             user_address.postal_code = self.cleaned_data['postal_code']
#             user_address.country = self.cleaned_data['country']
#             user_address.save()

#         return user