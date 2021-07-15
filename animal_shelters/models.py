from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ANIMAL_SIZE = (
    ("SMALL", "small"),
    ("MEDIUM", "medium"),
    ("LARGE", "large")
)

SEX = (
    ("MALE", "male"),
    ("FEMALE", "female"),
    ("SEXLESS", "sexless")
)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shelter_name = models.CharField(max_length=256, default='')
    street = models.CharField(max_length=256)
    number = models.CharField(max_length=6)
    city = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=6)
    shelter = models.BooleanField()
    capacity = models.PositiveIntegerField(blank=True)
    opening_hours = models.TextField(blank=True)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    about = models.TextField(blank=True)
    regulations = models.TextField(blank=True)
    donations = models.TextField(blank=True)

    def __str__(self):
        return self.user


class AnimalType(models.Model):
    type = models.CharField(max_length=128)
    breed = models.CharField(max_length=128)
    picture = models.ImageField(null=True, blank=True)
    description = models.TextField()
    FCI_number = models.IntegerField()

    def __str__(self):
        return f'Type: {self.type}; Breed: {self.breed}; FCI number: {self.FCI_number}'


class Food(models.Model):
    name = models.CharField(max_length=128)
    age_start = models.PositiveIntegerField()
    age_end = models.PositiveIntegerField()
    weight_start = models.PositiveIntegerField(default=0)
    weight_end = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}; Age range: {self.age_start}-{self.age_end}; Weight range: {self.weight_start}-' \
               f'{self.weight_end}; Amount: {self.amount}'


class Animal(models.Model):
    name = models.CharField(max_length=128)
    sex = models.CharField(max_length=128, choices=SEX)
    chip_number = models.PositiveIntegerField(blank=True)
    birth_date = models.DateField()
    colour = models.CharField(max_length=56)
    distinguishing_marks = models.CharField(max_length=256)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length=128, choices=ANIMAL_SIZE)
    description = models.TextField()
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ManyToManyField(Owner, through='AnimalOwner')

    def __str__(self):
        return self.name


class AnimalCare(models.Model):
    type = models.CharField(max_length=128)
    name = models.CharField(max_length=128, blank=True)
    drug = models.CharField(max_length=128, blank=True)
    date = models.DateField()
    animal = models.ManyToManyField(Animal)

    def __str__(self):
        return self.name


class AnimalOwner(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField(null=True)
