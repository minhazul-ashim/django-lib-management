from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from accounts.models import UserAccount
from django.views import View
from django.shortcuts import redirect
from borrow.models import Borrow;

class UserRegistrationView(FormView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        user = form.save(request=self.request)
        login(self.request, user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('homePage')

def userlogoutView(request) :
    logout(request);
    return redirect('login')


class UserAccountUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        borrows = Borrow.objects.filter(user=request.user);
        balance = UserAccount.objects.get(user=self.request.user).balance;
        return render(request, self.template_name, {'form': form, 'borrows': borrows, 'balance' : balance})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})