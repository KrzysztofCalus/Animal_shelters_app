# Generated by Django 3.2.4 on 2021-07-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelters', '0005_alter_animalowner_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='weight_start',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
