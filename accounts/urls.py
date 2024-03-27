
from django.urls import path
from .views import UserRegistrationView, UserLoginView, userlogoutView, UserAccountUpdateView
from django.contrib.auth.decorators import login_required
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', userlogoutView, name='logout'),
    path('profile/', login_required(UserAccountUpdateView.as_view()), name='profile' )
]