from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Redactor


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = [
            "username",
            "first_name",
            "last_name",
            "years_of_experience"
        ]


class RedactorUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Redactor
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "years_of_experience"
        ]


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by title"
            }
        ),
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        ),
    )
