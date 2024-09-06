from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_STYLE = "bg-blanco border-2 border-verder_claro rounded-lg focus:border-verder_claro focus:ring-verder_claro"
CHECKBOX_STYLE = "bg-blanco border-2 border-verder_claro focus:border-verder_claro focus:ring-verder_claro"

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Ingrese su usuario",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Ingrese su contrasena",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Confirme su contrasena",
            }
        )
    )
    checkbox = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "class": CHECKBOX_STYLE,
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "checkbox")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Ingrese su usuario",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Ingrese su contrasena",
            }
        )
    )
    checkbox = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": CHECKBOX_STYLE,
            },
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password", "checkbox")
        