from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
# from simplemathcaptcha.fields import MathCaptchaField
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm,):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# some_text_field = models.CharField(max_length=50)
# captcha = MathCaptchaField()


class Meta:
    model = User
    fields = ['username', 'password1', 'password2']
    widgets = {
        'username': TextInput(attrs={'class': 'form-control'}),
    }
