from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password']

    username = UsernameField(
        label=_("ユーザ名"),
        widget=forms.TextInput(attrs={'autofocus': True}),
        error_messages={
            "required": "必須項目です",
        }
    )

    password = forms.CharField(
        label=_("パスワード"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        error_messages={
            "required": "必須項目です",
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.label = ""

    error_messages = {
        'invalid_login': _(
            "ユーザ名とパスワードが間違いです"
        ),
        'inactive': _(
            "無効です"
        ),
    }


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','password1','password2','age',)
    
    username = UsernameField(
        label=_("ユーザ名"),
        widget=forms.TextInput(attrs={'autofocus': True}),
        error_messages={
            "required": "必須項目です",
            'unique': "ユーザ名が重複しています",
        },
    )

    password1 = forms.CharField(
        label=_("パスワード"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        error_messages={
            "required": "必須項目です",
        }
    )

    password2 = forms.CharField(
        label=_("パスワード再確認用"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        error_messages={
            "required": "必須項目です",
        }
    )

    age = forms.CharField(
        label=_("年齢"),
        strip=False,
        widget=forms.NumberInput(attrs={}),
        error_messages={
            "required": "必須項目です",
        }
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.label = ""

    error_messages = {
        'password_mismatch': _('パスワードが異なります'),
    }

