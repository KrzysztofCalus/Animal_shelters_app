# Generated by Django 3.2.4 on 2021-07-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelters', '0006_food_weight_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaltype',
            name='picture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
