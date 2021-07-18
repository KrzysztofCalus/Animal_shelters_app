from animal_shelters.models import AnimalType, Food, Owner, Animal, AnimalCare, AnimalOwner
from django.contrib.auth.models import User
import pytest


def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


def test_new_user(django_user_model):
    django_user_model.objects.create(username="someone", password="something")


@pytest.mark.django_db
@pytest.fixture
def test_user():
    return User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 1


@pytest.mark.django_db
@pytest.fixture
def test_create_type():
    typ = AnimalType.objects.create(type="Type", breed_number=1, breed="Breed",
                                    description="Des", picture="pic.jpg")
    assert typ.type == "Type"
    assert typ.breed_number == 1
    assert typ.breed == "Breed"
    assert typ.description == "Des"
    assert typ.picture == "pic.jpg"


@pytest.mark.django_db
def test_filter_type():
    AnimalType.objects.create(type="Type", breed_number=1, breed="Breed",
                              description="Des", picture="pic.jpg")
    assert AnimalType.objects.filter(type="Type").exists()


@pytest.mark.django_db
def test_update_type():
    typ = AnimalType.objects.create(type="Type", breed_number=1, breed="Breed",
                                    description="Des", picture="pic.jpg")
    typ.type = "New_type"
    typ.save()
    typ_from_db = AnimalType.objects.get(type="New_type")
    assert typ_from_db.type == "New_type"


@pytest.mark.django_db
@pytest.fixture
def test_create_food():
    food = Food.objects.create(name="Name", age_start=0, age_end=5, weight_start=0,
                               weight_end=20, amount=0.5)
    assert food.name == "Name"
    assert food.age_start == 0
    assert food.age_end == 5
    assert food.weight_start == 0
    assert food.weight_end == 20
    assert food.amount == 0.5


@pytest.mark.django_db
def test_filter_food():
    Food.objects.create(name="Name", age_start=0, age_end=5, weight_start=0,
                        weight_end=20, amount=0.5)
    assert Food.objects.filter(name="Name").exists()


@pytest.mark.django_db
def test_update_food():
    food = Food.objects.create(name="Name", age_start=0, age_end=5, weight_start=0,
                               weight_end=20, amount=0.5)
    food.name = "New_name"
    food.save()
    food_from_db = Food.objects.get(name="New_name")
    assert food_from_db.name == "New_name"


@pytest.mark.django_db
@pytest.fixture
def test_create_owner(test_user):
    owner = Owner.objects.create(user=test_user, shelter_name="Shelter", street="Street",
                                 number=0, city="City", postal_code="00-000", phone=123456789,
                                 email="user@gmail.com", shelter=True, capacity=100,
                                 opening_hours="8-18", about="About", regulations="Regulations",
                                 donations="Donations")
    assert owner.user == test_user
    assert owner.shelter_name == "Shelter"
    assert owner.street == "Street"
    assert owner.number == 0
    assert owner.city == "City"
    assert owner.postal_code == "00-000"
    assert owner.phone == 123456789
    assert owner.email == "user@gmail.com"
    assert owner.shelter is True
    assert owner.capacity == 100
    assert owner.opening_hours == "8-18"
    assert owner.about == "About"
    assert owner.regulations == "Regulations"
    assert owner.donations == "Donations"


@pytest.mark.django_db
def test_filter_owner(test_user):
    Owner.objects.create(user=test_user, shelter_name="Shelter", street="Street",
                         number=0, city="City", postal_code="00-000", phone=123456789,
                         email="user@gmail.com", shelter=True, capacity=100,
                         opening_hours="8-18", about="About", regulations="Regulations",
                         donations="Donations")
    assert Owner.objects.filter(shelter_name="Shelter").exists()


@pytest.mark.django_db
def test_update_owner(test_user):
    owner = Owner.objects.create(user=test_user, shelter_name="Shelter", street="Street",
                                 number=0, city="City", postal_code="00-000", phone=123456789,
                                 email="user@gmail.com", shelter=True, capacity=100,
                                 opening_hours="8-18", about="About", regulations="Regulations",
                                 donations="Donations")
    owner.shelter_name = "New_name"
    owner.capacity = 50
    owner.save()
    owner_from_db = Owner.objects.get(shelter_name="New_name")
    assert owner_from_db.shelter_name == "New_name"
    assert owner_from_db.capacity == 50


@pytest.mark.django_db
@pytest.fixture
def test_create_animal(test_create_type, test_create_food):
    animal = Animal.objects.create(name="Name", sex="male", chip_number=123,
                                   birth_date="2020-02-02", colour="Black",
                                   distinguishing_marks="n/a", weight=2.5,
                                   size="small", description="Description",
                                   animal_type=test_create_type, picture="pic.jpg",
                                   food=test_create_food, owner=test_create_owner)
    assert animal.name == "Name"
    assert animal.sex == "male"
    assert animal.chip_number == 123
    assert animal.birth_date == "2020-02-02"
    assert animal.colour == "Black"
    assert animal.distinguishing_marks == "n/a"
    assert animal.weight == 2.5
    assert animal.size == "small"
    assert animal.description == "Description"
    assert animal.animal_type == test_create_type
    assert animal.picture == "pic.jpg"
    assert animal.food == test_create_food
    assert animal.owner == test_create_owner


@pytest.mark.django_db
def test_filter_animal(test_create_type, test_create_food):
    Animal.objects.create(name="Name", sex="male", chip_number=123, birth_date="2020-10-10",
                          colour="Black", distinguishing_marks="n/a", weight=2.5, size="small",
                          description="Description", animal_type=test_create_type,
                          picture="pic.jpg", food=test_create_food)
    assert Animal.objects.filter(name="Name").exists()


@pytest.mark.django_db
def test_update_animal(test_create_type, test_create_food):
    animal = Animal.objects.create(name="Name", sex="male", chip_number=123,
                                   birth_date="2020-02-02", colour="Black",
                                   distinguishing_marks="n/a", weight=2.5, size="small",
                                   description="Description", animal_type=test_create_type,
                                   picture="pic.jpg", food=test_create_food)
    animal.name = "New_name"
    animal.picture = "pic.png"
    animal.save()
    animal_from_db = Animal.objects.get(name="New_name")
    assert animal_from_db.name == "New_name"
    assert animal_from_db.picture == "pic.png"


@pytest.mark.django_db
def test_create_care():
    care = AnimalCare.objects.create(type="Type", name="Name", drug="Drug", date="2020-02-02")
    assert care.type == "Type"
    assert care.name == "Name"
    assert care.drug == "Drug"
    assert care.date == "2020-02-02"
    assert care.animal == 5
    assert care.animal == test_create_animal


@pytest.mark.django_db
def test_filter_care(test_create_animal):
    AnimalCare.objects.create(type="Type", name="Name", drug="Drug", date="2020-02-02",
                              animal=test_create_animal)
    assert AnimalCare.objects.filter(type="Type").exists()


@pytest.mark.django_db
def test_update_care(test_create_animal):
    care = AnimalCare.objects.create(type="Type", name="Name", drug="Drug", date="2020-02-02",
                                     animal=test_create_animal)
    care.type = "New_type"
    care.name = "New_name"
    care.save()
    care_from_db = AnimalCare.objects.get(type="New_type")
    assert care_from_db.type == "New_type"
    assert care_from_db.name == "New_name"


@pytest.mark.django_db
def test_create_animal_owner(test_create_owner, test_create_animal):
    animal_owner = AnimalOwner.objects.create(animal_id=test_create_animal,
                                              owner_id=test_create_owner,
                                              start="2020-02-02", end="2020-02-02")
    assert animal_owner.animal_id == test_create_animal
    assert animal_owner.owner_id == test_create_owner
    assert animal_owner.start == "2020-02-02"
    assert animal_owner.end == "2020-02-02"


@pytest.mark.django_db
def test_filter_animal_owner(test_create_owner, test_create_animal):
    AnimalOwner.objects.create(animal=test_create_animal,
                               owner=test_create_owner,
                               start="2020-02-02", end="2020-02-02")
    assert AnimalOwner.objects.filter(animal=test_create_animal).exists()


@pytest.mark.django_db
def test_update_animal_owner(test_create_owner, test_create_animal):
    animal_owner = AnimalOwner.objects.create(animal=test_create_animal,
                                              owner=test_create_owner, start="2020-02-02",
                                              end="2020-02-02")
    animal_owner.start = "2021-01-01"
    animal_owner.save()
    animal_owner_from_db = AnimalOwner.objects.get(start="2021-01-01")
    assert animal_owner_from_db.start == "2021-01-01"
