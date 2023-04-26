from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User
from tkinter import Widget

class ManagerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        # widgets = {
        #      'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
        #      'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        #      'password1' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        #      'password2' : forms.PasswordInput(attrs={'class':'password','placeholder':'password'}),
        #  }
       
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager1 = True
        user.save()
        return user    


class DeveloperRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        # widgets = {
        #      'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
        #      'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
        #      'password1' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        #      'password2' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'reenter password'}),
        #  }

        def _init_(self, *args, **kwargs):
            super()._init_(*args, **kwargs)

            self.fields['username'].widget.attrs.update({
            'class' : 'form-control','placeholder': 'Enter your user name','id': 'inputFirstName','type': 'text'})

            self.fields['email'].widget.attrs.update({
             'class' : 'form-control','placeholder': 'name@example.com','id': 'inputEmail','type': 'email'}),

            self.fields['password1'].widget.attrs.update({
             'class' : 'form-control','placeholder': 'Create a password','id': 'inputPassword','type': 'password'}),

            self.fields['password2'].widget.attrs.update({
             'class' : 'form-control','placeholder': 'Confirm password','id': 'inputPasswordConfirm','type': 'password'}),

    

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_developer = True
        user.save()
        return user       
    
    
# class SignUpForm(forms.Form):
#     CHOICES = (
#         ('manager', 'Manager'),
#         ('developer', 'Developer'),
#     )
#     account_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
