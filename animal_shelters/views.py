from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic, View

from animal_shelters.forms import AccountForm, SheltersForm

# Create your views here.
from animal_shelters.models import Owner, AnimalOwner, Animal


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class AccountView(View):
    def get(self, request):
        if Owner.objects.filter(user_id=self.request.user.id).exists():
            account = Owner.objects.get(user_id=self.request.user.id)
            form = AccountForm(instance=account)
            return render(request, 'owner_form.html', {'form': form})
        else:
            form = AccountForm()
            return render(request, 'owner_form.html', {'form': form})

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            user = self.request.user.id
            shelter_name = form.cleaned_data['shelter_name']
            street = form.cleaned_data['street']
            number = form.cleaned_data['number']
            city = form.cleaned_data['city']
            postal_code = form.cleaned_data['postal_code']
            shelter = form.cleaned_data['shelter']
            capacity = form.cleaned_data['capacity']
            opening_hours = form.cleaned_data['opening_hours']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            about = form.cleaned_data['about']
            regulations = form.cleaned_data['regulations']
            donations = form.cleaned_data['donations']
            if Owner.objects.filter(user_id=self.request.user.id).exists():
                Owner.objects.filter(user_id=self.request.user.id).update(user_id=user, street=street, number=number,
                                                                          city=city, postal_code=postal_code,
                                                                          shelter=shelter, capacity=capacity,
                                                                          opening_hours=opening_hours, phone=phone,
                                                                          email=email, about=about,
                                                                          regulations=regulations, donations=donations,
                                                                          shelter_name=shelter_name)
            else:
                Owner.objects.create(user_id=user, street=street, number=number, city=city, postal_code=postal_code,
                                     shelter=shelter, capacity=capacity, opening_hours=opening_hours, phone=phone,
                                     email=email, about=about, regulations=regulations, donations=donations,
                                     shelter_name=shelter_name)
            return HttpResponseRedirect('account')


class SheltersView(View):
    def get(self, request):
        shelters = Owner.objects.filter(shelter=True)
        form = SheltersForm()
        return render(request, 'shelters.html', {"shelters": shelters,
                                                 "form": form})

    def post(self, request):
        form = SheltersForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            shelters = Owner.objects.filter(city=city).filter(shelter=True)
        return render(request, 'shelters.html', {"shelters": shelters,
                                                 "form": form})


class AddShelterAnimalsView(View):
    pass


class ShelterAnimalsView(View):
    def get(self, request, shelter_id):
        t = Owner.objects.get(id=shelter_id)
        animals = t.animal_set.all()
        return render(request, 'shelter_animals.html', {'animals': animals})
