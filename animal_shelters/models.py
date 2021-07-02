from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ANIMAL_SIZE = (
    (1, "small"),
    (2, "medium"),
    (3, "large")
)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField()
    surname = models.CharField()
    street = models.CharField()
    number = models.CharField()
    city = models.CharField()
    postal_code = models.CharField()
    capacity = models.IntegerField()
    opening_hours = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    about = models.TextField()
    regulations = models.TextField()
    donations = models.TextField()


class AnimalInfo(models.Model):
    type = models.CharField()
    breed = models.CharField()
    picture = models.FileField()
    description = models.TextField()
    FCI_number = models.IntegerField()


class Food(models.Model):
    name = models.CharField()
    age_start = models.IntegerField()
    age_end = models.IntegerField()
    weight_start = models.IntegerField()
    weight_end = models.IntegerField()
    amount = models.DecimalField()


class Animal(models.Model):
    name = models.CharField()
    chip_number = models.IntegerField()
    birth_date = models.DateField()
    weight = models.DecimalField()
    size = models.CharField(choices=ANIMAL_SIZE)
    description = models.TextField()
    animal_info = models.ForeignKey(AnimalInfo, on_delete=models.CASCADE)
    picture = models.FileField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)


class AnimalCare(models.Model):
    type = models.CharField()
    name = models.CharField()
    drug = models.CharField()
    date = models.DateField()
    animal = models.ManyToManyField(Animal)


class AnimalOwner(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
