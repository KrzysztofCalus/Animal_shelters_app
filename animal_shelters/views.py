from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic, View
from datetime import date

from animal_shelters.forms import AccountForm, SheltersForm, AddAnimalForm, AddFoodForm, AddTypeForm, AddCareForm

# Create your views here.
from animal_shelters.models import Owner, AnimalOwner, Animal, Food, AnimalType, AnimalCare


class SignUpView(generic.CreateView):
    """
    Signup for new users
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class AccountView(View):
    """
    Checking if user already add account data if yes allowing to change if no allowing to add
    """

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
    """
    Showing all shelters and allowing to search by 'city'
    """

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
    """
    Add animal data and assign to user which is creating
    """

    def get(self, request):
        form = AddAnimalForm()
        return render(request, 'add_animal_form.html', {'form': form})

    def post(self, request):
        form = AddAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            sex = form.cleaned_data['sex']
            chip_number = form.cleaned_data['chip_number']
            birth_date = form.cleaned_data['birth_date']
            colour = form.cleaned_data['colour']
            distinguishing_marks = form.cleaned_data['distinguishing_marks']
            weight = form.cleaned_data['weight']
            size = form.cleaned_data['size']
            description = form.cleaned_data['description']
            animal_type = form.cleaned_data['animal_type']
            picture = form.cleaned_data['picture']
            food = form.cleaned_data['food']
            a = Animal.objects.create(name=name, sex=sex, chip_number=chip_number, birth_date=birth_date, colour=colour,
                                      distinguishing_marks=distinguishing_marks, weight=weight, size=size,
                                      description=description, animal_type_id=animal_type.id, picture=picture,
                                      food_id=food.id)
            owner = Owner.objects.get(user_id=self.request.user.id)
            AnimalOwner.objects.create(animal_id=a.id, owner_id=owner.id, start=date.today())
        return HttpResponseRedirect('/owner/animals')


class EditShelterAnimalsView(View):
    """
    Editing animal data
    """

    def get(self, request, animal_id):
        animal = Animal.objects.get(id=animal_id)
        form = AddAnimalForm(instance=animal)
        return render(request, 'add_animal_form.html', {'form': form})

    def post(self, request, animal_id):
        form = AddAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            sex = form.cleaned_data['sex']
            chip_number = form.cleaned_data['chip_number']
            birth_date = form.cleaned_data['birth_date']
            colour = form.cleaned_data['colour']
            distinguishing_marks = form.cleaned_data['distinguishing_marks']
            weight = form.cleaned_data['weight']
            size = form.cleaned_data['size']
            description = form.cleaned_data['description']
            animal_type = form.cleaned_data['animal_type']
            picture = form.cleaned_data['picture']
            food = form.cleaned_data['food']
            Animal.objects.filter(id=animal_id).update(name=name, sex=sex, chip_number=chip_number,
                                                       birth_date=birth_date, colour=colour,
                                                       distinguishing_marks=distinguishing_marks, weight=weight,
                                                       size=size,
                                                       description=description, animal_type_id=animal_type,
                                                       picture=picture, food_id=food)
        return HttpResponseRedirect('/owner/animals')


class ShelterAnimalsView(View):
    """
    Showing animals in chosen shelter
    """

    def get(self, request, shelter_id):
        o = Owner.objects.get(id=shelter_id)
        animals = o.animal_set.all()
        return render(request, 'shelter_animals.html', {'animals': animals})


class OwnerAnimalsView(View):
    """
    Showing animals assign to logged user
    """

    def get(self, request):
        if Owner.objects.filter(user_id=self.request.user.id).exists():
            o = Owner.objects.get(user_id=self.request.user.id)
            animals = o.animal_set.all()
            return render(request, 'owner-animals.html', {'animals': animals})
        else:
            return render(request, 'no-animals.html')


class FoodView(View):
    """
    Showing all added food's
    """

    def get(self, request):
        foods = Food.objects.all()
        return render(request, 'food.html', {'foods': foods})


class AddFoodView(View):
    """
    Allowing to add food data
    """

    def get(self, request):
        form = AddFoodForm()
        return render(request, 'add_food_form.html', {'form': form})

    def post(self, request):
        form = AddFoodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age_start = form.cleaned_data['age_start']
            age_end = form.cleaned_data['age_end']
            weight_start = form.cleaned_data['weight_start']
            weight_end = form.cleaned_data['weight_end']
            amount = form.cleaned_data['amount']
            Food.objects.create(name=name, age_start=age_start, age_end=age_end, weight_start=weight_start,
                                weight_end=weight_end, amount=amount)
        return HttpResponseRedirect('/food')


class AnimalTypeView(View):
    """
    Showing all animal types
    """

    def get(self, request):
        types = AnimalType.objects.all()
        return render(request, 'animal_type.html', {'types': types})


class AddAnimalTypeView(View):
    """
    Allowing to add animal type
    """

    def get(self, request):
        form = AddTypeForm()
        return render(request, 'add_type_form.html', {'form': form})

    def post(self, request):
        form = AddTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            type = form.cleaned_data['type']
            breed = form.cleaned_data['breed']
            breed_number = form.cleaned_data['breed_number']
            picture = form.cleaned_data['picture']
            description = form.cleaned_data['description']
            AnimalType.objects.create(type=type, breed=breed, breed_number=breed_number, picture=picture,
                                      description=description)
        return HttpResponseRedirect('/type')


class CareView(View):
    """
    Showing all care for indicated animal
    """

    def get(self, request, animal_id):
        care = AnimalCare.objects.filter(animal_id=animal_id)
        return render(request, 'animal_care.html', {'care': care,
                                                    'animal_id': animal_id})


class AddCareView(View):
    """
    Allowing to add animal care
    """

    def get(self, request, animal_id):
        form = AddCareForm()
        return render(request, 'add_care_form.html', {'form': form})

    def post(self, request, animal_id):
        form = AddCareForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            name = form.cleaned_data['name']
            drug = form.cleaned_data['drug']
            date = form.cleaned_data['date']
            AnimalCare.objects.create(type=type, name=name, drug=drug, date=date, animal_id=animal_id)
        return HttpResponseRedirect(f'/care/{animal_id}')
