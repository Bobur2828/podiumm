from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm,ProfileForm,UserPasswordChangeForm,PofilForm
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView
from my_app.models import Profile
def Profile(request):
    if request.method == 'POST':
        form = PofilForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('userauth:profile')
     
            
    else:
        form = PofilForm()
    return render(request,'anketa.html',{'form':form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,(f" Salom {user.first_name} {user.last_name} sizni yana ko'rib turganimizdan hursandmiz"))
                return redirect('index')
            else:
                messages.error(request,("Login yoki parolni notogri kiritdingiz  iltimos qayta urinib koring "))

    else:
        form = LoginForm()



    return render(request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,("Shaxsiy kabinetdan chiqdingiz"))
    return redirect('index')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,(" Ro'yhatdan o'tish muvaffaqiyatli yakunlandi "))
            return HttpResponseRedirect(reverse('userauth:login')) 
            
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

class ProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class=ProfileForm
    template_name= 'my_account.html'
    def get_success_url(self):
        messages.success(self.request,(" Ma'lumotlar o'zgartirish muvaffaqiyatli yakunlandi "))

        return reverse_lazy('userauth:profile')

    def get_object(self):
        return self.request.user
    
class UserPasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        messages.success(self.request, "Parolingiz muvaffaqiyatli o'zgartirildi")
        return super().form_valid(form)
    


    
    
    
