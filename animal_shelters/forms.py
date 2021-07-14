from django import forms

from animal_shelters.models import Owner, Animal, Food, AnimalType, AnimalCare


class AccountForm(forms.ModelForm):
    class Meta:
        model = Owner
        exclude = ['user']


class SheltersForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['city']


class AddAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ['owner']


class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ['id']


class AddTypeForm(forms.ModelForm):
    class Meta:
        model = AnimalType
        exclude = ['id']


class AddCareForm(forms.ModelForm):
    class Meta:
        model = AnimalCare
        exclude = ['id']
