from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from my_app.models import Profile, DAVLAT, SHAXAR
class LoginForm(forms.Form):
    username = forms.CharField(label='Username kiriting')
    password = forms.CharField(label='Parolingizni kiriting',widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    username=forms.CharField(label='Login kiriting')
    password=forms.CharField(label='Parol yarating', widget=forms.PasswordInput )
    password2=forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput )

    class Meta:
        model= User
        fields=['username' ,'email','password','password2','first_name','last_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password']!= cd['password2']:
           
            raise forms.ValidationError('Parollar bir biriga mos emas')
        
        else:
            return cd['password2']
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bunday email allaqachon mavjud')
        return email
from django.contrib.auth import get_user_model
class ProfileForm(forms.ModelForm):
    username=forms.CharField(label='Username', disabled=True)
    email = forms.CharField(label='Email', disabled=True)

    class Meta:
        model = get_user_model()
        fields=('first_name', 'last_name', 'username', 'email')

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Eski parolingiz', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Yangi parol', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Parolni tasdiqlang', widget=forms.PasswordInput)

class PofilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','image', 'phone_number', 'country', 'city', 'adress', 'zipcode']
        labels = {
            'user': '<NAME>',
            'image': 'Rasm',
            'phone_number': 'Telefon raqami',
            'country': 'Davlat',
            'city': 'Shahar',
            'adress': 'Manzil',
            'zipcode': 'Indeks',
        }
        widgets = {
            'country': forms.Select(choices=DAVLAT),
            'city': forms.Select(choices=SHAXAR),
        }

