from django import forms

from animal_shelters.models import Owner


class AccountForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude = ['user']


class SheltersForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['city']