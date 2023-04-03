from django import forms
from django.forms.utils import ErrorList
from .models import User, Todo


class PErrorList(ErrorList):

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return ''.join(['<p class="text-danger">%s</p>' % e for e in self])


class CreateUserForm(forms.ModelForm):

    class Meta:
        model = User
        error_css_class = 'tex-danger'
        fields = [
                'first_name',
                'last_name',
                'email',
                'password',
            ]
        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control'})
            }
        error_messages = {
                'email': {
                    'unique': 'User with this email already exists',
                }
            }


class CreateTodoForm(forms.Form):
    title = forms.CharField(max_length=256)

class LoginForm(forms.Form):
    email = forms.EmailField(
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    password = forms.CharField(
            max_length=256,
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )

