from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  # Ensure this imports your custom user model

class CivilianRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phonenumber = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser  # Ensure CustomUser model has username, email, and phonenumber fields
        fields = ['username', 'email', 'phonenumber', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phonenumber = self.cleaned_data['phonenumber']
        if commit:
            user.save()
        return user

class CivilianLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
