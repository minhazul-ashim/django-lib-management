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



class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance:
    #         try:
    #             user_account = self.instance.account
    #         except UserAccount.DoesNotExist:
    #             user_account = None
    #             user_address = None

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        return user