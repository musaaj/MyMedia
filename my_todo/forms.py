from django import forms
from .models import User, Todo

class CreateUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'phone_number',
                'password',
            ]
        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control'})
            }

class CreateTodoForm(forms.Form):
    title = forms.CharField(max_length=256)

class LoginForm(forms.Form):
    phone_number = forms.CharField(
            max_length=11,
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    password = forms.CharField(
            max_length=256,
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )

