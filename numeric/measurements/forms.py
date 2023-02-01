from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class AddMeasurements(forms.ModelForm):
    class Meta:  # this class for formatting view of fields
        model = Measurements
        fields = ['Shoulders', 'Chest', 'Waist', 'Buttocks', 'Hips', 'Weight']
        widgets = {  # this is for individual design fields
            'Shoulders': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Chest': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Waist': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Buttocks': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Hips': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Weight': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': None, 'type': 'number',}),
        }
