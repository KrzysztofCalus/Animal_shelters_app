from django.forms import ModelForm

from animal_shelters.models import Owner


class AccountForm(ModelForm):
    class Meta:
        model = Owner
        exclude = ['user']


