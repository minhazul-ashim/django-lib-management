from django.contrib.auth.forms import UserCreationForm;
from django.contrib.auth.models import User;
from django.contrib.auth import authenticate, login
from django import forms;
from accounts.models import UserAccount;

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True, request=None):
        user = super().save(commit=False)
        if commit:
            user.save()
            if request is not None and user is not None:
                user = authenticate(username=user.username, password=self.cleaned_data['password1'])
                if user is not None:
                    login(request, user)
                    UserAccount.objects.create(user=user)

        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        return user