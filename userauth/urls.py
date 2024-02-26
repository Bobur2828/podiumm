from django.urls import path
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from . import views

app_name='userauth'

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.user_register,name='register'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('password/',views.UserPasswordView.as_view(),name='password'),
    path('password_change/',views.PasswordChangeView.as_view(template_name='change_password.html'),name='password_change_done'),
    path('anketa/',views.Profile,name='anketa'),



]