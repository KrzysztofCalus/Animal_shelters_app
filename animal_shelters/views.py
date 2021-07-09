from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from animal_shelters.models import Owner

# Create your views here.
from django.views.generic import CreateView


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class AccountView(generic.CreateView):
    model = Owner
    fields = '__all__'
    success_url = reverse_lazy('account')
    template_name = 'owner_form.html'
